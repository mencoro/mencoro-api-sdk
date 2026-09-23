# AnalyticsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAvailableFilters**](AnalyticsApi.md#getAvailableFilters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/available-filters | Filter values a project is configured for |
| [**getCitedSources**](AnalyticsApi.md#getCitedSources) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/cited-sources | Domains and pages the AI answers cited |
| [**getClusterBreakdown**](AnalyticsApi.md#getClusterBreakdown) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/clusters | Rank-tracking metrics per keyword cluster |
| [**getCompetitorCoOccurrence**](AnalyticsApi.md#getCompetitorCoOccurrence) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/co-occurrence | Head-to-head record of the brand against each tracked competitor |
| [**getMentionMix**](AnalyticsApi.md#getMentionMix) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions/mix | Composition of a project brand mentions in AI answers |
| [**getMentionSamples**](AnalyticsApi.md#getMentionSamples) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions | Sample of the raw AI mention texts of a project |
| [**getMetricGlossary**](AnalyticsApi.md#getMetricGlossary) | **GET** /api/v1/metric-glossary | Map everyday wording to a metric and the operation that serves it |
| [**getOrganizationOverview**](AnalyticsApi.md#getOrganizationOverview) | **GET** /api/v1/organizations/{organizationId}/overview | Snapshot rank-health board across an organization active projects |
| [**getProjectMetrics**](AnalyticsApi.md#getProjectMetrics) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics | Headline visibility metrics of a project |
| [**getProjectSentiment**](AnalyticsApi.md#getProjectSentiment) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/sentiment | Sentiment breakdown of a project brand mentions |
| [**getProjectTimeSeries**](AnalyticsApi.md#getProjectTimeSeries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/timeseries | Rank-tracking metrics of a project over time |
| [**getQueryMovers**](AnalyticsApi.md#getQueryMovers) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/movers | Tracked queries ranked by how much a metric moved |
| [**getShareOfVoiceFormula**](AnalyticsApi.md#getShareOfVoiceFormula) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/share-of-voice-formula | The constants behind the Share of Voice score |
| [**getTrackedQueryTimeSeries**](AnalyticsApi.md#getTrackedQueryTimeSeries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/timeseries | Rank-tracking time series of a single tracked query |
| [**getTrackingCoverage**](AnalyticsApi.md#getTrackingCoverage) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/coverage | Coverage and staleness of a project tracked queries |
| [**listKeywordListings**](AnalyticsApi.md#listKeywordListings) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/keyword-listings | List a project&#39;s keywords with their windowed metrics |


<a id="getAvailableFilters"></a>
# **getAvailableFilters**
> GetAvailableFilters200Response getAvailableFilters(organizationId, projectId)

Filter values a project is configured for

Minimum role: viewer. Call this first: it is where every other analytics operation sends you for the valid engines, countries and keyword clusters of a project, and the values it returns are the exact strings the engines, countries and queryClusterIds parameters accept — anything else is rejected as a 400. Engines are engine codes, countries are ISO-3166 alpha-2 codes, and clusters are {id, name} objects whose id goes in queryClusterIds. Takes no date window: it describes how the project is configured right now, so a value is listed as soon as a tracked query uses it, even when no response has been captured for it yet. An empty list therefore means nothing is configured for it, not that no data was collected. Competitor ids are not part of this response.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    try {
      GetAvailableFilters200Response result = apiInstance.getAvailableFilters(organizationId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getAvailableFilters");
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

### Return type

[**GetAvailableFilters200Response**](GetAvailableFilters200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The engines, countries and clusters configured on the project |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getCitedSources"></a>
# **getCitedSources**
> CitedSourcesResponse getCitedSources(organizationId, projectId, dateFrom, dateTo, engines, groupBy, limit, offset)

Domains and pages the AI answers cited

Minimum role: viewer. The sources the answer engines drew on across a project&#39;s AI answers over a date window, ranked by how often they were cited. Per source: citationCount, the total number of citations; distinctResponseCount and distinctQueryCount, how many captured answers and tracked queries it appeared in; avgPosition, its average 1-based rank inside the answers&#39; citation lists, where LOWER is better. A null avgPosition means no citation in the window carried a position, not a rank of zero; a null domain or sampleTitle means the citation never carried one. &#x60;total&#x60; counts the distinct sources matching the window, before paging. The list is UNFILTERED by ownership: the brand&#39;s, competitors&#39; and third-party sources sit in the same ranking. Only the AI answer engines (chatgpt, perplexity, google_ai_overview, google_ai_mode) produce citations, so filtering by google_serp or google_shopping is accepted and returns nothing. Citations still behind an answer engine&#39;s redirect (a google.com/goto link, whose URL names the engine rather than the source) are excluded, so a source cited only through such links is absent from this list rather than counted as zero.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d.
    List<String> engines = Arrays.asList(); // List<String> | Repeatable, or comma-separated. Only the AI engines carry citations.
    String groupBy = "domain"; // String | Grain of the roll-up: \"domain\" by host, \"page\" by exact URL.
    Integer limit = 20; // Integer | Page size. A larger value is rejected, never silently reduced.
    Integer offset = 0; // Integer | Number of sources to skip.
    try {
      CitedSourcesResponse result = apiInstance.getCitedSources(organizationId, projectId, dateFrom, dateTo, engines, groupBy, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getCitedSources");
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
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. Only the AI engines carry citations. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **groupBy** | **String**| Grain of the roll-up: \&quot;domain\&quot; by host, \&quot;page\&quot; by exact URL. | [optional] [default to domain] [enum: domain, page] |
| **limit** | **Integer**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **Integer**| Number of sources to skip. | [optional] [default to 0] |

### Return type

[**CitedSourcesResponse**](CitedSourcesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cited sources for this page, plus the total number of distinct sources in the window |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter or page bound was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getClusterBreakdown"></a>
# **getClusterBreakdown**
> ProjectRankTrackingClusterBreakdown getClusterBreakdown(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries)

Rank-tracking metrics per keyword cluster

Minimum role: viewer. One row per keyword cluster over a date window, with its tracked query and keyword counts, average positions, rates, share of voice and sentiment split. A row whose clusterId is null is the ungrouped bucket: the tracked queries belonging to no cluster. Position metrics are 1-based and LOWER is better; rates, positivityIndex and shareOfVoice are 0-100 percentages where higher is better. A null metric means nothing was captured for that cluster in the window — it is not a zero, and averaging or charting it as one would misstate the period. dataDirtySince is non-null while a recalculation is pending, meaning the numbers predate the latest configuration change.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d.
    List<String> engines = Arrays.asList(); // List<String> | Repeatable, or comma-separated.
    List<String> countries = Arrays.asList(); // List<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
    List<UUID> queryClusterIds = Arrays.asList(); // List<UUID> | Restrict to these clusters. Each must belong to the project.
    Boolean includeUngroupedQueries = false; // Boolean | Sent alone, returns only the ungrouped bucket rather than adding it to every cluster.
    try {
      ProjectRankTrackingClusterBreakdown result = apiInstance.getClusterBreakdown(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getClusterBreakdown");
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
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | [**List&lt;String&gt;**](String.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **queryClusterIds** | [**List&lt;UUID&gt;**](UUID.md)| Restrict to these clusters. Each must belong to the project. | [optional] |
| **includeUngroupedQueries** | **Boolean**| Sent alone, returns only the ungrouped bucket rather than adding it to every cluster. | [optional] [default to false] |

### Return type

[**ProjectRankTrackingClusterBreakdown**](ProjectRankTrackingClusterBreakdown.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per keyword cluster, plus the ungrouped bucket where it applies |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getCompetitorCoOccurrence"></a>
# **getCompetitorCoOccurrence**
> CompetitorCoOccurrenceResponse getCompetitorCoOccurrence(organizationId, projectId, dateFrom, dateTo, engines, countries, competitorId)

Head-to-head record of the brand against each tracked competitor

Minimum role: viewer. Restricted to the AI answers where the brand and a competitor are BOTH mentioned, one row per tracked competitor: sharedResponseCount is how many such answers there are, and brandWins / competitorWins / ties split them by who holds the better (lower) best mention position. winRate is the percentage 0-100 of those answers the brand wins; avgOwnPosition and avgCompetitorPosition are the average best mention position each side held, 1-based, so LOWER is better. exampleQueryText and exampleAiResponseId point at one representative shared answer. Every nullable field means \&quot;not known yet\&quot; rather than zero: a null winRate or average position is the absence of a shared answer in the window, not a record of losing. Tracked competitors only.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d.
    List<String> engines = Arrays.asList(); // List<String> | Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence.
    List<String> countries = Arrays.asList(); // List<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
    UUID competitorId = UUID.randomUUID(); // UUID | Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids.
    try {
      CompetitorCoOccurrenceResponse result = apiInstance.getCompetitorCoOccurrence(organizationId, projectId, dateFrom, dateTo, engines, countries, competitorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getCompetitorCoOccurrence");
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
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | [**List&lt;String&gt;**](String.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **competitorId** | **UUID**| Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids. | [optional] |

### Return type

[**CompetitorCoOccurrenceResponse**](CompetitorCoOccurrenceResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One head-to-head row per tracked competitor, under \&quot;competitors\&quot; |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getMentionMix"></a>
# **getMentionMix**
> ProjectMentionMixResponse getMentionMix(organizationId, projectId, dateFrom, dateTo, engines, countries)

Composition of a project brand mentions in AI answers

Minimum role: viewer. Counts of the project brand&#39;s own text mentions in AI answers over a date window, grouped three ways: byType (recommendation, comparison, listing, example, reference), byTone (positive, neutral, negative) and byQualifier (direct, conditional — a conditional mention is one the answer hedged with a condition). These are the inputs behind the Share of Voice weighted score. Every bucket is always present and is a plain count, never null: a zero means no mention of that kind was found in the window. The three groupings count the same mentions, so each one sums to the same total. Only the project brand is counted, never a competitor, and only mentions inside the answer text — a citation of the brand&#39;s URL is not a mention here. Only AI answer engines produce mentions, so restricting engines to google_serp or google_shopping alone returns all zeros. For the positive/neutral/negative split per engine and per competitor use the sentiment endpoint.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d.
    List<String> engines = Arrays.asList(); // List<String> | Repeatable, or comma-separated. Non-AI engines contribute no mentions.
    List<String> countries = Arrays.asList(); // List<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
    try {
      ProjectMentionMixResponse result = apiInstance.getMentionMix(organizationId, projectId, dateFrom, dateTo, engines, countries);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getMentionMix");
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
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. Non-AI engines contribute no mentions. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | [**List&lt;String&gt;**](String.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |

### Return type

[**ProjectMentionMixResponse**](ProjectMentionMixResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Mention counts by type, by tone and by qualifier |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getMentionSamples"></a>
# **getMentionSamples**
> ProjectMentionSamplesResponse getMentionSamples(organizationId, projectId, dateFrom, dateTo, engines, countries, sentiment, mentionType, competitorId, sortBy, limit, offset)

Sample of the raw AI mention texts of a project

Minimum role: viewer. A paginated page of the individual mention texts behind the aggregate numbers, for qualitative review and for checking sentiment labels by eye. Each sample carries the mention text, the engine and country it was seen in, the tracked query that produced it, its sentiment and mention type, and mentionPosition — a 1-based rank inside the answer where LOWER is better, always present. &#x60;total&#x60; counts every mention matching the filters, not the size of the page returned. Only mentions inside the answer text are returned: a citation of the brand URL is not a mention here, and only AI answer engines produce mentions, so restricting engines to google_serp or google_shopping alone returns an empty page rather than an error. Two fields carry a \&quot;not known\&quot; rather than a zero: country is null and queryText is empty when the tracked query behind the mention has since been deleted, and competitorId is null when the mention row stores no competitor id — which is NOT an assertion that the mention is about your own brand, since an untracked competitor also stores none. Read mentionRelation instead: &#x60;own&#x60; and &#x60;tracked-competitor&#x60; are what the scraper resolved to a configured entity, &#x60;untracked-competitor&#x60; is a rival the project does not track, and null means the row predates the field. brandName carries the mentioned brand, and is the only way to name an untracked competitor, which has no competitor id to resolve one from. Omitting the competitorId filter returns exactly the rows with no competitor id stored — that is, own-brand AND untracked-competitor mentions together, not every competitor; pass a competitor UUID to restrict the page to that competitor, and use mentionRelation to separate the rest. For the aggregate positive/neutral/negative split use the sentiment endpoint, and for weighted mention-type counts the mention mix endpoint.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d.
    List<String> engines = Arrays.asList(); // List<String> | Repeatable, or comma-separated. Non-AI engines contribute no mentions.
    List<String> countries = Arrays.asList(); // List<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
    String sentiment = "positive"; // String | Restrict to one sentiment label. Omit for every sentiment.
    String mentionType = "recommendation"; // String | Restrict to one mention type. Omit for every type.
    UUID competitorId = UUID.randomUUID(); // UUID | UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart.
    String sortBy = "recent"; // String | recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default.
    Integer limit = 20; // Integer | Page size. A larger value is rejected, never silently reduced.
    Integer offset = 0; // Integer | Number of matching mentions to skip before the page starts.
    try {
      ProjectMentionSamplesResponse result = apiInstance.getMentionSamples(organizationId, projectId, dateFrom, dateTo, engines, countries, sentiment, mentionType, competitorId, sortBy, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getMentionSamples");
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
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. Non-AI engines contribute no mentions. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | [**List&lt;String&gt;**](String.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **sentiment** | **String**| Restrict to one sentiment label. Omit for every sentiment. | [optional] [enum: positive, neutral, negative] |
| **mentionType** | **String**| Restrict to one mention type. Omit for every type. | [optional] [enum: recommendation, comparison, listing, example, reference] |
| **competitorId** | **UUID**| UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart. | [optional] |
| **sortBy** | **String**| recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default. | [optional] [default to recent] [enum: recent, negative, engine, country] |
| **limit** | **Integer**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **Integer**| Number of matching mentions to skip before the page starts. | [optional] [default to 0] |

### Return type

[**ProjectMentionSamplesResponse**](ProjectMentionSamplesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of mention samples and the total matching the filters |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getMetricGlossary"></a>
# **getMetricGlossary**
> GetMetricGlossary200Response getMetricGlossary()

Map everyday wording to a metric and the operation that serves it

Static reference, no project data. Each entry gives a metric, the everyday words people use for it, its unit and range, whether higher or lower is better, the operation that returns it, and example questions. Useful when turning a vague or non-technical request into the right call.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    try {
      GetMetricGlossary200Response result = apiInstance.getMetricGlossary();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getMetricGlossary");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMetricGlossary200Response**](GetMetricGlossary200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric catalogue |  -  |
| **403** | The key lacks the read capability |  -  |
| **401** | Missing or invalid API key |  -  |

<a id="getOrganizationOverview"></a>
# **getOrganizationOverview**
> GetOrganizationOverview200Response getOrganizationOverview(organizationId)

Snapshot rank-health board across an organization active projects

Minimum role: viewer. One row per active project — share of voice, mention rate, average mention position, positivity index and tracked-query count — ordered by share of voice, plus an organization-level aggregate of the same metrics. Archived projects are excluded. This is a current-state snapshot and takes no date window; for a date-ranged comparison call the per-project operations (getProjectMetrics, getProjectTimeSeries) for each projectId returned here. Every metric is nullable, and a null means the project has no rank data yet — not a score of zero. Higher is better for shareOfVoice, mentionRate and positivityIndex; avgMentionPosition is a 1-based rank, so LOWER is better.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    try {
      GetOrganizationOverview200Response result = apiInstance.getOrganizationOverview(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getOrganizationOverview");
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

### Return type

[**GetOrganizationOverview200Response**](GetOrganizationOverview200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-project snapshot rows and the organization aggregate |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

<a id="getProjectMetrics"></a>
# **getProjectMetrics**
> ProjectRankTrackingStats getProjectMetrics(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries)

Headline visibility metrics of a project

Minimum role: viewer. The project overview over a date window: share of voice (own and per competitor), mention / SERP / shopping rates, average and best positions, position stability, the sentiment split and the position-distribution buckets. Positions are 1-based, so a LOWER number is better; rates, the positivity index and share of voice are percentages from 0 to 100, where HIGHER is better. Every &#x60;trend*&#x60; field is the signed change against the immediately preceding window of the same length: negative means an improved position, positive means an improved rate or score. A null metric means \&quot;not known yet\&quot;, never zero: a scalar is null when the window holds no checks at all, and a &#x60;trend*&#x60; field is null when there is no earlier window to compare against. The counters (&#x60;mentionCount&#x60;, &#x60;*TrackedQueryCount&#x60;, &#x60;*QueriesWithResult&#x60;, &#x60;sentiment*&#x60; and &#x60;mentionTypeCounts&#x60;) are genuine zeros instead, so an empty window reads as zero counts with null rates. &#x60;dataDirtySince&#x60; is non-null while a recalculation is pending, meaning the figures may still move for dates from then on.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d.
    List<String> engines = Arrays.asList(); // List<String> | Repeatable, or comma-separated.
    List<String> countries = Arrays.asList(); // List<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
    List<UUID> queryClusterIds = Arrays.asList(); // List<UUID> | Restrict to these keyword clusters. Each must belong to this project.
    Boolean includeUngroupedQueries = false; // Boolean | Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster.
    try {
      ProjectRankTrackingStats result = apiInstance.getProjectMetrics(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getProjectMetrics");
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
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | [**List&lt;String&gt;**](String.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **queryClusterIds** | [**List&lt;UUID&gt;**](UUID.md)| Restrict to these keyword clusters. Each must belong to this project. | [optional] |
| **includeUngroupedQueries** | **Boolean**| Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster. | [optional] [default to false] |

### Return type

[**ProjectRankTrackingStats**](ProjectRankTrackingStats.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Headline metrics, trends, sentiment split, per-competitor share of voice and position distributions |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getProjectSentiment"></a>
# **getProjectSentiment**
> ProjectSentimentBreakdown getProjectSentiment(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries)

Sentiment breakdown of a project brand mentions

Minimum role: viewer. Positive, neutral and negative split of the brand mentions in AI answers over a date window, per engine and per competitor. A null positivityIndex means no mentions were found in the window, which is not the same as a score of zero.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d.
    List<String> engines = Arrays.asList(); // List<String> | Repeatable, or comma-separated.
    List<String> countries = Arrays.asList(); // List<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
    List<UUID> queryClusterIds = Arrays.asList(); // List<UUID> | 
    Boolean includeUngroupedQueries = false; // Boolean | 
    try {
      ProjectSentimentBreakdown result = apiInstance.getProjectSentiment(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getProjectSentiment");
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
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | [**List&lt;String&gt;**](String.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **queryClusterIds** | [**List&lt;UUID&gt;**](UUID.md)|  | [optional] |
| **includeUngroupedQueries** | **Boolean**|  | [optional] [default to false] |

### Return type

[**ProjectSentimentBreakdown**](ProjectSentimentBreakdown.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sentiment per engine and per competitor |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getProjectTimeSeries"></a>
# **getProjectTimeSeries**
> ProjectRankTrackingTimeSeries getProjectTimeSeries(organizationId, projectId, dateFrom, dateTo, granularity, engines, countries, queryClusterIds, includeUngroupedQueries, competitorIds)

Rank-tracking metrics of a project over time

Minimum role: viewer. One point per bucket over the date window, each carrying the brand metrics and one same-shaped entry per requested competitor. Rank metrics (serp, shopping, mention, link) are 1-based averages where LOWER is better; positivity (0-100), shareOfVoice (0-100), mentionRate (0-100) and serpRate (0-100) are scores where higher is better. Every metric is nullable, and a null means no data was collected for that bucket, which is not the same as a value of zero. A project with no tracked queries returns an empty points list. Prefer weekly or monthly granularity over a long window to keep the response compact.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d.
    String granularity = "daily"; // String | Bucket size of each point.
    List<String> engines = Arrays.asList(); // List<String> | Repeatable, or comma-separated.
    List<String> countries = Arrays.asList(); // List<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
    List<UUID> queryClusterIds = Arrays.asList(); // List<UUID> | 
    Boolean includeUngroupedQueries = false; // Boolean | On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them.
    List<UUID> competitorIds = Arrays.asList(); // List<UUID> | Repeatable, or comma-separated. Each id adds one series under the competitors map of every point.
    try {
      ProjectRankTrackingTimeSeries result = apiInstance.getProjectTimeSeries(organizationId, projectId, dateFrom, dateTo, granularity, engines, countries, queryClusterIds, includeUngroupedQueries, competitorIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getProjectTimeSeries");
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
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. | |
| **granularity** | **String**| Bucket size of each point. | [optional] [default to daily] [enum: daily, weekly, monthly] |
| **engines** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | [**List&lt;String&gt;**](String.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **queryClusterIds** | [**List&lt;UUID&gt;**](UUID.md)|  | [optional] |
| **includeUngroupedQueries** | **Boolean**| On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them. | [optional] [default to false] |
| **competitorIds** | [**List&lt;UUID&gt;**](UUID.md)| Repeatable, or comma-separated. Each id adds one series under the competitors map of every point. | [optional] |

### Return type

[**ProjectRankTrackingTimeSeries**](ProjectRankTrackingTimeSeries.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Points in bucket order, plus dataDirtySince: a date from which the rank data is being recomputed, or null when nothing is pending |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getQueryMovers"></a>
# **getQueryMovers**
> TrackedQueryMoversResponse getQueryMovers(organizationId, projectId, dateFrom, dateTo, engines, countries, sortBy, sortOrder, limit, offset)

Tracked queries ranked by how much a metric moved

Minimum role: viewer. One row per tracked query — a single engine plus country — carrying its current metric envelope and the signed change against the immediately preceding window of equal length: a 7-day window is compared with the 7 days before it. Every trend delta is signed so that POSITIVE means improved, including the position trends, where the underlying avgSerpPosition / avgShoppingPosition / avgMentionPosition / avgLinkPosition are 1-based ranks and therefore LOWER is better. shareOfVoice and positivityIndex are percentages from 0 to 100, where HIGHER is better. Sorting applies to the trend keys only: sortOrder&#x3D;desc gives the top gainers, asc the top losers. Every nullable field means \&quot;not known yet\&quot; rather than zero — a null position or shareOfVoice is a query with no data in the window, and a null positivityIndex or trend is a period with no mentions to score, neither of which is a record of losing ground. total counts the tracked queries the filters match, not the rows on this page. dataDirtySince is a date from which the rank data is being recomputed, or null when nothing is pending; while it is non-null the deltas may still move.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d.
    List<String> engines = Arrays.asList(); // List<String> | Repeatable, or comma-separated.
    List<String> countries = Arrays.asList(); // List<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
    String sortBy = "trend_serp"; // String | Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default.
    String sortOrder = "asc"; // String | desc for the top gainers, asc for the top losers.
    Integer limit = 20; // Integer | Page size. A value above the maximum is rejected, never clamped.
    Integer offset = 0; // Integer | 
    try {
      TrackedQueryMoversResponse result = apiInstance.getQueryMovers(organizationId, projectId, dateFrom, dateTo, engines, countries, sortBy, sortOrder, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getQueryMovers");
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
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | [**List&lt;String&gt;**](String.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **sortBy** | **String**| Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default. | [optional] [default to trend_share_of_voice] [enum: trend_serp, trend_shopping, trend_mention, trend_link, trend_share_of_voice] |
| **sortOrder** | **String**| desc for the top gainers, asc for the top losers. | [optional] [default to desc] [enum: asc, desc] |
| **limit** | **Integer**| Page size. A value above the maximum is rejected, never clamped. | [optional] [default to 20] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**TrackedQueryMoversResponse**](TrackedQueryMoversResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ranked tracked queries under \&quot;rows\&quot;, with \&quot;total\&quot; and \&quot;dataDirtySince\&quot; |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter or page bound was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getShareOfVoiceFormula"></a>
# **getShareOfVoiceFormula**
> GetShareOfVoiceFormula200Response getShareOfVoiceFormula(organizationId, projectId)

The constants behind the Share of Voice score

Minimum role: viewer. Static reference data, the same for every project: the weights and multipliers that turn individual brand mentions into a Share of Voice score. Each mention is worth &#x60;mentionTypeWeights[type] * sentimentMultipliers[tone] * (conditional ? conditionalMultiplier : directMultiplier)&#x60;, and a competitor&#39;s Share of Voice is its share of the summed weights of every brand in the window, as a percentage. mentionTypeWeights is keyed by mention type (recommendation, comparison, listing, example, reference) and sentimentMultipliers by tone (positive, neutral, negative); a negative mention is discounted, not discarded, because it still evidences presence. A conditional mention is one the answer hedged with a condition (\&quot;if you need X\&quot;). Use this to explain a score, not to recompute one: the counts it applies to come from the mention mix endpoint. Every value is always present and is never null.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    try {
      GetShareOfVoiceFormula200Response result = apiInstance.getShareOfVoiceFormula(organizationId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getShareOfVoiceFormula");
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

### Return type

[**GetShareOfVoiceFormula200Response**](GetShareOfVoiceFormula200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Share of Voice weighting constants |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | Not reachable here: the endpoint accepts no query parameters, so it has nothing to reject. Listed because the error envelope is shared across the API |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="getTrackedQueryTimeSeries"></a>
# **getTrackedQueryTimeSeries**
> TrackedQueryRankTrackingTimeSeries getTrackedQueryTimeSeries(organizationId, projectId, trackedQueryId, dateFrom, dateTo, granularity, competitorIds)

Rank-tracking time series of a single tracked query

Minimum role: viewer. One point per bucket over the date window, each carrying the brand metrics and one same-shaped entry per requested competitor. Positions (serp, shopping, mention, link) are 1-based, so a LOWER number is better; positivity, shareOfVoice, mentionRate and serpRate are percentages from 0 to 100, where higher is better. Every metric is nullable, and a null means nothing was captured for that entity in that bucket — it is not a zero: a null shareOfVoice means no measurement, a shareOfVoice of 0 means measured and never mentioned. The tracked query fixes its own engine and country, so no engine or country filter is accepted. A non-null dataDirtySince is a timestamp warning that tracked queries were deleted from the project and historical buckets may still include their contributions until the nightly refresh rebuilds them.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    UUID trackedQueryId = UUID.randomUUID(); // UUID | Must belong to the project in the path.
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d.
    String granularity = "daily"; // String | Bucket size. Prefer weekly or monthly for long windows.
    List<UUID> competitorIds = Arrays.asList(); // List<UUID> | Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint.
    try {
      TrackedQueryRankTrackingTimeSeries result = apiInstance.getTrackedQueryTimeSeries(organizationId, projectId, trackedQueryId, dateFrom, dateTo, granularity, competitorIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getTrackedQueryTimeSeries");
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
| **trackedQueryId** | **UUID**| Must belong to the project in the path. | |
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. | |
| **granularity** | **String**| Bucket size. Prefer weekly or monthly for long windows. | [optional] [default to daily] [enum: daily, weekly, monthly] |
| **competitorIds** | [**List&lt;UUID&gt;**](UUID.md)| Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint. | [optional] |

### Return type

[**TrackedQueryRankTrackingTimeSeries**](TrackedQueryRankTrackingTimeSeries.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One point per bucket, with brand and per-competitor metrics |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization, project or tracked query the caller can access under these ids |  -  |

<a id="getTrackingCoverage"></a>
# **getTrackingCoverage**
> GetTrackingCoverage200Response getTrackingCoverage(organizationId, projectId)

Coverage and staleness of a project tracked queries

Minimum role: viewer. A current-state snapshot answering \&quot;what is stale or not being tracked\&quot;: total is every tracked query on the project, active and paused split it by status, neverChecked counts the active queries that have never run, and overdue counts the active queries whose last check is older than their own check-frequency interval (daily, weekly or monthly). neverChecked and overdue are disjoint — a query that has never run is never also counted as overdue — and both ignore paused queries, which are not expected to be checked at all. sample lists up to 20 of the overdue queries, most stale first; it is a sample of overdue only, so it never contains a never-checked query and is empty when overdue is 0. Takes no date window: every count describes the project as it stands right now.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    try {
      GetTrackingCoverage200Response result = apiInstance.getTrackingCoverage(organizationId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getTrackingCoverage");
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

### Return type

[**GetTrackingCoverage200Response**](GetTrackingCoverage200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Coverage counts and a sample of the most-overdue queries |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | The request was rejected before it reached the project; this endpoint accepts no query parameters, so no filter can be refused here |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

<a id="listKeywordListings"></a>
# **listKeywordListings**
> ListKeywordListings200Response listKeywordListings(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries, status, checkFrequencies, nPasses, search, sortBy, sortOrder, limit, offset)

List a project&#39;s keywords with their windowed metrics

Minimum role: viewer. One row per distinct keyword text of the project — every tracked query asking that text, on any engine in any country, collapsed into a single row whose variantIds name the tracked queries behind it. Each row carries the metrics of the requested window and a signed trend against the window of equal length immediately before it, where POSITIVE ALWAYS MEANS BETTER whichever direction the metric itself runs. Positions are 1-based and lower is better; rates, positivityIndex and shareOfVoice are 0-100 and higher is better; mentionPositionStability is a day-to-day spread, so lower is steadier. A null metric means nothing was captured for that keyword in the window — it is not a zero. &#x60;total&#x60; counts the KEYWORDS matching the filters, not the rows on this page and not tracked queries; &#x60;totalVariantCount&#x60; counts the tracked queries behind the keywords matching every filter EXCEPT &#x60;search&#x60; — with a text search applied it still counts the project&#39;s variants, so do not size a force-check budget from it on a searched page. NEITHER IS THE PROJECT&#39;S TRACKED-QUERY COUNT: the count operation reads the write model, while this listing reads projections refreshed in the background from it, so the numbers legitimately differ while those projections catch up. A project whose cached tracked-query count has not been refreshed yet answers an empty page with total 0 — the same answer as a project with no tracked queries at all — so treat an unexpected empty page right after creating queries as \&quot;not projected yet\&quot;, not as \&quot;no data\&quot;. dataDirtySince is non-null while a recalculation is pending, meaning the metrics predate the latest configuration change. Filters narrow which VARIANTS count towards a row, so engines, countries, statuses, checkFrequencies and nPassesValues each report what the filters selected rather than everything the keyword has. A filter or sort key this endpoint cannot honour is rejected by name, never ignored, and a limit above the maximum is rejected rather than quietly reduced. This operation answers JSON only: a keyword row carries a nested mentionTypeCounts object, so it is not part of the CSV family.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    LocalDate dateTo = LocalDate.now(); // LocalDate | Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom.
    List<String> engines = Arrays.asList(); // List<String> | Repeatable, or comma-separated. Narrows which variants count towards each row.
    List<String> countries = Arrays.asList(); // List<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
    List<UUID> queryClusterIds = Arrays.asList(); // List<UUID> | Restrict to keywords with a variant in these clusters. Each must belong to the project.
    Boolean includeUngroupedQueries = false; // Boolean | Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection.
    String status = "active"; // String | Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \"mixed\".
    List<String> checkFrequencies = Arrays.asList(); // List<String> | Repeatable, or comma-separated.
    List<Integer> nPasses = Arrays.asList(); // List<Integer> | Repeatable, or comma-separated. Restrict to variants configured with these pass counts.
    String search = "search_example"; // String | Case-insensitive substring match on the keyword text.
    String sortBy = "keyword"; // String | Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default.
    String sortOrder = "asc"; // String | 
    Integer limit = 20; // Integer | Page size. A larger value is rejected, never silently reduced.
    Integer offset = 0; // Integer | Number of matching keywords to skip before the page starts.
    try {
      ListKeywordListings200Response result = apiInstance.listKeywordListings(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries, status, checkFrequencies, nPasses, search, sortBy, sortOrder, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#listKeywordListings");
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
| **dateFrom** | **LocalDate**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **dateTo** | **LocalDate**| Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom. | |
| **engines** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. Narrows which variants count towards each row. | [optional] [enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | [**List&lt;String&gt;**](String.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **queryClusterIds** | [**List&lt;UUID&gt;**](UUID.md)| Restrict to keywords with a variant in these clusters. Each must belong to the project. | [optional] |
| **includeUngroupedQueries** | **Boolean**| Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection. | [optional] [default to false] |
| **status** | **String**| Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \&quot;mixed\&quot;. | [optional] [enum: active, paused] |
| **checkFrequencies** | [**List&lt;String&gt;**](String.md)| Repeatable, or comma-separated. | [optional] [enum: daily, weekly, monthly] |
| **nPasses** | [**List&lt;Integer&gt;**](Integer.md)| Repeatable, or comma-separated. Restrict to variants configured with these pass counts. | [optional] |
| **search** | **String**| Case-insensitive substring match on the keyword text. | [optional] |
| **sortBy** | **String**| Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default. | [optional] [default to keyword] [enum: keyword, variantCount, lastCheckedAt, statusSummary, positivityIndex, shareOfVoice, avgMentionPosition, avgLinkPosition, mentionPositionStability, avgSerpPosition, avgShoppingPosition] |
| **sortOrder** | **String**|  | [optional] [default to asc] [enum: asc, desc] |
| **limit** | **Integer**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **Integer**| Number of matching keywords to skip before the page starts. | [optional] [default to 0] |

### Return type

[**ListKeywordListings200Response**](ListKeywordListings200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of keywords, the totals behind it, and whether the metrics are pending recalculation |  -  |
| **400** | A filter, sort key or page bound was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

