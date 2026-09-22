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
| TypeScript (Node 18+, browsers) | `@mencoro/api` | [![npm](https://img.shields.io/npm/v/%40mencoro%2Fapi?label=npm&color=informational)](https://www.npmjs.com/package/@mencoro/api) | [`typescript/`](typescript/) |
| PHP 8.1+ | `mencoro/mencoro-api-sdk` | [![Packagist](https://img.shields.io/packagist/v/mencoro/mencoro-api-sdk?label=packagist&color=informational)](https://packagist.org/packages/mencoro/mencoro-api-sdk) | [`php/`](php/) |
| Go 1.21+ | `github.com/mencoro/mencoro-api-sdk/go` | [![Go module](https://img.shields.io/github/v/tag/mencoro/mencoro-api-sdk?filter=go%2F*&label=go&color=informational)](https://pkg.go.dev/github.com/mencoro/mencoro-api-sdk/go) | [`go/`](go/) |
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

	mencoro "github.com/mencoro/mencoro-api-sdk/go"
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

Two corrections are applied by the generator script rather than by hand, because a hand edit would
be discarded on the next run:

- **Go** has no package registry, so the import path is the repository URL plus the directory. The
  generator derives the module path from the Go package name, and `go` is a keyword, so it cannot
  produce `.../mencoro-api-sdk/go` on its own.
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
