# TrackedQueriesApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addClustersToTrackedQuery**](TrackedQueriesApi.md#addclusterstotrackedquery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Add a tracked query to clusters |
| [**batchChangeTrackedQueriesCheckFrequency**](TrackedQueriesApi.md#batchchangetrackedqueriescheckfrequency) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/check-frequency | Change how often several tracked queries are checked |
| [**batchChangeTrackedQueriesNPasses**](TrackedQueriesApi.md#batchchangetrackedqueriesnpasses) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/passes | Change how many passes several tracked queries run per check |
| [**batchCreateTrackedQueries**](TrackedQueriesApi.md#batchcreatetrackedqueries) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Create tracked queries |
| [**batchForceCheckTrackedQueries**](TrackedQueriesApi.md#batchforcechecktrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check | Check several tracked queries now |
| [**batchPauseTrackedQueries**](TrackedQueriesApi.md#batchpausetrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/pause | Pause several tracked queries |
| [**batchResumeTrackedQueries**](TrackedQueriesApi.md#batchresumetrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/resume | Resume several tracked queries |
| [**bulkAddClustersToTrackedQueries**](TrackedQueriesApi.md#bulkaddclusterstotrackedqueriesoperation) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Add many tracked queries to clusters |
| [**bulkDeleteTrackedQueries**](TrackedQueriesApi.md#bulkdeletetrackedqueries) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk-delete | Delete tracked queries |
| [**bulkRemoveClustersFromTrackedQueries**](TrackedQueriesApi.md#bulkremoveclustersfromtrackedqueriesoperation) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Remove many tracked queries from clusters |
| [**changeTrackedQueryCheckFrequency**](TrackedQueriesApi.md#changetrackedquerycheckfrequency) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/check-frequency | Change how often a tracked query is checked |
| [**changeTrackedQueryNPasses**](TrackedQueriesApi.md#changetrackedquerynpasses) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/passes | Change how many passes a tracked query runs per check |
| [**countTrackedQueries**](TrackedQueriesApi.md#counttrackedqueries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/count | Count a project\&#39;s tracked queries and price checking them |
| [**forceCheckAllActiveTrackedQueries**](TrackedQueriesApi.md#forcecheckallactivetrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check-all | Check every eligible tracked query of a project now |
| [**getTrackedQuery**](TrackedQueriesApi.md#gettrackedquery) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId} | Get a tracked query |
| [**pauseTrackedQuery**](TrackedQueriesApi.md#pausetrackedquery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/pause | Pause a tracked query |
| [**removeClustersFromTrackedQuery**](TrackedQueriesApi.md#removeclustersfromtrackedquery) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Remove a tracked query from clusters |
| [**reportAiResponse**](TrackedQueriesApi.md#reportairesponseoperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/responses/{aiResponseId}/report | Report a problem with a captured AI answer |
| [**resumeTrackedQuery**](TrackedQueriesApi.md#resumetrackedquery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/resume | Resume a tracked query |
| [**searchTrackedQueries**](TrackedQueriesApi.md#searchtrackedqueries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Search a project\&#39;s tracked queries |
| [**searchTrackedQueryMentionMatches**](TrackedQueriesApi.md#searchtrackedquerymentionmatches) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/mention-matches | List stored mention matches of a tracked query |
| [**searchTrackedQuerySerpMatches**](TrackedQueriesApi.md#searchtrackedqueryserpmatches) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/serp-matches | List stored serp matches of a tracked query |



## addClustersToTrackedQuery

> TrackedQueryDetailResource addClustersToTrackedQuery(organizationId, projectId, trackedQueryId, idempotencyKey, clusterMembershipRequestData)

Add a tracked query to clusters

Minimum role: manager. Adds the tracked query to every cluster named in \&quot;queryClusterIds\&quot; and answers with the query in its new state. Membership is a set: a cluster the query already belongs to is skipped, not reported as an error, and the response still lists it. Clusters the query belongs to and this call does not name are left alone — this adds, it does not replace the membership. Every cluster must belong to the project in the path; one that does not is rejected with its field named, and nothing is written. The \&quot;Idempotency-Key\&quot; header is required, and a repeat of the same key and body returns the recorded answer without adding anything again.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { AddClustersToTrackedQueryRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write.
    idempotencyKey: idempotencyKey_example,
    // ClusterMembershipRequestData
    clusterMembershipRequestData: ...,
  } satisfies AddClustersToTrackedQueryRequest;

  try {
    const data = await api.addClustersToTrackedQuery(body);
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
| **trackedQueryId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write. | [Defaults to `undefined`] |
| **clusterMembershipRequestData** | [ClusterMembershipRequestData](ClusterMembershipRequestData.md) |  | |

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tracked query, including the clusters it now belongs to |  -  |
| **400** | The body was rejected: an unknown field, a malformed cluster id, a cluster outside this project, or a missing Idempotency-Key |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or tracked query the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, the idempotency key was reused for a different body, or a cluster was deleted between validation and the write, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## batchChangeTrackedQueriesCheckFrequency

> BatchWriteOutcome batchChangeTrackedQueriesCheckFrequency(organizationId, projectId, idempotencyKey, batchChangeTrackedQueryCheckFrequencyRequestData)

Change how often several tracked queries are checked

Minimum role: manager. Sets the same check frequency on every tracked query named in &#x60;ids&#x60;, at most 100 distinct ids per call. The organization must be active and the project must not be archived. Partial success: an id that is not a tracked query of this project — unknown, malformed, already deleted, or belonging to somewhere else — is reported under &#x60;failed&#x60; with &#x60;tracked_query_not_found&#x60; while the rest are changed, and the call still answers 200. Nothing is rolled back because an item failed. Setting the frequency a query already has is accepted and changes nothing. This does NOT run a check and does not reschedule one already in flight. It never changes more than the ids it is given: there is no \&quot;change everything matching a filter\&quot; mode. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { BatchChangeTrackedQueriesCheckFrequencyRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
    idempotencyKey: idempotencyKey_example,
    // BatchChangeTrackedQueryCheckFrequencyRequestData
    batchChangeTrackedQueryCheckFrequencyRequestData: ...,
  } satisfies BatchChangeTrackedQueriesCheckFrequencyRequest;

  try {
    const data = await api.batchChangeTrackedQueriesCheckFrequency(body);
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
| **idempotencyKey** | `string` | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | [Defaults to `undefined`] |
| **batchChangeTrackedQueryCheckFrequencyRequestData** | [BatchChangeTrackedQueryCheckFrequencyRequestData](BatchChangeTrackedQueryCheckFrequencyRequestData.md) |  | |

### Return type

[**BatchWriteOutcome**](BatchWriteOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-id results. Read &#x60;failed&#x60;: a non-empty &#x60;failed&#x60; with a 200 is the normal partial-success answer. |  -  |
| **400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## batchChangeTrackedQueriesNPasses

> BatchWriteOutcome batchChangeTrackedQueriesNPasses(organizationId, projectId, idempotencyKey, batchChangeTrackedQueryPassesRequestData)

Change how many passes several tracked queries run per check

Minimum role: manager. Sets the same passes-per-check on every tracked query named in &#x60;ids&#x60;, at most 100 distinct ids per call. The organization must be active and the project must not be archived. Partial success, and two distinct reasons appear under &#x60;failed&#x60;: an id that is not a tracked query of this project answers &#x60;tracked_query_not_found&#x60;, and a &#x60;google_serp&#x60; or &#x60;google_shopping&#x60; query asked for more than one pass answers &#x60;n_passes_not_supported_for_engine&#x60; — those engines run a single pass. Both leave the rest of the batch changed and the call still answers 200. Setting the value back to 1 is always allowed, so a batch that lowers sampling never fails on engine grounds. This does NOT run a check and does not change history already captured. More passes cost proportionally more of the plan\&#39;s check budget. It never changes more than the ids it is given: there is no \&quot;change everything matching a filter\&quot; mode. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { BatchChangeTrackedQueriesNPassesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
    idempotencyKey: idempotencyKey_example,
    // BatchChangeTrackedQueryPassesRequestData
    batchChangeTrackedQueryPassesRequestData: ...,
  } satisfies BatchChangeTrackedQueriesNPassesRequest;

  try {
    const data = await api.batchChangeTrackedQueriesNPasses(body);
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
| **idempotencyKey** | `string` | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | [Defaults to `undefined`] |
| **batchChangeTrackedQueryPassesRequestData** | [BatchChangeTrackedQueryPassesRequestData](BatchChangeTrackedQueryPassesRequestData.md) |  | |

### Return type

[**BatchWriteOutcome**](BatchWriteOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-id results. Read &#x60;failed&#x60;: a non-empty &#x60;failed&#x60; with a 200 is the normal partial-success answer. |  -  |
| **400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## batchCreateTrackedQueries

> BatchCreateTrackedQueriesResultResource batchCreateTrackedQueries(organizationId, projectId, idempotencyKey, batchCreateTrackedQueriesRequestData)

Create tracked queries

Minimum role: manager. Creates the cross product of &#x60;queryTexts&#x60; x &#x60;engines&#x60; x &#x60;countries&#x60;: three texts, two engines and two countries create twelve tracked queries, not three. At most 100 combinations per call. The organization must be active and the project must not be archived. Partial success: the response lists, per combination, either the id it was created under or why nothing was created for it, and the status code never reports item-level outcomes. A combination the project already tracks is NOT created again and NOT re-identified — it appears under &#x60;failed&#x60; with &#x60;tracked_query_already_exists&#x60;, keeps the id it already had, and has any &#x60;queryClusterIds&#x60; in this request merged into it. Query text is normalised before it is compared and stored (lower-cased, whitespace collapsed, leading list markers stripped), so two texts differing only in those respects are one tracked query: the first of them owns the outcome and every later one appears under &#x60;failed&#x60; with &#x60;duplicate_combination_in_request&#x60;, naming the entry it repeats. &#x60;nPasses&#x60; applies to AI engines only: &#x60;google_serp&#x60; and &#x60;google_shopping&#x60; rows are always created with one pass, whatever is sent. Google AI Mode is unavailable in a few countries and those combinations are reported under &#x60;failed&#x60; rather than created. Creating a tracked query does not run a check: the first check happens on the normal schedule for the &#x60;checkFrequency&#x60; chosen. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without creating anything again.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { BatchCreateTrackedQueriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of creating anything again.
    idempotencyKey: idempotencyKey_example,
    // BatchCreateTrackedQueriesRequestData
    batchCreateTrackedQueriesRequestData: ...,
  } satisfies BatchCreateTrackedQueriesRequest;

  try {
    const data = await api.batchCreateTrackedQueries(body);
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
| **idempotencyKey** | `string` | A client-chosen key, unique per operation. Replaying it returns the first answer instead of creating anything again. | [Defaults to `undefined`] |
| **batchCreateTrackedQueriesRequestData** | [BatchCreateTrackedQueriesRequestData](BatchCreateTrackedQueriesRequestData.md) |  | |

### Return type

[**BatchCreateTrackedQueriesResultResource**](BatchCreateTrackedQueriesResultResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-combination results. Read &#x60;failed&#x60;: a non-empty &#x60;failed&#x60; with a 200 is the normal partial-success answer. |  -  |
| **400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or query cluster the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |
| **422** | A query cluster exists but belongs to another project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## batchForceCheckTrackedQueries

> BatchForceCheckTrackedQueries200Response batchForceCheckTrackedQueries(organizationId, projectId, idempotencyKey, batchTargetsRequestData)

Check several tracked queries now

Minimum role: manager. Asks for a fresh check of up to 100 named tracked queries straight away, ignoring how recently each was last checked. Answers 200 with per-item results and NO job id: a check that is already in flight for a query is reused rather than started again, so there is no id this operation could hand back that is guaranteed to exist. Follow progress on the tracked query itself — its lastCheckedAt advances when the check completes. A successful item means the check was accepted for submission with budget available for it at that moment; it does not mean the check has run. A checked query costs one budget unit per pass (nPasses), and items that do not fit the remaining budget are reported as failed with &#x60;check_budget_forecast_exhausted&#x60;, or &#x60;subscription_not_found&#x60; when the organization has no entitled subscription — they are never reported as successful. That budget figure is a forecast for this batch, and a pessimistic one: a tracked query already being checked is joined to the check in flight and costs nothing, but it is still debited here, so an item refused this way may have fitted. Resubmit it in a later batch rather than treating the refusal as a statement about your subscription. A paused query is reported as failed with &#x60;tracked_query_already_paused&#x60;: paused queries are never checked. An id that is not a tracked query of this project is reported as failed with &#x60;tracked_query_not_found&#x60;, exactly as an id that does not exist. Requires an Idempotency-Key header; a retry must repeat the same ids in the same order.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { BatchForceCheckTrackedQueriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Repeating a request with the same key and the same ids answers with the first attempt\'s result instead of submitting again.
    idempotencyKey: idempotencyKey_example,
    // BatchTargetsRequestData
    batchTargetsRequestData: ...,
  } satisfies BatchForceCheckTrackedQueriesRequest;

  try {
    const data = await api.batchForceCheckTrackedQueries(body);
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
| **idempotencyKey** | `string` | Repeating a request with the same key and the same ids answers with the first attempt\&#39;s result instead of submitting again. | [Defaults to `undefined`] |
| **batchTargetsRequestData** | [BatchTargetsRequestData](BatchTargetsRequestData.md) |  | |

### Return type

[**BatchForceCheckTrackedQueries200Response**](BatchForceCheckTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-item results. &#x60;failed&#x60; is always present, empty list included: read it rather than inferring success from the status. |  -  |
| **400** | The Idempotency-Key header is missing, the body carried an unknown field, or \&quot;ids\&quot; was absent, malformed or larger than 100 distinct entries |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## batchPauseTrackedQueries

> BatchPauseTrackedQueries200Response batchPauseTrackedQueries(organizationId, projectId, idempotencyKey, batchTargetsRequestData)

Pause several tracked queries

Minimum role: manager. Pauses up to 100 tracked queries of one project, each independently. Always answers 200 when the batch itself was processed: read &#x60;failed&#x60; to find out which items were not paused, never the status code. Items are never rolled back because a later one failed. An id that is already paused is reported as successful — pausing asserts a state, not a transition. An id that is not a tracked query of this project is reported as failed with &#x60;tracked_query_not_found&#x60;, exactly as an id that does not exist at all, and nothing is written for it. Pausing does not cancel a check that is already running. Requires an Idempotency-Key header; a retry must repeat the same ids in the same order to be recognised as a retry rather than refused as a reused key.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { BatchPauseTrackedQueriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Repeating a request with the same key and the same ids answers with the first attempt\'s result.
    idempotencyKey: idempotencyKey_example,
    // BatchTargetsRequestData
    batchTargetsRequestData: ...,
  } satisfies BatchPauseTrackedQueriesRequest;

  try {
    const data = await api.batchPauseTrackedQueries(body);
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
| **idempotencyKey** | `string` | Repeating a request with the same key and the same ids answers with the first attempt\&#39;s result. | [Defaults to `undefined`] |
| **batchTargetsRequestData** | [BatchTargetsRequestData](BatchTargetsRequestData.md) |  | |

### Return type

[**BatchPauseTrackedQueries200Response**](BatchPauseTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-item results. &#x60;failed&#x60; is always present, empty list included: read it rather than inferring success from the status. |  -  |
| **400** | The Idempotency-Key header is missing, the body carried an unknown field, or \&quot;ids\&quot; was absent, malformed or larger than 100 distinct entries |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## batchResumeTrackedQueries

> BatchResumeTrackedQueries200Response batchResumeTrackedQueries(organizationId, projectId, idempotencyKey, batchTargetsRequestData)

Resume several tracked queries

Minimum role: manager. Puts up to 100 paused tracked queries of one project back under the scheduler, each independently. Always answers 200 when the batch itself was processed: read &#x60;failed&#x60; to find out which items were not resumed, never the status code. Items are never rolled back because a later one failed. An id that is already active is reported as successful — resuming asserts a state, not a transition. An id that is not a tracked query of this project is reported as failed with &#x60;tracked_query_not_found&#x60;, exactly as an id that does not exist at all, and nothing is written for it. No check is run by this operation and nothing is back-filled for the time the queries spent paused. Requires an Idempotency-Key header; a retry must repeat the same ids in the same order to be recognised as a retry rather than refused as a reused key.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { BatchResumeTrackedQueriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Repeating a request with the same key and the same ids answers with the first attempt\'s result.
    idempotencyKey: idempotencyKey_example,
    // BatchTargetsRequestData
    batchTargetsRequestData: ...,
  } satisfies BatchResumeTrackedQueriesRequest;

  try {
    const data = await api.batchResumeTrackedQueries(body);
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
| **idempotencyKey** | `string` | Repeating a request with the same key and the same ids answers with the first attempt\&#39;s result. | [Defaults to `undefined`] |
| **batchTargetsRequestData** | [BatchTargetsRequestData](BatchTargetsRequestData.md) |  | |

### Return type

[**BatchResumeTrackedQueries200Response**](BatchResumeTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-item results. &#x60;failed&#x60; is always present, empty list included: read it rather than inferring success from the status. |  -  |
| **400** | The Idempotency-Key header is missing, the body carried an unknown field, or \&quot;ids\&quot; was absent, malformed or larger than 100 distinct entries |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## bulkAddClustersToTrackedQueries

> BulkAddClustersToTrackedQueries200Response bulkAddClustersToTrackedQueries(organizationId, projectId, idempotencyKey, bulkAddClustersToTrackedQueriesRequest)

Add many tracked queries to clusters

Minimum role: manager. Adds every tracked query named in \&quot;ids\&quot; to every cluster named in \&quot;queryClusterIds\&quot;. At most 100 distinct tracked queries per call; duplicates in \&quot;ids\&quot; are collapsed. Partial success: the answer is 200 with a per-item \&quot;successful\&quot; and \&quot;failed\&quot; list even when some items failed, nothing is rolled back, and an id that is not a tracked query of this project is reported as a failed item rather than dropped. Clusters not named are left alone — this adds, it does not replace membership. Every cluster must belong to the project in the path; one that does not is rejected with its field named and nothing is written at all. The \&quot;Idempotency-Key\&quot; header is required, and a repeat of the same key and body returns the recorded answer without running the batch again.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { BulkAddClustersToTrackedQueriesOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch.
    idempotencyKey: idempotencyKey_example,
    // BulkAddClustersToTrackedQueriesRequest
    bulkAddClustersToTrackedQueriesRequest: ...,
  } satisfies BulkAddClustersToTrackedQueriesOperationRequest;

  try {
    const data = await api.bulkAddClustersToTrackedQueries(body);
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
| **idempotencyKey** | `string` | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch. | [Defaults to `undefined`] |
| **bulkAddClustersToTrackedQueriesRequest** | [BulkAddClustersToTrackedQueriesRequest](BulkAddClustersToTrackedQueriesRequest.md) |  | |

### Return type

[**BulkAddClustersToTrackedQueries200Response**](BulkAddClustersToTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-item results. Read \&quot;failed\&quot;: a 200 does not mean every item succeeded. |  -  |
| **400** | The body was rejected: an unknown field, a malformed or missing id, more than 100 distinct ids, a cluster outside this project, or a missing Idempotency-Key |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## bulkDeleteTrackedQueries

> BatchWriteOutcome bulkDeleteTrackedQueries(organizationId, projectId, idempotencyKey, batchTargetsRequestData)

Delete tracked queries

Minimum role: manager. Permanently deletes the tracked queries named in &#x60;ids&#x60;, at most 100 distinct ids per call. The organization must be active and the project must not be archived. Deletion is hard and cannot be undone: the tracked query is removed along with its captured answers, matches, search pages and rank history, and any check already in flight for it is cancelled. Those cascades run in the background, so a 200 means the tracked queries were deleted, not that every derived record has finished being purged. Partial success: an id that is not a tracked query of this project — unknown, malformed, already deleted, or belonging to somewhere else — is reported under &#x60;failed&#x60; with &#x60;tracked_query_not_found&#x60; while the rest are deleted. It never deletes more than the ids it is given: there is no \&quot;delete everything matching a filter\&quot; mode. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without deleting anything again.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { BulkDeleteTrackedQueriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of deleting anything again.
    idempotencyKey: idempotencyKey_example,
    // BatchTargetsRequestData
    batchTargetsRequestData: ...,
  } satisfies BulkDeleteTrackedQueriesRequest;

  try {
    const data = await api.bulkDeleteTrackedQueries(body);
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
| **idempotencyKey** | `string` | A client-chosen key, unique per operation. Replaying it returns the first answer instead of deleting anything again. | [Defaults to `undefined`] |
| **batchTargetsRequestData** | [BatchTargetsRequestData](BatchTargetsRequestData.md) |  | |

### Return type

[**BatchWriteOutcome**](BatchWriteOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-id results. Read &#x60;failed&#x60;: a non-empty &#x60;failed&#x60; with a 200 is the normal partial-success answer. |  -  |
| **400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## bulkRemoveClustersFromTrackedQueries

> BulkRemoveClustersFromTrackedQueries200Response bulkRemoveClustersFromTrackedQueries(organizationId, projectId, idempotencyKey, bulkRemoveClustersFromTrackedQueriesRequest)

Remove many tracked queries from clusters

Minimum role: manager. Removes every tracked query named in \&quot;ids\&quot; from every cluster named in \&quot;queryClusterIds\&quot;. At most 100 distinct tracked queries per call; duplicates in \&quot;ids\&quot; are collapsed. Partial success: the answer is 200 with a per-item \&quot;successful\&quot; and \&quot;failed\&quot; list even when some items failed, nothing is rolled back, and an id that is not a tracked query of this project is reported as a failed item rather than dropped. Neither the clusters nor the tracked queries are deleted: only the membership between them. Every cluster must belong to the project in the path; one that does not is rejected with its field named and nothing is written at all. NOTE: this DELETE requires a request body — some HTTP client libraries and proxies strip bodies from DELETE, and a stripped body is refused with a validation error rather than interpreted as \&quot;remove everything\&quot;. The \&quot;Idempotency-Key\&quot; header is required, and a repeat of the same key and body returns the recorded answer without running the batch again.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { BulkRemoveClustersFromTrackedQueriesOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch.
    idempotencyKey: idempotencyKey_example,
    // BulkRemoveClustersFromTrackedQueriesRequest | Required. A DELETE with no body is rejected.
    bulkRemoveClustersFromTrackedQueriesRequest: ...,
  } satisfies BulkRemoveClustersFromTrackedQueriesOperationRequest;

  try {
    const data = await api.bulkRemoveClustersFromTrackedQueries(body);
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
| **idempotencyKey** | `string` | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch. | [Defaults to `undefined`] |
| **bulkRemoveClustersFromTrackedQueriesRequest** | [BulkRemoveClustersFromTrackedQueriesRequest](BulkRemoveClustersFromTrackedQueriesRequest.md) | Required. A DELETE with no body is rejected. | |

### Return type

[**BulkRemoveClustersFromTrackedQueries200Response**](BulkRemoveClustersFromTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-item results. Read \&quot;failed\&quot;: a 200 does not mean every item succeeded. |  -  |
| **400** | The body was rejected or missing: an unknown field, a malformed or missing id, more than 100 distinct ids, a cluster outside this project, a stripped DELETE body, or a missing Idempotency-Key |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## changeTrackedQueryCheckFrequency

> TrackedQueryDetailResource changeTrackedQueryCheckFrequency(organizationId, projectId, trackedQueryId, idempotencyKey, changeTrackedQueryCheckFrequencyRequestData)

Change how often a tracked query is checked

Minimum role: manager. Sets how often one tracked query is checked while it is active. The organization must be active and the project must not be archived. Setting the frequency it already has is accepted and changes nothing. This does NOT run a check, does not backfill history, and does not reschedule a check already in flight: the new cadence applies from the next time the query is considered. A paused query keeps the setting but is not checked until it is resumed. A tracked query belonging to another project answers 404, the same answer an unknown id gets. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { ChangeTrackedQueryCheckFrequencyRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
    idempotencyKey: idempotencyKey_example,
    // ChangeTrackedQueryCheckFrequencyRequestData
    changeTrackedQueryCheckFrequencyRequestData: ...,
  } satisfies ChangeTrackedQueryCheckFrequencyRequest;

  try {
    const data = await api.changeTrackedQueryCheckFrequency(body);
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
| **trackedQueryId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | [Defaults to `undefined`] |
| **changeTrackedQueryCheckFrequencyRequestData** | [ChangeTrackedQueryCheckFrequencyRequestData](ChangeTrackedQueryCheckFrequencyRequestData.md) |  | |

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tracked query in its new state |  -  |
| **400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or tracked query the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## changeTrackedQueryNPasses

> TrackedQueryDetailResource changeTrackedQueryNPasses(organizationId, projectId, trackedQueryId, idempotencyKey, changeTrackedQueryPassesRequestData)

Change how many passes a tracked query runs per check

Minimum role: manager. Sets how many times one tracked query is asked per check. AI engines are not deterministic, so several passes are averaged; &#x60;google_serp&#x60; and &#x60;google_shopping&#x60; run a single pass and refuse any value above one with 409 &#x60;n_passes_not_supported_for_engine&#x60;. Setting the value back to 1 is always allowed. The organization must be active and the project must not be archived. Setting the value it already has is accepted and changes nothing. This does NOT run a check and does not change history already captured: it applies from the next check. More passes cost proportionally more of the plan\&#39;s check budget. A tracked query belonging to another project answers 404, the same answer an unknown id gets. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { ChangeTrackedQueryNPassesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
    idempotencyKey: idempotencyKey_example,
    // ChangeTrackedQueryPassesRequestData
    changeTrackedQueryPassesRequestData: ...,
  } satisfies ChangeTrackedQueryNPassesRequest;

  try {
    const data = await api.changeTrackedQueryNPasses(body);
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
| **trackedQueryId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | [Defaults to `undefined`] |
| **changeTrackedQueryPassesRequestData** | [ChangeTrackedQueryPassesRequestData](ChangeTrackedQueryPassesRequestData.md) |  | |

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tracked query in its new state |  -  |
| **400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or tracked query the caller can access under these ids |  -  |
| **409** | The engine runs a single pass and cannot take more; or the organization or project is archived; or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## countTrackedQueries

> TrackedQueryCountResource countTrackedQueries(organizationId, projectId, status)

Count a project\&#39;s tracked queries and price checking them

Minimum role: viewer. Two numbers about one project: how many tracked queries it holds, and what force-checking that same set would cost. Omit &#x60;status&#x60; to count every tracked query whatever its status; send &#x60;active&#x60; or &#x60;paused&#x60; to count and price only those. &#x60;checkCost&#x60; is a PRICED DRY RUN expressed in check budget units — one unit per pass, the same unit the plan allowance is counted in, so it is directly comparable with &#x60;checksAvailable&#x60; from the entitlements operation — and it is the sum of each matched tracked query\&#39;s configured passes. Asking reserves nothing, debits nothing and starts no check. It is deliberately NOT a forecast of what the check-all operation will consume: that operation skips paused queries, skips a query whose check is already pending or running, re-runs a check awaiting retry without charging for it again, and stops at whatever budget is left — none of which is subtracted here. Count with &#x60;status&#x3D;active&#x60; for the figure closest to a full check-all. Both numbers are read from the write model, so a tracked query created moments ago is already in them; that is why they can be AHEAD of the &#x60;total&#x60; returned by the tracked-queries listing, which counts a search projection, and ahead of the keyword listings, which read projections refreshed in the background. Summing the unfiltered count over every project of an organization, archived projects included, reproduces countOrganizationTrackedQueries, which counts through the same counter in the same store. An archived project still answers, because this is a read, but no check can be submitted there while it stays archived, so its cost is hypothetical. For a month of scheduled rounds across the whole organization instead of one round over one project, read getOrganizationProjectedMonthlyChecks. No monetary amount is published or implied: the cost of a check is published only in budget units.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { CountTrackedQueriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // 'active' | 'paused' | Restrict both numbers to one status. Lower-case; an unknown value is rejected, not ignored. Omitted, every status is counted and priced. (optional)
    status: status_example,
  } satisfies CountTrackedQueriesRequest;

  try {
    const data = await api.countTrackedQueries(body);
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
| **status** | `active`, `paused` | Restrict both numbers to one status. Lower-case; an unknown value is rejected, not ignored. Omitted, every status is counted and priced. | [Optional] [Defaults to `undefined`] [Enum: active, paused] |

### Return type

[**TrackedQueryCountResource**](TrackedQueryCountResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tracked query count and the budget cost of checking that set |  -  |
| **400** | The status parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## forceCheckAllActiveTrackedQueries

> SubmittedChecksResource forceCheckAllActiveTrackedQueries(organizationId, projectId, idempotencyKey)

Check every eligible tracked query of a project now

Minimum role: manager. Submits a fresh check for every eligible tracked query of the project, ignoring how recently each was last checked, least-recently-checked first, and at most 1000 tracked queries per call. Eligible is narrower than active: a paused query is skipped, and so is one whose check is already pending or running for the same engine. A query whose check is awaiting a retry is included and, WHEN THE ENGINE HAS NOT CHANGED SINCE, costs nothing extra, because its first submission already paid for it; if the engine did change, the pending run is replaced and the replacement is paid for. What is left is trimmed to what the organization\&#39;s remaining check budget can pay for — a check costs one budget unit per pass. While a subscription is cancelled but still inside its paid grace window nothing is submitted at all and &#x60;submitted&#x60; is 0; name the queries explicitly through the check operation to run them in that window. CALLING AGAIN DOES NOT CONTINUE WHERE THIS CALL STOPPED: submissions are handed to a worker, and a tracked query stops being selected only once that worker has started its check, so a second call made before the queue drains selects and submits the same tracked queries again. That is safe while the first check is still running — the duplicate is collapsed, and nothing is checked or charged twice — but a check that has already finished is run again and charged again, because this operation ignores staleness by design. To cover a project with more than 1000 eligible tracked queries, wait for the submitted wave to be picked up — each tracked query\&#39;s lastCheckedAt advances when its check completes — and call again then. The response lists the tracked queries submitted and carries NO job id: a check already in flight is reused rather than started again, so no id could be guaranteed to exist. Submission is accepted, not completed: a listed tracked query can still lose the last budget units to another caller before the worker reaches it. The request takes no body, and any field sent is rejected. Requires an Idempotency-Key header.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { ForceCheckAllActiveTrackedQueriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Repeating a request with the same key answers with the first attempt\'s result instead of submitting a second wave.
    idempotencyKey: idempotencyKey_example,
  } satisfies ForceCheckAllActiveTrackedQueriesRequest;

  try {
    const data = await api.forceCheckAllActiveTrackedQueries(body);
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
| **idempotencyKey** | `string` | Repeating a request with the same key answers with the first attempt\&#39;s result instead of submitting a second wave. | [Defaults to `undefined`] |

### Return type

[**SubmittedChecksResource**](SubmittedChecksResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tracked queries submitted for a check |  -  |
| **400** | The Idempotency-Key header is missing or malformed, or the request carried a body |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getTrackedQuery

> TrackedQueryDetailResource getTrackedQuery(organizationId, projectId, trackedQueryId)

Get a tracked query

Minimum role: viewer. The configuration of one tracked query: the text sent to the engine, the engine, locale and country it is asked in, the clusters it belongs to, and how often it is checked. A lastCheckedAt of null means no check has completed yet — it is not a check that found nothing. A tracked query belonging to another project answers 404, the same answer an unknown id gets, so the API never confirms that an inaccessible tracked query exists. Rank positions, share of voice and sentiment are not part of this response: they belong to a date window and are served by the analytics endpoints.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { GetTrackedQueryRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetTrackedQueryRequest;

  try {
    const data = await api.getTrackedQuery(body);
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
| **trackedQueryId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tracked query |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization, project or tracked query the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## pauseTrackedQuery

> TrackedQueryDetailResource pauseTrackedQuery(organizationId, projectId, trackedQueryId, idempotencyKey)

Pause a tracked query

Minimum role: manager. Stops the scheduler from checking this tracked query; it keeps its configuration, its clusters and every result already collected, and nothing is deleted. Pausing a query that is already paused succeeds and answers the same body — this is a PUT asserting a state, not a transition, so it is safe to repeat. It does NOT cancel a check that is already running: a check in flight when the pause lands still completes and still consumes the budget unit it reserved. The request takes no body, and any field sent is rejected. Requires an Idempotency-Key header.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { PauseTrackedQueryRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Repeating a request with the same key answers with the first attempt\'s result instead of pausing again.
    idempotencyKey: idempotencyKey_example,
  } satisfies PauseTrackedQueryRequest;

  try {
    const data = await api.pauseTrackedQuery(body);
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
| **trackedQueryId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Repeating a request with the same key answers with the first attempt\&#39;s result instead of pausing again. | [Defaults to `undefined`] |

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tracked query, paused |  -  |
| **400** | The Idempotency-Key header is missing or malformed, or the request carried a body |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or tracked query the caller can access under these ids |  -  |
| **409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## removeClustersFromTrackedQuery

> TrackedQueryDetailResource removeClustersFromTrackedQuery(organizationId, projectId, trackedQueryId, idempotencyKey, clusterMembershipRequestData)

Remove a tracked query from clusters

Minimum role: manager. Removes the tracked query from every cluster named in \&quot;queryClusterIds\&quot; and answers with the query in its new state. A cluster the query does not belong to is skipped, not reported as an error. Neither the clusters nor the tracked query are deleted: only the membership between them. Every cluster must belong to the project in the path. NOTE: this DELETE requires a request body — some HTTP client libraries and proxies strip bodies from DELETE, and a stripped body is refused with a validation error rather than interpreted as \&quot;remove all clusters\&quot;. The \&quot;Idempotency-Key\&quot; header is required, and a repeat of the same key and body returns the recorded answer without removing anything again.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { RemoveClustersFromTrackedQueryRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write.
    idempotencyKey: idempotencyKey_example,
    // ClusterMembershipRequestData | Required. A DELETE with no body is rejected.
    clusterMembershipRequestData: ...,
  } satisfies RemoveClustersFromTrackedQueryRequest;

  try {
    const data = await api.removeClustersFromTrackedQuery(body);
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
| **trackedQueryId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write. | [Defaults to `undefined`] |
| **clusterMembershipRequestData** | [ClusterMembershipRequestData](ClusterMembershipRequestData.md) | Required. A DELETE with no body is rejected. | |

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tracked query, including the clusters it still belongs to |  -  |
| **400** | The body was rejected or missing: an unknown field, a malformed cluster id, a cluster outside this project, a stripped DELETE body, or a missing Idempotency-Key |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or tracked query the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, the idempotency key was reused for a different body, or a cluster was deleted between validation and the write, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## reportAiResponse

> AiResponseReportResource reportAiResponse(organizationId, projectId, trackedQueryId, aiResponseId, idempotencyKey, reportAiResponseRequest)

Report a problem with a captured AI answer

Minimum role: viewer — deliberately lower than the other tracked-query writes, because a report changes nothing a viewer cannot already read. The key still needs the \&quot;write\&quot; capability. The report is forwarded to the team that reviews the scrape run behind the capture; it does not change the capture, the tracked query, or any metric derived from them, and nothing in this API will show the report afterwards. A 200 means the report was accepted for review, not that anything was corrected, and there is no identifier to poll. A capture that belongs to another tracked query or project answers 404, the same answer an unknown id gets. A capture that cannot be routed back to its scrape run answers 409 \&quot;ai_check_session_unavailable\&quot;, and it cannot be reported. That code covers two moments, which behave differently for your key: when the capture carries no scrape run at all the refusal is decided BEFORE anything is sent, so the idempotency key is left unused and the same key answers the same way however often it is presented; when the review system itself rejects the run — its own retention having elapsed — the refusal comes after the forward was attempted, so the key is spent like any outcome we cannot confirm. You can tell them apart without guessing: retry the same key, and a reply of \&quot;operation_outcome_uncertain\&quot; means the refusal came from the review system. Delivery is at-most-once: the \&quot;Idempotency-Key\&quot; header is required and a repeat of the same key and body returns the recorded answer, but a delivery whose outcome is unknown refuses replay on that key rather than risk filing the report twice.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { ReportAiResponseOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A capture id from the AI responses listing. Must belong to the tracked query in the path.
    aiResponseId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | A client-chosen key, unique per report, so a lost response can be retried without filing the report twice.
    idempotencyKey: idempotencyKey_example,
    // ReportAiResponseRequest
    reportAiResponseRequest: ...,
  } satisfies ReportAiResponseOperationRequest;

  try {
    const data = await api.reportAiResponse(body);
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
| **trackedQueryId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |
| **aiResponseId** | `string` | A capture id from the AI responses listing. Must belong to the tracked query in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A client-chosen key, unique per report, so a lost response can be retried without filing the report twice. | [Defaults to `undefined`] |
| **reportAiResponseRequest** | [ReportAiResponseRequest](ReportAiResponseRequest.md) |  | |

### Return type

[**AiResponseReportResource**](AiResponseReportResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The report as accepted, in its normalised form |  -  |
| **400** | The body was rejected: an unknown field, a missing or unsupported \&quot;type\&quot;, an over-long comment or brand name, or a missing Idempotency-Key |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project, tracked query or capture the caller can access under these ids |  -  |
| **409** | The organization is archived, the capture can no longer be routed back to its scrape run, the idempotency key was reused for a different body, or a previous attempt with this key ended with an unknown outcome |  -  |
| **502** | The review system could not be reached or refused the forward. Whether the report was filed is UNKNOWN: delivery is at-most-once and the failure can happen after the report was recorded upstream. This idempotency key will not replay; retrying with a new key may file the report twice. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## resumeTrackedQuery

> TrackedQueryDetailResource resumeTrackedQuery(organizationId, projectId, trackedQueryId, idempotencyKey)

Resume a tracked query

Minimum role: manager. Puts a paused tracked query back under the scheduler. Resuming a query that is already active succeeds and answers the same body — this is a PUT asserting a state, not a transition. It does NOT run a check: the query is checked when it next falls due under its own checkFrequency, and results collected while it was paused are unaffected. Nothing is back-filled for the time it spent paused. The request takes no body, and any field sent is rejected. Requires an Idempotency-Key header.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { ResumeTrackedQueryRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Repeating a request with the same key answers with the first attempt\'s result instead of resuming again.
    idempotencyKey: idempotencyKey_example,
  } satisfies ResumeTrackedQueryRequest;

  try {
    const data = await api.resumeTrackedQuery(body);
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
| **trackedQueryId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Repeating a request with the same key answers with the first attempt\&#39;s result instead of resuming again. | [Defaults to `undefined`] |

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tracked query, active |  -  |
| **400** | The Idempotency-Key header is missing or malformed, or the request carried a body |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or tracked query the caller can access under these ids |  -  |
| **409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## searchTrackedQueries

> SearchTrackedQueries200Response searchTrackedQueries(organizationId, projectId, limit, offset, search, status, engines, countries, sortBy, sortOrder)

Search a project\&#39;s tracked queries

Minimum role: viewer. One row per tracked query — a single keyword on a single engine in a single country — carrying the metrics of its most recent completed check. Filter by status, engine, country and a free-text search over the keyword, and sort by any of the returned metrics. Positions (lastSerpPosition, lastMentionPosition, lastLinkPosition, lastShoppingPosition) are 1-based ranks, so LOWER is better; lastShareOfVoice and lastPositivityIndex are percentages from 0 to 100, where HIGHER is better. Every nullable field means \&quot;not known yet\&quot; rather than zero: a null position is a query with no data for that surface, a null lastPositivityIndex is a check with no mentions to score, and a null lastCheckedAt is a query that has never been checked — none of them is a score of zero. This listing reads a projection refreshed by background subscribers, not the write model, so a tracked query created or changed moments ago may not appear here yet or may still show its previous settings. It catches up on its own; nothing is lost. If you need to read back what you just wrote, the creation response carries the new ids and the single tracked-query operation reads the write model directly. total counts the tracked queries the filters match, not the rows on this page. A limit above the maximum is rejected, never clamped, and a filter this endpoint does not support is rejected rather than ignored.Send &#x60;Accept: text/csv&#x60; to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no &#x60;total&#x60;, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with &#x60;; &#x60; as a display projection — parse the JSON if you need the structure. Cells beginning with &#x60;&#x3D;&#x60;, &#x60;+&#x60;, &#x60;-&#x60; or &#x60;@&#x60; are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { SearchTrackedQueriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Page size. A value above the maximum is rejected, never clamped. (optional)
    limit: 56,
    // number (optional)
    offset: 56,
    // string | Free-text search over the keyword. (optional)
    search: search_example,
    // 'active' | 'paused' (optional)
    status: status_example,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. (optional)
    engines: ...,
    // Array<string> | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    countries: ...,
    // 'queryText' | 'lastSerpPosition' | 'lastMentionPosition' | 'lastShoppingPosition' | 'lastShareOfVoice' | 'lastPositivityIndex' | 'lastMentionCount' | 'lastCheckedAt' (optional)
    sortBy: sortBy_example,
    // 'asc' | 'desc' (optional)
    sortOrder: sortOrder_example,
  } satisfies SearchTrackedQueriesRequest;

  try {
    const data = await api.searchTrackedQueries(body);
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
| **limit** | `number` | Page size. A value above the maximum is rejected, never clamped. | [Optional] [Defaults to `20`] |
| **offset** | `number` |  | [Optional] [Defaults to `0`] |
| **search** | `string` | Free-text search over the keyword. | [Optional] [Defaults to `undefined`] |
| **status** | `active`, `paused` |  | [Optional] [Defaults to `undefined`] [Enum: active, paused] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | `Array<string>` | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [Optional] |
| **sortBy** | `queryText`, `lastSerpPosition`, `lastMentionPosition`, `lastShoppingPosition`, `lastShareOfVoice`, `lastPositivityIndex`, `lastMentionCount`, `lastCheckedAt` |  | [Optional] [Defaults to `&#39;queryText&#39;`] [Enum: queryText, lastSerpPosition, lastMentionPosition, lastShoppingPosition, lastShareOfVoice, lastPositivityIndex, lastMentionCount, lastCheckedAt] |
| **sortOrder** | `asc`, `desc` |  | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**SearchTrackedQueries200Response**](SearchTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project\&#39;s tracked queries |  -  |
| **400** | A filter or page bound was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## searchTrackedQueryMentionMatches

> SearchTrackedQueryMentionMatches200Response searchTrackedQueryMentionMatches(organizationId, projectId, trackedQueryId, dateFrom, dateTo, limit, offset, sortOrder)

List stored mention matches of a tracked query

Minimum role: viewer. Text mentions across own brand and tracked or untracked competitors. Citation-only rows are excluded before pagination. Read mentionRelation to distinguish own brand from untracked competitors; a null competitorId alone does not classify the mention. Newest first by detection time, with an id tie-break. Dates cover whole UTC days. Only the retained 16-month window is readable, including when dateFrom is omitted. Unknown filters are rejected. The total counts all matching rows before pagination. Send Accept: text/csv for the same bounded page and filters as CSV, with formula-safe cells and no total.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { SearchTrackedQueryMentionMatchesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive UTC day; defaults to the retention floor. (optional)
    dateFrom: 2013-10-20,
    // Date | Inclusive UTC day. (optional)
    dateTo: 2013-10-20,
    // number (optional)
    limit: 56,
    // number (optional)
    offset: 56,
    // 'asc' | 'desc' (optional)
    sortOrder: sortOrder_example,
  } satisfies SearchTrackedQueryMentionMatchesRequest;

  try {
    const data = await api.searchTrackedQueryMentionMatches(body);
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
| **trackedQueryId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive UTC day; defaults to the retention floor. | [Optional] [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive UTC day. | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `20`] |
| **offset** | `number` |  | [Optional] [Defaults to `0`] |
| **sortOrder** | `asc`, `desc` |  | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**SearchTrackedQueryMentionMatches200Response**](SearchTrackedQueryMentionMatches200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stored matches and total under the same filters |  -  |
| **400** | Invalid or unsupported query parameters |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | Organization, project or tracked query is not accessible |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## searchTrackedQuerySerpMatches

> SearchTrackedQuerySerpMatches200Response searchTrackedQuerySerpMatches(organizationId, projectId, trackedQueryId, dateFrom, dateTo, limit, offset, sortOrder)

List stored serp matches of a tracked query

Minimum role: viewer. Stored organic-search matches with the competitor attribution and position recorded at detection time. A null competitorId identifies the own-brand match. These are historical matches, not a reclassification using the current brand profile. Newest first by detection time, with an id tie-break. Dates cover whole UTC days. Only the retained 16-month window is readable, including when dateFrom is omitted. Unknown filters are rejected. The total counts all matching rows before pagination. Send Accept: text/csv for the same bounded page and filters as CSV, with formula-safe cells and no total.

### Example

```ts
import {
  Configuration,
  TrackedQueriesApi,
} from '@mencoro/api';
import type { SearchTrackedQuerySerpMatchesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TrackedQueriesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive UTC day; defaults to the retention floor. (optional)
    dateFrom: 2013-10-20,
    // Date | Inclusive UTC day. (optional)
    dateTo: 2013-10-20,
    // number (optional)
    limit: 56,
    // number (optional)
    offset: 56,
    // 'asc' | 'desc' (optional)
    sortOrder: sortOrder_example,
  } satisfies SearchTrackedQuerySerpMatchesRequest;

  try {
    const data = await api.searchTrackedQuerySerpMatches(body);
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
| **trackedQueryId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive UTC day; defaults to the retention floor. | [Optional] [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive UTC day. | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `20`] |
| **offset** | `number` |  | [Optional] [Defaults to `0`] |
| **sortOrder** | `asc`, `desc` |  | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**SearchTrackedQuerySerpMatches200Response**](SearchTrackedQuerySerpMatches200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stored matches and total under the same filters |  -  |
| **400** | Invalid or unsupported query parameters |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | Organization, project or tracked query is not accessible |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

