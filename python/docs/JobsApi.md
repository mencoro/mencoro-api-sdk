# mencoro.JobsApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_async_job**](JobsApi.md#get_async_job) | **GET** /api/v1/organizations/{organizationId}/jobs/{jobId} | Get an asynchronous job


# **get_async_job**
> AsyncJobResource get_async_job(organization_id, job_id)

Get an asynchronous job

Minimum role: manager. The status of one asynchronous job started inside this organization — geo prompt discovery, keyword discovery, query clustering, brand discovery or brand-name suggestion — and, once it has completed, its result. Poll it until `status` is terminal: `completed` or `failed`. A null `result` means the result is not known, either because the job is still in flight or because it failed; it never means the job produced an empty result. A failed job carries no reason: the stored one is an internal exception message, not a published field. A job started by another organization, a job of a type this API does not publish, and a job id that does not exist all answer 404 alike, so the API never confirms that an inaccessible job exists.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.async_job_resource import AsyncJobResource
from mencoro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mencoro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mencoro.Configuration(
    host = "https://api.mencoro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = mencoro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mencoro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mencoro.JobsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    job_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must be a job started inside the organization in the path.

    try:
        # Get an asynchronous job
        api_response = api_instance.get_async_job(organization_id, job_id)
        print("The response of JobsApi->get_async_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_async_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **job_id** | **UUID**| Must be a job started inside the organization in the path. | 

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
**200** | The job, and its result once it has completed |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization or job the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

