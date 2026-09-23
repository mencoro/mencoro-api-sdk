# Mencoro.Api.Api.AnalyticsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetAvailableFilters**](AnalyticsApi.md#getavailablefilters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/available-filters | Filter values a project is configured for |
| [**GetCitedSources**](AnalyticsApi.md#getcitedsources) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/cited-sources | Domains and pages the AI answers cited |
| [**GetClusterBreakdown**](AnalyticsApi.md#getclusterbreakdown) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/clusters | Rank-tracking metrics per keyword cluster |
| [**GetCompetitorCoOccurrence**](AnalyticsApi.md#getcompetitorcooccurrence) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/co-occurrence | Head-to-head record of the brand against each tracked competitor |
| [**GetMentionMix**](AnalyticsApi.md#getmentionmix) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions/mix | Composition of a project brand mentions in AI answers |
| [**GetMentionSamples**](AnalyticsApi.md#getmentionsamples) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions | Sample of the raw AI mention texts of a project |
| [**GetMetricGlossary**](AnalyticsApi.md#getmetricglossary) | **GET** /api/v1/metric-glossary | Map everyday wording to a metric and the operation that serves it |
| [**GetOrganizationOverview**](AnalyticsApi.md#getorganizationoverview) | **GET** /api/v1/organizations/{organizationId}/overview | Snapshot rank-health board across an organization active projects |
| [**GetProjectMetrics**](AnalyticsApi.md#getprojectmetrics) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics | Headline visibility metrics of a project |
| [**GetProjectSentiment**](AnalyticsApi.md#getprojectsentiment) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/sentiment | Sentiment breakdown of a project brand mentions |
| [**GetProjectTimeSeries**](AnalyticsApi.md#getprojecttimeseries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/timeseries | Rank-tracking metrics of a project over time |
| [**GetQueryMovers**](AnalyticsApi.md#getquerymovers) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/movers | Tracked queries ranked by how much a metric moved |
| [**GetShareOfVoiceFormula**](AnalyticsApi.md#getshareofvoiceformula) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/share-of-voice-formula | The constants behind the Share of Voice score |
| [**GetTrackedQueryTimeSeries**](AnalyticsApi.md#gettrackedquerytimeseries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/timeseries | Rank-tracking time series of a single tracked query |
| [**GetTrackingCoverage**](AnalyticsApi.md#gettrackingcoverage) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/coverage | Coverage and staleness of a project tracked queries |
| [**ListKeywordListings**](AnalyticsApi.md#listkeywordlistings) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/keyword-listings | List a project&#39;s keywords with their windowed metrics |

<a id="getavailablefilters"></a>
# **GetAvailableFilters**
> GetAvailableFilters200Response GetAvailableFilters (Guid organizationId, Guid projectId)

Filter values a project is configured for

Minimum role: viewer. Call this first: it is where every other analytics operation sends you for the valid engines, countries and keyword clusters of a project, and the values it returns are the exact strings the engines, countries and queryClusterIds parameters accept — anything else is rejected as a 400. Engines are engine codes, countries are ISO-3166 alpha-2 codes, and clusters are {id, name} objects whose id goes in queryClusterIds. Takes no date window: it describes how the project is configured right now, so a value is listed as soon as a tracked query uses it, even when no response has been captured for it yet. An empty list therefore means nothing is configured for it, not that no data was collected. Competitor ids are not part of this response.

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
    public class GetAvailableFiltersExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 

            try
            {
                // Filter values a project is configured for
                GetAvailableFilters200Response result = apiInstance.GetAvailableFilters(organizationId, projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetAvailableFilters: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetAvailableFiltersWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Filter values a project is configured for
    ApiResponse<GetAvailableFilters200Response> response = apiInstance.GetAvailableFiltersWithHttpInfo(organizationId, projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetAvailableFiltersWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getcitedsources"></a>
# **GetCitedSources**
> CitedSourcesResponse GetCitedSources (Guid organizationId, Guid projectId, DateOnly dateFrom, DateOnly dateTo, List<string>? engines = null, string? groupBy = null, int? limit = null, int? offset = null)

Domains and pages the AI answers cited

Minimum role: viewer. The sources the answer engines drew on across a project's AI answers over a date window, ranked by how often they were cited. Per source: citationCount, the total number of citations; distinctResponseCount and distinctQueryCount, how many captured answers and tracked queries it appeared in; avgPosition, its average 1-based rank inside the answers' citation lists, where LOWER is better. A null avgPosition means no citation in the window carried a position, not a rank of zero; a null domain or sampleTitle means the citation never carried one. `total` counts the distinct sources matching the window, before paging. The list is UNFILTERED by ownership: the brand's, competitors' and third-party sources sit in the same ranking. Only the AI answer engines (chatgpt, perplexity, google_ai_overview, google_ai_mode) produce citations, so filtering by google_serp or google_shopping is accepted and returns nothing. Citations still behind an answer engine's redirect (a google.com/goto link, whose URL names the engine rather than the source) are excluded, so a source cited only through such links is absent from this list rather than counted as zero.

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
    public class GetCitedSourcesExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d.
            var engines = new List<string>?(); // List<string>? | Repeatable, or comma-separated. Only the AI engines carry citations. (optional) 
            var groupBy = "domain";  // string? | Grain of the roll-up: \"domain\" by host, \"page\" by exact URL. (optional)  (default to domain)
            var limit = 20;  // int? | Page size. A larger value is rejected, never silently reduced. (optional)  (default to 20)
            var offset = 0;  // int? | Number of sources to skip. (optional)  (default to 0)

            try
            {
                // Domains and pages the AI answers cited
                CitedSourcesResponse result = apiInstance.GetCitedSources(organizationId, projectId, dateFrom, dateTo, engines, groupBy, limit, offset);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetCitedSources: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetCitedSourcesWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Domains and pages the AI answers cited
    ApiResponse<CitedSourcesResponse> response = apiInstance.GetCitedSourcesWithHttpInfo(organizationId, projectId, dateFrom, dateTo, engines, groupBy, limit, offset);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetCitedSourcesWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. Only the AI engines carry citations. | [optional]  |
| **groupBy** | **string?** | Grain of the roll-up: \&quot;domain\&quot; by host, \&quot;page\&quot; by exact URL. | [optional] [default to domain] |
| **limit** | **int?** | Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int?** | Number of sources to skip. | [optional] [default to 0] |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getclusterbreakdown"></a>
# **GetClusterBreakdown**
> ProjectRankTrackingClusterBreakdown GetClusterBreakdown (Guid organizationId, Guid projectId, DateOnly dateFrom, DateOnly dateTo, List<string>? engines = null, List<string>? countries = null, List<Guid>? queryClusterIds = null, bool? includeUngroupedQueries = null)

Rank-tracking metrics per keyword cluster

Minimum role: viewer. One row per keyword cluster over a date window, with its tracked query and keyword counts, average positions, rates, share of voice and sentiment split. A row whose clusterId is null is the ungrouped bucket: the tracked queries belonging to no cluster. Position metrics are 1-based and LOWER is better; rates, positivityIndex and shareOfVoice are 0-100 percentages where higher is better. A null metric means nothing was captured for that cluster in the window — it is not a zero, and averaging or charting it as one would misstate the period. dataDirtySince is non-null while a recalculation is pending, meaning the numbers predate the latest configuration change.

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
    public class GetClusterBreakdownExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d.
            var engines = new List<string>?(); // List<string>? | Repeatable, or comma-separated. (optional) 
            var countries = new List<string>?(); // List<string>? | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional) 
            var queryClusterIds = new List<Guid>?(); // List<Guid>? | Restrict to these clusters. Each must belong to the project. (optional) 
            var includeUngroupedQueries = false;  // bool? | Sent alone, returns only the ungrouped bucket rather than adding it to every cluster. (optional)  (default to false)

            try
            {
                // Rank-tracking metrics per keyword cluster
                ProjectRankTrackingClusterBreakdown result = apiInstance.GetClusterBreakdown(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetClusterBreakdown: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetClusterBreakdownWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Rank-tracking metrics per keyword cluster
    ApiResponse<ProjectRankTrackingClusterBreakdown> response = apiInstance.GetClusterBreakdownWithHttpInfo(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetClusterBreakdownWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. | [optional]  |
| **countries** | [**List&lt;string&gt;?**](string.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional]  |
| **queryClusterIds** | [**List&lt;Guid&gt;?**](Guid.md) | Restrict to these clusters. Each must belong to the project. | [optional]  |
| **includeUngroupedQueries** | **bool?** | Sent alone, returns only the ungrouped bucket rather than adding it to every cluster. | [optional] [default to false] |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getcompetitorcooccurrence"></a>
# **GetCompetitorCoOccurrence**
> CompetitorCoOccurrenceResponse GetCompetitorCoOccurrence (Guid organizationId, Guid projectId, DateOnly dateFrom, DateOnly dateTo, List<string>? engines = null, List<string>? countries = null, Guid? competitorId = null)

Head-to-head record of the brand against each tracked competitor

Minimum role: viewer. Restricted to the AI answers where the brand and a competitor are BOTH mentioned, one row per tracked competitor: sharedResponseCount is how many such answers there are, and brandWins / competitorWins / ties split them by who holds the better (lower) best mention position. winRate is the percentage 0-100 of those answers the brand wins; avgOwnPosition and avgCompetitorPosition are the average best mention position each side held, 1-based, so LOWER is better. exampleQueryText and exampleAiResponseId point at one representative shared answer. Every nullable field means \"not known yet\" rather than zero: a null winRate or average position is the absence of a shared answer in the window, not a record of losing. Tracked competitors only.

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
    public class GetCompetitorCoOccurrenceExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d.
            var engines = new List<string>?(); // List<string>? | Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence. (optional) 
            var countries = new List<string>?(); // List<string>? | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional) 
            var competitorId = "competitorId_example";  // Guid? | Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids. (optional) 

            try
            {
                // Head-to-head record of the brand against each tracked competitor
                CompetitorCoOccurrenceResponse result = apiInstance.GetCompetitorCoOccurrence(organizationId, projectId, dateFrom, dateTo, engines, countries, competitorId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetCompetitorCoOccurrence: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetCompetitorCoOccurrenceWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Head-to-head record of the brand against each tracked competitor
    ApiResponse<CompetitorCoOccurrenceResponse> response = apiInstance.GetCompetitorCoOccurrenceWithHttpInfo(organizationId, projectId, dateFrom, dateTo, engines, countries, competitorId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetCompetitorCoOccurrenceWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence. | [optional]  |
| **countries** | [**List&lt;string&gt;?**](string.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional]  |
| **competitorId** | **Guid?** | Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids. | [optional]  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getmentionmix"></a>
# **GetMentionMix**
> ProjectMentionMixResponse GetMentionMix (Guid organizationId, Guid projectId, DateOnly dateFrom, DateOnly dateTo, List<string>? engines = null, List<string>? countries = null)

Composition of a project brand mentions in AI answers

Minimum role: viewer. Counts of the project brand's own text mentions in AI answers over a date window, grouped three ways: byType (recommendation, comparison, listing, example, reference), byTone (positive, neutral, negative) and byQualifier (direct, conditional — a conditional mention is one the answer hedged with a condition). These are the inputs behind the Share of Voice weighted score. Every bucket is always present and is a plain count, never null: a zero means no mention of that kind was found in the window. The three groupings count the same mentions, so each one sums to the same total. Only the project brand is counted, never a competitor, and only mentions inside the answer text — a citation of the brand's URL is not a mention here. Only AI answer engines produce mentions, so restricting engines to google_serp or google_shopping alone returns all zeros. For the positive/neutral/negative split per engine and per competitor use the sentiment endpoint.

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
    public class GetMentionMixExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d.
            var engines = new List<string>?(); // List<string>? | Repeatable, or comma-separated. Non-AI engines contribute no mentions. (optional) 
            var countries = new List<string>?(); // List<string>? | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional) 

            try
            {
                // Composition of a project brand mentions in AI answers
                ProjectMentionMixResponse result = apiInstance.GetMentionMix(organizationId, projectId, dateFrom, dateTo, engines, countries);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetMentionMix: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetMentionMixWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Composition of a project brand mentions in AI answers
    ApiResponse<ProjectMentionMixResponse> response = apiInstance.GetMentionMixWithHttpInfo(organizationId, projectId, dateFrom, dateTo, engines, countries);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetMentionMixWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. Non-AI engines contribute no mentions. | [optional]  |
| **countries** | [**List&lt;string&gt;?**](string.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional]  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getmentionsamples"></a>
# **GetMentionSamples**
> ProjectMentionSamplesResponse GetMentionSamples (Guid organizationId, Guid projectId, DateOnly dateFrom, DateOnly dateTo, List<string>? engines = null, List<string>? countries = null, string? sentiment = null, string? mentionType = null, Guid? competitorId = null, string? sortBy = null, int? limit = null, int? offset = null)

Sample of the raw AI mention texts of a project

Minimum role: viewer. A paginated page of the individual mention texts behind the aggregate numbers, for qualitative review and for checking sentiment labels by eye. Each sample carries the mention text, the engine and country it was seen in, the tracked query that produced it, its sentiment and mention type, and mentionPosition — a 1-based rank inside the answer where LOWER is better, always present. `total` counts every mention matching the filters, not the size of the page returned. Only mentions inside the answer text are returned: a citation of the brand URL is not a mention here, and only AI answer engines produce mentions, so restricting engines to google_serp or google_shopping alone returns an empty page rather than an error. Two fields carry a \"not known\" rather than a zero: country is null and queryText is empty when the tracked query behind the mention has since been deleted, and competitorId is null when the mention row stores no competitor id — which is NOT an assertion that the mention is about your own brand, since an untracked competitor also stores none. Read mentionRelation instead: `own` and `tracked-competitor` are what the scraper resolved to a configured entity, `untracked-competitor` is a rival the project does not track, and null means the row predates the field. brandName carries the mentioned brand, and is the only way to name an untracked competitor, which has no competitor id to resolve one from. Omitting the competitorId filter returns exactly the rows with no competitor id stored — that is, own-brand AND untracked-competitor mentions together, not every competitor; pass a competitor UUID to restrict the page to that competitor, and use mentionRelation to separate the rest. For the aggregate positive/neutral/negative split use the sentiment endpoint, and for weighted mention-type counts the mention mix endpoint.

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
    public class GetMentionSamplesExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d.
            var engines = new List<string>?(); // List<string>? | Repeatable, or comma-separated. Non-AI engines contribute no mentions. (optional) 
            var countries = new List<string>?(); // List<string>? | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional) 
            var sentiment = "positive";  // string? | Restrict to one sentiment label. Omit for every sentiment. (optional) 
            var mentionType = "recommendation";  // string? | Restrict to one mention type. Omit for every type. (optional) 
            var competitorId = "competitorId_example";  // Guid? | UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart. (optional) 
            var sortBy = "recent";  // string? | recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default. (optional)  (default to recent)
            var limit = 20;  // int? | Page size. A larger value is rejected, never silently reduced. (optional)  (default to 20)
            var offset = 0;  // int? | Number of matching mentions to skip before the page starts. (optional)  (default to 0)

            try
            {
                // Sample of the raw AI mention texts of a project
                ProjectMentionSamplesResponse result = apiInstance.GetMentionSamples(organizationId, projectId, dateFrom, dateTo, engines, countries, sentiment, mentionType, competitorId, sortBy, limit, offset);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetMentionSamples: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetMentionSamplesWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Sample of the raw AI mention texts of a project
    ApiResponse<ProjectMentionSamplesResponse> response = apiInstance.GetMentionSamplesWithHttpInfo(organizationId, projectId, dateFrom, dateTo, engines, countries, sentiment, mentionType, competitorId, sortBy, limit, offset);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetMentionSamplesWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. Non-AI engines contribute no mentions. | [optional]  |
| **countries** | [**List&lt;string&gt;?**](string.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional]  |
| **sentiment** | **string?** | Restrict to one sentiment label. Omit for every sentiment. | [optional]  |
| **mentionType** | **string?** | Restrict to one mention type. Omit for every type. | [optional]  |
| **competitorId** | **Guid?** | UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart. | [optional]  |
| **sortBy** | **string?** | recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default. | [optional] [default to recent] |
| **limit** | **int?** | Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int?** | Number of matching mentions to skip before the page starts. | [optional] [default to 0] |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getmetricglossary"></a>
# **GetMetricGlossary**
> GetMetricGlossary200Response GetMetricGlossary ()

Map everyday wording to a metric and the operation that serves it

Static reference, no project data. Each entry gives a metric, the everyday words people use for it, its unit and range, whether higher or lower is better, the operation that returns it, and example questions. Useful when turning a vague or non-technical request into the right call.

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
    public class GetMetricGlossaryExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);

            try
            {
                // Map everyday wording to a metric and the operation that serves it
                GetMetricGlossary200Response result = apiInstance.GetMetricGlossary();
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetMetricGlossary: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetMetricGlossaryWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Map everyday wording to a metric and the operation that serves it
    ApiResponse<GetMetricGlossary200Response> response = apiInstance.GetMetricGlossaryWithHttpInfo();
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetMetricGlossaryWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getorganizationoverview"></a>
# **GetOrganizationOverview**
> GetOrganizationOverview200Response GetOrganizationOverview (Guid organizationId)

Snapshot rank-health board across an organization active projects

Minimum role: viewer. One row per active project — share of voice, mention rate, average mention position, positivity index and tracked-query count — ordered by share of voice, plus an organization-level aggregate of the same metrics. Archived projects are excluded. This is a current-state snapshot and takes no date window; for a date-ranged comparison call the per-project operations (getProjectMetrics, getProjectTimeSeries) for each projectId returned here. Every metric is nullable, and a null means the project has no rank data yet — not a score of zero. Higher is better for shareOfVoice, mentionRate and positivityIndex; avgMentionPosition is a 1-based rank, so LOWER is better.

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
    public class GetOrganizationOverviewExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 

            try
            {
                // Snapshot rank-health board across an organization active projects
                GetOrganizationOverview200Response result = apiInstance.GetOrganizationOverview(organizationId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetOrganizationOverview: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetOrganizationOverviewWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Snapshot rank-health board across an organization active projects
    ApiResponse<GetOrganizationOverview200Response> response = apiInstance.GetOrganizationOverviewWithHttpInfo(organizationId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetOrganizationOverviewWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getprojectmetrics"></a>
# **GetProjectMetrics**
> ProjectRankTrackingStats GetProjectMetrics (Guid organizationId, Guid projectId, DateOnly dateFrom, DateOnly dateTo, List<string>? engines = null, List<string>? countries = null, List<Guid>? queryClusterIds = null, bool? includeUngroupedQueries = null)

Headline visibility metrics of a project

Minimum role: viewer. The project overview over a date window: share of voice (own and per competitor), mention / SERP / shopping rates, average and best positions, position stability, the sentiment split and the position-distribution buckets. Positions are 1-based, so a LOWER number is better; rates, the positivity index and share of voice are percentages from 0 to 100, where HIGHER is better. Every `trend*` field is the signed change against the immediately preceding window of the same length: negative means an improved position, positive means an improved rate or score. A null metric means \"not known yet\", never zero: a scalar is null when the window holds no checks at all, and a `trend*` field is null when there is no earlier window to compare against. The counters (`mentionCount`, `*TrackedQueryCount`, `*QueriesWithResult`, `sentiment*` and `mentionTypeCounts`) are genuine zeros instead, so an empty window reads as zero counts with null rates. `dataDirtySince` is non-null while a recalculation is pending, meaning the figures may still move for dates from then on.

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
    public class GetProjectMetricsExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d.
            var engines = new List<string>?(); // List<string>? | Repeatable, or comma-separated. (optional) 
            var countries = new List<string>?(); // List<string>? | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional) 
            var queryClusterIds = new List<Guid>?(); // List<Guid>? | Restrict to these keyword clusters. Each must belong to this project. (optional) 
            var includeUngroupedQueries = false;  // bool? | Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster. (optional)  (default to false)

            try
            {
                // Headline visibility metrics of a project
                ProjectRankTrackingStats result = apiInstance.GetProjectMetrics(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetProjectMetrics: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetProjectMetricsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Headline visibility metrics of a project
    ApiResponse<ProjectRankTrackingStats> response = apiInstance.GetProjectMetricsWithHttpInfo(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetProjectMetricsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. | [optional]  |
| **countries** | [**List&lt;string&gt;?**](string.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional]  |
| **queryClusterIds** | [**List&lt;Guid&gt;?**](Guid.md) | Restrict to these keyword clusters. Each must belong to this project. | [optional]  |
| **includeUngroupedQueries** | **bool?** | Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster. | [optional] [default to false] |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getprojectsentiment"></a>
# **GetProjectSentiment**
> ProjectSentimentBreakdown GetProjectSentiment (Guid organizationId, Guid projectId, DateOnly dateFrom, DateOnly dateTo, List<string>? engines = null, List<string>? countries = null, List<Guid>? queryClusterIds = null, bool? includeUngroupedQueries = null)

Sentiment breakdown of a project brand mentions

Minimum role: viewer. Positive, neutral and negative split of the brand mentions in AI answers over a date window, per engine and per competitor. A null positivityIndex means no mentions were found in the window, which is not the same as a score of zero.

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
    public class GetProjectSentimentExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d.
            var engines = new List<string>?(); // List<string>? | Repeatable, or comma-separated. (optional) 
            var countries = new List<string>?(); // List<string>? | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional) 
            var queryClusterIds = new List<Guid>?(); // List<Guid>? |  (optional) 
            var includeUngroupedQueries = false;  // bool? |  (optional)  (default to false)

            try
            {
                // Sentiment breakdown of a project brand mentions
                ProjectSentimentBreakdown result = apiInstance.GetProjectSentiment(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetProjectSentiment: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetProjectSentimentWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Sentiment breakdown of a project brand mentions
    ApiResponse<ProjectSentimentBreakdown> response = apiInstance.GetProjectSentimentWithHttpInfo(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetProjectSentimentWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. | [optional]  |
| **countries** | [**List&lt;string&gt;?**](string.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional]  |
| **queryClusterIds** | [**List&lt;Guid&gt;?**](Guid.md) |  | [optional]  |
| **includeUngroupedQueries** | **bool?** |  | [optional] [default to false] |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getprojecttimeseries"></a>
# **GetProjectTimeSeries**
> ProjectRankTrackingTimeSeries GetProjectTimeSeries (Guid organizationId, Guid projectId, DateOnly dateFrom, DateOnly dateTo, string? granularity = null, List<string>? engines = null, List<string>? countries = null, List<Guid>? queryClusterIds = null, bool? includeUngroupedQueries = null, List<Guid>? competitorIds = null)

Rank-tracking metrics of a project over time

Minimum role: viewer. One point per bucket over the date window, each carrying the brand metrics and one same-shaped entry per requested competitor. Rank metrics (serp, shopping, mention, link) are 1-based averages where LOWER is better; positivity (0-100), shareOfVoice (0-100), mentionRate (0-100) and serpRate (0-100) are scores where higher is better. Every metric is nullable, and a null means no data was collected for that bucket, which is not the same as a value of zero. A project with no tracked queries returns an empty points list. Prefer weekly or monthly granularity over a long window to keep the response compact.

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
    public class GetProjectTimeSeriesExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d.
            var granularity = "daily";  // string? | Bucket size of each point. (optional)  (default to daily)
            var engines = new List<string>?(); // List<string>? | Repeatable, or comma-separated. (optional) 
            var countries = new List<string>?(); // List<string>? | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional) 
            var queryClusterIds = new List<Guid>?(); // List<Guid>? |  (optional) 
            var includeUngroupedQueries = false;  // bool? | On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them. (optional)  (default to false)
            var competitorIds = new List<Guid>?(); // List<Guid>? | Repeatable, or comma-separated. Each id adds one series under the competitors map of every point. (optional) 

            try
            {
                // Rank-tracking metrics of a project over time
                ProjectRankTrackingTimeSeries result = apiInstance.GetProjectTimeSeries(organizationId, projectId, dateFrom, dateTo, granularity, engines, countries, queryClusterIds, includeUngroupedQueries, competitorIds);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetProjectTimeSeries: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetProjectTimeSeriesWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Rank-tracking metrics of a project over time
    ApiResponse<ProjectRankTrackingTimeSeries> response = apiInstance.GetProjectTimeSeriesWithHttpInfo(organizationId, projectId, dateFrom, dateTo, granularity, engines, countries, queryClusterIds, includeUngroupedQueries, competitorIds);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetProjectTimeSeriesWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. |  |
| **granularity** | **string?** | Bucket size of each point. | [optional] [default to daily] |
| **engines** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. | [optional]  |
| **countries** | [**List&lt;string&gt;?**](string.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional]  |
| **queryClusterIds** | [**List&lt;Guid&gt;?**](Guid.md) |  | [optional]  |
| **includeUngroupedQueries** | **bool?** | On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them. | [optional] [default to false] |
| **competitorIds** | [**List&lt;Guid&gt;?**](Guid.md) | Repeatable, or comma-separated. Each id adds one series under the competitors map of every point. | [optional]  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getquerymovers"></a>
# **GetQueryMovers**
> TrackedQueryMoversResponse GetQueryMovers (Guid organizationId, Guid projectId, DateOnly dateFrom, DateOnly dateTo, List<string>? engines = null, List<string>? countries = null, string? sortBy = null, string? sortOrder = null, int? limit = null, int? offset = null)

Tracked queries ranked by how much a metric moved

Minimum role: viewer. One row per tracked query — a single engine plus country — carrying its current metric envelope and the signed change against the immediately preceding window of equal length: a 7-day window is compared with the 7 days before it. Every trend delta is signed so that POSITIVE means improved, including the position trends, where the underlying avgSerpPosition / avgShoppingPosition / avgMentionPosition / avgLinkPosition are 1-based ranks and therefore LOWER is better. shareOfVoice and positivityIndex are percentages from 0 to 100, where HIGHER is better. Sorting applies to the trend keys only: sortOrder=desc gives the top gainers, asc the top losers. Every nullable field means \"not known yet\" rather than zero — a null position or shareOfVoice is a query with no data in the window, and a null positivityIndex or trend is a period with no mentions to score, neither of which is a record of losing ground. total counts the tracked queries the filters match, not the rows on this page. dataDirtySince is a date from which the rank data is being recomputed, or null when nothing is pending; while it is non-null the deltas may still move.

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
    public class GetQueryMoversExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d.
            var engines = new List<string>?(); // List<string>? | Repeatable, or comma-separated. (optional) 
            var countries = new List<string>?(); // List<string>? | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional) 
            var sortBy = "trend_serp";  // string? | Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default. (optional)  (default to trend_share_of_voice)
            var sortOrder = "asc";  // string? | desc for the top gainers, asc for the top losers. (optional)  (default to desc)
            var limit = 20;  // int? | Page size. A value above the maximum is rejected, never clamped. (optional)  (default to 20)
            var offset = 0;  // int? |  (optional)  (default to 0)

            try
            {
                // Tracked queries ranked by how much a metric moved
                TrackedQueryMoversResponse result = apiInstance.GetQueryMovers(organizationId, projectId, dateFrom, dateTo, engines, countries, sortBy, sortOrder, limit, offset);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetQueryMovers: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetQueryMoversWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Tracked queries ranked by how much a metric moved
    ApiResponse<TrackedQueryMoversResponse> response = apiInstance.GetQueryMoversWithHttpInfo(organizationId, projectId, dateFrom, dateTo, engines, countries, sortBy, sortOrder, limit, offset);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetQueryMoversWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. | [optional]  |
| **countries** | [**List&lt;string&gt;?**](string.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional]  |
| **sortBy** | **string?** | Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default. | [optional] [default to trend_share_of_voice] |
| **sortOrder** | **string?** | desc for the top gainers, asc for the top losers. | [optional] [default to desc] |
| **limit** | **int?** | Page size. A value above the maximum is rejected, never clamped. | [optional] [default to 20] |
| **offset** | **int?** |  | [optional] [default to 0] |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getshareofvoiceformula"></a>
# **GetShareOfVoiceFormula**
> GetShareOfVoiceFormula200Response GetShareOfVoiceFormula (Guid organizationId, Guid projectId)

The constants behind the Share of Voice score

Minimum role: viewer. Static reference data, the same for every project: the weights and multipliers that turn individual brand mentions into a Share of Voice score. Each mention is worth `mentionTypeWeights[type] * sentimentMultipliers[tone] * (conditional ? conditionalMultiplier : directMultiplier)`, and a competitor's Share of Voice is its share of the summed weights of every brand in the window, as a percentage. mentionTypeWeights is keyed by mention type (recommendation, comparison, listing, example, reference) and sentimentMultipliers by tone (positive, neutral, negative); a negative mention is discounted, not discarded, because it still evidences presence. A conditional mention is one the answer hedged with a condition (\"if you need X\"). Use this to explain a score, not to recompute one: the counts it applies to come from the mention mix endpoint. Every value is always present and is never null.

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
    public class GetShareOfVoiceFormulaExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 

            try
            {
                // The constants behind the Share of Voice score
                GetShareOfVoiceFormula200Response result = apiInstance.GetShareOfVoiceFormula(organizationId, projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetShareOfVoiceFormula: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetShareOfVoiceFormulaWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // The constants behind the Share of Voice score
    ApiResponse<GetShareOfVoiceFormula200Response> response = apiInstance.GetShareOfVoiceFormulaWithHttpInfo(organizationId, projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetShareOfVoiceFormulaWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="gettrackedquerytimeseries"></a>
# **GetTrackedQueryTimeSeries**
> TrackedQueryRankTrackingTimeSeries GetTrackedQueryTimeSeries (Guid organizationId, Guid projectId, Guid trackedQueryId, DateOnly dateFrom, DateOnly dateTo, string? granularity = null, List<Guid>? competitorIds = null)

Rank-tracking time series of a single tracked query

Minimum role: viewer. One point per bucket over the date window, each carrying the brand metrics and one same-shaped entry per requested competitor. Positions (serp, shopping, mention, link) are 1-based, so a LOWER number is better; positivity, shareOfVoice, mentionRate and serpRate are percentages from 0 to 100, where higher is better. Every metric is nullable, and a null means nothing was captured for that entity in that bucket — it is not a zero: a null shareOfVoice means no measurement, a shareOfVoice of 0 means measured and never mentioned. The tracked query fixes its own engine and country, so no engine or country filter is accepted. A non-null dataDirtySince is a timestamp warning that tracked queries were deleted from the project and historical buckets may still include their contributions until the nightly refresh rebuilds them.

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
    public class GetTrackedQueryTimeSeriesExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var trackedQueryId = "trackedQueryId_example";  // Guid | Must belong to the project in the path.
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d.
            var granularity = "daily";  // string? | Bucket size. Prefer weekly or monthly for long windows. (optional)  (default to daily)
            var competitorIds = new List<Guid>?(); // List<Guid>? | Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint. (optional) 

            try
            {
                // Rank-tracking time series of a single tracked query
                TrackedQueryRankTrackingTimeSeries result = apiInstance.GetTrackedQueryTimeSeries(organizationId, projectId, trackedQueryId, dateFrom, dateTo, granularity, competitorIds);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetTrackedQueryTimeSeries: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetTrackedQueryTimeSeriesWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Rank-tracking time series of a single tracked query
    ApiResponse<TrackedQueryRankTrackingTimeSeries> response = apiInstance.GetTrackedQueryTimeSeriesWithHttpInfo(organizationId, projectId, trackedQueryId, dateFrom, dateTo, granularity, competitorIds);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetTrackedQueryTimeSeriesWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **trackedQueryId** | **Guid** | Must belong to the project in the path. |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. |  |
| **granularity** | **string?** | Bucket size. Prefer weekly or monthly for long windows. | [optional] [default to daily] |
| **competitorIds** | [**List&lt;Guid&gt;?**](Guid.md) | Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint. | [optional]  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="gettrackingcoverage"></a>
# **GetTrackingCoverage**
> GetTrackingCoverage200Response GetTrackingCoverage (Guid organizationId, Guid projectId)

Coverage and staleness of a project tracked queries

Minimum role: viewer. A current-state snapshot answering \"what is stale or not being tracked\": total is every tracked query on the project, active and paused split it by status, neverChecked counts the active queries that have never run, and overdue counts the active queries whose last check is older than their own check-frequency interval (daily, weekly or monthly). neverChecked and overdue are disjoint — a query that has never run is never also counted as overdue — and both ignore paused queries, which are not expected to be checked at all. sample lists up to 20 of the overdue queries, most stale first; it is a sample of overdue only, so it never contains a never-checked query and is empty when overdue is 0. Takes no date window: every count describes the project as it stands right now.

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
    public class GetTrackingCoverageExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 

            try
            {
                // Coverage and staleness of a project tracked queries
                GetTrackingCoverage200Response result = apiInstance.GetTrackingCoverage(organizationId, projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.GetTrackingCoverage: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetTrackingCoverageWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Coverage and staleness of a project tracked queries
    ApiResponse<GetTrackingCoverage200Response> response = apiInstance.GetTrackingCoverageWithHttpInfo(organizationId, projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.GetTrackingCoverageWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listkeywordlistings"></a>
# **ListKeywordListings**
> ListKeywordListings200Response ListKeywordListings (Guid organizationId, Guid projectId, DateOnly dateFrom, DateOnly dateTo, List<string>? engines = null, List<string>? countries = null, List<Guid>? queryClusterIds = null, bool? includeUngroupedQueries = null, string? status = null, List<string>? checkFrequencies = null, List<int>? nPasses = null, string? search = null, string? sortBy = null, string? sortOrder = null, int? limit = null, int? offset = null)

List a project's keywords with their windowed metrics

Minimum role: viewer. One row per distinct keyword text of the project — every tracked query asking that text, on any engine in any country, collapsed into a single row whose variantIds name the tracked queries behind it. Each row carries the metrics of the requested window and a signed trend against the window of equal length immediately before it, where POSITIVE ALWAYS MEANS BETTER whichever direction the metric itself runs. Positions are 1-based and lower is better; rates, positivityIndex and shareOfVoice are 0-100 and higher is better; mentionPositionStability is a day-to-day spread, so lower is steadier. A null metric means nothing was captured for that keyword in the window — it is not a zero. `total` counts the KEYWORDS matching the filters, not the rows on this page and not tracked queries; `totalVariantCount` counts the tracked queries behind the keywords matching every filter EXCEPT `search` — with a text search applied it still counts the project's variants, so do not size a force-check budget from it on a searched page. NEITHER IS THE PROJECT'S TRACKED-QUERY COUNT: the count operation reads the write model, while this listing reads projections refreshed in the background from it, so the numbers legitimately differ while those projections catch up. A project whose cached tracked-query count has not been refreshed yet answers an empty page with total 0 — the same answer as a project with no tracked queries at all — so treat an unexpected empty page right after creating queries as \"not projected yet\", not as \"no data\". dataDirtySince is non-null while a recalculation is pending, meaning the metrics predate the latest configuration change. Filters narrow which VARIANTS count towards a row, so engines, countries, statuses, checkFrequencies and nPassesValues each report what the filters selected rather than everything the keyword has. A filter or sort key this endpoint cannot honour is rejected by name, never ignored, and a limit above the maximum is rejected rather than quietly reduced. This operation answers JSON only: a keyword row carries a nested mentionTypeCounts object, so it is not part of the CSV family.

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
    public class ListKeywordListingsExample
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
            var apiInstance = new AnalyticsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var dateFrom = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
            var dateTo = DateOnly.Parse("2013-10-20");  // DateOnly | Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom.
            var engines = new List<string>?(); // List<string>? | Repeatable, or comma-separated. Narrows which variants count towards each row. (optional) 
            var countries = new List<string>?(); // List<string>? | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional) 
            var queryClusterIds = new List<Guid>?(); // List<Guid>? | Restrict to keywords with a variant in these clusters. Each must belong to the project. (optional) 
            var includeUngroupedQueries = false;  // bool? | Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection. (optional)  (default to false)
            var status = "active";  // string? | Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \"mixed\". (optional) 
            var checkFrequencies = new List<string>?(); // List<string>? | Repeatable, or comma-separated. (optional) 
            var nPasses = new List<int>?(); // List<int>? | Repeatable, or comma-separated. Restrict to variants configured with these pass counts. (optional) 
            var search = "search_example";  // string? | Case-insensitive substring match on the keyword text. (optional) 
            var sortBy = "keyword";  // string? | Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default. (optional)  (default to keyword)
            var sortOrder = "asc";  // string? |  (optional)  (default to asc)
            var limit = 20;  // int? | Page size. A larger value is rejected, never silently reduced. (optional)  (default to 20)
            var offset = 0;  // int? | Number of matching keywords to skip before the page starts. (optional)  (default to 0)

            try
            {
                // List a project's keywords with their windowed metrics
                ListKeywordListings200Response result = apiInstance.ListKeywordListings(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries, status, checkFrequencies, nPasses, search, sortBy, sortOrder, limit, offset);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AnalyticsApi.ListKeywordListings: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListKeywordListingsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List a project's keywords with their windowed metrics
    ApiResponse<ListKeywordListings200Response> response = apiInstance.ListKeywordListingsWithHttpInfo(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries, status, checkFrequencies, nPasses, search, sortBy, sortOrder, limit, offset);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AnalyticsApi.ListKeywordListingsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **dateFrom** | **DateOnly** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **dateTo** | **DateOnly** | Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom. |  |
| **engines** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. Narrows which variants count towards each row. | [optional]  |
| **countries** | [**List&lt;string&gt;?**](string.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional]  |
| **queryClusterIds** | [**List&lt;Guid&gt;?**](Guid.md) | Restrict to keywords with a variant in these clusters. Each must belong to the project. | [optional]  |
| **includeUngroupedQueries** | **bool?** | Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection. | [optional] [default to false] |
| **status** | **string?** | Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \&quot;mixed\&quot;. | [optional]  |
| **checkFrequencies** | [**List&lt;string&gt;?**](string.md) | Repeatable, or comma-separated. | [optional]  |
| **nPasses** | [**List&lt;int&gt;?**](int.md) | Repeatable, or comma-separated. Restrict to variants configured with these pass counts. | [optional]  |
| **search** | **string?** | Case-insensitive substring match on the keyword text. | [optional]  |
| **sortBy** | **string?** | Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default. | [optional] [default to keyword] |
| **sortOrder** | **string?** |  | [optional] [default to asc] |
| **limit** | **int?** | Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int?** | Number of matching keywords to skip before the page starts. | [optional] [default to 0] |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

