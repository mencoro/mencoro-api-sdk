# JobsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAsyncJob**](JobsApi.md#getasyncjob) | **GET** /api/v1/organizations/{organizationId}/jobs/{jobId} | Get an asynchronous job |



## getAsyncJob

> AsyncJobResource getAsyncJob(organizationId, jobId)

Get an asynchronous job

Minimum role: manager. The status of one asynchronous job started inside this organization — geo prompt discovery, keyword discovery, query clustering, brand discovery or brand-name suggestion — and, once it has completed, its result. Poll it until &#x60;status&#x60; is terminal: &#x60;completed&#x60; or &#x60;failed&#x60;. A null &#x60;result&#x60; means the result is not known, either because the job is still in flight or because it failed; it never means the job produced an empty result. A failed job carries no reason: the stored one is an internal exception message, not a published field. A job started by another organization, a job of a type this API does not publish, and a job id that does not exist all answer 404 alike, so the API never confirms that an inaccessible job exists.

### Example

```ts
import {
  Configuration,
  JobsApi,
} from '@mencoro/api';
import type { GetAsyncJobRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new JobsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must be a job started inside the organization in the path.
    jobId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetAsyncJobRequest;

  try {
    const data = await api.getAsyncJob(body);
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
| **jobId** | `string` | Must be a job started inside the organization in the path. | [Defaults to `undefined`] |

### Return type

[**AsyncJobResource**](AsyncJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job, and its result once it has completed |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or job the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

