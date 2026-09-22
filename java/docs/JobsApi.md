# JobsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAsyncJob**](JobsApi.md#getAsyncJob) | **GET** /api/v1/organizations/{organizationId}/jobs/{jobId} | Get an asynchronous job |


<a id="getAsyncJob"></a>
# **getAsyncJob**
> AsyncJobResource getAsyncJob(organizationId, jobId)

Get an asynchronous job

Minimum role: manager. The status of one asynchronous job started inside this organization — geo prompt discovery, keyword discovery, query clustering, brand discovery or brand-name suggestion — and, once it has completed, its result. Poll it until &#x60;status&#x60; is terminal: &#x60;completed&#x60; or &#x60;failed&#x60;. A null &#x60;result&#x60; means the result is not known, either because the job is still in flight or because it failed; it never means the job produced an empty result. A failed job carries no reason: the stored one is an internal exception message, not a published field. A job started by another organization, a job of a type this API does not publish, and a job id that does not exist all answer 404 alike, so the API never confirms that an inaccessible job exists.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID jobId = UUID.randomUUID(); // UUID | Must be a job started inside the organization in the path.
    try {
      AsyncJobResource result = apiInstance.getAsyncJob(organizationId, jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#getAsyncJob");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **UUID**|  | |
| **jobId** | **UUID**| Must be a job started inside the organization in the path. | |

### Return type

[**AsyncJobResource**](AsyncJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job, and its result once it has completed |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or job the caller can access under these ids |  -  |

