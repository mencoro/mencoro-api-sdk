#!/usr/bin/env bash
#
# Regenerates every client in this repository from openapi.json.
#
# Each client is generated whole from the contract, so there is nothing to port between languages
# and nothing to keep in sync by hand: adding a language means one entry in sdks.json, and a change
# to the API reaches all of them in the same run.
#
# Usage:
#   ./generate.sh                regenerate every SDK from the committed openapi.json
#   ./generate.sh python go      regenerate only these
#   ./generate.sh --sync         fetch the live contract first, then regenerate everything
#
# The fetch is opt-in on purpose. A regeneration that silently pulls a new contract turns a
# mechanical rerun into a content change nobody reviewed, and the diff runs to six figures of lines
# across seven languages — the one place a surprise must not hide.

set -euo pipefail

cd "$(dirname "$0")"

GENERATOR_VERSION=$(python3 -c 'import json; print(json.load(open("sdks.json"))["generatorVersion"])')
PACKAGE_VERSION=$(python3 -c 'import json; print(json.load(open("sdks.json"))["packageVersion"])')
CONTRACT_URL="${MENCORO_CONTRACT_URL:-$(python3 -c 'import json; print(json.load(open("sdks.json"))["contractUrl"])')}"
IMAGE="openapitools/openapi-generator-cli:v${GENERATOR_VERSION}"

GO_TOOLCHAIN=$(python3 -c 'import json; print(json.load(open("sdks.json"))["goToolchain"])')
GO_MODULE="github.com/mencoro/mencoro-api-sdk/go"
GO_GENERATED_MODULE="github.com/mencoro/mencoro-api-sdk/$(python3 -c '
import json
sdk = next(s for s in json.load(open("sdks.json"))["sdks"] if s["dir"] == "go")
print(sdk["config"]["packageName"])
')"

sync_contract() {
  echo "fetching ${CONTRACT_URL}"
  curl --fail --silent --show-error "${CONTRACT_URL}" | python3 -m json.tool > openapi.json.new

  local operations
  operations=$(python3 -c '
import json
methods = {"get", "post", "put", "patch", "delete"}
paths = json.load(open("openapi.json.new")).get("paths", {})
print(sum(len(methods & set(item)) for item in paths.values()))
')

  # A contract that lost most of its surface is far more likely to be a misrouted response or a
  # half-booted container than a real change, and regenerating from it would gut every client here.
  if [[ "${operations}" -lt 50 ]]; then
    echo "contract published only ${operations} operations; refusing to overwrite" >&2
    rm -f openapi.json.new
    exit 1
  fi

  mv openapi.json.new openapi.json
  echo "openapi.json updated (${operations} operations)"
}

targets=()
for argument in "$@"; do
  case "${argument}" in
    --sync) sync_contract ;;
    -*) echo "unknown option: ${argument}" >&2; exit 1 ;;
    *) targets+=("${argument}") ;;
  esac
done

mapfile -t all_dirs < <(python3 -c '
import json
for sdk in json.load(open("sdks.json"))["sdks"]:
    print(sdk["dir"])
')

if [[ ${#targets[@]} -eq 0 ]]; then
  targets=("${all_dirs[@]}")
else
  for target in "${targets[@]}"; do
    if [[ ! " ${all_dirs[*]} " =~ " ${target} " ]]; then
      echo "unknown sdk: ${target} (known: ${all_dirs[*]})" >&2
      exit 1
    fi
  done
fi

mkdir -p .generator-configs

for target in "${targets[@]}"; do
  generator=$(python3 -c "
import json
sdk = next(s for s in json.load(open('sdks.json'))['sdks'] if s['dir'] == '${target}')
print(sdk['generator'])
")

  # The per-language config is derived rather than committed: the fields every language shares —
  # version, repository, user agent — must not be able to disagree between seven copies.
  python3 -c "
import json
manifest = json.load(open('sdks.json'))
sdk = next(s for s in manifest['sdks'] if s['dir'] == '${target}')
config = dict(sdk['config'])
config.update({
    'packageVersion': manifest['packageVersion'],
    'gitUserId': 'mencoro',
    'gitRepoId': 'mencoro-api-sdk',
    'httpUserAgent': 'mencoro-${target}/' + manifest['packageVersion'],
    'hideGenerationTimestamp': True,
})
json.dump(config, open('.generator-configs/${target}.json', 'w'), indent=2)
"

  # A property whose name collides with something the generator itself declares has to be renamed
  # in that language's client. It is a CLI option rather than a config field, so it is assembled
  # here from the manifest.
  mapfile -t name_mappings < <(python3 -c "
import json
sdk = next(s for s in json.load(open('sdks.json'))['sdks'] if s['dir'] == '${target}')
for source, renamed in sdk.get('nameMappings', {}).items():
    print(f'{source}={renamed}')
")

  mapping_args=()
  if [[ ${#name_mappings[@]} -gt 0 ]]; then
    mapping_args=(--name-mappings "$(IFS=,; echo "${name_mappings[*]}")")
  fi

  echo "==> ${target} (${generator})"
  docker run --rm \
    -u "$(id -u):$(id -g)" \
    -v "$PWD:/local" \
    "${IMAGE}" \
    generate \
    -i /local/openapi.json \
    -g "${generator}" \
    -o "/local/${target}" \
    -c "/local/.generator-configs/${target}.json" \
    "${mapping_args[@]}" \
    2>&1 | grep -E "^\[main\] (ERROR|WARN o.o.codegen.InlineModelResolver)" || true

  if [[ "${target}" == "php" ]]; then
    # Packagist reads composer.json from the repository ROOT and has no notion of a package living
    # in a subdirectory — the same shape of problem Go has, and with no equivalent of Go's
    # directory-prefixed tags. So the published PHP manifest is the root one, derived here from the
    # generated php/composer.json rather than written by hand, because two manifests maintained
    # separately are two manifests that disagree.
    python3 scripts/php-root-manifest.py
    echo "    root composer.json <- php/composer.json"
  fi

  if [[ "${target}" == "go" ]]; then
    # Go has no package registry: the import path IS the repository URL plus the directory, so in a
    # monorepo it has to be ".../mencoro-api-sdk/go". The generator derives the module path from
    # packageName, which is also the Go package name — and `go` is a keyword, so it cannot produce
    # that path. The module line and the 28 files that echo it are corrected here rather than by
    # hand, because a hand edit would be discarded by the next run.
    grep -rl "${GO_GENERATED_MODULE}" go \
      | xargs sed -i "s|${GO_GENERATED_MODULE}|${GO_MODULE}|g"
    echo "    module path -> ${GO_MODULE}"

    # The generated go.sum covers the client but not the generated tests, so `go build ./...`
    # fails on a fresh checkout with "no required module provides package". Tidying here keeps
    # that fix inside the generation step, where the next run reproduces it, instead of leaving a
    # manual `go mod tidy` that regeneration would silently undo.
    docker run --rm -u "$(id -u):$(id -g)" \
      -e GOCACHE=/tmp/go-build -e GOMODCACHE=/tmp/go-mod \
      -v "$PWD/go:/src" -w /src \
      "golang:${GO_TOOLCHAIN}-alpine" go mod tidy
  fi
done

echo
echo "generated ${#targets[@]} sdk(s) at version ${PACKAGE_VERSION}. Review the diff before committing."
