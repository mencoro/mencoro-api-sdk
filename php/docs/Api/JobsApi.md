# Mencoro\Api\JobsApi

Jobs

All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAsyncJob()**](JobsApi.md#getAsyncJob) | **GET** /api/v1/organizations/{organizationId}/jobs/{jobId} | Get an asynchronous job |


## `getAsyncJob()`

```php
getAsyncJob($organization_id, $job_id): \Mencoro\Api\Model\AsyncJobResource
```

Get an asynchronous job

Minimum role: manager. The status of one asynchronous job started inside this organization — geo prompt discovery, keyword discovery, query clustering, brand discovery or brand-name suggestion — and, once it has completed, its result. Poll it until `status` is terminal: `completed` or `failed`. A null `result` means the result is not known, either because the job is still in flight or because it failed; it never means the job produced an empty result. A failed job carries no reason: the stored one is an internal exception message, not a published field. A job started by another organization, a job of a type this API does not publish, and a job id that does not exist all answer 404 alike, so the API never confirms that an inaccessible job exists.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\JobsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$job_id = 'job_id_example'; // string | Must be a job started inside the organization in the path.

try {
    $result = $apiInstance->getAsyncJob($organization_id, $job_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling JobsApi->getAsyncJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **job_id** | **string**| Must be a job started inside the organization in the path. | |

### Return type

[**\Mencoro\Api\Model\AsyncJobResource**](../Model/AsyncJobResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
