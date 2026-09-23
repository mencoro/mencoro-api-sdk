"""Exercise the generation entry point without Docker or generated-source edits."""

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


if __name__ == "__main__":
    unittest.main()
