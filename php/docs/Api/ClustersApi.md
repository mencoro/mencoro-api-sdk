# Mencoro\Api\ClustersApi

Clusters

All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**applyClusteringJob()**](ClustersApi.md#applyClusteringJob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs/{jobId}/apply | Apply the result of a clustering job |
| [**batchCreateQueryClusters()**](ClustersApi.md#batchCreateQueryClusters) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/batch | Create several keyword clusters at once |
| [**createQueryCluster()**](ClustersApi.md#createQueryCluster) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | Create a keyword cluster |
| [**deleteQueryCluster()**](ClustersApi.md#deleteQueryCluster) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Delete a keyword cluster |
| [**renameQueryCluster()**](ClustersApi.md#renameQueryCluster) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Rename a keyword cluster |
| [**startClusteringJob()**](ClustersApi.md#startClusteringJob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs | Start a keyword clustering job |


## `applyClusteringJob()`

```php
applyClusteringJob($organization_id, $project_id, $job_id, $idempotency_key): \Mencoro\Api\Model\ApplyClusteringJobOutcome
```

Apply the result of a clustering job

Minimum role: manager. Writes a completed clustering job onto the tracked queries it was computed for: it creates the clusters the job proposed that the project does not have yet, then assigns each tracked query according to the merge mode the job was started with — fill_gaps leaves already grouped queries alone, add_on_top only adds, full_regroup replaces a query's clusters with the proposed set and therefore REMOVES clusters that are not in it — but only for a tracked query the job actually returned an assignment for. A tracked query the job was started over and produced no assignment for is listed under `unassigned` and left exactly as it was, under every mode; it is not treated as \"belongs to no cluster\" and is never stripped. That matters most with restrictToExistingClusters, where the model is expected to return nothing for queries that fit no existing cluster. The body must be empty: the assignments, the target tracked queries and the mode all come from the job, so this call cannot apply something the job did not produce. Synchronous and partially successful — always 200, with each tracked query under `successful` or `failed`, and nothing rolled back because one failed. A job that is not completed, or one that produced no assignments, is refused with 409. Requires the write capability and an Idempotency-Key header; repeating the key returns the first answer rather than applying twice.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ClustersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$job_id = 'job_id_example'; // string | Must be a clustering job started for this organization and project.
$idempotency_key = 'idempotency_key_example'; // string | Repeat it to retry a lost response without applying the job twice.

try {
    $result = $apiInstance->applyClusteringJob($organization_id, $project_id, $job_id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ClustersApi->applyClusteringJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **job_id** | **string**| Must be a clustering job started for this organization and project. | |
| **idempotency_key** | **string**| Repeat it to retry a lost response without applying the job twice. | |

### Return type

[**\Mencoro\Api\Model\ApplyClusteringJobOutcome**](../Model/ApplyClusteringJobOutcome.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `batchCreateQueryClusters()`

```php
batchCreateQueryClusters($organization_id, $project_id, $idempotency_key, $batch_create_query_clusters_request_data): \Mencoro\Api\Model\BatchCreateQueryClustersOutcome
```

Create several keyword clusters at once

Minimum role: manager. Creates up to 100 empty keyword clusters in one call. Names are trimmed and lower-cased and repeated names in the body are collapsed before anything is written. Partial success: the answer is always 200 and reports every name under `successful` or under `failed` — a name already taken in the project fails with query_cluster_name_already_exists and is NOT resolved to the existing cluster, while the other names are still created. Nothing is rolled back because one name failed. The clusters are created empty; no tracked query is assigned to them. The organization must not be archived; an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ClustersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | Repeat it to retry a lost response without creating the batch twice.
$batch_create_query_clusters_request_data = new \Mencoro\Api\Model\BatchCreateQueryClustersRequestData(); // \Mencoro\Api\Model\BatchCreateQueryClustersRequestData

try {
    $result = $apiInstance->batchCreateQueryClusters($organization_id, $project_id, $idempotency_key, $batch_create_query_clusters_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ClustersApi->batchCreateQueryClusters: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| Repeat it to retry a lost response without creating the batch twice. | |
| **batch_create_query_clusters_request_data** | [**\Mencoro\Api\Model\BatchCreateQueryClustersRequestData**](../Model/BatchCreateQueryClustersRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\BatchCreateQueryClustersOutcome**](../Model/BatchCreateQueryClustersOutcome.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createQueryCluster()`

```php
createQueryCluster($organization_id, $project_id, $idempotency_key, $create_query_cluster_request): \Mencoro\Api\Model\QueryClusterResource
```

Create a keyword cluster

Minimum role: manager. Creates one empty keyword cluster in the project. The name is trimmed and lower-cased before it is stored, and it must be unique within the project: a name that already exists is refused with 409 and nothing is merged into the existing cluster. The cluster starts with no tracked queries in it — this operation does not assign anything to it. The organization must not be archived; an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ClustersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 3f9d2c18-6b4a-4c77-9f10-6f2d5a7c8e21; // string | A token you choose per operation, 8 to 255 printable ASCII characters with no spaces; a UUID is the obvious choice. Repeat it to retry a lost response without creating a second cluster. The key is scoped to your API key, and it is bound to the method, the path and the body of the first attempt: repeating it with anything else changed is refused with 409 rather than replayed.
$create_query_cluster_request = {"name":"Agencia SEO"}; // \Mencoro\Api\Model\CreateQueryClusterRequest

try {
    $result = $apiInstance->createQueryCluster($organization_id, $project_id, $idempotency_key, $create_query_cluster_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ClustersApi->createQueryCluster: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| A token you choose per operation, 8 to 255 printable ASCII characters with no spaces; a UUID is the obvious choice. Repeat it to retry a lost response without creating a second cluster. The key is scoped to your API key, and it is bound to the method, the path and the body of the first attempt: repeating it with anything else changed is refused with 409 rather than replayed. | |
| **create_query_cluster_request** | [**\Mencoro\Api\Model\CreateQueryClusterRequest**](../Model/CreateQueryClusterRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\QueryClusterResource**](../Model/QueryClusterResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteQueryCluster()`

```php
deleteQueryCluster($organization_id, $project_id, $cluster_id, $idempotency_key): \Mencoro\Api\Model\DeleteQueryCluster200Response
```

Delete a keyword cluster

Minimum role: manager. Deletes one keyword cluster. The tracked queries that were in it are NOT deleted: they are unassigned from this cluster and keep every other cluster they belong to. Analytics filtered by this cluster id return nothing afterwards, including for dates before the deletion, because that filter reads current membership. This cannot be undone — recreating a cluster with the same name produces a new id and an empty cluster. The organization must not be archived, and neither must the project: an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ClustersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$cluster_id = 'cluster_id_example'; // string | Must be a cluster of the project in the path.
$idempotency_key = 'idempotency_key_example'; // string | Repeat it to retry a lost response; a fresh key answers 404 once the cluster is gone.

try {
    $result = $apiInstance->deleteQueryCluster($organization_id, $project_id, $cluster_id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ClustersApi->deleteQueryCluster: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **cluster_id** | **string**| Must be a cluster of the project in the path. | |
| **idempotency_key** | **string**| Repeat it to retry a lost response; a fresh key answers 404 once the cluster is gone. | |

### Return type

[**\Mencoro\Api\Model\DeleteQueryCluster200Response**](../Model/DeleteQueryCluster200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `renameQueryCluster()`

```php
renameQueryCluster($organization_id, $project_id, $cluster_id, $idempotency_key, $create_query_cluster_request): \Mencoro\Api\Model\QueryClusterResource
```

Rename a keyword cluster

Minimum role: manager. Changes the name of one keyword cluster and nothing else: the tracked queries assigned to it are untouched, and its id does not change, so nothing a client stored breaks. The new name is trimmed and lower-cased and must be unique within the project; a collision is refused with 409. Renaming to the name the cluster already has is accepted and is a no-op. The organization must not be archived; an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ClustersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$cluster_id = 'cluster_id_example'; // string | Must be a cluster of the project in the path.
$idempotency_key = 'idempotency_key_example'; // string | Repeat it to retry a lost response without renaming twice.
$create_query_cluster_request = new \Mencoro\Api\Model\CreateQueryClusterRequest(); // \Mencoro\Api\Model\CreateQueryClusterRequest

try {
    $result = $apiInstance->renameQueryCluster($organization_id, $project_id, $cluster_id, $idempotency_key, $create_query_cluster_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ClustersApi->renameQueryCluster: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **cluster_id** | **string**| Must be a cluster of the project in the path. | |
| **idempotency_key** | **string**| Repeat it to retry a lost response without renaming twice. | |
| **create_query_cluster_request** | [**\Mencoro\Api\Model\CreateQueryClusterRequest**](../Model/CreateQueryClusterRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\QueryClusterResource**](../Model/QueryClusterResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startClusteringJob()`

```php
startClusteringJob($organization_id, $project_id, $idempotency_key, $start_clustering_job_request_data): \Mencoro\Api\Model\AcceptedJobResource
```

Start a keyword clustering job

Minimum role: manager. Asks the clustering service to propose keyword clusters for up to 500 tracked queries of the project, and answers 202 with the job to poll — the work runs in the background and a 202 says it was accepted, never that it succeeded. THE JOB WRITES NOTHING: it produces a proposal, and nothing changes until it is applied through the apply operation, which is a separate call. Duplicate query texts within the selection are sent once. Requires an entitled subscription (402 otherwise) and the organization must be active and the project not archived. Rate limited to 10 starts per minute per organization, shared with the same operation in the web application. Requires the write capability and an Idempotency-Key header; repeating the key returns the first job rather than starting a second.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ClustersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | Repeat it to retry a lost response without starting a second job.
$start_clustering_job_request_data = new \Mencoro\Api\Model\StartClusteringJobRequestData(); // \Mencoro\Api\Model\StartClusteringJobRequestData

try {
    $result = $apiInstance->startClusteringJob($organization_id, $project_id, $idempotency_key, $start_clustering_job_request_data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ClustersApi->startClusteringJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**| Repeat it to retry a lost response without starting a second job. | |
| **start_clustering_job_request_data** | [**\Mencoro\Api\Model\StartClusteringJobRequestData**](../Model/StartClusteringJobRequestData.md)|  | |

### Return type

[**\Mencoro\Api\Model\AcceptedJobResource**](../Model/AcceptedJobResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
