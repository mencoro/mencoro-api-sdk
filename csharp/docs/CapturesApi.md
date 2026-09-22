# Mencoro.Api.Api.CapturesApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ListAiResponses**](CapturesApi.md#listairesponses) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/ai-responses | List captured AI answers |
| [**ListSearchSnapshots**](CapturesApi.md#listsearchsnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/search-snapshots | List captured search-results pages |
| [**ListShoppingSnapshots**](CapturesApi.md#listshoppingsnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/shopping-snapshots | List captured shopping-results pages |

<a id="listairesponses"></a>
# **ListAiResponses**
> ListAiResponses200Response ListAiResponses (Guid organizationId, Guid projectId, DateOnly? dateFrom = null, DateOnly? dateTo = null, Guid? trackedQueryId = null, List<string>? engines = null, int? limit = null, int? offset = null, string? sortOrder = null)

List captured AI answers

Minimum role: viewer. Every AI answer captured for a project, newest first, one page at a time. This is the evidence under the analytics operations: the full answer text and the sources the engine cited, exactly as captured. Read `unresolved` on a citation before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector, not to the publisher; count the citation, do not credit the site. `passIndex` and `passCount` describe multi-pass sampling: rows sharing a `trackedQueryId` and `capturedAt` are passes of one run, not duplicates, so aggregating across them without dividing by `passCount` double-counts that run. `responseText` is the whole answer, so a page of 100 is a large response — lower `limit` rather than paging blind. Captures are kept for 16 months and purged after that; a `dateFrom` before the window is rejected rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

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
    public class ListAiResponsesExample
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
            var apiInstance = new CapturesApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly? | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. (optional) 
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly? | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional) 
            var trackedQueryId = "trackedQueryId_example";  // Guid? | Only captures of this tracked query. Must belong to the project in the path. (optional) 
            var engines = new List<string>?(); // List<string>? | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. (optional) 
            var limit = 20;  // int? | Page size. A larger value is rejected, never silently reduced. (optional)  (default to 20)
            var offset = 0;  // int? | Number of captures to skip before the page starts. (optional)  (default to 0)
            var sortOrder = "asc";  // string? | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional)  (default to desc)

            try
            {
                // List captured AI answers
                ListAiResponses200Response result = apiInstance.ListAiResponses(organizationId, projectId, dateFrom, dateTo, trackedQueryId, engines, limit, offset, sortOrder);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CapturesApi.ListAiResponses: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListAiResponsesWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List captured AI answers
    ApiResponse<ListAiResponses200Response> response = apiInstance.ListAiResponsesWithHttpInfo(organizationId, projectId, dateFrom, dateTo, trackedQueryId, engines, limit, offset, sortOrder);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CapturesApi.ListAiResponsesWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly?** | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [optional]  |
| **dateTo** | **DateOnly?** | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional]  |
| **trackedQueryId** | **Guid?** | Only captures of this tracked query. Must belong to the project in the path. | [optional]  |
| **engines** | [**List&lt;string&gt;?**](string.md) | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. | [optional]  |
| **limit** | **int?** | Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int?** | Number of captures to skip before the page starts. | [optional] [default to 0] |
| **sortOrder** | **string?** | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to desc] |

### Return type

