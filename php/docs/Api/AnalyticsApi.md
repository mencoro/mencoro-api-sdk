# Mencoro\Api\AnalyticsApi

Analytics

All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAvailableFilters()**](AnalyticsApi.md#getAvailableFilters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/available-filters | Filter values a project is configured for |
| [**getCitedSources()**](AnalyticsApi.md#getCitedSources) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/cited-sources | Domains and pages the AI answers cited |
| [**getClusterBreakdown()**](AnalyticsApi.md#getClusterBreakdown) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/clusters | Rank-tracking metrics per keyword cluster |
| [**getCompetitorCoOccurrence()**](AnalyticsApi.md#getCompetitorCoOccurrence) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/co-occurrence | Head-to-head record of the brand against each tracked competitor |
| [**getMentionMix()**](AnalyticsApi.md#getMentionMix) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions/mix | Composition of a project brand mentions in AI answers |
| [**getMentionSamples()**](AnalyticsApi.md#getMentionSamples) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions | Sample of the raw AI mention texts of a project |
| [**getMetricGlossary()**](AnalyticsApi.md#getMetricGlossary) | **GET** /api/v1/metric-glossary | Map everyday wording to a metric and the operation that serves it |
| [**getOrganizationOverview()**](AnalyticsApi.md#getOrganizationOverview) | **GET** /api/v1/organizations/{organizationId}/overview | Snapshot rank-health board across an organization active projects |
| [**getProjectMetrics()**](AnalyticsApi.md#getProjectMetrics) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics | Headline visibility metrics of a project |
| [**getProjectSentiment()**](AnalyticsApi.md#getProjectSentiment) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/sentiment | Sentiment breakdown of a project brand mentions |
| [**getProjectTimeSeries()**](AnalyticsApi.md#getProjectTimeSeries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/timeseries | Rank-tracking metrics of a project over time |
| [**getQueryMovers()**](AnalyticsApi.md#getQueryMovers) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/movers | Tracked queries ranked by how much a metric moved |
| [**getShareOfVoiceFormula()**](AnalyticsApi.md#getShareOfVoiceFormula) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/share-of-voice-formula | The constants behind the Share of Voice score |
| [**getTrackedQueryTimeSeries()**](AnalyticsApi.md#getTrackedQueryTimeSeries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/timeseries | Rank-tracking time series of a single tracked query |
| [**getTrackingCoverage()**](AnalyticsApi.md#getTrackingCoverage) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/coverage | Coverage and staleness of a project tracked queries |
| [**listKeywordListings()**](AnalyticsApi.md#listKeywordListings) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/keyword-listings | List a project&#39;s keywords with their windowed metrics |


## `getAvailableFilters()`

```php
getAvailableFilters($organization_id, $project_id): \Mencoro\Api\Model\GetAvailableFilters200Response
```

Filter values a project is configured for

Minimum role: viewer. Call this first: it is where every other analytics operation sends you for the valid engines, countries and keyword clusters of a project, and the values it returns are the exact strings the engines, countries and queryClusterIds parameters accept — anything else is rejected as a 400. Engines are engine codes, countries are ISO-3166 alpha-2 codes, and clusters are {id, name} objects whose id goes in queryClusterIds. Takes no date window: it describes how the project is configured right now, so a value is listed as soon as a tracked query uses it, even when no response has been captured for it yet. An empty list therefore means nothing is configured for it, not that no data was collected. Competitor ids are not part of this response.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string

try {
    $result = $apiInstance->getAvailableFilters($organization_id, $project_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getAvailableFilters: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\GetAvailableFilters200Response**](../Model/GetAvailableFilters200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCitedSources()`

```php
getCitedSources($organization_id, $project_id, $date_from, $date_to, $engines, $group_by, $limit, $offset): \Mencoro\Api\Model\CitedSourcesResponse
```

Domains and pages the AI answers cited

Minimum role: viewer. The sources the answer engines drew on across a project's AI answers over a date window, ranked by how often they were cited. Per source: citationCount, the total number of citations; distinctResponseCount and distinctQueryCount, how many captured answers and tracked queries it appeared in; avgPosition, its average 1-based rank inside the answers' citation lists, where LOWER is better. A null avgPosition means no citation in the window carried a position, not a rank of zero; a null domain or sampleTitle means the citation never carried one. `total` counts the distinct sources matching the window, before paging. The list is UNFILTERED by ownership: the brand's, competitors' and third-party sources sit in the same ranking. Only the AI answer engines (chatgpt, perplexity, google_ai_overview, google_ai_mode) produce citations, so filtering by google_serp or google_shopping is accepted and returns nothing. Citations still behind an answer engine's redirect (a google.com/goto link, whose URL names the engine rather than the source) are excluded, so a source cited only through such links is absent from this list rather than counted as zero.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d.
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated. Only the AI engines carry citations.
$group_by = 'domain'; // string | Grain of the roll-up: \"domain\" by host, \"page\" by exact URL.
$limit = 20; // int | Page size. A larger value is rejected, never silently reduced.
$offset = 0; // int | Number of sources to skip.

try {
    $result = $apiInstance->getCitedSources($organization_id, $project_id, $date_from, $date_to, $engines, $group_by, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getCitedSources: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. Only the AI engines carry citations. | [optional] |
| **group_by** | **string**| Grain of the roll-up: \&quot;domain\&quot; by host, \&quot;page\&quot; by exact URL. | [optional] [default to &#39;domain&#39;] |
| **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int**| Number of sources to skip. | [optional] [default to 0] |

### Return type

[**\Mencoro\Api\Model\CitedSourcesResponse**](../Model/CitedSourcesResponse.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getClusterBreakdown()`

```php
getClusterBreakdown($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $query_cluster_ids, $include_ungrouped_queries): \Mencoro\Api\Model\ProjectRankTrackingClusterBreakdown
```

Rank-tracking metrics per keyword cluster

Minimum role: viewer. One row per keyword cluster over a date window, with its tracked query and keyword counts, average positions, rates, share of voice and sentiment split. A row whose clusterId is null is the ungrouped bucket: the tracked queries belonging to no cluster. Position metrics are 1-based and LOWER is better; rates, positivityIndex and shareOfVoice are 0-100 percentages where higher is better. A null metric means nothing was captured for that cluster in the window — it is not a zero, and averaging or charting it as one would misstate the period. dataDirtySince is non-null while a recalculation is pending, meaning the numbers predate the latest configuration change.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d.
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated.
$countries = array('countries_example'); // string[] | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
$query_cluster_ids = array('query_cluster_ids_example'); // string[] | Restrict to these clusters. Each must belong to the project.
$include_ungrouped_queries = false; // bool | Sent alone, returns only the ungrouped bucket rather than adding it to every cluster.

try {
    $result = $apiInstance->getClusterBreakdown($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $query_cluster_ids, $include_ungrouped_queries);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getClusterBreakdown: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. | [optional] |
| **countries** | [**string[]**](../Model/string.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **query_cluster_ids** | [**string[]**](../Model/string.md)| Restrict to these clusters. Each must belong to the project. | [optional] |
| **include_ungrouped_queries** | **bool**| Sent alone, returns only the ungrouped bucket rather than adding it to every cluster. | [optional] [default to false] |

### Return type

[**\Mencoro\Api\Model\ProjectRankTrackingClusterBreakdown**](../Model/ProjectRankTrackingClusterBreakdown.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCompetitorCoOccurrence()`

```php
getCompetitorCoOccurrence($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $competitor_id): \Mencoro\Api\Model\CompetitorCoOccurrenceResponse
```

Head-to-head record of the brand against each tracked competitor

Minimum role: viewer. Restricted to the AI answers where the brand and a competitor are BOTH mentioned, one row per tracked competitor: sharedResponseCount is how many such answers there are, and brandWins / competitorWins / ties split them by who holds the better (lower) best mention position. winRate is the percentage 0-100 of those answers the brand wins; avgOwnPosition and avgCompetitorPosition are the average best mention position each side held, 1-based, so LOWER is better. exampleQueryText and exampleAiResponseId point at one representative shared answer. Every nullable field means \"not known yet\" rather than zero: a null winRate or average position is the absence of a shared answer in the window, not a record of losing. Tracked competitors only.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d.
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence.
$countries = array('countries_example'); // string[] | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
$competitor_id = 'competitor_id_example'; // string | Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids.

try {
    $result = $apiInstance->getCompetitorCoOccurrence($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $competitor_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getCompetitorCoOccurrence: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence. | [optional] |
| **countries** | [**string[]**](../Model/string.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **competitor_id** | **string**| Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids. | [optional] |

### Return type

[**\Mencoro\Api\Model\CompetitorCoOccurrenceResponse**](../Model/CompetitorCoOccurrenceResponse.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMentionMix()`

```php
getMentionMix($organization_id, $project_id, $date_from, $date_to, $engines, $countries): \Mencoro\Api\Model\ProjectMentionMixResponse
```

Composition of a project brand mentions in AI answers

Minimum role: viewer. Counts of the project brand's own text mentions in AI answers over a date window, grouped three ways: byType (recommendation, comparison, listing, example, reference), byTone (positive, neutral, negative) and byQualifier (direct, conditional — a conditional mention is one the answer hedged with a condition). These are the inputs behind the Share of Voice weighted score. Every bucket is always present and is a plain count, never null: a zero means no mention of that kind was found in the window. The three groupings count the same mentions, so each one sums to the same total. Only the project brand is counted, never a competitor, and only mentions inside the answer text — a citation of the brand's URL is not a mention here. Only AI answer engines produce mentions, so restricting engines to google_serp or google_shopping alone returns all zeros. For the positive/neutral/negative split per engine and per competitor use the sentiment endpoint.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d.
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated. Non-AI engines contribute no mentions.
$countries = array('countries_example'); // string[] | ISO-3166 alpha-2 codes or English names. Must be configured on the project.

try {
    $result = $apiInstance->getMentionMix($organization_id, $project_id, $date_from, $date_to, $engines, $countries);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getMentionMix: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. Non-AI engines contribute no mentions. | [optional] |
| **countries** | [**string[]**](../Model/string.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |

### Return type

[**\Mencoro\Api\Model\ProjectMentionMixResponse**](../Model/ProjectMentionMixResponse.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMentionSamples()`

```php
getMentionSamples($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $sentiment, $mention_type, $competitor_id, $sort_by, $limit, $offset): \Mencoro\Api\Model\ProjectMentionSamplesResponse
```

Sample of the raw AI mention texts of a project

Minimum role: viewer. A paginated page of the individual mention texts behind the aggregate numbers, for qualitative review and for checking sentiment labels by eye. Each sample carries the mention text, the engine and country it was seen in, the tracked query that produced it, its sentiment and mention type, and mentionPosition — a 1-based rank inside the answer where LOWER is better, always present. `total` counts every mention matching the filters, not the size of the page returned. Only mentions inside the answer text are returned: a citation of the brand URL is not a mention here, and only AI answer engines produce mentions, so restricting engines to google_serp or google_shopping alone returns an empty page rather than an error. Two fields carry a \"not known\" rather than a zero: country is null and queryText is empty when the tracked query behind the mention has since been deleted, and competitorId is null when the mention row stores no competitor id — which is NOT an assertion that the mention is about your own brand, since an untracked competitor also stores none. Read mentionRelation instead: `own` and `tracked-competitor` are what the scraper resolved to a configured entity, `untracked-competitor` is a rival the project does not track, and null means the row predates the field. brandName carries the mentioned brand, and is the only way to name an untracked competitor, which has no competitor id to resolve one from. Omitting the competitorId filter returns exactly the rows with no competitor id stored — that is, own-brand AND untracked-competitor mentions together, not every competitor; pass a competitor UUID to restrict the page to that competitor, and use mentionRelation to separate the rest. For the aggregate positive/neutral/negative split use the sentiment endpoint, and for weighted mention-type counts the mention mix endpoint.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d.
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated. Non-AI engines contribute no mentions.
$countries = array('countries_example'); // string[] | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
$sentiment = 'sentiment_example'; // string | Restrict to one sentiment label. Omit for every sentiment.
$mention_type = 'mention_type_example'; // string | Restrict to one mention type. Omit for every type.
$competitor_id = 'competitor_id_example'; // string | UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart.
$sort_by = 'recent'; // string | recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default.
$limit = 20; // int | Page size. A larger value is rejected, never silently reduced.
$offset = 0; // int | Number of matching mentions to skip before the page starts.

try {
    $result = $apiInstance->getMentionSamples($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $sentiment, $mention_type, $competitor_id, $sort_by, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getMentionSamples: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. Non-AI engines contribute no mentions. | [optional] |
| **countries** | [**string[]**](../Model/string.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **sentiment** | **string**| Restrict to one sentiment label. Omit for every sentiment. | [optional] |
| **mention_type** | **string**| Restrict to one mention type. Omit for every type. | [optional] |
| **competitor_id** | **string**| UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart. | [optional] |
| **sort_by** | **string**| recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;recent&#39;] |
| **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int**| Number of matching mentions to skip before the page starts. | [optional] [default to 0] |

### Return type

[**\Mencoro\Api\Model\ProjectMentionSamplesResponse**](../Model/ProjectMentionSamplesResponse.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMetricGlossary()`

```php
getMetricGlossary(): \Mencoro\Api\Model\GetMetricGlossary200Response
```

Map everyday wording to a metric and the operation that serves it

Static reference, no project data. Each entry gives a metric, the everyday words people use for it, its unit and range, whether higher or lower is better, the operation that returns it, and example questions. Useful when turning a vague or non-technical request into the right call.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getMetricGlossary();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getMetricGlossary: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\Mencoro\Api\Model\GetMetricGlossary200Response**](../Model/GetMetricGlossary200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getOrganizationOverview()`

```php
getOrganizationOverview($organization_id): \Mencoro\Api\Model\GetOrganizationOverview200Response
```

Snapshot rank-health board across an organization active projects

Minimum role: viewer. One row per active project — share of voice, mention rate, average mention position, positivity index and tracked-query count — ordered by share of voice, plus an organization-level aggregate of the same metrics. Archived projects are excluded. This is a current-state snapshot and takes no date window; for a date-ranged comparison call the per-project operations (getProjectMetrics, getProjectTimeSeries) for each projectId returned here. Every metric is nullable, and a null means the project has no rank data yet — not a score of zero. Higher is better for shareOfVoice, mentionRate and positivityIndex; avgMentionPosition is a 1-based rank, so LOWER is better.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string

try {
    $result = $apiInstance->getOrganizationOverview($organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getOrganizationOverview: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\GetOrganizationOverview200Response**](../Model/GetOrganizationOverview200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getProjectMetrics()`

```php
getProjectMetrics($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $query_cluster_ids, $include_ungrouped_queries): \Mencoro\Api\Model\ProjectRankTrackingStats
```

Headline visibility metrics of a project

Minimum role: viewer. The project overview over a date window: share of voice (own and per competitor), mention / SERP / shopping rates, average and best positions, position stability, the sentiment split and the position-distribution buckets. Positions are 1-based, so a LOWER number is better; rates, the positivity index and share of voice are percentages from 0 to 100, where HIGHER is better. Every `trend*` field is the signed change against the immediately preceding window of the same length: negative means an improved position, positive means an improved rate or score. A null metric means \"not known yet\", never zero: a scalar is null when the window holds no checks at all, and a `trend*` field is null when there is no earlier window to compare against. The counters (`mentionCount`, `*TrackedQueryCount`, `*QueriesWithResult`, `sentiment*` and `mentionTypeCounts`) are genuine zeros instead, so an empty window reads as zero counts with null rates. `dataDirtySince` is non-null while a recalculation is pending, meaning the figures may still move for dates from then on.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d.
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated.
$countries = array('countries_example'); // string[] | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
$query_cluster_ids = array('query_cluster_ids_example'); // string[] | Restrict to these keyword clusters. Each must belong to this project.
$include_ungrouped_queries = false; // bool | Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster.

try {
    $result = $apiInstance->getProjectMetrics($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $query_cluster_ids, $include_ungrouped_queries);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getProjectMetrics: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. | [optional] |
| **countries** | [**string[]**](../Model/string.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **query_cluster_ids** | [**string[]**](../Model/string.md)| Restrict to these keyword clusters. Each must belong to this project. | [optional] |
| **include_ungrouped_queries** | **bool**| Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster. | [optional] [default to false] |

### Return type

[**\Mencoro\Api\Model\ProjectRankTrackingStats**](../Model/ProjectRankTrackingStats.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getProjectSentiment()`

```php
getProjectSentiment($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $query_cluster_ids, $include_ungrouped_queries): \Mencoro\Api\Model\ProjectSentimentBreakdown
```

Sentiment breakdown of a project brand mentions

Minimum role: viewer. Positive, neutral and negative split of the brand mentions in AI answers over a date window, per engine and per competitor. A null positivityIndex means no mentions were found in the window, which is not the same as a score of zero.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d.
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated.
$countries = array('countries_example'); // string[] | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
$query_cluster_ids = array('query_cluster_ids_example'); // string[]
$include_ungrouped_queries = false; // bool

try {
    $result = $apiInstance->getProjectSentiment($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $query_cluster_ids, $include_ungrouped_queries);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getProjectSentiment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. | [optional] |
| **countries** | [**string[]**](../Model/string.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **query_cluster_ids** | [**string[]**](../Model/string.md)|  | [optional] |
| **include_ungrouped_queries** | **bool**|  | [optional] [default to false] |

### Return type

[**\Mencoro\Api\Model\ProjectSentimentBreakdown**](../Model/ProjectSentimentBreakdown.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getProjectTimeSeries()`

```php
getProjectTimeSeries($organization_id, $project_id, $date_from, $date_to, $granularity, $engines, $countries, $query_cluster_ids, $include_ungrouped_queries, $competitor_ids): \Mencoro\Api\Model\ProjectRankTrackingTimeSeries
```

Rank-tracking metrics of a project over time

Minimum role: viewer. One point per bucket over the date window, each carrying the brand metrics and one same-shaped entry per requested competitor. Rank metrics (serp, shopping, mention, link) are 1-based averages where LOWER is better; positivity (0-100), shareOfVoice (0-100), mentionRate (0-100) and serpRate (0-100) are scores where higher is better. Every metric is nullable, and a null means no data was collected for that bucket, which is not the same as a value of zero. A project with no tracked queries returns an empty points list. Prefer weekly or monthly granularity over a long window to keep the response compact.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d.
$granularity = 'daily'; // string | Bucket size of each point.
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated.
$countries = array('countries_example'); // string[] | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
$query_cluster_ids = array('query_cluster_ids_example'); // string[]
$include_ungrouped_queries = false; // bool | On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them.
$competitor_ids = array('competitor_ids_example'); // string[] | Repeatable, or comma-separated. Each id adds one series under the competitors map of every point.

try {
    $result = $apiInstance->getProjectTimeSeries($organization_id, $project_id, $date_from, $date_to, $granularity, $engines, $countries, $query_cluster_ids, $include_ungrouped_queries, $competitor_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getProjectTimeSeries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. | |
| **granularity** | **string**| Bucket size of each point. | [optional] [default to &#39;daily&#39;] |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. | [optional] |
| **countries** | [**string[]**](../Model/string.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **query_cluster_ids** | [**string[]**](../Model/string.md)|  | [optional] |
| **include_ungrouped_queries** | **bool**| On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them. | [optional] [default to false] |
| **competitor_ids** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. Each id adds one series under the competitors map of every point. | [optional] |

### Return type

[**\Mencoro\Api\Model\ProjectRankTrackingTimeSeries**](../Model/ProjectRankTrackingTimeSeries.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getQueryMovers()`

```php
getQueryMovers($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $sort_by, $sort_order, $limit, $offset): \Mencoro\Api\Model\TrackedQueryMoversResponse
```

Tracked queries ranked by how much a metric moved

Minimum role: viewer. One row per tracked query — a single engine plus country — carrying its current metric envelope and the signed change against the immediately preceding window of equal length: a 7-day window is compared with the 7 days before it. Every trend delta is signed so that POSITIVE means improved, including the position trends, where the underlying avgSerpPosition / avgShoppingPosition / avgMentionPosition / avgLinkPosition are 1-based ranks and therefore LOWER is better. shareOfVoice and positivityIndex are percentages from 0 to 100, where HIGHER is better. Sorting applies to the trend keys only: sortOrder=desc gives the top gainers, asc the top losers. Every nullable field means \"not known yet\" rather than zero — a null position or shareOfVoice is a query with no data in the window, and a null positivityIndex or trend is a period with no mentions to score, neither of which is a record of losing ground. total counts the tracked queries the filters match, not the rows on this page. dataDirtySince is a date from which the rank data is being recomputed, or null when nothing is pending; while it is non-null the deltas may still move.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d.
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated.
$countries = array('countries_example'); // string[] | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
$sort_by = 'trend_share_of_voice'; // string | Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default.
$sort_order = 'desc'; // string | desc for the top gainers, asc for the top losers.
$limit = 20; // int | Page size. A value above the maximum is rejected, never clamped.
$offset = 0; // int

try {
    $result = $apiInstance->getQueryMovers($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $sort_by, $sort_order, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getQueryMovers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. | |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. | [optional] |
| **countries** | [**string[]**](../Model/string.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **sort_by** | **string**| Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;trend_share_of_voice&#39;] |
| **sort_order** | **string**| desc for the top gainers, asc for the top losers. | [optional] [default to &#39;desc&#39;] |
| **limit** | **int**| Page size. A value above the maximum is rejected, never clamped. | [optional] [default to 20] |
| **offset** | **int**|  | [optional] [default to 0] |

### Return type

[**\Mencoro\Api\Model\TrackedQueryMoversResponse**](../Model/TrackedQueryMoversResponse.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getShareOfVoiceFormula()`

```php
getShareOfVoiceFormula($organization_id, $project_id): \Mencoro\Api\Model\GetShareOfVoiceFormula200Response
```

The constants behind the Share of Voice score

Minimum role: viewer. Static reference data, the same for every project: the weights and multipliers that turn individual brand mentions into a Share of Voice score. Each mention is worth `mentionTypeWeights[type] * sentimentMultipliers[tone] * (conditional ? conditionalMultiplier : directMultiplier)`, and a competitor's Share of Voice is its share of the summed weights of every brand in the window, as a percentage. mentionTypeWeights is keyed by mention type (recommendation, comparison, listing, example, reference) and sentimentMultipliers by tone (positive, neutral, negative); a negative mention is discounted, not discarded, because it still evidences presence. A conditional mention is one the answer hedged with a condition (\"if you need X\"). Use this to explain a score, not to recompute one: the counts it applies to come from the mention mix endpoint. Every value is always present and is never null.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string

try {
    $result = $apiInstance->getShareOfVoiceFormula($organization_id, $project_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getShareOfVoiceFormula: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\GetShareOfVoiceFormula200Response**](../Model/GetShareOfVoiceFormula200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getTrackedQueryTimeSeries()`

```php
getTrackedQueryTimeSeries($organization_id, $project_id, $tracked_query_id, $date_from, $date_to, $granularity, $competitor_ids): \Mencoro\Api\Model\TrackedQueryRankTrackingTimeSeries
```

Rank-tracking time series of a single tracked query

Minimum role: viewer. One point per bucket over the date window, each carrying the brand metrics and one same-shaped entry per requested competitor. Positions (serp, shopping, mention, link) are 1-based, so a LOWER number is better; positivity, shareOfVoice, mentionRate and serpRate are percentages from 0 to 100, where higher is better. Every metric is nullable, and a null means nothing was captured for that entity in that bucket — it is not a zero: a null shareOfVoice means no measurement, a shareOfVoice of 0 means measured and never mentioned. The tracked query fixes its own engine and country, so no engine or country filter is accepted. A non-null dataDirtySince is a timestamp warning that tracked queries were deleted from the project and historical buckets may still include their contributions until the nightly refresh rebuilds them.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$tracked_query_id = 'tracked_query_id_example'; // string | Must belong to the project in the path.
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d.
$granularity = 'daily'; // string | Bucket size. Prefer weekly or monthly for long windows.
$competitor_ids = array('competitor_ids_example'); // string[] | Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint.

try {
    $result = $apiInstance->getTrackedQueryTimeSeries($organization_id, $project_id, $tracked_query_id, $date_from, $date_to, $granularity, $competitor_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getTrackedQueryTimeSeries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **tracked_query_id** | **string**| Must belong to the project in the path. | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. | |
| **granularity** | **string**| Bucket size. Prefer weekly or monthly for long windows. | [optional] [default to &#39;daily&#39;] |
| **competitor_ids** | [**string[]**](../Model/string.md)| Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint. | [optional] |

### Return type

[**\Mencoro\Api\Model\TrackedQueryRankTrackingTimeSeries**](../Model/TrackedQueryRankTrackingTimeSeries.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getTrackingCoverage()`

```php
getTrackingCoverage($organization_id, $project_id): \Mencoro\Api\Model\GetTrackingCoverage200Response
```

Coverage and staleness of a project tracked queries

Minimum role: viewer. A current-state snapshot answering \"what is stale or not being tracked\": total is every tracked query on the project, active and paused split it by status, neverChecked counts the active queries that have never run, and overdue counts the active queries whose last check is older than their own check-frequency interval (daily, weekly or monthly). neverChecked and overdue are disjoint — a query that has never run is never also counted as overdue — and both ignore paused queries, which are not expected to be checked at all. sample lists up to 20 of the overdue queries, most stale first; it is a sample of overdue only, so it never contains a never-checked query and is empty when overdue is 0. Takes no date window: every count describes the project as it stands right now.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string

try {
    $result = $apiInstance->getTrackingCoverage($organization_id, $project_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getTrackingCoverage: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\GetTrackingCoverage200Response**](../Model/GetTrackingCoverage200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listKeywordListings()`

```php
listKeywordListings($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $query_cluster_ids, $include_ungrouped_queries, $status, $check_frequencies, $n_passes, $search, $sort_by, $sort_order, $limit, $offset): \Mencoro\Api\Model\ListKeywordListings200Response
```

List a project's keywords with their windowed metrics

Minimum role: viewer. One row per distinct keyword text of the project — every tracked query asking that text, on any engine in any country, collapsed into a single row whose variantIds name the tracked queries behind it. Each row carries the metrics of the requested window and a signed trend against the window of equal length immediately before it, where POSITIVE ALWAYS MEANS BETTER whichever direction the metric itself runs. Positions are 1-based and lower is better; rates, positivityIndex and shareOfVoice are 0-100 and higher is better; mentionPositionStability is a day-to-day spread, so lower is steadier. A null metric means nothing was captured for that keyword in the window — it is not a zero. `total` counts the KEYWORDS matching the filters, not the rows on this page and not tracked queries; `totalVariantCount` counts the tracked queries behind the keywords matching every filter EXCEPT `search` — with a text search applied it still counts the project's variants, so do not size a force-check budget from it on a searched page. NEITHER IS THE PROJECT'S TRACKED-QUERY COUNT: the count operation reads the write model, while this listing reads projections refreshed in the background from it, so the numbers legitimately differ while those projections catch up. A project whose cached tracked-query count has not been refreshed yet answers an empty page with total 0 — the same answer as a project with no tracked queries at all — so treat an unexpected empty page right after creating queries as \"not projected yet\", not as \"no data\". dataDirtySince is non-null while a recalculation is pending, meaning the metrics predate the latest configuration change. Filters narrow which VARIANTS count towards a row, so engines, countries, statuses, checkFrequencies and nPassesValues each report what the filters selected rather than everything the keyword has. A filter or sort key this endpoint cannot honour is rejected by name, never ignored, and a limit above the maximum is rejected rather than quietly reduced. This operation answers JSON only: a keyword row carries a nested mentionTypeCounts object, so it is not part of the CSV family.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom.
$engines = array('engines_example'); // string[] | Repeatable, or comma-separated. Narrows which variants count towards each row.
$countries = array('countries_example'); // string[] | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
$query_cluster_ids = array('query_cluster_ids_example'); // string[] | Restrict to keywords with a variant in these clusters. Each must belong to the project.
$include_ungrouped_queries = false; // bool | Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection.
$status = 'status_example'; // string | Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \"mixed\".
$check_frequencies = array('check_frequencies_example'); // string[] | Repeatable, or comma-separated.
$n_passes = array(56); // int[] | Repeatable, or comma-separated. Restrict to variants configured with these pass counts.
$search = 'search_example'; // string | Case-insensitive substring match on the keyword text.
$sort_by = 'keyword'; // string | Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default.
$sort_order = 'asc'; // string
$limit = 20; // int | Page size. A larger value is rejected, never silently reduced.
$offset = 0; // int | Number of matching keywords to skip before the page starts.

try {
    $result = $apiInstance->listKeywordListings($organization_id, $project_id, $date_from, $date_to, $engines, $countries, $query_cluster_ids, $include_ungrouped_queries, $status, $check_frequencies, $n_passes, $search, $sort_by, $sort_order, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->listKeywordListings: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | |
| **date_to** | **\DateTime**| Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom. | |
| **engines** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. Narrows which variants count towards each row. | [optional] |
| **countries** | [**string[]**](../Model/string.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **query_cluster_ids** | [**string[]**](../Model/string.md)| Restrict to keywords with a variant in these clusters. Each must belong to the project. | [optional] |
| **include_ungrouped_queries** | **bool**| Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection. | [optional] [default to false] |
| **status** | **string**| Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \&quot;mixed\&quot;. | [optional] |
| **check_frequencies** | [**string[]**](../Model/string.md)| Repeatable, or comma-separated. | [optional] |
| **n_passes** | [**int[]**](../Model/int.md)| Repeatable, or comma-separated. Restrict to variants configured with these pass counts. | [optional] |
| **search** | **string**| Case-insensitive substring match on the keyword text. | [optional] |
| **sort_by** | **string**| Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default. | [optional] [default to &#39;keyword&#39;] |
| **sort_order** | **string**|  | [optional] [default to &#39;asc&#39;] |
| **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int**| Number of matching keywords to skip before the page starts. | [optional] [default to 0] |

### Return type

[**\Mencoro\Api\Model\ListKeywordListings200Response**](../Model/ListKeywordListings200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
