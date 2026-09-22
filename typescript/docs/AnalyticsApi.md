# AnalyticsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAvailableFilters**](AnalyticsApi.md#getavailablefilters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/available-filters | Filter values a project is configured for |
| [**getCitedSources**](AnalyticsApi.md#getcitedsources) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/cited-sources | Domains and pages the AI answers cited |
| [**getClusterBreakdown**](AnalyticsApi.md#getclusterbreakdown) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/clusters | Rank-tracking metrics per keyword cluster |
| [**getCompetitorCoOccurrence**](AnalyticsApi.md#getcompetitorcooccurrence) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/co-occurrence | Head-to-head record of the brand against each tracked competitor |
| [**getMentionMix**](AnalyticsApi.md#getmentionmix) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions/mix | Composition of a project brand mentions in AI answers |
| [**getMentionSamples**](AnalyticsApi.md#getmentionsamples) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions | Sample of the raw AI mention texts of a project |
| [**getMetricGlossary**](AnalyticsApi.md#getmetricglossary) | **GET** /api/v1/metric-glossary | Map everyday wording to a metric and the operation that serves it |
| [**getOrganizationOverview**](AnalyticsApi.md#getorganizationoverview) | **GET** /api/v1/organizations/{organizationId}/overview | Snapshot rank-health board across an organization active projects |
| [**getProjectMetrics**](AnalyticsApi.md#getprojectmetrics) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics | Headline visibility metrics of a project |
| [**getProjectSentiment**](AnalyticsApi.md#getprojectsentiment) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/sentiment | Sentiment breakdown of a project brand mentions |
| [**getProjectTimeSeries**](AnalyticsApi.md#getprojecttimeseries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/timeseries | Rank-tracking metrics of a project over time |
| [**getQueryMovers**](AnalyticsApi.md#getquerymovers) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/movers | Tracked queries ranked by how much a metric moved |
| [**getShareOfVoiceFormula**](AnalyticsApi.md#getshareofvoiceformula) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/share-of-voice-formula | The constants behind the Share of Voice score |
| [**getTrackedQueryTimeSeries**](AnalyticsApi.md#gettrackedquerytimeseries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/timeseries | Rank-tracking time series of a single tracked query |
| [**getTrackingCoverage**](AnalyticsApi.md#gettrackingcoverage) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/coverage | Coverage and staleness of a project tracked queries |
| [**listKeywordListings**](AnalyticsApi.md#listkeywordlistings) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/keyword-listings | List a project\&#39;s keywords with their windowed metrics |



## getAvailableFilters

> GetAvailableFilters200Response getAvailableFilters(organizationId, projectId)

Filter values a project is configured for

Minimum role: viewer. Call this first: it is where every other analytics operation sends you for the valid engines, countries and keyword clusters of a project, and the values it returns are the exact strings the engines, countries and queryClusterIds parameters accept — anything else is rejected as a 400. Engines are engine codes, countries are ISO-3166 alpha-2 codes, and clusters are {id, name} objects whose id goes in queryClusterIds. Takes no date window: it describes how the project is configured right now, so a value is listed as soon as a tracked query uses it, even when no response has been captured for it yet. An empty list therefore means nothing is configured for it, not that no data was collected. Competitor ids are not part of this response.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetAvailableFiltersRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetAvailableFiltersRequest;

  try {
    const data = await api.getAvailableFilters(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**GetAvailableFilters200Response**](GetAvailableFilters200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The engines, countries and clusters configured on the project |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getCitedSources

> getCitedSources(organizationId, projectId, dateFrom, dateTo, engines, groupBy, limit, offset)

Domains and pages the AI answers cited

Minimum role: viewer. The sources the answer engines drew on across a project\&#39;s AI answers over a date window, ranked by how often they were cited. Per source: citationCount, the total number of citations; distinctResponseCount and distinctQueryCount, how many captured answers and tracked queries it appeared in; avgPosition, its average 1-based rank inside the answers\&#39; citation lists, where LOWER is better. A null avgPosition means no citation in the window carried a position, not a rank of zero; a null domain or sampleTitle means the citation never carried one. &#x60;total&#x60; counts the distinct sources matching the window, before paging. The list is UNFILTERED by ownership: the brand\&#39;s, competitors\&#39; and third-party sources sit in the same ranking. Only the AI answer engines (chatgpt, perplexity, google_ai_overview, google_ai_mode) produce citations, so filtering by google_serp or google_shopping is accepted and returns nothing. Citations still behind an answer engine\&#39;s redirect (a google.com/goto link, whose URL names the engine rather than the source) are excluded, so a source cited only through such links is absent from this list rather than counted as zero.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetCitedSourcesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d.
    dateTo: 2013-10-20,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. Only the AI engines carry citations. (optional)
    engines: ...,
    // 'domain' | 'page' | Grain of the roll-up: \"domain\" by host, \"page\" by exact URL. (optional)
    groupBy: groupBy_example,
    // number | Page size. A larger value is rejected, never silently reduced. (optional)
    limit: 56,
    // number | Number of sources to skip. (optional)
    offset: 56,
  } satisfies GetCitedSourcesRequest;

  try {
    const data = await api.getCitedSources(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. | [Defaults to `undefined`] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. Only the AI engines carry citations. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **groupBy** | `domain`, `page` | Grain of the roll-up: \&quot;domain\&quot; by host, \&quot;page\&quot; by exact URL. | [Optional] [Defaults to `&#39;domain&#39;`] [Enum: domain, page] |
| **limit** | `number` | Page size. A larger value is rejected, never silently reduced. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Number of sources to skip. | [Optional] [Defaults to `0`] |

### Return type

`void` (Empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cited sources for this page, plus the total number of distinct sources in the window |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter or page bound was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getClusterBreakdown

> getClusterBreakdown(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries)

Rank-tracking metrics per keyword cluster

Minimum role: viewer. One row per keyword cluster over a date window, with its tracked query and keyword counts, average positions, rates, share of voice and sentiment split. A row whose clusterId is null is the ungrouped bucket: the tracked queries belonging to no cluster. Position metrics are 1-based and LOWER is better; rates, positivityIndex and shareOfVoice are 0-100 percentages where higher is better. A null metric means nothing was captured for that cluster in the window — it is not a zero, and averaging or charting it as one would misstate the period. dataDirtySince is non-null while a recalculation is pending, meaning the numbers predate the latest configuration change.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetClusterBreakdownRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d.
    dateTo: 2013-10-20,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. (optional)
    engines: ...,
    // Array<string> | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    countries: ...,
    // Array<string> | Restrict to these clusters. Each must belong to the project. (optional)
    queryClusterIds: ...,
    // boolean | Sent alone, returns only the ungrouped bucket rather than adding it to every cluster. (optional)
    includeUngroupedQueries: true,
  } satisfies GetClusterBreakdownRequest;

  try {
    const data = await api.getClusterBreakdown(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. | [Defaults to `undefined`] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | `Array<string>` | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [Optional] |
| **queryClusterIds** | `Array<string>` | Restrict to these clusters. Each must belong to the project. | [Optional] |
| **includeUngroupedQueries** | `boolean` | Sent alone, returns only the ungrouped bucket rather than adding it to every cluster. | [Optional] [Defaults to `false`] |

### Return type

`void` (Empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per keyword cluster, plus the ungrouped bucket where it applies |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getCompetitorCoOccurrence

> getCompetitorCoOccurrence(organizationId, projectId, dateFrom, dateTo, engines, countries, competitorId)

Head-to-head record of the brand against each tracked competitor

Minimum role: viewer. Restricted to the AI answers where the brand and a competitor are BOTH mentioned, one row per tracked competitor: sharedResponseCount is how many such answers there are, and brandWins / competitorWins / ties split them by who holds the better (lower) best mention position. winRate is the percentage 0-100 of those answers the brand wins; avgOwnPosition and avgCompetitorPosition are the average best mention position each side held, 1-based, so LOWER is better. exampleQueryText and exampleAiResponseId point at one representative shared answer. Every nullable field means \&quot;not known yet\&quot; rather than zero: a null winRate or average position is the absence of a shared answer in the window, not a record of losing. Tracked competitors only.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetCompetitorCoOccurrenceRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d.
    dateTo: 2013-10-20,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence. (optional)
    engines: ...,
    // Array<string> | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    countries: ...,
    // string | Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids. (optional)
    competitorId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetCompetitorCoOccurrenceRequest;

  try {
    const data = await api.getCompetitorCoOccurrence(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. | [Defaults to `undefined`] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | `Array<string>` | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [Optional] |
| **competitorId** | `string` | Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids. | [Optional] [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One head-to-head row per tracked competitor, under \&quot;competitors\&quot; |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getMentionMix

> getMentionMix(organizationId, projectId, dateFrom, dateTo, engines, countries)

Composition of a project brand mentions in AI answers

Minimum role: viewer. Counts of the project brand\&#39;s own text mentions in AI answers over a date window, grouped three ways: byType (recommendation, comparison, listing, example, reference), byTone (positive, neutral, negative) and byQualifier (direct, conditional — a conditional mention is one the answer hedged with a condition). These are the inputs behind the Share of Voice weighted score. Every bucket is always present and is a plain count, never null: a zero means no mention of that kind was found in the window. The three groupings count the same mentions, so each one sums to the same total. Only the project brand is counted, never a competitor, and only mentions inside the answer text — a citation of the brand\&#39;s URL is not a mention here. Only AI answer engines produce mentions, so restricting engines to google_serp or google_shopping alone returns all zeros. For the positive/neutral/negative split per engine and per competitor use the sentiment endpoint.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetMentionMixRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d.
    dateTo: 2013-10-20,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. Non-AI engines contribute no mentions. (optional)
    engines: ...,
    // Array<string> | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    countries: ...,
  } satisfies GetMentionMixRequest;

  try {
    const data = await api.getMentionMix(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. | [Defaults to `undefined`] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. Non-AI engines contribute no mentions. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | `Array<string>` | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [Optional] |

### Return type

`void` (Empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Mention counts by type, by tone and by qualifier |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getMentionSamples

> getMentionSamples(organizationId, projectId, dateFrom, dateTo, engines, countries, sentiment, mentionType, competitorId, sortBy, limit, offset)

Sample of the raw AI mention texts of a project

Minimum role: viewer. A paginated page of the individual mention texts behind the aggregate numbers, for qualitative review and for checking sentiment labels by eye. Each sample carries the mention text, the engine and country it was seen in, the tracked query that produced it, its sentiment and mention type, and mentionPosition — a 1-based rank inside the answer where LOWER is better, always present. &#x60;total&#x60; counts every mention matching the filters, not the size of the page returned. Only mentions inside the answer text are returned: a citation of the brand URL is not a mention here, and only AI answer engines produce mentions, so restricting engines to google_serp or google_shopping alone returns an empty page rather than an error. Two fields carry a \&quot;not known\&quot; rather than a zero: country is null and queryText is empty when the tracked query behind the mention has since been deleted, and competitorId is null when the mention row stores no competitor id — which is NOT an assertion that the mention is about your own brand, since an untracked competitor also stores none. Read mentionRelation instead: &#x60;own&#x60; and &#x60;tracked-competitor&#x60; are what the scraper resolved to a configured entity, &#x60;untracked-competitor&#x60; is a rival the project does not track, and null means the row predates the field. brandName carries the mentioned brand, and is the only way to name an untracked competitor, which has no competitor id to resolve one from. Omitting the competitorId filter returns exactly the rows with no competitor id stored — that is, own-brand AND untracked-competitor mentions together, not every competitor; pass a competitor UUID to restrict the page to that competitor, and use mentionRelation to separate the rest. For the aggregate positive/neutral/negative split use the sentiment endpoint, and for weighted mention-type counts the mention mix endpoint.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetMentionSamplesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d.
    dateTo: 2013-10-20,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. Non-AI engines contribute no mentions. (optional)
    engines: ...,
    // Array<string> | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    countries: ...,
    // 'positive' | 'neutral' | 'negative' | Restrict to one sentiment label. Omit for every sentiment. (optional)
    sentiment: sentiment_example,
    // 'recommendation' | 'comparison' | 'listing' | 'example' | 'reference' | Restrict to one mention type. Omit for every type. (optional)
    mentionType: mentionType_example,
    // string | UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart. (optional)
    competitorId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // 'recent' | 'negative' | 'engine' | 'country' | recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default. (optional)
    sortBy: sortBy_example,
    // number | Page size. A larger value is rejected, never silently reduced. (optional)
    limit: 56,
    // number | Number of matching mentions to skip before the page starts. (optional)
    offset: 56,
  } satisfies GetMentionSamplesRequest;

  try {
    const data = await api.getMentionSamples(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. | [Defaults to `undefined`] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. Non-AI engines contribute no mentions. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | `Array<string>` | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [Optional] |
| **sentiment** | `positive`, `neutral`, `negative` | Restrict to one sentiment label. Omit for every sentiment. | [Optional] [Defaults to `undefined`] [Enum: positive, neutral, negative] |
| **mentionType** | `recommendation`, `comparison`, `listing`, `example`, `reference` | Restrict to one mention type. Omit for every type. | [Optional] [Defaults to `undefined`] [Enum: recommendation, comparison, listing, example, reference] |
| **competitorId** | `string` | UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart. | [Optional] [Defaults to `undefined`] |
| **sortBy** | `recent`, `negative`, `engine`, `country` | recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default. | [Optional] [Defaults to `&#39;recent&#39;`] [Enum: recent, negative, engine, country] |
| **limit** | `number` | Page size. A larger value is rejected, never silently reduced. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Number of matching mentions to skip before the page starts. | [Optional] [Defaults to `0`] |

### Return type

`void` (Empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of mention samples and the total matching the filters |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getMetricGlossary

> GetMetricGlossary200Response getMetricGlossary()

Map everyday wording to a metric and the operation that serves it

Static reference, no project data. Each entry gives a metric, the everyday words people use for it, its unit and range, whether higher or lower is better, the operation that returns it, and example questions. Useful when turning a vague or non-technical request into the right call.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetMetricGlossaryRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  try {
    const data = await api.getMetricGlossary();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMetricGlossary200Response**](GetMetricGlossary200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric catalogue |  -  |
| **403** | The key lacks the read capability |  -  |
| **401** | Missing or invalid API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getOrganizationOverview

> GetOrganizationOverview200Response getOrganizationOverview(organizationId)

Snapshot rank-health board across an organization active projects

Minimum role: viewer. One row per active project — share of voice, mention rate, average mention position, positivity index and tracked-query count — ordered by share of voice, plus an organization-level aggregate of the same metrics. Archived projects are excluded. This is a current-state snapshot and takes no date window; for a date-ranged comparison call the per-project operations (getProjectMetrics, getProjectTimeSeries) for each projectId returned here. Every metric is nullable, and a null means the project has no rank data yet — not a score of zero. Higher is better for shareOfVoice, mentionRate and positivityIndex; avgMentionPosition is a 1-based rank, so LOWER is better.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetOrganizationOverviewRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetOrganizationOverviewRequest;

  try {
    const data = await api.getOrganizationOverview(body);
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

### Return type

[**GetOrganizationOverview200Response**](GetOrganizationOverview200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-project snapshot rows and the organization aggregate |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getProjectMetrics

> getProjectMetrics(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries)

Headline visibility metrics of a project

Minimum role: viewer. The project overview over a date window: share of voice (own and per competitor), mention / SERP / shopping rates, average and best positions, position stability, the sentiment split and the position-distribution buckets. Positions are 1-based, so a LOWER number is better; rates, the positivity index and share of voice are percentages from 0 to 100, where HIGHER is better. Every &#x60;trend*&#x60; field is the signed change against the immediately preceding window of the same length: negative means an improved position, positive means an improved rate or score. A null metric means \&quot;not known yet\&quot;, never zero: a scalar is null when the window holds no checks at all, and a &#x60;trend*&#x60; field is null when there is no earlier window to compare against. The counters (&#x60;mentionCount&#x60;, &#x60;*TrackedQueryCount&#x60;, &#x60;*QueriesWithResult&#x60;, &#x60;sentiment*&#x60; and &#x60;mentionTypeCounts&#x60;) are genuine zeros instead, so an empty window reads as zero counts with null rates. &#x60;dataDirtySince&#x60; is non-null while a recalculation is pending, meaning the figures may still move for dates from then on.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetProjectMetricsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d.
    dateTo: 2013-10-20,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. (optional)
    engines: ...,
    // Array<string> | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    countries: ...,
    // Array<string> | Restrict to these keyword clusters. Each must belong to this project. (optional)
    queryClusterIds: ...,
    // boolean | Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster. (optional)
    includeUngroupedQueries: true,
  } satisfies GetProjectMetricsRequest;

  try {
    const data = await api.getProjectMetrics(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. | [Defaults to `undefined`] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | `Array<string>` | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [Optional] |
| **queryClusterIds** | `Array<string>` | Restrict to these keyword clusters. Each must belong to this project. | [Optional] |
| **includeUngroupedQueries** | `boolean` | Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster. | [Optional] [Defaults to `false`] |

### Return type

`void` (Empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Headline metrics, trends, sentiment split, per-competitor share of voice and position distributions |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getProjectSentiment

> getProjectSentiment(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries)

Sentiment breakdown of a project brand mentions

Minimum role: viewer. Positive, neutral and negative split of the brand mentions in AI answers over a date window, per engine and per competitor. A null positivityIndex means no mentions were found in the window, which is not the same as a score of zero.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetProjectSentimentRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d.
    dateTo: 2013-10-20,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. (optional)
    engines: ...,
    // Array<string> | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    countries: ...,
    // Array<string> (optional)
    queryClusterIds: ...,
    // boolean (optional)
    includeUngroupedQueries: true,
  } satisfies GetProjectSentimentRequest;

  try {
    const data = await api.getProjectSentiment(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. | [Defaults to `undefined`] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | `Array<string>` | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [Optional] |
| **queryClusterIds** | `Array<string>` |  | [Optional] |
| **includeUngroupedQueries** | `boolean` |  | [Optional] [Defaults to `false`] |

### Return type

`void` (Empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sentiment per engine and per competitor |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getProjectTimeSeries

> getProjectTimeSeries(organizationId, projectId, dateFrom, dateTo, granularity, engines, countries, queryClusterIds, includeUngroupedQueries, competitorIds)

Rank-tracking metrics of a project over time

Minimum role: viewer. One point per bucket over the date window, each carrying the brand metrics and one same-shaped entry per requested competitor. Rank metrics (serp, shopping, mention, link) are 1-based averages where LOWER is better; positivity (0-100), shareOfVoice (0-100), mentionRate (0-100) and serpRate (0-100) are scores where higher is better. Every metric is nullable, and a null means no data was collected for that bucket, which is not the same as a value of zero. A project with no tracked queries returns an empty points list. Prefer weekly or monthly granularity over a long window to keep the response compact.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetProjectTimeSeriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d.
    dateTo: 2013-10-20,
    // 'daily' | 'weekly' | 'monthly' | Bucket size of each point. (optional)
    granularity: granularity_example,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. (optional)
    engines: ...,
    // Array<string> | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    countries: ...,
    // Array<string> (optional)
    queryClusterIds: ...,
    // boolean | On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them. (optional)
    includeUngroupedQueries: true,
    // Array<string> | Repeatable, or comma-separated. Each id adds one series under the competitors map of every point. (optional)
    competitorIds: ...,
  } satisfies GetProjectTimeSeriesRequest;

  try {
    const data = await api.getProjectTimeSeries(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. | [Defaults to `undefined`] |
| **granularity** | `daily`, `weekly`, `monthly` | Bucket size of each point. | [Optional] [Defaults to `&#39;daily&#39;`] [Enum: daily, weekly, monthly] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | `Array<string>` | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [Optional] |
| **queryClusterIds** | `Array<string>` |  | [Optional] |
| **includeUngroupedQueries** | `boolean` | On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them. | [Optional] [Defaults to `false`] |
| **competitorIds** | `Array<string>` | Repeatable, or comma-separated. Each id adds one series under the competitors map of every point. | [Optional] |

### Return type

`void` (Empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Points in bucket order, plus dataDirtySince: a date from which the rank data is being recomputed, or null when nothing is pending |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getQueryMovers

> getQueryMovers(organizationId, projectId, dateFrom, dateTo, engines, countries, sortBy, sortOrder, limit, offset)

Tracked queries ranked by how much a metric moved

Minimum role: viewer. One row per tracked query — a single engine plus country — carrying its current metric envelope and the signed change against the immediately preceding window of equal length: a 7-day window is compared with the 7 days before it. Every trend delta is signed so that POSITIVE means improved, including the position trends, where the underlying avgSerpPosition / avgShoppingPosition / avgMentionPosition / avgLinkPosition are 1-based ranks and therefore LOWER is better. shareOfVoice and positivityIndex are percentages from 0 to 100, where HIGHER is better. Sorting applies to the trend keys only: sortOrder&#x3D;desc gives the top gainers, asc the top losers. Every nullable field means \&quot;not known yet\&quot; rather than zero — a null position or shareOfVoice is a query with no data in the window, and a null positivityIndex or trend is a period with no mentions to score, neither of which is a record of losing ground. total counts the tracked queries the filters match, not the rows on this page. dataDirtySince is a date from which the rank data is being recomputed, or null when nothing is pending; while it is non-null the deltas may still move.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetQueryMoversRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d.
    dateTo: 2013-10-20,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. (optional)
    engines: ...,
    // Array<string> | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    countries: ...,
    // 'trend_serp' | 'trend_shopping' | 'trend_mention' | 'trend_link' | 'trend_share_of_voice' | Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default. (optional)
    sortBy: sortBy_example,
    // 'asc' | 'desc' | desc for the top gainers, asc for the top losers. (optional)
    sortOrder: sortOrder_example,
    // number | Page size. A value above the maximum is rejected, never clamped. (optional)
    limit: 56,
    // number (optional)
    offset: 56,
  } satisfies GetQueryMoversRequest;

  try {
    const data = await api.getQueryMovers(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. | [Defaults to `undefined`] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | `Array<string>` | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [Optional] |
| **sortBy** | `trend_serp`, `trend_shopping`, `trend_mention`, `trend_link`, `trend_share_of_voice` | Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default. | [Optional] [Defaults to `&#39;trend_share_of_voice&#39;`] [Enum: trend_serp, trend_shopping, trend_mention, trend_link, trend_share_of_voice] |
| **sortOrder** | `asc`, `desc` | desc for the top gainers, asc for the top losers. | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |
| **limit** | `number` | Page size. A value above the maximum is rejected, never clamped. | [Optional] [Defaults to `20`] |
| **offset** | `number` |  | [Optional] [Defaults to `0`] |

### Return type

`void` (Empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ranked tracked queries under \&quot;rows\&quot;, with \&quot;total\&quot; and \&quot;dataDirtySince\&quot; |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter or page bound was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getShareOfVoiceFormula

> GetShareOfVoiceFormula200Response getShareOfVoiceFormula(organizationId, projectId)

The constants behind the Share of Voice score

Minimum role: viewer. Static reference data, the same for every project: the weights and multipliers that turn individual brand mentions into a Share of Voice score. Each mention is worth &#x60;mentionTypeWeights[type] * sentimentMultipliers[tone] * (conditional ? conditionalMultiplier : directMultiplier)&#x60;, and a competitor\&#39;s Share of Voice is its share of the summed weights of every brand in the window, as a percentage. mentionTypeWeights is keyed by mention type (recommendation, comparison, listing, example, reference) and sentimentMultipliers by tone (positive, neutral, negative); a negative mention is discounted, not discarded, because it still evidences presence. A conditional mention is one the answer hedged with a condition (\&quot;if you need X\&quot;). Use this to explain a score, not to recompute one: the counts it applies to come from the mention mix endpoint. Every value is always present and is never null.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetShareOfVoiceFormulaRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetShareOfVoiceFormulaRequest;

  try {
    const data = await api.getShareOfVoiceFormula(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**GetShareOfVoiceFormula200Response**](GetShareOfVoiceFormula200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Share of Voice weighting constants |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | Not reachable here: the endpoint accepts no query parameters, so it has nothing to reject. Listed because the error envelope is shared across the API |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getTrackedQueryTimeSeries

> getTrackedQueryTimeSeries(organizationId, projectId, trackedQueryId, dateFrom, dateTo, granularity, competitorIds)

Rank-tracking time series of a single tracked query

Minimum role: viewer. One point per bucket over the date window, each carrying the brand metrics and one same-shaped entry per requested competitor. Positions (serp, shopping, mention, link) are 1-based, so a LOWER number is better; positivity, shareOfVoice, mentionRate and serpRate are percentages from 0 to 100, where higher is better. Every metric is nullable, and a null means nothing was captured for that entity in that bucket — it is not a zero: a null shareOfVoice means no measurement, a shareOfVoice of 0 means measured and never mentioned. The tracked query fixes its own engine and country, so no engine or country filter is accepted. A non-null dataDirtySince is a timestamp warning that tracked queries were deleted from the project and historical buckets may still include their contributions until the nightly refresh rebuilds them.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetTrackedQueryTimeSeriesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the project in the path.
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d.
    dateTo: 2013-10-20,
    // 'daily' | 'weekly' | 'monthly' | Bucket size. Prefer weekly or monthly for long windows. (optional)
    granularity: granularity_example,
    // Array<string> | Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint. (optional)
    competitorIds: ...,
  } satisfies GetTrackedQueryTimeSeriesRequest;

  try {
    const data = await api.getTrackedQueryTimeSeries(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **trackedQueryId** | `string` | Must belong to the project in the path. | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. | [Defaults to `undefined`] |
| **granularity** | `daily`, `weekly`, `monthly` | Bucket size. Prefer weekly or monthly for long windows. | [Optional] [Defaults to `&#39;daily&#39;`] [Enum: daily, weekly, monthly] |
| **competitorIds** | `Array<string>` | Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint. | [Optional] |

### Return type

`void` (Empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One point per bucket, with brand and per-competitor metrics |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | A filter was rejected; the details name the field |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization, project or tracked query the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getTrackingCoverage

> GetTrackingCoverage200Response getTrackingCoverage(organizationId, projectId)

Coverage and staleness of a project tracked queries

Minimum role: viewer. A current-state snapshot answering \&quot;what is stale or not being tracked\&quot;: total is every tracked query on the project, active and paused split it by status, neverChecked counts the active queries that have never run, and overdue counts the active queries whose last check is older than their own check-frequency interval (daily, weekly or monthly). neverChecked and overdue are disjoint — a query that has never run is never also counted as overdue — and both ignore paused queries, which are not expected to be checked at all. sample lists up to 20 of the overdue queries, most stale first; it is a sample of overdue only, so it never contains a never-checked query and is empty when overdue is 0. Takes no date window: every count describes the project as it stands right now.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { GetTrackingCoverageRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetTrackingCoverageRequest;

  try {
    const data = await api.getTrackingCoverage(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**GetTrackingCoverage200Response**](GetTrackingCoverage200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Coverage counts and a sample of the most-overdue queries |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | The request was rejected before it reached the project; this endpoint accepts no query parameters, so no filter can be refused here |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listKeywordListings

> ListKeywordListings200Response listKeywordListings(organizationId, projectId, dateFrom, dateTo, engines, countries, queryClusterIds, includeUngroupedQueries, status, checkFrequencies, nPasses, search, sortBy, sortOrder, limit, offset)

List a project\&#39;s keywords with their windowed metrics

Minimum role: viewer. One row per distinct keyword text of the project — every tracked query asking that text, on any engine in any country, collapsed into a single row whose variantIds name the tracked queries behind it. Each row carries the metrics of the requested window and a signed trend against the window of equal length immediately before it, where POSITIVE ALWAYS MEANS BETTER whichever direction the metric itself runs. Positions are 1-based and lower is better; rates, positivityIndex and shareOfVoice are 0-100 and higher is better; mentionPositionStability is a day-to-day spread, so lower is steadier. A null metric means nothing was captured for that keyword in the window — it is not a zero. &#x60;total&#x60; counts the KEYWORDS matching the filters, not the rows on this page and not tracked queries; &#x60;totalVariantCount&#x60; counts the tracked queries behind the keywords matching every filter EXCEPT &#x60;search&#x60; — with a text search applied it still counts the project\&#39;s variants, so do not size a force-check budget from it on a searched page. NEITHER IS THE PROJECT\&#39;S TRACKED-QUERY COUNT: the count operation reads the write model, while this listing reads projections refreshed in the background from it, so the numbers legitimately differ while those projections catch up. A project whose cached tracked-query count has not been refreshed yet answers an empty page with total 0 — the same answer as a project with no tracked queries at all — so treat an unexpected empty page right after creating queries as \&quot;not projected yet\&quot;, not as \&quot;no data\&quot;. dataDirtySince is non-null while a recalculation is pending, meaning the metrics predate the latest configuration change. Filters narrow which VARIANTS count towards a row, so engines, countries, statuses, checkFrequencies and nPassesValues each report what the filters selected rather than everything the keyword has. A filter or sort key this endpoint cannot honour is rejected by name, never ignored, and a limit above the maximum is rejected rather than quietly reduced. This operation answers JSON only: a keyword row carries a nested mentionTypeCounts object, so it is not part of the CSV family.

### Example

```ts
import {
  Configuration,
  AnalyticsApi,
} from '@mencoro/api';
import type { ListKeywordListingsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AnalyticsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
    dateFrom: 2013-10-20,
    // Date | Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom.
    dateTo: 2013-10-20,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode' | 'google_serp' | 'google_shopping'> | Repeatable, or comma-separated. Narrows which variants count towards each row. (optional)
    engines: ...,
    // Array<string> | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    countries: ...,
    // Array<string> | Restrict to keywords with a variant in these clusters. Each must belong to the project. (optional)
    queryClusterIds: ...,
    // boolean | Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection. (optional)
    includeUngroupedQueries: true,
    // 'active' | 'paused' | Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \"mixed\". (optional)
    status: status_example,
    // Array<'daily' | 'weekly' | 'monthly'> | Repeatable, or comma-separated. (optional)
    checkFrequencies: ...,
    // Array<number> | Repeatable, or comma-separated. Restrict to variants configured with these pass counts. (optional)
    nPasses: ...,
    // string | Case-insensitive substring match on the keyword text. (optional)
    search: search_example,
    // 'keyword' | 'variantCount' | 'lastCheckedAt' | 'statusSummary' | 'positivityIndex' | 'shareOfVoice' | 'avgMentionPosition' | 'avgLinkPosition' | 'mentionPositionStability' | 'avgSerpPosition' | 'avgShoppingPosition' | Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default. (optional)
    sortBy: sortBy_example,
    // 'asc' | 'desc' (optional)
    sortOrder: sortOrder_example,
    // number | Page size. A larger value is rejected, never silently reduced. (optional)
    limit: 56,
    // number | Number of matching keywords to skip before the page starts. (optional)
    offset: 56,
  } satisfies ListKeywordListingsRequest;

  try {
    const data = await api.listKeywordListings(body);
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
| **projectId** | `string` |  | [Defaults to `undefined`] |
| **dateFrom** | `Date` | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom. | [Defaults to `undefined`] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode`, `google_serp`, `google_shopping` | Repeatable, or comma-separated. Narrows which variants count towards each row. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode, google_serp, google_shopping] |
| **countries** | `Array<string>` | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [Optional] |
| **queryClusterIds** | `Array<string>` | Restrict to keywords with a variant in these clusters. Each must belong to the project. | [Optional] |
| **includeUngroupedQueries** | `boolean` | Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection. | [Optional] [Defaults to `false`] |
| **status** | `active`, `paused` | Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \&quot;mixed\&quot;. | [Optional] [Defaults to `undefined`] [Enum: active, paused] |
| **checkFrequencies** | `daily`, `weekly`, `monthly` | Repeatable, or comma-separated. | [Optional] [Enum: daily, weekly, monthly] |
| **nPasses** | `Array<number>` | Repeatable, or comma-separated. Restrict to variants configured with these pass counts. | [Optional] |
| **search** | `string` | Case-insensitive substring match on the keyword text. | [Optional] [Defaults to `undefined`] |
| **sortBy** | `keyword`, `variantCount`, `lastCheckedAt`, `statusSummary`, `positivityIndex`, `shareOfVoice`, `avgMentionPosition`, `avgLinkPosition`, `mentionPositionStability`, `avgSerpPosition`, `avgShoppingPosition` | Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default. | [Optional] [Defaults to `&#39;keyword&#39;`] [Enum: keyword, variantCount, lastCheckedAt, statusSummary, positivityIndex, shareOfVoice, avgMentionPosition, avgLinkPosition, mentionPositionStability, avgSerpPosition, avgShoppingPosition] |
| **sortOrder** | `asc`, `desc` |  | [Optional] [Defaults to `&#39;asc&#39;`] [Enum: asc, desc] |
| **limit** | `number` | Page size. A larger value is rejected, never silently reduced. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Number of matching keywords to skip before the page starts. | [Optional] [Defaults to `0`] |

### Return type

[**ListKeywordListings200Response**](ListKeywordListings200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of keywords, the totals behind it, and whether the metrics are pending recalculation |  -  |
| **400** | A filter, sort key or page bound was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

