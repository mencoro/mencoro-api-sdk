# Mencoro API SDKs

[![CI](https://github.com/mencoro/mencoro-api-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/mencoro/mencoro-api-sdk/actions/workflows/ci.yml)
[![Release](https://github.com/mencoro/mencoro-api-sdk/actions/workflows/release.yml/badge.svg)](https://github.com/mencoro/mencoro-api-sdk/actions/workflows/release.yml)

Official clients for the [Mencoro API](https://mencoro.com/api-docs/) — 86 operations over your
projects, tracked queries, captures and the analytics computed from them.

Every client here is **generated from the OpenAPI contract the API itself publishes**, so they say
what the running service does rather than what a handwritten wrapper remembers about it. One
contract, one generator run, one version: a change to the API reaches all seven languages together.

| Language | Package | Version | Directory |
|---|---|---|---|
| Python 3.9+ | `mencoro` | [![PyPI](https://img.shields.io/pypi/v/mencoro?label=pypi&color=informational)](https://pypi.org/project/mencoro/) | [`python/`](python/) |
| TypeScript (Node 22+, browsers) | `@mencoro/api` | [![npm](https://img.shields.io/npm/v/%40mencoro%2Fapi?label=npm&color=informational)](https://www.npmjs.com/package/@mencoro/api) | [`typescript/`](typescript/) |
| PHP 8.1+ | `mencoro/mencoro-api-sdk` | [![Packagist](https://img.shields.io/packagist/v/mencoro/mencoro-api-sdk?label=packagist&color=informational)](https://packagist.org/packages/mencoro/mencoro-api-sdk) | [`php/`](php/) |
| Go 1.23+ | `github.com/mencoro/mencoro-api-sdk/go/v2` | [![Go module](https://img.shields.io/github/v/tag/mencoro/mencoro-api-sdk?filter=go%2F*&label=go&color=informational)](https://pkg.go.dev/github.com/mencoro/mencoro-api-sdk/go/v2) | [`go/`](go/) |
| Java 11+ | `com.mencoro:mencoro-api` | [![Maven Central](https://img.shields.io/maven-central/v/com.mencoro/mencoro-api?label=maven%20central&color=informational)](https://central.sonatype.com/artifact/com.mencoro/mencoro-api) | [`java/`](java/) |
| .NET 8 | `Mencoro.Api` | [![NuGet](https://img.shields.io/nuget/v/Mencoro.Api?label=nuget&color=informational)](https://www.nuget.org/packages/Mencoro.Api/) | [`csharp/`](csharp/) |
| Ruby 3.0+ | `mencoro` | [![RubyGems](https://img.shields.io/gem/v/mencoro?label=gem&color=informational)](https://rubygems.org/gems/mencoro) | [`ruby/`](ruby/) |

Each directory carries the generated reference for its language: one page per resource and one per
model under its own `docs/`.

## Get a key

Create one from your Mencoro account, under **API keys** in the user menu. **The plaintext key is
shown once, at creation, and never again** — store it where you store any other secret. If you lose
it, revoke it and issue another; revocation takes effect on the very next request.

A key carries capabilities and a set of organizations, and it only ever **restricts**. It never
grants more than its owner's live membership and role already allow, and every request re-checks
those: if your role is narrowed or your membership withdrawn, the key loses that access
immediately, without being revoked and without being reissued.

| Capability | What it allows |
|---|---|
| `read` | Every listing and every analytics operation. The floor — every key has it. |
| `write` | Projects, tracked queries, clusters, competitors and discovery jobs. |
| `organization:manage` | Members, invitations and the organization itself. Requested explicitly at creation. |

## First call

`getMe` returns the user the key belongs to, plus the key's capabilities and scope. It is the
quickest way to confirm a key works and to see which organizations it reaches.

<details open>
<summary><strong>Python</strong></summary>

```python
import os

from mencoro import ApiClient, Configuration
from mencoro.api import AccountApi, ProjectsApi

config = Configuration(
    host="https://api.mencoro.com",
    access_token=os.environ["MENCORO_API_KEY"],
)

with ApiClient(config) as client:
    me = AccountApi(client).get_me()
    print(me.email, me.capabilities, me.scope_mode)

    for organization_id in me.organization_ids:
        page = ProjectsApi(client).list_projects(organization_id=organization_id, limit=100)
        print(organization_id, f"{len(page.items)} of {page.total} projects")
```
</details>

<details>
<summary><strong>TypeScript</strong></summary>

```ts
import { Configuration, AccountApi, ProjectsApi } from "@mencoro/api"

const config = new Configuration({
  basePath: "https://api.mencoro.com",
  accessToken: process.env.MENCORO_API_KEY,
})

const me = await new AccountApi(config).getMe()
console.log(me.email, me.capabilities, me.scopeMode)

for (const organizationId of me.organizationIds ?? []) {
  const page = await new ProjectsApi(config).listProjects({ organizationId, limit: 100 })
  console.log(organizationId, `${page.items?.length} of ${page.total} projects`)
}
```
</details>

<details>
<summary><strong>Go</strong></summary>

```go
import (
	"context"
	"os"

	mencoro "github.com/mencoro/mencoro-api-sdk/go/v2"
)

config := mencoro.NewConfiguration()
config.Servers = mencoro.ServerConfigurations{{URL: "https://api.mencoro.com"}}
client := mencoro.NewAPIClient(config)

ctx := context.WithValue(context.Background(), mencoro.ContextAccessToken, os.Getenv("MENCORO_API_KEY"))
me, _, err := client.AccountAPI.GetMe(ctx).Execute()
```
</details>

<details>
<summary><strong>PHP</strong></summary>

```php
use Mencoro\Api\Api\AccountApi;
use Mencoro\Api\Configuration;

$config = Configuration::getDefaultConfiguration()
    ->setHost('https://api.mencoro.com')
    ->setAccessToken(getenv('MENCORO_API_KEY'));

$me = (new AccountApi(new GuzzleHttp\Client(), $config))->getMe();
```
</details>

<details>
<summary><strong>Ruby</strong></summary>

```ruby
require "mencoro"

Mencoro.configure do |config|
  config.host = "api.mencoro.com"
  config.access_token = ENV.fetch("MENCORO_API_KEY")
end

me = Mencoro::AccountApi.new.get_me
```
</details>

<details>
<summary><strong>Java</strong></summary>

```java
import com.mencoro.api.ApiClient;
import com.mencoro.api.api.AccountApi;

ApiClient client = new ApiClient();
client.setBasePath("https://api.mencoro.com");
client.setBearerToken(System.getenv("MENCORO_API_KEY"));

var me = new AccountApi(client).getMe();
```
</details>

<details>
<summary><strong>C#</strong></summary>

```csharp
using Mencoro.Api.Api;
using Mencoro.Api.Client;

var config = new Configuration
{
    BasePath = "https://api.mencoro.com",
    AccessToken = Environment.GetEnvironmentVariable("MENCORO_API_KEY"),
};

var me = new AccountApi(config).GetMe();
```
</details>

## Changes in 2.0.1

No API change. Maven Central rejected 2.0.0 because of the publishing plugin, so Java moves from
1.0.1 straight to 2.0.1. Every other language has both versions. The notes below still apply.

## Changes in 2.0.0

**Some code written for 1.0.1 breaks.** Reading responses with Python, PHP, Java or Ruby needs no
change:

- **TypeScript:** `@mencoro/api` now declares Node 22 or newer. Browsers are not affected.
- **Go:** the module moves to `github.com/mencoro/mencoro-api-sdk/go/v2`, because Go requires a
  second major version to carry `/v2`. Update every import and run
  `go get github.com/mencoro/mencoro-api-sdk/go/v2@v2.0.0`. The package is still `mencoro`, and the
  old path stays at 1.0.1.
- **Models built by hand.** `projectAccessMode` and `projectIds` are now required on
  `InvitationResource`, `CreateInvitation201Response` and `MemberResource`, and `carriedPositions`
  on `KeywordListingResource`. Their Go constructors gain those parameters. The C# constructors do
  too, as optional ones, so old calls still compile and throw `ArgumentNullException` at runtime. A
  TypeScript literal or Python model of those types has to set them.
- **Nullable counts.** `invitations.pending` and `members.total` of `getOrganizationStats` are null
  for a member restricted to selected projects. The Go fields become `NullableInt32`, the C# ones
  `int?` and the TypeScript ones `number | null`.

The contract also gains, without breaking anything:

- **Project access per member.** `setMemberProjectAccess` restricts a member to selected projects
  and `createInvitation` takes an optional `projectAccess`. A restricted member sees narrower lists
  and aggregates, null plan and budget fields on the subscription, and a `404` on `createProject`
  and `startBrandNameSuggestionJob`.
- **Carried positions.** `carriedPositions` on a keyword listing says when a position figure
  includes a measurement from before the window. The matching `trend*` field is then null.
- **Tracked queries by engine family.** `getOrganizationOverview` adds `aiTrackedQueryCount`,
  `serpTrackedQueryCount` and `shoppingTrackedQueryCount` per project.
- **Cluster filters.** The contract now documents that a `queryClusterIds` or
  `includeUngroupedQueries` selection matching no tracked query answers `400`, and that
  `includeUngroupedQueries` sent alone keeps only the tracked queries in no cluster.

## Conventions

These hold in every language. The per-language docs cover the signatures; this is what the contract
cannot state about itself.

### Errors

Every refusal answers the same envelope, and every one carries a `requestId`. Quote it to support
and it identifies your exact request.

```json
{
  "code": "validation_error",
  "message": "The request failed validation.",
  "requestId": "01a0c58a-3370-7170-acdb-a0a7b760bc83",
  "details": {
    "limit": [
      { "code": "out_of_range", "message": "\"limit\" must be between 1 and 100." }
    ]
  }
}
```

`details` is keyed by field, and each entry carries one of seven codes: `missing_field`,
`invalid_type`, `invalid_value`, `invalid_uuid`, `invalid_email`, `out_of_range`, `unknown_field`.
**An unrecognised parameter is reported rather than ignored**, so a typo in a filter never silently
hands you the unfiltered set.

### Rate limits

600 requests per user and 300 per key, every 60 seconds. The per-user ceiling is the real one:
issuing more keys divides the same budget rather than adding to it.

Over budget answers `429` with a `Retry-After` header in seconds. Honour it:

```python
import time

from mencoro.exceptions import ApiException


def with_backoff(call, attempts=3):
    for attempt in range(attempts):
        try:
            return call()
        except ApiException as error:
            if error.status != 429 or attempt == attempts - 1:
                raise
            time.sleep(int(error.headers.get("Retry-After", "1")))
```

### Writes are idempotent

**Every write requires an `Idempotency-Key`** — 8 to 255 printable ASCII characters with no spaces,
and a UUID is the obvious choice. Reuse it when you retry and the stored result is replayed rather
than the operation running again, so a lost response never becomes a duplicate project or a second
batch of tracked queries.

```python
import uuid

from mencoro.api import TrackedQueriesApi
from mencoro.models import BatchCreateTrackedQueriesRequestData

TrackedQueriesApi(client).batch_create_tracked_queries(
    organization_id=organization_id,
    project_id=project_id,
    idempotency_key=str(uuid.uuid4()),
    batch_create_tracked_queries_request_data=BatchCreateTrackedQueriesRequestData(
        query_texts=["best crm for startups"],
        engines=["chatgpt", "perplexity"],
        countries=["ES"],
        check_frequency="daily",
        n_passes=3,
        query_cluster_ids=[],
    ),
)
```

Generate the key **outside** the retry loop. A fresh key per attempt is the same as having no
idempotency at all.

A key is scoped to the API key that used it and bound to the request it first answered — method,
path and body. Reusing it for a different request is refused with `idempotency_key_reused` rather
than answering the wrong operation.

### Changes to the organization are confirmed

Archiving an organization, changing a member's role, inviting somebody — anything whose effects
reach beyond your own data — takes two calls:

```python
from mencoro.api import MembersApi, OrganizationOperationsApi
from mencoro.models import PreviewOrganizationOperationRequest

preview = OrganizationOperationsApi(client).preview_organization_operation(
    preview_organization_operation_request=PreviewOrganizationOperationRequest(
        action="change_member_role",
        organization_id=organization_id,
        resource_id=member_id,
        payload={"role": "manager"},
    ),
)
print(preview.changes, preview.side_effects, preview.warnings)

MembersApi(client).change_member_role(
    organization_id=organization_id,
    member_id=member_id,
    x_mencoro_confirmation=preview.confirmation.token,
    idempotency_key=str(uuid.uuid4()),
    change_member_role_request=...,
)
```

The token is single use, valid for five minutes, and bound to the effects the preview declared. If
the organization changed in between, the call is refused with `409` rather than doing more than was
agreed. Without the header it answers `428`.

### Paging

Listings take `limit` (default 20, maximum 100) and `offset`. A limit above the maximum is
**refused, never quietly clamped**, so the page you asked for is the page you get. `total` counts
everything the filter matches, not the size of the page.

Several listings also answer `text/csv` when asked for it with an `Accept` header. That is the same
page of the same rows, encoded differently: the 100-row maximum applies unchanged, because it is a
page and not a bulk export.

### Dates

`YYYY-MM-DD`, covering whole days in UTC.

## Also available over MCP

To read the same data inside an AI client rather than from your own code, the
[Mencoro MCP server](https://mencoro.com/features/mcp-server/) exposes it to Claude, ChatGPT,
Cursor and anything else that speaks MCP. Same data, no code to write.

## Regenerating

```bash
./generate.sh                # every SDK, from the committed openapi.json
./generate.sh python go      # only these
./generate.sh --sync         # fetch the live contract first, then regenerate everything
```

Requires Docker; nothing else. Everything inside each language directory is generated and must not
be edited by hand — the next run discards it. Adding a language is one entry in
[`sdks.json`](sdks.json).

The fetch is opt-in because a regeneration that silently pulls a new contract turns a mechanical
rerun into a content change nobody reviewed, and the diff runs to six figures of lines across seven
languages — the one place a surprise must not hide.

`--sync` writes the contract in the layout of the committed `openapi.json` — two-space indent, UTF-8
left unescaped, a trailing newline — so the diff it leaves is only what the contract changed. For
today's contract that is byte for byte what `jq .` produces. It is written with Python's `json`
module, which would differ from `jq` in two cases the contract does not contain: U+007F (DEL) is
written raw where `jq` escapes it, and a number literal is rewritten in Python's form (`1e3` becomes
`1000.0`, `1.50` becomes `1.5`).

The generator never deletes a file it no longer emits, so after each language is generated the
script deletes every file the previous `.openapi-generator/FILES` listed and the new one does not.
Three kinds of listed path are kept, because their absence from the new list does not mean the
contract dropped them:

- **Test stubs**, except Go's. The generator writes a stub only when it is missing and lists it only
  on the run that writes it, so a stub added in one run is gone from the next run's list. Nothing
  under the directory named by the SDK's `testStubDir` in [`sdks.json`](sdks.json) is deleted
  (`python/test/`, `php/test/`, `java/src/test/`, `csharp/src/Mencoro.Api.Test/`, `ruby/spec/`), so
  when the contract drops a schema or operation its stub has to be deleted by hand. Go is generated
  into an empty directory, so its stubs are written and listed on every run and are removed with
  the rest; TypeScript has none. For the same reason, after a contract change that adds a schema or
  operation, run the script twice before committing: the first run lists the new stubs in
  `.openapi-generator/FILES` and the second drops them again, which is the list CI expects.
- **`.openapi-generator-ignore`**, which the generator likewise writes only when it is missing.
- **Any path the target's `.openapi-generator-ignore` names**: the generator stopped writing it
  because it is now maintained by hand.

Two corrections are applied by the generator script rather than by hand, because a hand edit would
be discarded on the next run:

- **Go** has no package registry, so the import path is the repository URL plus the directory, and
  from 2.0.0 on the `/v2` Go requires of a second major. The generator derives the module path from
  the Go package name, and `go` is a keyword, so it cannot produce `.../mencoro-api-sdk/go/v2`
  on its own.
- **PHP**'s generated models all declare `getModelName()` to report their schema name, which
  collides with the contract's own `modelName` property on `AiResponseResource` — two methods of
  one name is a fatal parse error. The property is renamed to `engineModelName` in the PHP client
  only; the wire field is untouched.

## Contract

- [`openapi.json`](openapi.json) — the contract every client here is generated from
- [Live contract](https://api.mencoro.com/api/v1/doc/json) and
  [browsable reference](https://api.mencoro.com/api/v1/doc)
- [API documentation](https://mencoro.com/api-docs/)
- [`llms-full.txt`](https://mencoro.com/api-docs/llms-full.txt) — the whole reference as plain text,
  for pasting into an AI assistant

## License

MIT. See [LICENSE](LICENSE). Use of the Mencoro API itself is governed by
[Mencoro's terms](https://mencoro.com/legal/).
