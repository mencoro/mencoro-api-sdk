# OrganizationsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**archiveOrganization**](OrganizationsApi.md#archiveorganization) | **POST** /api/v1/organizations/{organizationId}/archive | Archive an organization |
| [**countOrganizationTrackedQueries**](OrganizationsApi.md#countorganizationtrackedqueries) | **GET** /api/v1/organizations/{organizationId}/usage/tracked-queries | Count the tracked queries an organization has configured |
| [**createOrganization**](OrganizationsApi.md#createorganizationoperation) | **POST** /api/v1/organizations | Create an organization |
| [**getEntitlements**](OrganizationsApi.md#getentitlements) | **GET** /api/v1/organizations/{organizationId}/entitlements | Get an organization\&#39;s plan allowance and consumption |
| [**getMembershipStats**](OrganizationsApi.md#getmembershipstats) | **GET** /api/v1/organizations/{organizationId}/membership-stats | Membership, project and invitation counts for an organization |
| [**getOrganization**](OrganizationsApi.md#getorganization) | **GET** /api/v1/organizations/{organizationId} | Get an organization |
| [**getOrganizationProjectedMonthlyChecks**](OrganizationsApi.md#getorganizationprojectedmonthlychecks) | **GET** /api/v1/organizations/{organizationId}/usage/projected-monthly-checks | Project a month of check consumption from the current tracking configuration |
| [**getOrganizationStats**](OrganizationsApi.md#getorganizationstats) | **GET** /api/v1/organizations/{organizationId}/stats | Headline counts for an organization |
| [**listOrganizations**](OrganizationsApi.md#listorganizations) | **GET** /api/v1/organizations | List accessible organizations |
| [**restoreOrganization**](OrganizationsApi.md#restoreorganization) | **POST** /api/v1/organizations/{organizationId}/restore | Restore an archived organization |
| [**updateOrganization**](OrganizationsApi.md#updateorganizationoperation) | **PATCH** /api/v1/organizations/{organizationId} | Update an organization profile |



## archiveOrganization

> OrganizationResource archiveOrganization(organizationId, xMencoroConfirmation, idempotencyKey)

Archive an organization

Minimum role: owner. Archiving also archives the active projects of the organization, cancels its pending invitations and cancels its subscription at the end of the current billing period. Those effects are applied by background subscribers, so a 200 means the organization was archived, not that every effect has finished. Preview it first to see exactly what will be touched.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { ArchiveOrganizationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | The `confirmation.token` returned by POST /api/v1/organization-operation-previews for this exact action, organization and body. Single use, valid for five minutes, and bound to the effects the preview declared: if the organization gained a project or lost an invitation in between, it is refused with 409 rather than doing more than was agreed. Without it the call answers 428.
    xMencoroConfirmation: mencoro_conf_VmajQznkILZjvFf63JexmT1AKX7iYZjOGSrBZYxlUTk,
    // string | Repeat it to retry a lost response. The replay is answered from the record without claiming the confirmation again, so a retry is never refused for presenting a confirmation the first attempt already spent.
    idempotencyKey: 5c1b8e42-0d7f-4a93-8c61-9b2e4d0a7f38,
  } satisfies ArchiveOrganizationRequest;

  try {
    const data = await api.archiveOrganization(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **xMencoroConfirmation** | `string` | The &#x60;confirmation.token&#x60; returned by POST /api/v1/organization-operation-previews for this exact action, organization and body. Single use, valid for five minutes, and bound to the effects the preview declared: if the organization gained a project or lost an invitation in between, it is refused with 409 rather than doing more than was agreed. Without it the call answers 428. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Repeat it to retry a lost response. The replay is answered from the record without claiming the confirmation again, so a retry is never refused for presenting a confirmation the first attempt already spent. | [Defaults to `undefined`] |

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The confirmation is invalid, expired, already used, or its declared effects changed; or the status transition is not allowed |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## countOrganizationTrackedQueries

> TrackedQueryUsageResource countOrganizationTrackedQueries(organizationId)

Count the tracked queries an organization has configured

Minimum role: viewer. How many tracked queries the organization has configured, counted live in PostgreSQL — the write model — over EVERY project it owns, archived projects included, and over every tracked query in them, active and paused alike. It is deliberately a DIFFERENT number from &#x60;aggregate.totalTrackedQueries&#x60; in getOrganizationOverview: that one sums a per-project copy held in the Elasticsearch read model and covers ACTIVE projects only, so it excludes archived projects and can lag behind a change that already shows here. Expect the two to disagree and do not treat either as wrong. This figure does reconcile exactly with countTrackedQueries, which counts one project through the same counter in the same store: sum its unfiltered &#x60;count&#x60; over every project, archived included, and you get this number. For the ACTIVE subset and what it will consume, call getOrganizationProjectedMonthlyChecks, which ranges over the same projects. Do NOT derive the paused count by subtracting one from the other: this number is read live from Postgres while that one is served from a cache invalidated by background subscribers, so the two can disagree while that invalidation catches up and the difference is then a count of nothing. For how many projects this ranges over, read &#x60;projects.total&#x60; and &#x60;projects.active&#x60; from getOrganizationStats. The value is never null: 0 means none are configured. This operation takes no query parameters — the population is fixed, and a parameter it cannot honour is rejected with 400 rather than silently ignored.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { CountOrganizationTrackedQueriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CountOrganizationTrackedQueriesRequest;

  try {
    const data = await api.countOrganizationTrackedQueries(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**TrackedQueryUsageResource**](TrackedQueryUsageResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization\&#39;s tracked-query count |  -  |
| **400** | A query parameter was sent to an operation that accepts none; the details name it |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createOrganization

> CreateOrganization201Response createOrganization(xMencoroConfirmation, idempotencyKey, createOrganizationRequest)

Create an organization

Requires a key scoped to all organizations and the \&quot;organization:manage\&quot; capability: a key limited to named organizations cannot widen its own reach by creating one. Preview it first and send the confirmation in X-Mencoro-Confirmation together with an Idempotency-Key.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { CreateOrganizationOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // string
    xMencoroConfirmation: xMencoroConfirmation_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // CreateOrganizationRequest
    createOrganizationRequest: ...,
  } satisfies CreateOrganizationOperationRequest;

  try {
    const data = await api.createOrganization(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xMencoroConfirmation** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **createOrganizationRequest** | [CreateOrganizationRequest](CreateOrganizationRequest.md) |  | |

### Return type

[**CreateOrganization201Response**](CreateOrganization201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Organization created. Your owner membership follows asynchronously, so a read immediately afterwards can answer 404 until it lands. |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key is not scoped to all organizations, or lacks \&quot;organization:manage\&quot; |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getEntitlements

> EntitlementsResource getEntitlements(organizationId)

Get an organization\&#39;s plan allowance and consumption

Minimum role: owner. Returns what the current plan allows, how much of it has been consumed and when the allowance next resets, taken from the most recent subscription contract whether it is running or cancelled. An organization that has never subscribed answers &#x60;status: \&quot;none\&quot;&#x60; with every budget and consumption field null — null means \&quot;no plan on file, so not known\&quot;, which is deliberately distinct from a budget or a consumption of zero. Commercial and provider details (prices, Stripe identifiers, internal tier codes) are not part of this contract.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { GetEntitlementsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetEntitlementsRequest;

  try {
    const data = await api.getEntitlements(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**EntitlementsResource**](EntitlementsResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization\&#39;s allowance and consumption |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller owns under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getMembershipStats

> GetMembershipStats200Response getMembershipStats(organizationId)

Membership, project and invitation counts for an organization

Minimum role: owner. Pre-computed counts of the organization\&#39;s members, projects and outstanding invitations, read from a materialized view that is refreshed periodically — &#x60;computedAt&#x60; says when the snapshot was taken, so a member added since the last refresh is not counted yet. Every count is always an integer and a zero means zero; an organization whose row has not been computed yet answers 404 with code &#x60;organization_membership_stats_not_found&#x60;, never a body of zeros, so \&quot;none\&quot; and \&quot;not known yet\&quot; are never confused. Counts cover the whole organization, active and inactive alike: &#x60;totalMembersCount&#x60; includes suspended members, and &#x60;totalProjectsCount&#x60; includes archived projects. &#x60;pendingInvitationsCount&#x60; counts only invitations that are still pending and not yet expired.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { GetMembershipStatsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetMembershipStatsRequest;

  try {
    const data = await api.getMembershipStats(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**GetMembershipStats200Response**](GetMembershipStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization\&#39;s membership snapshot |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller owns under this id (code &#x60;organization_not_found&#x60;), or the snapshot has not been computed for it yet (code &#x60;organization_membership_stats_not_found&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getOrganization

> OrganizationResource getOrganization(organizationId)

Get an organization

Minimum role: viewer. An organization outside the key\&#39;s scope, or one the caller is not an active member of, answers 404 - the API never confirms that an inaccessible organization exists.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { GetOrganizationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetOrganizationRequest;

  try {
    const data = await api.getOrganization(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getOrganizationProjectedMonthlyChecks

> ProjectedMonthlyChecksResource getOrganizationProjectedMonthlyChecks(organizationId)

Project a month of check consumption from the current tracking configuration

Minimum role: viewer. What the organization\&#39;s current configuration would consume in a month, in check budget units — the same unit &#x60;checkBudget&#x60; and &#x60;checksAvailable&#x60; are counted in by the entitlements operation — so the two are directly comparable when sizing a plan. The arithmetic is published so it can be reproduced rather than trusted: for each ACTIVE tracked query, runs per month (daily 30, weekly 4, monthly 1) multiplied by its nPasses, summed. A weekly query bills 4, not 4.345: a month is modelled as 30 days and 4 weeks, a planning convention rather than a calendar. Take &#x60;checkFrequency&#x60; and &#x60;nPasses&#x60; from the tracked-query listing and the arithmetic will match — though the two sides are read from different places and settle at different times: this figure is computed in the Postgres write model and served from a cache that background subscribers invalidate, while that listing reads an Elasticsearch projection. Immediately after a write the two can disagree; neither is wrong, they are catching up. PAUSED queries are excluded from both figures; archived PROJECTS are not — archiving a project does not pause its tracked queries, so they still count here, exactly as they do in countOrganizationTrackedQueries. &#x60;activeTrackedQueryCount&#x60; describes the same population as that count, minus the paused queries — but do not compute the difference to learn how many are paused: THIS OPERATION IS CACHED and that one is read live, so the two can disagree while the cache is invalidated in the background. This is a projection of the configuration, not a forecast of what will actually be spent: it does not look at the remaining plan budget, does not know which checks will be skipped or retried, and reserves and debits nothing. It is also not the &#x60;checkCost&#x60; of countTrackedQueries, which prices one round over one project rather than a month over the organization. Both values are never null: 0 means nothing is scheduled. This operation takes no query parameters — the population is fixed, and a parameter it cannot honour is rejected with 400 rather than silently ignored.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { GetOrganizationProjectedMonthlyChecksRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetOrganizationProjectedMonthlyChecksRequest;

  try {
    const data = await api.getOrganizationProjectedMonthlyChecks(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ProjectedMonthlyChecksResource**](ProjectedMonthlyChecksResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The projected monthly checks and the active tracked queries behind them |  -  |
| **400** | A query parameter was sent to an operation that accepts none; the details name it |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getOrganizationStats

> GetOrganizationStats200Response getOrganizationStats(organizationId)

Headline counts for an organization

Minimum role: viewer. Active members, projects (total and active) and pending invitations, in one call. Every value is a count and is always known: 0 means the organization really has none of that thing, and no field is ever null. &#x60;members.total&#x60; counts ACTIVE memberships only, so a suspended member is not included; &#x60;projects.total&#x60; counts every project including archived ones, and &#x60;projects.active&#x60; the non-archived subset. This is a current-state snapshot and takes no date window.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { GetOrganizationStatsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetOrganizationStatsRequest;

  try {
    const data = await api.getOrganizationStats(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**GetOrganizationStats200Response**](GetOrganizationStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization counts |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listOrganizations

> ListOrganizations200Response listOrganizations(limit, offset, search, status, sortBy, sortOrder)

List accessible organizations

Returns the organizations the key\&#39;s owner is an active member of, narrowed to the key\&#39;s scope. A key scoped to all organizations also sees organizations joined after it was created.Send &#x60;Accept: text/csv&#x60; to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no &#x60;total&#x60;, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with &#x60;&#x3D;&#x60;, &#x60;+&#x60;, &#x60;-&#x60; or &#x60;@&#x60; are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { ListOrganizationsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // number (optional)
    limit: 56,
    // number (optional)
    offset: 56,
    // string (optional)
    search: search_example,
    // 'active' | 'archived' (optional)
    status: status_example,
    // 'createdAt' | 'name' (optional)
    sortBy: sortBy_example,
    // 'asc' | 'desc' (optional)
    sortOrder: sortOrder_example,
  } satisfies ListOrganizationsRequest;

  try {
    const data = await api.listOrganizations(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | `number` |  | [Optional] [Defaults to `20`] |
| **offset** | `number` |  | [Optional] [Defaults to `0`] |
| **search** | `string` |  | [Optional] [Defaults to `undefined`] |
| **status** | `active`, `archived` |  | [Optional] [Defaults to `undefined`] [Enum: active, archived] |
| **sortBy** | `createdAt`, `name` |  | [Optional] [Defaults to `&#39;createdAt&#39;`] [Enum: createdAt, name] |
| **sortOrder** | `asc`, `desc` |  | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**ListOrganizations200Response**](ListOrganizations200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accessible organizations |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreOrganization

> OrganizationResource restoreOrganization(organizationId, xMencoroConfirmation, idempotencyKey)

Restore an archived organization

Minimum role: owner. Restoring reinstates the projects that were archived as part of archiving this organization - projects archived on their own stay archived - and aborts a pending subscription cancellation. Invitations cancelled by the archive are not reinstated. Preview it first to see which effects are reversible.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { RestoreOrganizationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    xMencoroConfirmation: xMencoroConfirmation_example,
    // string
    idempotencyKey: idempotencyKey_example,
  } satisfies RestoreOrganizationRequest;

  try {
    const data = await api.restoreOrganization(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **xMencoroConfirmation** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The confirmation is invalid, expired, already used, or its declared effects changed; or the status transition is not allowed |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateOrganization

> OrganizationResource updateOrganization(organizationId, xMencoroConfirmation, idempotencyKey, updateOrganizationRequest)

Update an organization profile

Minimum role: owner. A partial update: omit a field to leave it alone, send it as null to clear it. Preview it first; the confirmation is bound to the current values, so an edit made by somebody else in between invalidates it rather than being silently overwritten. The organization image is deliberately NOT writable here, although the Mencoro app accepts one in the equivalent call: a published JSON API is the wrong place to carry a 10MB base64 blob in a body that also has to be fingerprinted for idempotency and digested for the confirmation. The image stays readable as &#x60;imageUrl&#x60;; changing it is done in the app.

### Example

```ts
import {
  Configuration,
  OrganizationsApi,
} from '@mencoro/api';
import type { UpdateOrganizationOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    xMencoroConfirmation: xMencoroConfirmation_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // UpdateOrganizationRequest
    updateOrganizationRequest: ...,
  } satisfies UpdateOrganizationOperationRequest;

  try {
    const data = await api.updateOrganization(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **xMencoroConfirmation** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **updateOrganizationRequest** | [UpdateOrganizationRequest](UpdateOrganizationRequest.md) |  | |

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated organization |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The confirmation is invalid, expired, already used, or the organization changed since the preview |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

