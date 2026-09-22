# Mencoro.Api.Api.DiscoveryApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**StartBrandDiscoveryJob**](DiscoveryApi.md#startbranddiscoveryjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/brands | Start a brand discovery job for a project |
| [**StartBrandNameSuggestionJob**](DiscoveryApi.md#startbrandnamesuggestionjob) | **POST** /api/v1/organizations/{organizationId}/brand-name-suggestions | Start a brand-name alias suggestion job |
| [**StartKeywordDiscoveryJob**](DiscoveryApi.md#startkeyworddiscoveryjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/keywords | Start a keyword discovery job for a project |
| [**StartPromptDiscoveryJob**](DiscoveryApi.md#startpromptdiscoveryjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/prompts | Start a geo prompt discovery job for a project |

<a id="startbranddiscoveryjob"></a>
# **StartBrandDiscoveryJob**
> AcceptedJobResource StartBrandDiscoveryJob (Guid organizationId, Guid projectId, string idempotencyKey, StartBrandDiscoveryJobRequest? startBrandDiscoveryJobRequest = null)

Start a brand discovery job for a project

Minimum role: manager. Starts background discovery of the brands and competitors around a project and answers 202 with the job to poll; it never returns brands inline. The job PROPOSES names: it creates and updates nothing, so neither the brand profile nor the competitor list changes because this endpoint was called. The organization must be active. Unlike keyword and prompt discovery this operation does not require an entitled subscription, matching the application behaviour it mirrors. Ten starts per minute per organization, counted across every key of every member and shared with the same operation in the Mencoro app; a retry carrying an Idempotency-Key already answered is served from the record and does not count. A project whose brand monitoring profile has not been created yet is still accepted and still billed: the job runs grounded on the project name alone, with no website domains, brand names or competitors to work from, and completes normally. Configure the brand profile first if you want the discovery grounded.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class StartBrandDiscoveryJobExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new DiscoveryApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | Must belong to the organization in the path.
            var idempotencyKey = "idempotencyKey_example";  // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
            var startBrandDiscoveryJobRequest = new StartBrandDiscoveryJobRequest?(); // StartBrandDiscoveryJobRequest? |  (optional) 

            try
            {
                // Start a brand discovery job for a project
                AcceptedJobResource result = apiInstance.StartBrandDiscoveryJob(organizationId, projectId, idempotencyKey, startBrandDiscoveryJobRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling DiscoveryApi.StartBrandDiscoveryJob: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the StartBrandDiscoveryJobWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Start a brand discovery job for a project
    ApiResponse<AcceptedJobResource> response = apiInstance.StartBrandDiscoveryJobWithHttpInfo(organizationId, projectId, idempotencyKey, startBrandDiscoveryJobRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling DiscoveryApi.StartBrandDiscoveryJobWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** | Must belong to the organization in the path. |  |
| **idempotencyKey** | **string** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. |  |
| **startBrandDiscoveryJobRequest** | [**StartBrandDiscoveryJobRequest?**](StartBrandDiscoveryJobRequest?.md) |  | [optional]  |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The discovery job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten brand discovery starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="startbrandnamesuggestionjob"></a>
# **StartBrandNameSuggestionJob**
> AcceptedJobResource StartBrandNameSuggestionJob (Guid organizationId, string idempotencyKey, StartBrandNameSuggestionJobRequest startBrandNameSuggestionJobRequest)

Start a brand-name alias suggestion job

Minimum role: manager. Starts a background, web-search-grounded job that suggests alias spellings for one entity - a brand, a project or a competitor - described entirely by the body, and answers 202 with the job to poll; it never returns suggestions inline. The entity need not exist: nothing is looked up, nothing is attached and nothing is saved, so the suggestions are the caller's to apply. Names sent in `enteredBrandNames` are excluded from the result. The organization must be active; no subscription is required, matching the application behaviour this mirrors. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class StartBrandNameSuggestionJobExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new DiscoveryApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
            var startBrandNameSuggestionJobRequest = new StartBrandNameSuggestionJobRequest(); // StartBrandNameSuggestionJobRequest | 

            try
            {
                // Start a brand-name alias suggestion job
                AcceptedJobResource result = apiInstance.StartBrandNameSuggestionJob(organizationId, idempotencyKey, startBrandNameSuggestionJobRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling DiscoveryApi.StartBrandNameSuggestionJob: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the StartBrandNameSuggestionJobWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Start a brand-name alias suggestion job
    ApiResponse<AcceptedJobResource> response = apiInstance.StartBrandNameSuggestionJobWithHttpInfo(organizationId, idempotencyKey, startBrandNameSuggestionJobRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling DiscoveryApi.StartBrandNameSuggestionJobWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **idempotencyKey** | **string** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. |  |
| **startBrandNameSuggestionJobRequest** | [**StartBrandNameSuggestionJobRequest**](StartBrandNameSuggestionJobRequest.md) |  |  |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The suggestion job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten suggestion starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="startkeyworddiscoveryjob"></a>
# **StartKeywordDiscoveryJob**
> AcceptedJobResource StartKeywordDiscoveryJob (Guid organizationId, Guid projectId, string idempotencyKey, StartKeywordDiscoveryJobRequest startKeywordDiscoveryJobRequest)

Start a keyword discovery job for a project

Minimum role: manager. Starts background keyword discovery from free-text seed input and answers 202 with the job to poll; it never returns keywords inline. The job SUGGESTS keywords - it creates no tracked queries and changes nothing in the project, so a completed job is a list to choose from, not work that has been applied. Queries the project already tracks are excluded from the suggestions automatically; `excludeQueries` adds more on top for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class StartKeywordDiscoveryJobExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new DiscoveryApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | Must belong to the organization in the path.
            var idempotencyKey = "idempotencyKey_example";  // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
            var startKeywordDiscoveryJobRequest = new StartKeywordDiscoveryJobRequest(); // StartKeywordDiscoveryJobRequest | 

            try
            {
                // Start a keyword discovery job for a project
                AcceptedJobResource result = apiInstance.StartKeywordDiscoveryJob(organizationId, projectId, idempotencyKey, startKeywordDiscoveryJobRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling DiscoveryApi.StartKeywordDiscoveryJob: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the StartKeywordDiscoveryJobWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Start a keyword discovery job for a project
    ApiResponse<AcceptedJobResource> response = apiInstance.StartKeywordDiscoveryJobWithHttpInfo(organizationId, projectId, idempotencyKey, startKeywordDiscoveryJobRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling DiscoveryApi.StartKeywordDiscoveryJobWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** | Must belong to the organization in the path. |  |
| **idempotencyKey** | **string** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. |  |
| **startKeywordDiscoveryJobRequest** | [**StartKeywordDiscoveryJobRequest**](StartKeywordDiscoveryJobRequest.md) |  |  |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The discovery job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **402** | The organization has no entitled subscription |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten discovery starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="startpromptdiscoveryjob"></a>
# **StartPromptDiscoveryJob**
> AcceptedJobResource StartPromptDiscoveryJob (Guid organizationId, Guid projectId, string idempotencyKey, StartPromptDiscoveryJobRequest startPromptDiscoveryJobRequest)

Start a geo prompt discovery job for a project

Minimum role: manager. Starts background discovery of natural-language prompts - the questions an answer engine gets asked - from free-text seed input, and answers 202 with the job to poll; it never returns prompts inline. The job SUGGESTS prompts: it creates no tracked queries and changes nothing in the project. `country` is required here, unlike keyword discovery, because a prompt is a question asked from somewhere and the provider request has no default for it. Queries the project already tracks are excluded automatically; `excludeQueries` adds more for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class StartPromptDiscoveryJobExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new DiscoveryApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | Must belong to the organization in the path.
            var idempotencyKey = "idempotencyKey_example";  // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
            var startPromptDiscoveryJobRequest = new StartPromptDiscoveryJobRequest(); // StartPromptDiscoveryJobRequest | 

            try
            {
                // Start a geo prompt discovery job for a project
                AcceptedJobResource result = apiInstance.StartPromptDiscoveryJob(organizationId, projectId, idempotencyKey, startPromptDiscoveryJobRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling DiscoveryApi.StartPromptDiscoveryJob: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the StartPromptDiscoveryJobWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Start a geo prompt discovery job for a project
    ApiResponse<AcceptedJobResource> response = apiInstance.StartPromptDiscoveryJobWithHttpInfo(organizationId, projectId, idempotencyKey, startPromptDiscoveryJobRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling DiscoveryApi.StartPromptDiscoveryJobWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** | Must belong to the organization in the path. |  |
| **idempotencyKey** | **string** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. |  |
| **startPromptDiscoveryJobRequest** | [**StartPromptDiscoveryJobRequest**](StartPromptDiscoveryJobRequest.md) |  |  |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The discovery job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **402** | The organization has no entitled subscription |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten discovery starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

