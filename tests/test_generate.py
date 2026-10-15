"""Exercise the generation entry point without Docker or generated-source edits."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent


class GeneratorExitStatusTest(unittest.TestCase):
    def run_generator(self, status, output):
        with tempfile.TemporaryDirectory(prefix="mencoro-generation-test-") as directory:
            root = Path(directory)
            for name in ("generate.sh", "sdks.json"):
                shutil.copyfile(ROOT / name, root / name)
            commands = root / "bin"
            commands.mkdir()
            docker = commands / "docker"
            docker.write_text(f"#!/bin/sh\nprintf '%s\\n' '{output}'\nexit {status}\n")
            docker.chmod(0o755)
            return subprocess.run(
                ["bash", "generate.sh", "typescript"],
                cwd=root,
                env={**os.environ, "PATH": f"{commands}:{os.environ['PATH']}"},
                capture_output=True,
                text=True,
                check=False,
            )

    def test_generator_failure_is_not_reported_as_success(self):
        result = self.run_generator(42, "[main] ERROR generation failed")
        self.assertEqual(42, result.returncode)
        self.assertIn("generation failed", result.stdout)
        self.assertNotIn("generated 1 sdk(s)", result.stdout)

    def test_docker_failure_keeps_its_diagnostic(self):
        result = self.run_generator(125, "docker: unavailable image")
        self.assertEqual(125, result.returncode)
        self.assertIn("docker: unavailable image", result.stdout)

    def test_success_without_warnings_is_success(self):
        result = self.run_generator(0, "[main] INFO generating")
        self.assertEqual(0, result.returncode)
        self.assertIn("generated 1 sdk(s)", result.stdout)


class GoTestRegenerationTest(unittest.TestCase):
    def run_generator(self, status):
        with tempfile.TemporaryDirectory(prefix="mencoro-go-generation-test-") as directory:
            root = Path(directory)
            for name in ("generate.sh", "sdks.json"):
                shutil.copyfile(ROOT / name, root / name)
            test = root / "go/test/api_analytics_test.go"
            test.parent.mkdir(parents=True)
            test.write_text("old two-result test")
            preserved = root / "go/consumer-note.txt"
            preserved.write_text("preserve existing files")
            commands = root / "bin"
            commands.mkdir()
            docker = commands / "docker"
            docker.write_text(
                f"#!{sys.executable}\n"
                "import pathlib, sys\n"
                "if 'generate' not in sys.argv: sys.exit(0)\n"
                "output = pathlib.Path(sys.argv[sys.argv.index('-o') + 1].removeprefix('/local/'))\n"
                "test = output / 'test/api_analytics_test.go'\n"
                "test.parent.mkdir(parents=True, exist_ok=True)\n"
                "if not test.exists():\n"
                "    test.write_text('updated three-result test github.com/mencoro/mencoro-api-sdk/mencoro')\n"
                f"sys.exit({status})\n"
            )
            docker.chmod(0o755)
            result = subprocess.run(
                ["bash", "generate.sh", "go"],
                cwd=root,
                env={**os.environ, "PATH": f"{commands}:{os.environ['PATH']}"},
                capture_output=True,
                text=True,
                check=False,
            )
            return result, test.read_text(), preserved.read_text(), list((root / ".generator-configs").glob("go.*"))

    def test_regeneration_refreshes_go_tests_and_preserves_existing_files(self):
        result, test, preserved, temporary_outputs = self.run_generator(0)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("updated three-result test github.com/mencoro/mencoro-api-sdk/go", test)
        self.assertEqual("preserve existing files", preserved)
        self.assertEqual(["go.json"], [path.name for path in temporary_outputs])

    def test_failed_generation_does_not_replace_existing_go_tests(self):
        result, test, preserved, temporary_outputs = self.run_generator(42)
        self.assertEqual(42, result.returncode)
        self.assertEqual("old two-result test", test)
        self.assertEqual("preserve existing files", preserved)
        self.assertEqual(["go.json"], [path.name for path in temporary_outputs])


FAKE_GENERATOR = (
    "import os, pathlib, sys\n"
    "if 'generate' not in sys.argv: sys.exit(0)\n"
    "output = pathlib.Path(sys.argv[sys.argv.index('-o') + 1].removeprefix('/local/'))\n"
    "status = int(os.environ['FAKE_GENERATOR_STATUS'])\n"
    "if status: sys.exit(status)\n"
    "names = [name for name in os.environ['FAKE_GENERATOR_FILES'].split(',') if name]\n"
    "for name in names:\n"
    "    path = output / name\n"
    "    path.parent.mkdir(parents=True, exist_ok=True)\n"
    "    path.write_text('generated github.com/mencoro/mencoro-api-sdk/mencoro')\n"
    "listing = output / '.openapi-generator/FILES'\n"
    "listing.parent.mkdir(parents=True, exist_ok=True)\n"
    "listing.write_text(''.join(name + '\\n' for name in names))\n"
)


class OrphanedFileTest(unittest.TestCase):
    """A file the previous run generated and this one did not is deleted; nothing else is."""

    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="mencoro-orphan-test-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        for name in ("generate.sh", "sdks.json"):
            shutil.copyfile(ROOT / name, self.root / name)
        commands = self.root / "bin"
        commands.mkdir()
        docker = commands / "docker"
        docker.write_text(f"#!{sys.executable}\n" + FAKE_GENERATOR)
        docker.chmod(0o755)
        self.path = f"{commands}:{os.environ['PATH']}"

    def previous_run(self, sdk, listed, unlisted=()):
        for name in (*(listed or ()), *unlisted):
            path = self.root / sdk / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"previous {name}")
        if listed is not None:
            listing = self.root / sdk / ".openapi-generator/FILES"
            listing.parent.mkdir(parents=True, exist_ok=True)
            listing.write_text("".join(f"{name}\n" for name in listed))

    def generate(self, sdk, emitted, status=0):
        return subprocess.run(
            ["bash", "generate.sh", sdk],
            cwd=self.root,
            env={
                **os.environ,
                "PATH": self.path,
                "FAKE_GENERATOR_FILES": ",".join(emitted),
                "FAKE_GENERATOR_STATUS": str(status),
            },
            capture_output=True,
            text=True,
            check=False,
        )

    def assert_orphans_removed(self, sdk):
        self.previous_run(
            sdk,
            listed=["README.md", "docs/Removed.md", "models/removed/Removed.txt", "models/Kept.txt"],
            unlisted=["test/RemovedTest.txt", "notes.txt"],
        )
        result = self.generate(sdk, ["README.md", "models/Kept.txt", "docs/Added.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn(f"removed {sdk}/docs/Removed.md", result.stdout)
        self.assertIn(f"removed {sdk}/models/removed/Removed.txt", result.stdout)
        client = self.root / sdk
        self.assertFalse((client / "docs/Removed.md").exists())
        self.assertFalse((client / "models/removed").exists(), "an emptied directory is removed")
        for name in ("README.md", "models/Kept.txt", "docs/Added.md"):
            self.assertTrue((client / name).exists(), f"{name} is still generated")
        self.assertTrue((client / "docs").is_dir(), "a directory that still holds files is kept")
        # Not in the previous list, so not provably generated: a skipped test stub or a file
        # somebody added. Neither is the script's to delete.
        self.assertEqual("previous test/RemovedTest.txt", (client / "test/RemovedTest.txt").read_text())
        self.assertEqual("previous notes.txt", (client / "notes.txt").read_text())
        self.assertFalse(
            (self.root / f".generator-configs/{sdk}.FILES").exists(),
            "the copy of the previous list does not outlive the run",
        )

    def test_files_dropped_from_the_contract_are_removed(self):
        self.assert_orphans_removed("typescript")

    def test_go_removes_orphans_after_overlaying_the_temporary_output(self):
        self.assert_orphans_removed("go")

    def test_failed_generation_removes_nothing(self):
        self.previous_run("typescript", listed=["README.md", "docs/Removed.md"])
        result = self.generate("typescript", ["README.md"], status=42)
        self.assertEqual(42, result.returncode)
        self.assertTrue((self.root / "typescript/docs/Removed.md").exists())
        self.assertNotIn("removed", result.stdout)

    def test_a_first_generation_removes_nothing(self):
        self.previous_run("typescript", listed=None, unlisted=["notes.txt"])
        result = self.generate("typescript", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("previous notes.txt", (self.root / "typescript/notes.txt").read_text())

    def test_paths_outside_the_client_are_never_removed(self):
        outside = self.root / "outside.txt"
        outside.write_text("not generated")
        absolute = self.root / "absolute.txt"
        absolute.write_text("not generated")
        self.previous_run("typescript", listed=["README.md"])
        listing = self.root / "typescript/.openapi-generator/FILES"
        listing.write_text(f"README.md\n../outside.txt\n{absolute}\n")
        result = self.generate("typescript", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertTrue(outside.exists())
        self.assertTrue(absolute.exists())

    def test_a_path_through_a_symlink_out_of_the_client_is_never_removed(self):
        outside = self.root / "elsewhere"
        outside.mkdir()
        (outside / "kept.txt").write_text("not generated")
        self.previous_run("typescript", listed=["README.md"])
        (self.root / "typescript/link").symlink_to(outside, target_is_directory=True)
        listing = self.root / "typescript/.openapi-generator/FILES"
        listing.write_text("README.md\nlink/kept.txt\n")
        result = self.generate("typescript", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("not generated", (outside / "kept.txt").read_text())

    def test_an_unchanged_list_removes_nothing(self):
        self.previous_run("typescript", listed=["README.md", "docs/Kept.md"], unlisted=["test/Stub.txt"])
        result = self.generate("typescript", ["README.md", "docs/Kept.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertNotIn("removed", result.stdout)
        for name in ("README.md", "docs/Kept.md", "test/Stub.txt"):
            self.assertTrue((self.root / "typescript" / name).exists(), name)

    def test_an_orphan_already_gone_is_not_an_error(self):
        self.previous_run("typescript", listed=["README.md"])
        listing = self.root / "typescript/.openapi-generator/FILES"
        listing.write_text("README.md\ndocs/AlreadyDeleted.md\n")
        result = self.generate("typescript", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertNotIn("removed", result.stdout)


class ContractSyncTest(unittest.TestCase):
    """`--sync` writes the fetched contract in the committed layout, or not at all."""

    def sync(self, contract, curl_status=0):
        with tempfile.TemporaryDirectory(prefix="mencoro-sync-test-") as directory:
            root = Path(directory)
            for name in ("generate.sh", "sdks.json", "openapi.json"):
                shutil.copyfile(ROOT / name, root / name)
            commands = root / "bin"
            commands.mkdir()
            (commands / "fetched.json").write_bytes(contract)
            curl = commands / "curl"
            curl.write_text(f"#!/bin/sh\ncat '{commands / 'fetched.json'}'\nexit {curl_status}\n")
            curl.chmod(0o755)
            docker = commands / "docker"
            docker.write_text("#!/bin/sh\nexit 0\n")
            docker.chmod(0o755)
            result = subprocess.run(
                ["bash", "generate.sh", "--sync", "typescript"],
                cwd=root,
                env={**os.environ, "PATH": f"{commands}:{os.environ['PATH']}"},
                capture_output=True,
                text=True,
                check=False,
            )
            return result, (root / "openapi.json").read_bytes(), (root / "openapi.json.new").exists()

    def test_an_unchanged_contract_reproduces_the_committed_file_byte_for_byte(self):
        committed = (ROOT / "openapi.json").read_bytes()
        # Served compact and ASCII-escaped, the opposite of the committed layout on both counts.
        served = json.dumps(json.loads(committed), ensure_ascii=True, separators=(",", ":")).encode()
        self.assertNotEqual(committed, served)
        result, written, leftover = self.sync(served)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(committed, written)
        self.assertFalse(leftover)

    def test_a_changed_contract_changes_only_the_lines_it_changed(self):
        committed = (ROOT / "openapi.json").read_bytes()
        contract = json.loads(committed)
        version = contract["info"]["version"]
        contract["info"]["version"] = f"{version}-changed"
        served = json.dumps(contract, ensure_ascii=True, separators=(",", ":")).encode()
        result, written, _ = self.sync(served)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        before = committed.decode("utf-8").splitlines()
        after = written.decode("utf-8").splitlines()
        self.assertEqual(len(before), len(after))
        changed = [(old, new) for old, new in zip(before, after) if old != new]
        self.assertEqual(1, len(changed), changed)
        self.assertIn(f'"version": "{version}-changed"', changed[0][1])

    def test_the_committed_contract_uses_raw_utf8(self):
        # Without a non-ASCII character in the contract, the test above would not tell an escaped
        # layout from a raw one.
        self.assertFalse((ROOT / "openapi.json").read_bytes().decode("utf-8").isascii())

    def test_a_contract_that_lost_its_operations_is_refused(self):
        committed = (ROOT / "openapi.json").read_bytes()
        gutted = json.dumps({"openapi": "3.0.0", "paths": {"/health": {"get": {}}}}).encode()
        result, written, leftover = self.sync(gutted)
        self.assertEqual(1, result.returncode)
        self.assertIn("published only 1 operations", result.stderr)
        self.assertEqual(committed, written)
        self.assertFalse(leftover)

    def test_a_failed_fetch_keeps_the_committed_contract(self):
        committed = (ROOT / "openapi.json").read_bytes()
        result, written, leftover = self.sync(b"", curl_status=22)
        self.assertNotEqual(0, result.returncode)
        self.assertEqual(committed, written)
        self.assertFalse(leftover)


if __name__ == "__main__":
    unittest.main()
