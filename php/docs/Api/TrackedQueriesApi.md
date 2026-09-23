# Mencoro\Api\TrackedQueriesApi



All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addClustersToTrackedQuery()**](TrackedQueriesApi.md#addClustersToTrackedQuery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Add a tracked query to clusters |
| [**batchChangeTrackedQueriesCheckFrequency()**](TrackedQueriesApi.md#batchChangeTrackedQueriesCheckFrequency) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/check-frequency | Change how often several tracked queries are checked |
| [**batchChangeTrackedQueriesNPasses()**](TrackedQueriesApi.md#batchChangeTrackedQueriesNPasses) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/passes | Change how many passes several tracked queries run per check |
| [**batchCreateTrackedQueries()**](TrackedQueriesApi.md#batchCreateTrackedQueries) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Create tracked queries |
| [**batchForceCheckTrackedQueries()**](TrackedQueriesApi.md#batchForceCheckTrackedQueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check | Check several tracked queries now |
| [**batchPauseTrackedQueries()**](TrackedQueriesApi.md#batchPauseTrackedQueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/pause | Pause several tracked queries |
| [**batchResumeTrackedQueries()**](TrackedQueriesApi.md#batchResumeTrackedQueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/resume | Resume several tracked queries |
| [**bulkAddClustersToTrackedQueries()**](TrackedQueriesApi.md#bulkAddClustersToTrackedQueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Add many tracked queries to clusters |
| [**bulkDeleteTrackedQueries()**](TrackedQueriesApi.md#bulkDeleteTrackedQueries) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk-delete | Delete tracked queries |
| [**bulkRemoveClustersFromTrackedQueries()**](TrackedQueriesApi.md#bulkRemoveClustersFromTrackedQueries) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Remove many tracked queries from clusters |
| [**changeTrackedQueryCheckFrequency()**](TrackedQueriesApi.md#changeTrackedQueryCheckFrequency) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/check-frequency | Change how often a tracked query is checked |
| [**changeTrackedQueryNPasses()**](TrackedQueriesApi.md#changeTrackedQueryNPasses) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/passes | Change how many passes a tracked query runs per check |
| [**countTrackedQueries()**](TrackedQueriesApi.md#countTrackedQueries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/count | Count a project&#39;s tracked queries and price checking them |
| [**forceCheckAllActiveTrackedQueries()**](TrackedQueriesApi.md#forceCheckAllActiveTrackedQueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check-all | Check every eligible tracked query of a project now |
| [**getTrackedQuery()**](TrackedQueriesApi.md#getTrackedQuery) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId} | Get a tracked query |
| [**pauseTrackedQuery()**](TrackedQueriesApi.md#pauseTrackedQuery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/pause | Pause a tracked query |
| [**removeClustersFromTrackedQuery()**](TrackedQueriesApi.md#removeClustersFromTrackedQuery) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Remove a tracked query from clusters |
| [**reportAiResponse()**](TrackedQueriesApi.md#reportAiResponse) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/responses/{aiResponseId}/report | Report a problem with a captured AI answer |
| [**resumeTrackedQuery()**](TrackedQueriesApi.md#resumeTrackedQuery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/resume | Resume a tracked query |
| [**searchTrackedQueries()**](TrackedQueriesApi.md#searchTrackedQueries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Search a project&#39;s tracked queries |
| [**searchTrackedQueryMentionMatches()**](TrackedQueriesApi.md#searchTrackedQueryMentionMatches) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/mention-matches | List stored mention matches of a tracked query |
| [**searchTrackedQuerySerpMatches()**](TrackedQueriesApi.md#searchTrackedQuerySerpMatches) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/serp-matches | List stored serp matches of a tracked query |


## `addClustersToTrackedQuery()`

```php
addClustersToTrackedQuery($organization_id, $project_id, $tracked_query_id, $idempotency_key, $cluster_membership_request_data): \Mencoro\Api\Model\TrackedQueryDetailResource
```

Add a tracked query to clusters

Minimum role: manager. Adds the tracked query to every cluster named in \"queryClusterIds\" and answers with the query in its new state. Membership is a set: a cluster the query already belongs to is skipped, not reported as an error, and the response still lists it. Clusters the query belongs to and this call does not name are left alone — this adds, it does not replace the membership. Every cluster must belong to the project in the path; one that does not is rejected with its field named, and nothing is written. The \"Idempotency-Key\" header is required, and a repeat of the same key and body returns the recorded answer without adding anything again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string | Must belong to the project in the path.
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write.
$cluster_membership_request_data = new \Mencoro\Api\Model\ClusterMembershipRequestData(); // \Mencoro\Api\Model\ClusterMembershipRequestData

try {
    $result = $apiInstance->addClustersToTrackedQuery($organization_id, $project_id, $tracked_query_id, $idempotency_key, $cluster_membership_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->addClustersToTrackedQuery: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**| Must belong to the project in the path. | |
| **idempotency_key** | **string**| A client-chosen key, unique per operation, so a lost response can be retried without repeating the write. | |
| **cluster_membership_request_data** | [**\Mencoro\Api\Model\ClusterMembershipRequestData**](../Model/ClusterMembershipRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\TrackedQueryDetailResource**](../Model/TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `batchChangeTrackedQueriesCheckFrequency()`

```php
batchChangeTrackedQueriesCheckFrequency($organization_id, $project_id, $idempotency_key, $batch_change_tracked_query_check_frequency_request_data): \Mencoro\Api\Model\BatchWriteOutcome
```

Change how often several tracked queries are checked

Minimum role: manager. Sets the same check frequency on every tracked query named in `ids`, at most 100 distinct ids per call. The organization must be active and the project must not be archived. Partial success: an id that is not a tracked query of this project — unknown, malformed, already deleted, or belonging to somewhere else — is reported under `failed` with `tracked_query_not_found` while the rest are changed, and the call still answers 200. Nothing is rolled back because an item failed. Setting the frequency a query already has is accepted and changes nothing. This does NOT run a check and does not reschedule one already in flight. It never changes more than the ids it is given: there is no \"change everything matching a filter\" mode. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
$batch_change_tracked_query_check_frequency_request_data = new \Mencoro\Api\Model\BatchChangeTrackedQueryCheckFrequencyRequestData(); // \Mencoro\Api\Model\BatchChangeTrackedQueryCheckFrequencyRequestData

try {
    $result = $apiInstance->batchChangeTrackedQueriesCheckFrequency($organization_id, $project_id, $idempotency_key, $batch_change_tracked_query_check_frequency_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->batchChangeTrackedQueriesCheckFrequency: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | |
| **batch_change_tracked_query_check_frequency_request_data** | [**\Mencoro\Api\Model\BatchChangeTrackedQueryCheckFrequencyRequestData**](../Model/BatchChangeTrackedQueryCheckFrequencyRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\BatchWriteOutcome**](../Model/BatchWriteOutcome.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `batchChangeTrackedQueriesNPasses()`

```php
batchChangeTrackedQueriesNPasses($organization_id, $project_id, $idempotency_key, $batch_change_tracked_query_passes_request_data): \Mencoro\Api\Model\BatchWriteOutcome
```

Change how many passes several tracked queries run per check

Minimum role: manager. Sets the same passes-per-check on every tracked query named in `ids`, at most 100 distinct ids per call. The organization must be active and the project must not be archived. Partial success, and two distinct reasons appear under `failed`: an id that is not a tracked query of this project answers `tracked_query_not_found`, and a `google_serp` or `google_shopping` query asked for more than one pass answers `n_passes_not_supported_for_engine` — those engines run a single pass. Both leave the rest of the batch changed and the call still answers 200. Setting the value back to 1 is always allowed, so a batch that lowers sampling never fails on engine grounds. This does NOT run a check and does not change history already captured. More passes cost proportionally more of the plan's check budget. It never changes more than the ids it is given: there is no \"change everything matching a filter\" mode. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
$batch_change_tracked_query_passes_request_data = new \Mencoro\Api\Model\BatchChangeTrackedQueryPassesRequestData(); // \Mencoro\Api\Model\BatchChangeTrackedQueryPassesRequestData

try {
    $result = $apiInstance->batchChangeTrackedQueriesNPasses($organization_id, $project_id, $idempotency_key, $batch_change_tracked_query_passes_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->batchChangeTrackedQueriesNPasses: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | |
| **batch_change_tracked_query_passes_request_data** | [**\Mencoro\Api\Model\BatchChangeTrackedQueryPassesRequestData**](../Model/BatchChangeTrackedQueryPassesRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\BatchWriteOutcome**](../Model/BatchWriteOutcome.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `batchCreateTrackedQueries()`

```php
batchCreateTrackedQueries($organization_id, $project_id, $idempotency_key, $batch_create_tracked_queries_request_data): \Mencoro\Api\Model\BatchCreateTrackedQueriesResultResource
```

Create tracked queries

Minimum role: manager. Creates the cross product of `queryTexts` x `engines` x `countries`: three texts, two engines and two countries create twelve tracked queries, not three. At most 100 combinations per call. The organization must be active and the project must not be archived. Partial success: the response lists, per combination, either the id it was created under or why nothing was created for it, and the status code never reports item-level outcomes. A combination the project already tracks is NOT created again and NOT re-identified — it appears under `failed` with `tracked_query_already_exists`, keeps the id it already had, and has any `queryClusterIds` in this request merged into it. Query text is normalised before it is compared and stored (lower-cased, whitespace collapsed, leading list markers stripped), so two texts differing only in those respects are one tracked query: the first of them owns the outcome and every later one appears under `failed` with `duplicate_combination_in_request`, naming the entry it repeats. `nPasses` applies to AI engines only: `google_serp` and `google_shopping` rows are always created with one pass, whatever is sent. Google AI Mode is unavailable in a few countries and those combinations are reported under `failed` rather than created. Creating a tracked query does not run a check: the first check happens on the normal schedule for the `checkFrequency` chosen. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without creating anything again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of creating anything again.
$batch_create_tracked_queries_request_data = new \Mencoro\Api\Model\BatchCreateTrackedQueriesRequestData(); // \Mencoro\Api\Model\BatchCreateTrackedQueriesRequestData

try {
    $result = $apiInstance->batchCreateTrackedQueries($organization_id, $project_id, $idempotency_key, $batch_create_tracked_queries_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->batchCreateTrackedQueries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of creating anything again. | |
| **batch_create_tracked_queries_request_data** | [**\Mencoro\Api\Model\BatchCreateTrackedQueriesRequestData**](../Model/BatchCreateTrackedQueriesRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\BatchCreateTrackedQueriesResultResource**](../Model/BatchCreateTrackedQueriesResultResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `batchForceCheckTrackedQueries()`

```php
batchForceCheckTrackedQueries($organization_id, $project_id, $idempotency_key, $batch_targets_request_data): \Mencoro\Api\Model\BatchForceCheckTrackedQueries200Response
```

Check several tracked queries now

Minimum role: manager. Asks for a fresh check of up to 100 named tracked queries straight away, ignoring how recently each was last checked. Answers 200 with per-item results and NO job id: a check that is already in flight for a query is reused rather than started again, so there is no id this operation could hand back that is guaranteed to exist. Follow progress on the tracked query itself — its lastCheckedAt advances when the check completes. A successful item means the check was accepted for submission with budget available for it at that moment; it does not mean the check has run. A checked query costs one budget unit per pass (nPasses), and items that do not fit the remaining budget are reported as failed with `check_budget_forecast_exhausted`, or `subscription_not_found` when the organization has no entitled subscription — they are never reported as successful. That budget figure is a forecast for this batch, and a pessimistic one: a tracked query already being checked is joined to the check in flight and costs nothing, but it is still debited here, so an item refused this way may have fitted. Resubmit it in a later batch rather than treating the refusal as a statement about your subscription. A paused query is reported as failed with `tracked_query_already_paused`: paused queries are never checked. An id that is not a tracked query of this project is reported as failed with `tracked_query_not_found`, exactly as an id that does not exist. Requires an Idempotency-Key header; a retry must repeat the same ids in the same order.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | Repeating a request with the same key and the same ids answers with the first attempt's result instead of submitting again.
$batch_targets_request_data = new \Mencoro\Api\Model\BatchTargetsRequestData(); // \Mencoro\Api\Model\BatchTargetsRequestData

try {
    $result = $apiInstance->batchForceCheckTrackedQueries($organization_id, $project_id, $idempotency_key, $batch_targets_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->batchForceCheckTrackedQueries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| Repeating a request with the same key and the same ids answers with the first attempt&#39;s result instead of submitting again. | |
| **batch_targets_request_data** | [**\Mencoro\Api\Model\BatchTargetsRequestData**](../Model/BatchTargetsRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\BatchForceCheckTrackedQueries200Response**](../Model/BatchForceCheckTrackedQueries200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `batchPauseTrackedQueries()`

```php
batchPauseTrackedQueries($organization_id, $project_id, $idempotency_key, $batch_targets_request_data): \Mencoro\Api\Model\BatchPauseTrackedQueries200Response
```

Pause several tracked queries

Minimum role: manager. Pauses up to 100 tracked queries of one project, each independently. Always answers 200 when the batch itself was processed: read `failed` to find out which items were not paused, never the status code. Items are never rolled back because a later one failed. An id that is already paused is reported as successful — pausing asserts a state, not a transition. An id that is not a tracked query of this project is reported as failed with `tracked_query_not_found`, exactly as an id that does not exist at all, and nothing is written for it. Pausing does not cancel a check that is already running. Requires an Idempotency-Key header; a retry must repeat the same ids in the same order to be recognised as a retry rather than refused as a reused key.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | Repeating a request with the same key and the same ids answers with the first attempt's result.
$batch_targets_request_data = new \Mencoro\Api\Model\BatchTargetsRequestData(); // \Mencoro\Api\Model\BatchTargetsRequestData

try {
    $result = $apiInstance->batchPauseTrackedQueries($organization_id, $project_id, $idempotency_key, $batch_targets_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->batchPauseTrackedQueries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| Repeating a request with the same key and the same ids answers with the first attempt&#39;s result. | |
| **batch_targets_request_data** | [**\Mencoro\Api\Model\BatchTargetsRequestData**](../Model/BatchTargetsRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\BatchPauseTrackedQueries200Response**](../Model/BatchPauseTrackedQueries200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `batchResumeTrackedQueries()`

```php
batchResumeTrackedQueries($organization_id, $project_id, $idempotency_key, $batch_targets_request_data): \Mencoro\Api\Model\BatchResumeTrackedQueries200Response
```

Resume several tracked queries

Minimum role: manager. Puts up to 100 paused tracked queries of one project back under the scheduler, each independently. Always answers 200 when the batch itself was processed: read `failed` to find out which items were not resumed, never the status code. Items are never rolled back because a later one failed. An id that is already active is reported as successful — resuming asserts a state, not a transition. An id that is not a tracked query of this project is reported as failed with `tracked_query_not_found`, exactly as an id that does not exist at all, and nothing is written for it. No check is run by this operation and nothing is back-filled for the time the queries spent paused. Requires an Idempotency-Key header; a retry must repeat the same ids in the same order to be recognised as a retry rather than refused as a reused key.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | Repeating a request with the same key and the same ids answers with the first attempt's result.
$batch_targets_request_data = new \Mencoro\Api\Model\BatchTargetsRequestData(); // \Mencoro\Api\Model\BatchTargetsRequestData

try {
    $result = $apiInstance->batchResumeTrackedQueries($organization_id, $project_id, $idempotency_key, $batch_targets_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->batchResumeTrackedQueries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| Repeating a request with the same key and the same ids answers with the first attempt&#39;s result. | |
| **batch_targets_request_data** | [**\Mencoro\Api\Model\BatchTargetsRequestData**](../Model/BatchTargetsRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\BatchResumeTrackedQueries200Response**](../Model/BatchResumeTrackedQueries200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `bulkAddClustersToTrackedQueries()`

```php
bulkAddClustersToTrackedQueries($organization_id, $project_id, $idempotency_key, $bulk_add_clusters_to_tracked_queries_request): \Mencoro\Api\Model\BulkAddClustersToTrackedQueries200Response
```

Add many tracked queries to clusters

Minimum role: manager. Adds every tracked query named in \"ids\" to every cluster named in \"queryClusterIds\". At most 100 distinct tracked queries per call; duplicates in \"ids\" are collapsed. Partial success: the answer is 200 with a per-item \"successful\" and \"failed\" list even when some items failed, nothing is rolled back, and an id that is not a tracked query of this project is reported as a failed item rather than dropped. Clusters not named are left alone — this adds, it does not replace membership. Every cluster must belong to the project in the path; one that does not is rejected with its field named and nothing is written at all. The \"Idempotency-Key\" header is required, and a repeat of the same key and body returns the recorded answer without running the batch again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch.
$bulk_add_clusters_to_tracked_queries_request = new \Mencoro\Api\Model\BulkAddClustersToTrackedQueriesRequest(); // \Mencoro\Api\Model\BulkAddClustersToTrackedQueriesRequest

try {
    $result = $apiInstance->bulkAddClustersToTrackedQueries($organization_id, $project_id, $idempotency_key, $bulk_add_clusters_to_tracked_queries_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->bulkAddClustersToTrackedQueries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch. | |
| **bulk_add_clusters_to_tracked_queries_request** | [**\Mencoro\Api\Model\BulkAddClustersToTrackedQueriesRequest**](../Model/BulkAddClustersToTrackedQueriesRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\BulkAddClustersToTrackedQueries200Response**](../Model/BulkAddClustersToTrackedQueries200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `bulkDeleteTrackedQueries()`

```php
bulkDeleteTrackedQueries($organization_id, $project_id, $idempotency_key, $batch_targets_request_data): \Mencoro\Api\Model\BatchWriteOutcome
```

Delete tracked queries

Minimum role: manager. Permanently deletes the tracked queries named in `ids`, at most 100 distinct ids per call. The organization must be active and the project must not be archived. Deletion is hard and cannot be undone: the tracked query is removed along with its captured answers, matches, search pages and rank history, and any check already in flight for it is cancelled. Those cascades run in the background, so a 200 means the tracked queries were deleted, not that every derived record has finished being purged. Partial success: an id that is not a tracked query of this project — unknown, malformed, already deleted, or belonging to somewhere else — is reported under `failed` with `tracked_query_not_found` while the rest are deleted. It never deletes more than the ids it is given: there is no \"delete everything matching a filter\" mode. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without deleting anything again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of deleting anything again.
$batch_targets_request_data = new \Mencoro\Api\Model\BatchTargetsRequestData(); // \Mencoro\Api\Model\BatchTargetsRequestData

try {
    $result = $apiInstance->bulkDeleteTrackedQueries($organization_id, $project_id, $idempotency_key, $batch_targets_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->bulkDeleteTrackedQueries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of deleting anything again. | |
| **batch_targets_request_data** | [**\Mencoro\Api\Model\BatchTargetsRequestData**](../Model/BatchTargetsRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\BatchWriteOutcome**](../Model/BatchWriteOutcome.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `bulkRemoveClustersFromTrackedQueries()`

```php
bulkRemoveClustersFromTrackedQueries($organization_id, $project_id, $idempotency_key, $bulk_remove_clusters_from_tracked_queries_request): \Mencoro\Api\Model\BulkRemoveClustersFromTrackedQueries200Response
```

Remove many tracked queries from clusters

Minimum role: manager. Removes every tracked query named in \"ids\" from every cluster named in \"queryClusterIds\". At most 100 distinct tracked queries per call; duplicates in \"ids\" are collapsed. Partial success: the answer is 200 with a per-item \"successful\" and \"failed\" list even when some items failed, nothing is rolled back, and an id that is not a tracked query of this project is reported as a failed item rather than dropped. Neither the clusters nor the tracked queries are deleted: only the membership between them. Every cluster must belong to the project in the path; one that does not is rejected with its field named and nothing is written at all. NOTE: this DELETE requires a request body — some HTTP client libraries and proxies strip bodies from DELETE, and a stripped body is refused with a validation error rather than interpreted as \"remove everything\". The \"Idempotency-Key\" header is required, and a repeat of the same key and body returns the recorded answer without running the batch again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch.
$bulk_remove_clusters_from_tracked_queries_request = new \Mencoro\Api\Model\BulkRemoveClustersFromTrackedQueriesRequest(); // \Mencoro\Api\Model\BulkRemoveClustersFromTrackedQueriesRequest | Required. A DELETE with no body is rejected.

try {
    $result = $apiInstance->bulkRemoveClustersFromTrackedQueries($organization_id, $project_id, $idempotency_key, $bulk_remove_clusters_from_tracked_queries_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->bulkRemoveClustersFromTrackedQueries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch. | |
| **bulk_remove_clusters_from_tracked_queries_request** | [**\Mencoro\Api\Model\BulkRemoveClustersFromTrackedQueriesRequest**](../Model/BulkRemoveClustersFromTrackedQueriesRequest.md)| Required. A DELETE with no body is rejected. | |

### Return type

[**\Mencoro\Api\Model\BulkRemoveClustersFromTrackedQueries200Response**](../Model/BulkRemoveClustersFromTrackedQueries200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `changeTrackedQueryCheckFrequency()`

```php
changeTrackedQueryCheckFrequency($organization_id, $project_id, $tracked_query_id, $idempotency_key, $change_tracked_query_check_frequency_request_data): \Mencoro\Api\Model\TrackedQueryDetailResource
```

Change how often a tracked query is checked

Minimum role: manager. Sets how often one tracked query is checked while it is active. The organization must be active and the project must not be archived. Setting the frequency it already has is accepted and changes nothing. This does NOT run a check, does not backfill history, and does not reschedule a check already in flight: the new cadence applies from the next time the query is considered. A paused query keeps the setting but is not checked until it is resumed. A tracked query belonging to another project answers 404, the same answer an unknown id gets. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string | Must belong to the project in the path.
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
$change_tracked_query_check_frequency_request_data = new \Mencoro\Api\Model\ChangeTrackedQueryCheckFrequencyRequestData(); // \Mencoro\Api\Model\ChangeTrackedQueryCheckFrequencyRequestData

try {
    $result = $apiInstance->changeTrackedQueryCheckFrequency($organization_id, $project_id, $tracked_query_id, $idempotency_key, $change_tracked_query_check_frequency_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->changeTrackedQueryCheckFrequency: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**| Must belong to the project in the path. | |
| **idempotency_key** | **string**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | |
| **change_tracked_query_check_frequency_request_data** | [**\Mencoro\Api\Model\ChangeTrackedQueryCheckFrequencyRequestData**](../Model/ChangeTrackedQueryCheckFrequencyRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\TrackedQueryDetailResource**](../Model/TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `changeTrackedQueryNPasses()`

```php
changeTrackedQueryNPasses($organization_id, $project_id, $tracked_query_id, $idempotency_key, $change_tracked_query_passes_request_data): \Mencoro\Api\Model\TrackedQueryDetailResource
```

Change how many passes a tracked query runs per check

Minimum role: manager. Sets how many times one tracked query is asked per check. AI engines are not deterministic, so several passes are averaged; `google_serp` and `google_shopping` run a single pass and refuse any value above one with 409 `n_passes_not_supported_for_engine`. Setting the value back to 1 is always allowed. The organization must be active and the project must not be archived. Setting the value it already has is accepted and changes nothing. This does NOT run a check and does not change history already captured: it applies from the next check. More passes cost proportionally more of the plan's check budget. A tracked query belonging to another project answers 404, the same answer an unknown id gets. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string | Must belong to the project in the path.
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
$change_tracked_query_passes_request_data = new \Mencoro\Api\Model\ChangeTrackedQueryPassesRequestData(); // \Mencoro\Api\Model\ChangeTrackedQueryPassesRequestData

try {
    $result = $apiInstance->changeTrackedQueryNPasses($organization_id, $project_id, $tracked_query_id, $idempotency_key, $change_tracked_query_passes_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->changeTrackedQueryNPasses: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**| Must belong to the project in the path. | |
| **idempotency_key** | **string**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | |
| **change_tracked_query_passes_request_data** | [**\Mencoro\Api\Model\ChangeTrackedQueryPassesRequestData**](../Model/ChangeTrackedQueryPassesRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\TrackedQueryDetailResource**](../Model/TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `countTrackedQueries()`

```php
countTrackedQueries($organization_id, $project_id, $status): \Mencoro\Api\Model\TrackedQueryCountResource
```

Count a project's tracked queries and price checking them

Minimum role: viewer. Two numbers about one project: how many tracked queries it holds, and what force-checking that same set would cost. Omit `status` to count every tracked query whatever its status; send `active` or `paused` to count and price only those. `checkCost` is a PRICED DRY RUN expressed in check budget units — one unit per pass, the same unit the plan allowance is counted in, so it is directly comparable with `checksAvailable` from the entitlements operation — and it is the sum of each matched tracked query's configured passes. Asking reserves nothing, debits nothing and starts no check. It is deliberately NOT a forecast of what the check-all operation will consume: that operation skips paused queries, skips a query whose check is already pending or running, re-runs a check awaiting retry without charging for it again, and stops at whatever budget is left — none of which is subtracted here. Count with `status=active` for the figure closest to a full check-all. Both numbers are read from the write model, so a tracked query created moments ago is already in them; that is why they can be AHEAD of the `total` returned by the tracked-queries listing, which counts a search projection, and ahead of the keyword listings, which read projections refreshed in the background. Summing the unfiltered count over every project of an organization, archived projects included, reproduces countOrganizationTrackedQueries, which counts through the same counter in the same store. An archived project still answers, because this is a read, but no check can be submitted there while it stays archived, so its cost is hypothetical. For a month of scheduled rounds across the whole organization instead of one round over one project, read getOrganizationProjectedMonthlyChecks. No monetary amount is published or implied: the cost of a check is published only in budget units.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$status = 'status_example'; // string | Restrict both numbers to one status. Lower-case; an unknown value is rejected, not ignored. Omitted, every status is counted and priced.

try {
    $result = $apiInstance->countTrackedQueries($organization_id, $project_id, $status);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->countTrackedQueries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **status** | **string**| Restrict both numbers to one status. Lower-case; an unknown value is rejected, not ignored. Omitted, every status is counted and priced. | [optional] |

### Return type

[**\Mencoro\Api\Model\TrackedQueryCountResource**](../Model/TrackedQueryCountResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `forceCheckAllActiveTrackedQueries()`

```php
forceCheckAllActiveTrackedQueries($organization_id, $project_id, $idempotency_key): \Mencoro\Api\Model\SubmittedChecksResource
```

Check every eligible tracked query of a project now

Minimum role: manager. Submits a fresh check for every eligible tracked query of the project, ignoring how recently each was last checked, least-recently-checked first, and at most 1000 tracked queries per call. Eligible is narrower than active: a paused query is skipped, and so is one whose check is already pending or running for the same engine. A query whose check is awaiting a retry is included and, WHEN THE ENGINE HAS NOT CHANGED SINCE, costs nothing extra, because its first submission already paid for it; if the engine did change, the pending run is replaced and the replacement is paid for. What is left is trimmed to what the organization's remaining check budget can pay for — a check costs one budget unit per pass. While a subscription is cancelled but still inside its paid grace window nothing is submitted at all and `submitted` is 0; name the queries explicitly through the check operation to run them in that window. CALLING AGAIN DOES NOT CONTINUE WHERE THIS CALL STOPPED: submissions are handed to a worker, and a tracked query stops being selected only once that worker has started its check, so a second call made before the queue drains selects and submits the same tracked queries again. That is safe while the first check is still running — the duplicate is collapsed, and nothing is checked or charged twice — but a check that has already finished is run again and charged again, because this operation ignores staleness by design. To cover a project with more than 1000 eligible tracked queries, wait for the submitted wave to be picked up — each tracked query's lastCheckedAt advances when its check completes — and call again then. The response lists the tracked queries submitted and carries NO job id: a check already in flight is reused rather than started again, so no id could be guaranteed to exist. Submission is accepted, not completed: a listed tracked query can still lose the last budget units to another caller before the worker reaches it. The request takes no body, and any field sent is rejected. Requires an Idempotency-Key header.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | Repeating a request with the same key answers with the first attempt's result instead of submitting a second wave.

try {
    $result = $apiInstance->forceCheckAllActiveTrackedQueries($organization_id, $project_id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->forceCheckAllActiveTrackedQueries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| Repeating a request with the same key answers with the first attempt&#39;s result instead of submitting a second wave. | |

### Return type

[**\Mencoro\Api\Model\SubmittedChecksResource**](../Model/SubmittedChecksResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getTrackedQuery()`

```php
getTrackedQuery($organization_id, $project_id, $tracked_query_id): \Mencoro\Api\Model\TrackedQueryDetailResource
```

Get a tracked query

Minimum role: viewer. The configuration of one tracked query: the text sent to the engine, the engine, locale and country it is asked in, the clusters it belongs to, and how often it is checked. A lastCheckedAt of null means no check has completed yet — it is not a check that found nothing. A tracked query belonging to another project answers 404, the same answer an unknown id gets, so the API never confirms that an inaccessible tracked query exists. Rank positions, share of voice and sentiment are not part of this response: they belong to a date window and are served by the analytics endpoints.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string | Must belong to the project in the path.

try {
    $result = $apiInstance->getTrackedQuery($organization_id, $project_id, $tracked_query_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->getTrackedQuery: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**| Must belong to the project in the path. | |

### Return type

[**\Mencoro\Api\Model\TrackedQueryDetailResource**](../Model/TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `pauseTrackedQuery()`

```php
pauseTrackedQuery($organization_id, $project_id, $tracked_query_id, $idempotency_key): \Mencoro\Api\Model\TrackedQueryDetailResource
```

Pause a tracked query

Minimum role: manager. Stops the scheduler from checking this tracked query; it keeps its configuration, its clusters and every result already collected, and nothing is deleted. Pausing a query that is already paused succeeds and answers the same body — this is a PUT asserting a state, not a transition, so it is safe to repeat. It does NOT cancel a check that is already running: a check in flight when the pause lands still completes and still consumes the budget unit it reserved. The request takes no body, and any field sent is rejected. Requires an Idempotency-Key header.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string | Must belong to the project in the path.
$idempotency_key = 'idempotency_key_example'; // string | Repeating a request with the same key answers with the first attempt's result instead of pausing again.

try {
    $result = $apiInstance->pauseTrackedQuery($organization_id, $project_id, $tracked_query_id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->pauseTrackedQuery: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**| Must belong to the project in the path. | |
| **idempotency_key** | **string**| Repeating a request with the same key answers with the first attempt&#39;s result instead of pausing again. | |

### Return type

[**\Mencoro\Api\Model\TrackedQueryDetailResource**](../Model/TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `removeClustersFromTrackedQuery()`

```php
removeClustersFromTrackedQuery($organization_id, $project_id, $tracked_query_id, $idempotency_key, $cluster_membership_request_data): \Mencoro\Api\Model\TrackedQueryDetailResource
```

Remove a tracked query from clusters

Minimum role: manager. Removes the tracked query from every cluster named in \"queryClusterIds\" and answers with the query in its new state. A cluster the query does not belong to is skipped, not reported as an error. Neither the clusters nor the tracked query are deleted: only the membership between them. Every cluster must belong to the project in the path. NOTE: this DELETE requires a request body — some HTTP client libraries and proxies strip bodies from DELETE, and a stripped body is refused with a validation error rather than interpreted as \"remove all clusters\". The \"Idempotency-Key\" header is required, and a repeat of the same key and body returns the recorded answer without removing anything again.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string | Must belong to the project in the path.
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write.
$cluster_membership_request_data = new \Mencoro\Api\Model\ClusterMembershipRequestData(); // \Mencoro\Api\Model\ClusterMembershipRequestData | Required. A DELETE with no body is rejected.

try {
    $result = $apiInstance->removeClustersFromTrackedQuery($organization_id, $project_id, $tracked_query_id, $idempotency_key, $cluster_membership_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->removeClustersFromTrackedQuery: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**| Must belong to the project in the path. | |
| **idempotency_key** | **string**| A client-chosen key, unique per operation, so a lost response can be retried without repeating the write. | |
| **cluster_membership_request_data** | [**\Mencoro\Api\Model\ClusterMembershipRequestData**](../Model/ClusterMembershipRequestData.md)| Required. A DELETE with no body is rejected. | |

### Return type

[**\Mencoro\Api\Model\TrackedQueryDetailResource**](../Model/TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `reportAiResponse()`

```php
reportAiResponse($organization_id, $project_id, $tracked_query_id, $ai_response_id, $idempotency_key, $report_ai_response_request): \Mencoro\Api\Model\AiResponseReportResource
```

Report a problem with a captured AI answer

Minimum role: viewer — deliberately lower than the other tracked-query writes, because a report changes nothing a viewer cannot already read. The key still needs the \"write\" capability. The report is forwarded to the team that reviews the scrape run behind the capture; it does not change the capture, the tracked query, or any metric derived from them, and nothing in this API will show the report afterwards. A 200 means the report was accepted for review, not that anything was corrected, and there is no identifier to poll. A capture that belongs to another tracked query or project answers 404, the same answer an unknown id gets. A capture that cannot be routed back to its scrape run answers 409 \"ai_check_session_unavailable\", and it cannot be reported. That code covers two moments, which behave differently for your key: when the capture carries no scrape run at all the refusal is decided BEFORE anything is sent, so the idempotency key is left unused and the same key answers the same way however often it is presented; when the review system itself rejects the run — its own retention having elapsed — the refusal comes after the forward was attempted, so the key is spent like any outcome we cannot confirm. You can tell them apart without guessing: retry the same key, and a reply of \"operation_outcome_uncertain\" means the refusal came from the review system. Delivery is at-most-once: the \"Idempotency-Key\" header is required and a repeat of the same key and body returns the recorded answer, but a delivery whose outcome is unknown refuses replay on that key rather than risk filing the report twice.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string | Must belong to the project in the path.
$ai_response_id = 'ai_response_id_example'; // string | A capture id from the AI responses listing. Must belong to the tracked query in the path.
$idempotency_key = 'idempotency_key_example'; // string | A client-chosen key, unique per report, so a lost response can be retried without filing the report twice.
$report_ai_response_request = new \Mencoro\Api\Model\ReportAiResponseRequest(); // \Mencoro\Api\Model\ReportAiResponseRequest

try {
    $result = $apiInstance->reportAiResponse($organization_id, $project_id, $tracked_query_id, $ai_response_id, $idempotency_key, $report_ai_response_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->reportAiResponse: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**| Must belong to the project in the path. | |
| **ai_response_id** | **string**| A capture id from the AI responses listing. Must belong to the tracked query in the path. | |
| **idempotency_key** | **string**| A client-chosen key, unique per report, so a lost response can be retried without filing the report twice. | |
| **report_ai_response_request** | [**\Mencoro\Api\Model\ReportAiResponseRequest**](../Model/ReportAiResponseRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\AiResponseReportResource**](../Model/AiResponseReportResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `resumeTrackedQuery()`

```php
resumeTrackedQuery($organization_id, $project_id, $tracked_query_id, $idempotency_key): \Mencoro\Api\Model\TrackedQueryDetailResource
```

Resume a tracked query

Minimum role: manager. Puts a paused tracked query back under the scheduler. Resuming a query that is already active succeeds and answers the same body — this is a PUT asserting a state, not a transition. It does NOT run a check: the query is checked when it next falls due under its own checkFrequency, and results collected while it was paused are unaffected. Nothing is back-filled for the time it spent paused. The request takes no body, and any field sent is rejected. Requires an Idempotency-Key header.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string | Must belong to the project in the path.
$idempotency_key = 'idempotency_key_example'; // string | Repeating a request with the same key answers with the first attempt's result instead of resuming again.

try {
    $result = $apiInstance->resumeTrackedQuery($organization_id, $project_id, $tracked_query_id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->resumeTrackedQuery: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**| Must belong to the project in the path. | |
| **idempotency_key** | **string**| Repeating a request with the same key answers with the first attempt&#39;s result instead of resuming again. | |

### Return type

[**\Mencoro\Api\Model\TrackedQueryDetailResource**](../Model/TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchTrackedQueries()`

```php
searchTrackedQueries($organization_id, $project_id, $limit, $offset, $search, $status, $engines, $countries, $sort_by, $sort_order): \Mencoro\Api\Model\SearchTrackedQueries200Response
```

Search a project's tracked queries

Minimum role: viewer. One row per tracked query — a single keyword on a single engine in a single country — carrying the metrics of its most recent completed check. Filter by status, engine, country and a free-text search over the keyword, and sort by any of the returned metrics. Positions (lastSerpPosition, lastMentionPosition, lastLinkPosition, lastShoppingPosition) are 1-based ranks, so LOWER is better; lastShareOfVoice and lastPositivityIndex are percentages from 0 to 100, where HIGHER is better. Every nullable field means \"not known yet\" rather than zero: a null position is a query with no data for that surface, a null lastPositivityIndex is a check with no mentions to score, and a null lastCheckedAt is a query that has never been checked — none of them is a score of zero. This listing reads a projection refreshed by background subscribers, not the write model, so a tracked query created or changed moments ago may not appear here yet or may still show its previous settings. It catches up on its own; nothing is lost. If you need to read back what you just wrote, the creation response carries the new ids and the single tracked-query operation reads the write model directly. total counts the tracked queries the filters match, not the rows on this page. A limit above the maximum is rejected, never clamped, and a filter this endpoint does not support is rejected rather than ignored.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$limit = 20; // int | Page size. A value above the maximum is rejected, never clamped.
$offset = 0; // int
$search = 'search_example'; // string | Free-text search over the keyword.
$status = 'status_example'; // string
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated.
$countries = array('countries_example'); // string[] | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
$sort_by = 'queryText'; // string
$sort_order = 'desc'; // string

try {
    $result = $apiInstance->searchTrackedQueries($organization_id, $project_id, $limit, $offset, $search, $status, $engines, $countries, $sort_by, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->searchTrackedQueries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **limit** | **int**| Page size. A value above the maximum is rejected, never clamped. | [optional] [default to 20] |
| **offset** | **int**|  | [optional] [default to 0] |
| **search** | **string**| Free-text search over the keyword. | [optional] |
| **status** | **string**|  | [optional] |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. | [optional] |
| **countries** | [**string[]**](../Model/string.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **sort_by** | **string**|  | [optional] [default to &#39;queryText&#39;] |
| **sort_order** | **string**|  | [optional] [default to &#39;desc&#39;] |

### Return type

[**\Mencoro\Api\Model\SearchTrackedQueries200Response**](../Model/SearchTrackedQueries200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchTrackedQueryMentionMatches()`

```php
searchTrackedQueryMentionMatches($organization_id, $project_id, $tracked_query_id, $date_from, $date_to, $limit, $offset, $sort_order): \Mencoro\Api\Model\SearchTrackedQueryMentionMatches200Response
```

List stored mention matches of a tracked query

Minimum role: viewer. Text mentions across own brand and tracked or untracked competitors. Citation-only rows are excluded before pagination. Read mentionRelation to distinguish own brand from untracked competitors; a null competitorId alone does not classify the mention. Newest first by detection time, with an id tie-break. Dates cover whole UTC days. Only the retained 16-month window is readable, including when dateFrom is omitted. Unknown filters are rejected. The total counts all matching rows before pagination. Send Accept: text/csv for the same bounded page and filters as CSV, with formula-safe cells and no total.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive UTC day; defaults to the retention floor.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive UTC day.
$limit = 20; // int
$offset = 0; // int
$sort_order = 'desc'; // string

try {
    $result = $apiInstance->searchTrackedQueryMentionMatches($organization_id, $project_id, $tracked_query_id, $date_from, $date_to, $limit, $offset, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->searchTrackedQueryMentionMatches: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive UTC day; defaults to the retention floor. | [optional] |
| **date_to** | **\DateTime**| Inclusive UTC day. | [optional] |
| **limit** | **int**|  | [optional] [default to 20] |
| **offset** | **int**|  | [optional] [default to 0] |
| **sort_order** | **string**|  | [optional] [default to &#39;desc&#39;] |

### Return type

[**\Mencoro\Api\Model\SearchTrackedQueryMentionMatches200Response**](../Model/SearchTrackedQueryMentionMatches200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchTrackedQuerySerpMatches()`

```php
searchTrackedQuerySerpMatches($organization_id, $project_id, $tracked_query_id, $date_from, $date_to, $limit, $offset, $sort_order): \Mencoro\Api\Model\SearchTrackedQuerySerpMatches200Response
```

List stored serp matches of a tracked query

Minimum role: viewer. Stored organic-search matches with the competitor attribution and position recorded at detection time. A null competitorId identifies the own-brand match. These are historical matches, not a reclassification using the current brand profile. Newest first by detection time, with an id tie-break. Dates cover whole UTC days. Only the retained 16-month window is readable, including when dateFrom is omitted. Unknown filters are rejected. The total counts all matching rows before pagination. Send Accept: text/csv for the same bounded page and filters as CSV, with formula-safe cells and no total.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\TrackedQueriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive UTC day; defaults to the retention floor.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive UTC day.
$limit = 20; // int
$offset = 0; // int
$sort_order = 'desc'; // string

try {
    $result = $apiInstance->searchTrackedQuerySerpMatches($organization_id, $project_id, $tracked_query_id, $date_from, $date_to, $limit, $offset, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TrackedQueriesApi->searchTrackedQuerySerpMatches: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive UTC day; defaults to the retention floor. | [optional] |
| **date_to** | **\DateTime**| Inclusive UTC day. | [optional] |
| **limit** | **int**|  | [optional] [default to 20] |
| **offset** | **int**|  | [optional] [default to 0] |
| **sort_order** | **string**|  | [optional] [default to &#39;desc&#39;] |

### Return type

[**\Mencoro\Api\Model\SearchTrackedQuerySerpMatches200Response**](../Model/SearchTrackedQuerySerpMatches200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
