# CapturesApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listAiResponses**](CapturesApi.md#listAiResponses) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/ai-responses | List captured AI answers |
| [**listSearchSnapshots**](CapturesApi.md#listSearchSnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/search-snapshots | List captured search-results pages |
| [**listShoppingSnapshots**](CapturesApi.md#listShoppingSnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/shopping-snapshots | List captured shopping-results pages |


<a id="listAiResponses"></a>
# **listAiResponses**
> ListAiResponses200Response listAiResponses(organizationId, projectId, dateFrom, dateTo, trackedQueryId, engines, limit, offset, sortOrder)

List captured AI answers

Minimum role: viewer. Every AI answer captured for a project, newest first, one page at a time. This is the evidence under the analytics operations: the full answer text and the sources the engine cited, exactly as captured. Read &#x60;unresolved&#x60; on a citation before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector, not to the publisher; count the citation, do not credit the site. &#x60;passIndex&#x60; and &#x60;passCount&#x60; describe multi-pass sampling: rows sharing a &#x60;trackedQueryId&#x60; and &#x60;capturedAt&#x60; are passes of one run, not duplicates, so aggregating across them without dividing by &#x60;passCount&#x60; double-counts that run. &#x60;responseText&#x60; is the whole answer, so a page of 100 is a large response — lower &#x60;limit&#x60; rather than paging blind. Captures are kept for 16 months and purged after that; a &#x60;dateFrom&#x60; before the window is rejected rather than answered with an empty page. &#x60;total&#x60; counts every capture the filter matches, not the size of this page.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.CapturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    CapturesApi apiInstance = new CapturesApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive upper bound, widened to 23:59:59 UTC of the named day.
    UUID trackedQueryId = UUID.randomUUID(); // UUID | Only captures of this tracked query. Must belong to the project in the path.
    List<String> engines = Arrays.asList(); // List<String> | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine.
    Integer limit = 20; // Integer | Page size. A larger value is rejected, never silently reduced.
    Integer offset = 0; // Integer | Number of captures to skip before the page starts.
    String sortOrder = "asc"; // String | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default.
    try {
      ListAiResponses200Response result = apiInstance.listAiResponses(organizationId, projectId, dateFrom, dateTo, trackedQueryId, engines, limit, offset, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapturesApi#listAiResponses");
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
| **projectId** | **UUID**|  | |
| **dateFrom** | **LocalDate**| Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [optional] |
| **dateTo** | **LocalDate**| Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] |
| **trackedQueryId** | **UUID**| Only captures of this tracked query. Must belong to the project in the path. | [optional] |
| **engines** | [**List&lt;String&gt;**](String.md)| Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode] |
| **limit** | **Integer**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **Integer**| Number of captures to skip before the page starts. | [optional] [default to 0] |
| **sortOrder** | **String**| Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to desc] [enum: asc, desc] |

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

<a id="listSearchSnapshots"></a>
# **listSearchSnapshots**
> ListSearchSnapshots200Response listSearchSnapshots(organizationId, projectId, dateFrom, dateTo, trackedQueryId, limit, offset, sortOrder)

List captured search-results pages

Minimum role: viewer. Every organic search page captured for a project, newest first, one page at a time. This is what the rank figures in the analytics operations were computed from: the ranked results as they stood at &#x60;capturedAt&#x60;, not as they stand now. Read &#x60;unresolved&#x60; on a result before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector; count the result, do not credit the site. &#x60;rating&#x60; and &#x60;ratingVotes&#x60; come from a rich-result star rating when Google showed one and are absent far more often than present; their absence says nothing about the page. There is no &#x60;engines&#x60; filter because every capture here comes from Google SERP. Captures are kept for 16 months and purged after that; a &#x60;dateFrom&#x60; before the window is rejected rather than answered with an empty page. &#x60;total&#x60; counts every capture the filter matches, not the size of this page.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.CapturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    CapturesApi apiInstance = new CapturesApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive upper bound, widened to 23:59:59 UTC of the named day.
    UUID trackedQueryId = UUID.randomUUID(); // UUID | Only captures of this tracked query. Must belong to the project in the path.
    Integer limit = 20; // Integer | Page size. A larger value is rejected, never silently reduced.
    Integer offset = 0; // Integer | Number of captures to skip before the page starts.
    String sortOrder = "asc"; // String | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default.
    try {
      ListSearchSnapshots200Response result = apiInstance.listSearchSnapshots(organizationId, projectId, dateFrom, dateTo, trackedQueryId, limit, offset, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapturesApi#listSearchSnapshots");
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
| **projectId** | **UUID**|  | |
| **dateFrom** | **LocalDate**| Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [optional] |
| **dateTo** | **LocalDate**| Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] |
| **trackedQueryId** | **UUID**| Only captures of this tracked query. Must belong to the project in the path. | [optional] |
| **limit** | **Integer**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **Integer**| Number of captures to skip before the page starts. | [optional] [default to 0] |
| **sortOrder** | **String**| Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to desc] [enum: asc, desc] |

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

<a id="listShoppingSnapshots"></a>
# **listShoppingSnapshots**
> ListShoppingSnapshots200Response listShoppingSnapshots(organizationId, projectId, dateFrom, dateTo, trackedQueryId, limit, offset, sortOrder)

List captured shopping-results pages

Minimum role: viewer. Every shopping page captured for a project, newest first, one page at a time: the ranked offers as they stood at &#x60;capturedAt&#x60;. &#x60;price&#x60; and &#x60;currency&#x60; are what the seller showed at that moment — no tax normalisation, no shipping, no conversion — and two offers in one snapshot may carry different currencies, so convert before comparing. &#x60;productId&#x60; is the marketplace&#39;s own identifier for the listing, stable enough to follow one offer across snapshots, and it is not a Mencoro id. Offers turn over far faster than organic results, so two snapshots days apart routinely share none; that is the marketplace behaving normally, not a gap in the capture. Unlike organic results, a shopping offer carries no &#x60;unresolved&#x60; flag: the capture pipeline does not record one for this surface. Shopping captures are trimmed by the same raw-data purge as AI answers and search pages, so the same retention floor applies: a &#x60;dateFrom&#x60; before it is refused rather than answered with an empty page. &#x60;total&#x60; counts every capture the filter matches, not the size of this page.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.CapturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    CapturesApi apiInstance = new CapturesApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive upper bound, widened to 23:59:59 UTC of the named day.
    UUID trackedQueryId = UUID.randomUUID(); // UUID | Only captures of this tracked query. Must belong to the project in the path.
    Integer limit = 20; // Integer | Page size. A larger value is rejected, never silently reduced.
    Integer offset = 0; // Integer | Number of captures to skip before the page starts.
    String sortOrder = "asc"; // String | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default.
    try {
      ListShoppingSnapshots200Response result = apiInstance.listShoppingSnapshots(organizationId, projectId, dateFrom, dateTo, trackedQueryId, limit, offset, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapturesApi#listShoppingSnapshots");
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
| **projectId** | **UUID**|  | |
| **dateFrom** | **LocalDate**| Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. | [optional] |
| **dateTo** | **LocalDate**| Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] |
| **trackedQueryId** | **UUID**| Only captures of this tracked query. Must belong to the project in the path. | [optional] |
| **limit** | **Integer**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **Integer**| Number of captures to skip before the page starts. | [optional] [default to 0] |
| **sortOrder** | **String**| Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to desc] [enum: asc, desc] |

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