[**ListAiResponses200Response**](ListAiResponses200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of captured AI answers and the total the filter matches |  -  |
| **400** | A filter, pagination or ordering parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listsearchsnapshots"></a>
# **ListSearchSnapshots**
> ListSearchSnapshots200Response ListSearchSnapshots (Guid organizationId, Guid projectId, DateOnly? dateFrom = null, DateOnly? dateTo = null, Guid? trackedQueryId = null, int? limit = null, int? offset = null, string? sortOrder = null)

List captured search-results pages

Minimum role: viewer. Every organic search page captured for a project, newest first, one page at a time. This is what the rank figures in the analytics operations were computed from: the ranked results as they stood at `capturedAt`, not as they stand now. Read `unresolved` on a result before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector; count the result, do not credit the site. `rating` and `ratingVotes` come from a rich-result star rating when Google showed one and are absent far more often than present; their absence says nothing about the page. There is no `engines` filter because every capture here comes from Google SERP. Captures are kept for 16 months and purged after that; a `dateFrom` before the window is rejected rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

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
    public class ListSearchSnapshotsExample
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
            var apiInstance = new CapturesApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly? | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. (optional) 
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly? | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional) 
            var trackedQueryId = "trackedQueryId_example";  // Guid? | Only captures of this tracked query. Must belong to the project in the path. (optional) 
            var limit = 20;  // int? | Page size. A larger value is rejected, never silently reduced. (optional)  (default to 20)
            var offset = 0;  // int? | Number of captures to skip before the page starts. (optional)  (default to 0)
            var sortOrder = "asc";  // string? | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional)  (default to desc)

            try
            {
                // List captured search-results pages
                ListSearchSnapshots200Response result = apiInstance.ListSearchSnapshots(organizationId, projectId, dateFrom, dateTo, trackedQueryId, limit, offset, sortOrder);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CapturesApi.ListSearchSnapshots: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListSearchSnapshotsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List captured search-results pages
    ApiResponse<ListSearchSnapshots200Response> response = apiInstance.ListSearchSnapshotsWithHttpInfo(organizationId, projectId, dateFrom, dateTo, trackedQueryId, limit, offset, sortOrder);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CapturesApi.ListSearchSnapshotsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly?** | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [optional]  |
| **dateTo** | **DateOnly?** | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional]  |
| **trackedQueryId** | **Guid?** | Only captures of this tracked query. Must belong to the project in the path. | [optional]  |
| **limit** | **int?** | Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int?** | Number of captures to skip before the page starts. | [optional] [default to 0] |
| **sortOrder** | **string?** | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to desc] |

### Return type

[**ListSearchSnapshots200Response**](ListSearchSnapshots200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of captured search-results pages and the total the filter matches |  -  |
| **400** | A filter, pagination or ordering parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listshoppingsnapshots"></a>
# **ListShoppingSnapshots**
> ListShoppingSnapshots200Response ListShoppingSnapshots (Guid organizationId, Guid projectId, DateOnly? dateFrom = null, DateOnly? dateTo = null, Guid? trackedQueryId = null, int? limit = null, int? offset = null, string? sortOrder = null)

List captured shopping-results pages

Minimum role: viewer. Every shopping page captured for a project, newest first, one page at a time: the ranked offers as they stood at `capturedAt`. `price` and `currency` are what the seller showed at that moment — no tax normalisation, no shipping, no conversion — and two offers in one snapshot may carry different currencies, so convert before comparing. `productId` is the marketplace's own identifier for the listing, stable enough to follow one offer across snapshots, and it is not a Mencoro id. Offers turn over far faster than organic results, so two snapshots days apart routinely share none; that is the marketplace behaving normally, not a gap in the capture. Unlike organic results, a shopping offer carries no `unresolved` flag: the capture pipeline does not record one for this surface. Shopping captures are trimmed by the same raw-data purge as AI answers and search pages, so the same retention floor applies: a `dateFrom` before it is refused rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

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
    public class ListShoppingSnapshotsExample
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
            var apiInstance = new CapturesApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly? | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. (optional) 
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly? | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional) 
            var trackedQueryId = "trackedQueryId_example";  // Guid? | Only captures of this tracked query. Must belong to the project in the path. (optional) 
            var limit = 20;  // int? | Page size. A larger value is rejected, never silently reduced. (optional)  (default to 20)
            var offset = 0;  // int? | Number of captures to skip before the page starts. (optional)  (default to 0)
            var sortOrder = "asc";  // string? | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional)  (default to desc)

            try
            {
                // List captured shopping-results pages
                ListShoppingSnapshots200Response result = apiInstance.ListShoppingSnapshots(organizationId, projectId, dateFrom, dateTo, trackedQueryId, limit, offset, sortOrder);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CapturesApi.ListShoppingSnapshots: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListShoppingSnapshotsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List captured shopping-results pages
    ApiResponse<ListShoppingSnapshots200Response> response = apiInstance.ListShoppingSnapshotsWithHttpInfo(organizationId, projectId, dateFrom, dateTo, trackedQueryId, limit, offset, sortOrder);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CapturesApi.ListShoppingSnapshotsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly?** | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. | [optional]  |
| **dateTo** | **DateOnly?** | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional]  |
| **trackedQueryId** | **Guid?** | Only captures of this tracked query. Must belong to the project in the path. | [optional]  |
| **limit** | **int?** | Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int?** | Number of captures to skip before the page starts. | [optional] [default to 0] |
| **sortOrder** | **string?** | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to desc] |

### Return type

[**ListShoppingSnapshots200Response**](ListShoppingSnapshots200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of captured shopping-results pages and the total the filter matches |  -  |
| **400** | A filter, pagination or ordering parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

