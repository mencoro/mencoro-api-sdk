# ProjectsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**archiveProject**](ProjectsApi.md#archiveproject) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/archive | Archive a project |
| [**createCompetitor**](ProjectsApi.md#createcompetitoroperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | Add a competitor to a project |
| [**createProject**](ProjectsApi.md#createprojectoperation) | **POST** /api/v1/organizations/{organizationId}/projects | Create a project and the brand monitoring profile its checks run against |
| [**deleteCompetitor**](ProjectsApi.md#deletecompetitor) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Remove a competitor from a project |
| [**getBrandProfile**](ProjectsApi.md#getbrandprofile) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Get a project\&#39;s brand monitoring profile |
| [**getProject**](ProjectsApi.md#getproject) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId} | Get a project and its brand monitoring configuration |
| [**listCompetitors**](ProjectsApi.md#listcompetitors) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | List the competitors tracked by a project |
| [**listProjects**](ProjectsApi.md#listprojects) | **GET** /api/v1/organizations/{organizationId}/projects | List an organization\&#39;s projects |
| [**listQueryClusters**](ProjectsApi.md#listqueryclusters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | List the keyword clusters of a project |
| [**restoreProject**](ProjectsApi.md#restoreproject) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/restore | Restore an archived project |
| [**updateCompetitor**](ProjectsApi.md#updatecompetitor) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Replace a competitor |
| [**updateProject**](ProjectsApi.md#updateprojectoperation) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId} | Rename a project |
| [**updateProjectBrandProfile**](ProjectsApi.md#updateprojectbrandprofileoperation) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Replace a project\&#39;s brand monitoring profile |



## archiveProject

> ProjectDetailResource archiveProject(organizationId, projectId, idempotencyKey)

Archive a project

Minimum role: manager, in an active organization. Requires the \&quot;write\&quot; capability. Archiving stops a project from being modified: its name, brand profile and competitors are refused with 409 until it is restored. What is NOT done: nothing is deleted. Tracked queries, captured responses, mentions and every metric already collected stay exactly as they are, and restoreProject brings the project back with all of it. Archiving is recorded as done by the caller, not by an organization cascade, so restoring the organization later will not restore this project — restore it explicitly. This endpoint takes no body, and one carrying fields is refused. Archiving an already archived project answers 409, unless the call is a retry carrying the key that archived it. Send an Idempotency-Key; a retry with the same key returns the recorded answer.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { ArchiveProjectRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    idempotencyKey: idempotencyKey_example,
  } satisfies ArchiveProjectRequest;

  try {
    const data = await api.archiveProject(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project in its new state |  -  |
| **400** | A body was sent, or the Idempotency-Key was rejected |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is already archived, the organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createCompetitor

> CompetitorResource createCompetitor(organizationId, projectId, idempotencyKey, createCompetitorRequest)

Add a competitor to a project

Minimum role: manager, on an active organization and a project that is not archived. Creates one competitor with the domains and brand names its mentions are matched against. Both lists are required and neither may be empty: a competitor that matches on nothing would never be found in an answer. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \&quot;www.\&quot; is dropped. Duplicates are collapsed. The id is assigned by the server and cannot be chosen, and neither the auto-generated brand description nor the internal brand monitoring profile id can be set — sending either is refused as an unknown field. Adding a competitor does NOT re-match the answers already captured: it applies to checks from here on. A project whose brand monitoring profile has not been created yet answers 404. An Idempotency-Key header is required.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { CreateCompetitorOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the organization in the path.
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Unique per attempt. Without it a lost response cannot be retried without risking a second competitor.
    idempotencyKey: idempotencyKey_example,
    // CreateCompetitorRequest
    createCompetitorRequest: ...,
  } satisfies CreateCompetitorOperationRequest;

  try {
    const data = await api.createCompetitor(body);
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
| **projectId** | `string` | Must belong to the organization in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Unique per attempt. Without it a lost response cannot be retried without risking a second competitor. | [Defaults to `undefined`] |
| **createCompetitorRequest** | [CreateCompetitorRequest](CreateCompetitorRequest.md) |  | |

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The competitor as stored |  -  |
| **400** | The body failed validation, or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids, or the project has no brand monitoring profile |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createProject

> ProjectDetailResource createProject(organizationId, idempotencyKey, createProjectRequest)

Create a project and the brand monitoring profile its checks run against

Minimum role: manager, in an active organization. Requires the \&quot;write\&quot; capability. Creates the project, the brand monitoring profile holding the domains and brand names to watch, and one competitor per entry of &#x60;competitors&#x60;, in a single call. The project id is minted by the server; a caller-supplied id is rejected as an unknown field. What is NOT done: no tracked queries are created, no check is run and no scraping is scheduled — a new project has nothing collected against it until tracked queries are added. Each website entry may be a full URL or a bare domain: a URL is reduced to its host with any leading \&quot;www.\&quot; removed, so \&quot;https://www.acme.com/pricing\&quot; is stored as \&quot;acme.com\&quot;. Duplicate domains and duplicate brand names are collapsed, exactly as the stored value objects do. Send an Idempotency-Key: a retry with the same key and the same body returns this same project instead of creating a second one.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { CreateProjectOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    idempotencyKey: idempotencyKey_example,
    // CreateProjectRequest
    createProjectRequest: ...,
  } satisfies CreateProjectOperationRequest;

  try {
    const data = await api.createProject(body);
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
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **createProjectRequest** | [CreateProjectRequest](CreateProjectRequest.md) |  | |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created project and its brand monitoring configuration |  -  |
| **400** | The body or the Idempotency-Key was rejected; &#x60;details&#x60; names every field at fault |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteCompetitor

> CompetitorResource deleteCompetitor(organizationId, projectId, competitorId, idempotencyKey)

Remove a competitor from a project

Minimum role: manager, on an active organization and a project that is not archived. Removes the competitor and, asynchronously, every stored mention, search result and shopping result attributed to it, in AI answers and search captures already taken. This is permanent and it changes historical analytics: share of voice and competitor co-occurrence recomputed after the cascade will not include it. A 200 means the competitor is gone; the cascade runs on the event bus and finishes shortly afterwards. The response body is the competitor as it was immediately before removal, because it can no longer be read back. The request takes no body, and sending one is refused. A competitor belonging to another project answers 404, the same answer an unknown id gets. An Idempotency-Key header is required.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { DeleteCompetitorRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the organization in the path.
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    competitorId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Unique per attempt. A retry carrying the same key is answered from the record instead of running again.
    idempotencyKey: idempotencyKey_example,
  } satisfies DeleteCompetitorRequest;

  try {
    const data = await api.deleteCompetitor(body);
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
| **projectId** | `string` | Must belong to the organization in the path. | [Defaults to `undefined`] |
| **competitorId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Unique per attempt. A retry carrying the same key is answered from the record instead of running again. | [Defaults to `undefined`] |

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The competitor as it was immediately before removal |  -  |
| **400** | A body was sent, or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or competitor the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was reused for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getBrandProfile

> BrandProfileResource getBrandProfile(organizationId, projectId)

Get a project\&#39;s brand monitoring profile

Minimum role: viewer. The brand identity every check of this project is matched against: the tracked brand terms, the website domains, and the generated description of what the brand does. A null description means it has not been generated yet — the generator runs asynchronously after the names or domains change — which is not the same as an empty one. An empty brandNames or websiteDomains array means the profile exists and names nothing; a project whose profile has not been created at all answers 404.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { GetBrandProfileRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the organization in the path.
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetBrandProfileRequest;

  try {
    const data = await api.getBrandProfile(body);
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
| **projectId** | `string` | Must belong to the organization in the path. | [Defaults to `undefined`] |

### Return type

[**BrandProfileResource**](BrandProfileResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project\&#39;s brand monitoring profile |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids, or the project has no brand profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getProject

> ProjectDetailResource getProject(organizationId, projectId)

Get a project and its brand monitoring configuration

Minimum role: viewer. Returns the project together with the domains and brand names it is monitored for and the competitors it is measured against. A project that exists but belongs to another organization answers 404, never 403. A project that has been created but not yet configured for brand monitoring reports empty &#x60;websiteDomains&#x60;, &#x60;brandNames&#x60; and &#x60;competitors&#x60;. Headline metrics are not part of this response: use &#x60;listProjects&#x60; for the per-project figures, or &#x60;getProjectMetrics&#x60; for a window.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { GetProjectRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetProjectRequest;

  try {
    const data = await api.getProject(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project and its brand monitoring configuration |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id, or no project with this id inside it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listCompetitors

> ListCompetitors200Response listCompetitors(organizationId, projectId, limit, offset, sortOrder)

List the competitors tracked by a project

Minimum role: viewer. The competitors configured on the project, one page at a time, with the website domains and brand names each one is matched against. &#x60;total&#x60; counts every competitor of the project, not the size of this page, so a project with more than &#x60;limit&#x60; competitors needs &#x60;offset&#x60; to read them all. Ordering is by id, which for a UUID v7 is roughly creation order, and &#x60;sortOrder&#x60; chooses its direction; there is no other sort key and no text search, and sending &#x60;sortBy&#x60; or &#x60;search&#x60; is rejected rather than ignored. A project whose brand monitoring profile has not been created yet answers 200 with an empty collection, which means \&quot;nothing configured yet\&quot; rather than \&quot;no competitors found\&quot;. Internal fields the pipeline writes — the auto-generated brand description used by the mention classifier, and the internal brand monitoring profile id — are not part of this contract.Send &#x60;Accept: text/csv&#x60; to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no &#x60;total&#x60;, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with &#x60;; &#x60; as a display projection — parse the JSON if you need the structure. Cells beginning with &#x60;&#x3D;&#x60;, &#x60;+&#x60;, &#x60;-&#x60; or &#x60;@&#x60; are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { ListCompetitorsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Page size. A larger value is rejected, never silently reduced. (optional)
    limit: 56,
    // number | Number of competitors to skip before the page starts. (optional)
    offset: 56,
    // 'asc' | 'desc' | Direction of the id ordering. An unknown value is rejected, not replaced by the default. (optional)
    sortOrder: sortOrder_example,
  } satisfies ListCompetitorsRequest;

  try {
    const data = await api.listCompetitors(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **limit** | `number` | Page size. A larger value is rejected, never silently reduced. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Number of competitors to skip before the page starts. | [Optional] [Defaults to `0`] |
| **sortOrder** | `asc`, `desc` | Direction of the id ordering. An unknown value is rejected, not replaced by the default. | [Optional] [Defaults to `&#39;asc&#39;`] [Enum: asc, desc] |

### Return type

[**ListCompetitors200Response**](ListCompetitors200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project\&#39;s competitors |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listProjects

> ListProjects200Response listProjects(organizationId, limit, offset, search, status, sortBy, sortOrder)

List an organization\&#39;s projects

Minimum role: viewer. Metrics come from the same read model the application uses, so the figures match what the product shows. A null metric means \&quot;not known yet\&quot;, never zero.Send &#x60;Accept: text/csv&#x60; to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no &#x60;total&#x60;, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with &#x60;; &#x60; as a display projection — parse the JSON if you need the structure. Cells beginning with &#x60;&#x3D;&#x60;, &#x60;+&#x60;, &#x60;-&#x60; or &#x60;@&#x60; are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { ListProjectsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Page size. A larger value is rejected, never silently reduced. (optional)
    limit: 2,
    // number | Rows to skip before the page starts. Page by advancing it in steps of `limit` until it reaches `total`. (optional)
    offset: 4,
    // string (optional)
    search: search_example,
    // 'active' | 'archived' (optional)
    status: status_example,
    // 'createdAt' | 'name' | 'trackedQueryCount' | 'avgSerpPosition' | 'avgShoppingPosition' | 'avgMentionPosition' | 'avgLinkPosition' | 'mentionRate' | 'serpRate' | 'shoppingRate' | 'positivityIndex' | 'shareOfVoice' | 'serpPositionStability' | 'shoppingPositionStability' | 'lastRankDetectedAt' (optional)
    sortBy: sortBy_example,
    // 'asc' | 'desc' (optional)
    sortOrder: sortOrder_example,
  } satisfies ListProjectsRequest;

  try {
    const data = await api.listProjects(body);
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
| **limit** | `number` | Page size. A larger value is rejected, never silently reduced. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Rows to skip before the page starts. Page by advancing it in steps of &#x60;limit&#x60; until it reaches &#x60;total&#x60;. | [Optional] [Defaults to `0`] |
| **search** | `string` |  | [Optional] [Defaults to `undefined`] |
| **status** | `active`, `archived` |  | [Optional] [Defaults to `undefined`] [Enum: active, archived] |
| **sortBy** | `createdAt`, `name`, `trackedQueryCount`, `avgSerpPosition`, `avgShoppingPosition`, `avgMentionPosition`, `avgLinkPosition`, `mentionRate`, `serpRate`, `shoppingRate`, `positivityIndex`, `shareOfVoice`, `serpPositionStability`, `shoppingPositionStability`, `lastRankDetectedAt` |  | [Optional] [Defaults to `&#39;createdAt&#39;`] [Enum: createdAt, name, trackedQueryCount, avgSerpPosition, avgShoppingPosition, avgMentionPosition, avgLinkPosition, mentionRate, serpRate, shoppingRate, positivityIndex, shareOfVoice, serpPositionStability, shoppingPositionStability, lastRankDetectedAt] |
| **sortOrder** | `asc`, `desc` |  | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**ListProjects200Response**](ListProjects200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization\&#39;s projects |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listQueryClusters

> ListQueryClusters200Response listQueryClusters(organizationId, projectId, limit, offset, sortOrder)

List the keyword clusters of a project

Minimum role: viewer. The keyword clusters configured on a project, one page at a time. Each cluster id is exactly what the analytics operations accept in their queryClusterIds filter — pass the id, never the name. Names are unique within a project and are stored lower-cased, so the listing is ordered by name with no ties and paging over it neither repeats nor skips a cluster. &#x60;total&#x60; counts every cluster in the project, not the size of the page returned. A cluster carries no metrics of its own and no membership count: for the tracked queries inside a cluster, filter the tracked-query operations by its id. An empty list means the project has no clusters configured, which is not an error and is not a statement about whether any data has been collected.Send &#x60;Accept: text/csv&#x60; to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no &#x60;total&#x60;, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with &#x60;; &#x60; as a display projection — parse the JSON if you need the structure. Cells beginning with &#x60;&#x3D;&#x60;, &#x60;+&#x60;, &#x60;-&#x60; or &#x60;@&#x60; are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { ListQueryClustersRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Page size. A larger value is rejected, never silently reduced. (optional)
    limit: 56,
    // number | Number of clusters to skip before the page starts. (optional)
    offset: 56,
    // 'asc' | 'desc' | Direction of the name ordering. An unknown value is rejected, not replaced by the default. (optional)
    sortOrder: sortOrder_example,
  } satisfies ListQueryClustersRequest;

  try {
    const data = await api.listQueryClusters(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **limit** | `number` | Page size. A larger value is rejected, never silently reduced. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Number of clusters to skip before the page starts. | [Optional] [Defaults to `0`] |
| **sortOrder** | `asc`, `desc` | Direction of the name ordering. An unknown value is rejected, not replaced by the default. | [Optional] [Defaults to `&#39;asc&#39;`] [Enum: asc, desc] |

### Return type

[**ListQueryClusters200Response**](ListQueryClusters200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of the project\&#39;s keyword clusters and the total in the project |  -  |
| **400** | A pagination or ordering parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreProject

> ProjectDetailResource restoreProject(organizationId, projectId, idempotencyKey)

Restore an archived project

Minimum role: manager, in an active organization. Requires the \&quot;write\&quot; capability. Brings an archived project back to active, with every tracked query, capture and metric it had when it was archived. What is NOT done: no check is run and no scraping is scheduled as a result — collection resumes on the project\&#39;s own schedule. Restoring clears the record of who archived the project, so a project restored here is treated as an ordinary active project by any later organization archive. A project archived because its organization was archived cannot be restored on its own: restore the organization, which restores them all. Restoring a project that is already active answers 409, unless the call is a retry carrying the key that restored it. This endpoint takes no body, and one carrying fields is refused. Send an Idempotency-Key; a retry with the same key returns the recorded answer.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { RestoreProjectRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    idempotencyKey: idempotencyKey_example,
  } satisfies RestoreProjectRequest;

  try {
    const data = await api.restoreProject(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project in its new state |  -  |
| **400** | A body was sent, or the Idempotency-Key was rejected |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is not archived, the organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateCompetitor

> CompetitorResource updateCompetitor(organizationId, projectId, competitorId, idempotencyKey, createCompetitorRequest)

Replace a competitor

Minimum role: manager, on an active organization and a project that is not archived. Replaces the competitor\&#39;s name, domains and brand names: the lists sent become the lists stored, so a term left out is removed. Both lists are required and neither may be empty — a competitor that matches on nothing would never be found in an answer. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \&quot;www.\&quot; is dropped. Duplicates are collapsed. The auto-generated brand description cannot be set, and sending it is refused as an unknown field. Changing the matching rules does NOT re-match the answers already captured: it applies to checks from here on. A competitor belonging to another project answers 404, the same answer an unknown id gets. An Idempotency-Key header is required.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { UpdateCompetitorRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the organization in the path.
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    competitorId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
    idempotencyKey: idempotencyKey_example,
    // CreateCompetitorRequest
    createCompetitorRequest: ...,
  } satisfies UpdateCompetitorRequest;

  try {
    const data = await api.updateCompetitor(body);
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
| **projectId** | `string` | Must belong to the organization in the path. | [Defaults to `undefined`] |
| **competitorId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. | [Defaults to `undefined`] |
| **createCompetitorRequest** | [CreateCompetitorRequest](CreateCompetitorRequest.md) |  | |

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The competitor as stored |  -  |
| **400** | The body failed validation, or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or competitor the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateProject

> ProjectDetailResource updateProject(organizationId, projectId, idempotencyKey, updateProjectRequest)

Rename a project

Minimum role: manager, in an active organization. Requires the \&quot;write\&quot; capability. &#x60;name&#x60; is the only writable field and it is required. What is NOT done: the monitored domains and brand names are not touched (use updateProjectBrandProfile) and competitors are not touched, added or removed (use the competitor endpoints). Sending &#x60;websiteDomains&#x60;, &#x60;brandNames&#x60; or &#x60;competitors&#x60; here is refused with the field named, never applied in part and never ignored. Renaming a project changes nothing about the data already collected against it. A project that belongs to another organization answers 404, never 403. An archived project answers 409: restore it first — unless the call is a retry carrying the key of a rename that already succeeded, which is answered from the record whatever the project\&#39;s state is now. Send an Idempotency-Key; a retry with the same key and body returns the recorded answer.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { UpdateProjectOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    idempotencyKey: idempotencyKey_example,
    // UpdateProjectRequest
    updateProjectRequest: ...,
  } satisfies UpdateProjectOperationRequest;

  try {
    const data = await api.updateProject(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **updateProjectRequest** | [UpdateProjectRequest](UpdateProjectRequest.md) |  | |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project in its new state |  -  |
| **400** | The body or the Idempotency-Key was rejected; &#x60;details&#x60; names every field at fault |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, the organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateProjectBrandProfile

> BrandProfileResource updateProjectBrandProfile(organizationId, projectId, idempotencyKey, updateProjectBrandProfileRequest)

Replace a project\&#39;s brand monitoring profile

Minimum role: manager, on an active organization and a project that is not archived. Replaces the brand terms and website domains every check of this project is matched against: the lists sent become the lists stored, so a term left out is removed. Both lists are required and neither may be empty — a project must keep at least one brand name and one domain to match anything. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \&quot;www.\&quot; is dropped, which is the form the profile is read back in. Duplicates, including two URLs that reduce to the same host, are collapsed. This operation does NOT touch the project name or its competitors, which are separate resources, and it does not regenerate the brand description: that runs asynchronously afterwards, so the description in the response is the one stored at the time of the write. An Idempotency-Key header is required.

### Example

```ts
import {
  Configuration,
  ProjectsApi,
} from '@mencoro/api';
import type { UpdateProjectBrandProfileOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ProjectsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the organization in the path.
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
    idempotencyKey: idempotencyKey_example,
    // UpdateProjectBrandProfileRequest
    updateProjectBrandProfileRequest: ...,
  } satisfies UpdateProjectBrandProfileOperationRequest;

  try {
    const data = await api.updateProjectBrandProfile(body);
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
| **projectId** | `string` | Must belong to the organization in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. | [Defaults to `undefined`] |
| **updateProjectBrandProfileRequest** | [UpdateProjectBrandProfileRequest](UpdateProjectBrandProfileRequest.md) |  | |

### Return type

[**BrandProfileResource**](BrandProfileResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The profile as stored |  -  |
| **400** | The body failed validation, or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids, or the project has no brand profile |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

