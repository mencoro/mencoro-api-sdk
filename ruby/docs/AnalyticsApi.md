# Mencoro::AnalyticsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_available_filters**](AnalyticsApi.md#get_available_filters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/available-filters | Filter values a project is configured for |
| [**get_cited_sources**](AnalyticsApi.md#get_cited_sources) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/cited-sources | Domains and pages the AI answers cited |
| [**get_cluster_breakdown**](AnalyticsApi.md#get_cluster_breakdown) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/clusters | Rank-tracking metrics per keyword cluster |
| [**get_competitor_co_occurrence**](AnalyticsApi.md#get_competitor_co_occurrence) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/co-occurrence | Head-to-head record of the brand against each tracked competitor |
| [**get_mention_mix**](AnalyticsApi.md#get_mention_mix) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions/mix | Composition of a project brand mentions in AI answers |
| [**get_mention_samples**](AnalyticsApi.md#get_mention_samples) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions | Sample of the raw AI mention texts of a project |
| [**get_metric_glossary**](AnalyticsApi.md#get_metric_glossary) | **GET** /api/v1/metric-glossary | Map everyday wording to a metric and the operation that serves it |
| [**get_organization_overview**](AnalyticsApi.md#get_organization_overview) | **GET** /api/v1/organizations/{organizationId}/overview | Snapshot rank-health board across an organization active projects |
| [**get_project_metrics**](AnalyticsApi.md#get_project_metrics) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics | Headline visibility metrics of a project |
| [**get_project_sentiment**](AnalyticsApi.md#get_project_sentiment) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/sentiment | Sentiment breakdown of a project brand mentions |
| [**get_project_time_series**](AnalyticsApi.md#get_project_time_series) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/timeseries | Rank-tracking metrics of a project over time |
| [**get_query_movers**](AnalyticsApi.md#get_query_movers) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/movers | Tracked queries ranked by how much a metric moved |
| [**get_share_of_voice_formula**](AnalyticsApi.md#get_share_of_voice_formula) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/share-of-voice-formula | The constants behind the Share of Voice score |
| [**get_tracked_query_time_series**](AnalyticsApi.md#get_tracked_query_time_series) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/timeseries | Rank-tracking time series of a single tracked query |
| [**get_tracking_coverage**](AnalyticsApi.md#get_tracking_coverage) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/coverage | Coverage and staleness of a project tracked queries |
| [**list_keyword_listings**](AnalyticsApi.md#list_keyword_listings) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/keyword-listings | List a project&#39;s keywords with their windowed metrics |


## get_available_filters

> <GetAvailableFilters200Response> get_available_filters(organization_id, project_id)

Filter values a project is configured for

Minimum role: viewer. Call this first: it is where every other analytics operation sends you for the valid engines, countries and keyword clusters of a project, and the values it returns are the exact strings the engines, countries and queryClusterIds parameters accept — anything else is rejected as a 400. Engines are engine codes, countries are ISO-3166 alpha-2 codes, and clusters are {id, name} objects whose id goes in queryClusterIds. Takes no date window: it describes how the project is configured right now, so a value is listed as soon as a tracked query uses it, even when no response has been captured for it yet. An empty list therefore means nothing is configured for it, not that no data was collected. Competitor ids are not part of this response.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Filter values a project is configured for
  result = api_instance.get_available_filters(organization_id, project_id)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_available_filters: #{e}"
end
```

#### Using the get_available_filters_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetAvailableFilters200Response>, Integer, Hash)> get_available_filters_with_http_info(organization_id, project_id)

```ruby
begin
  # Filter values a project is configured for
  data, status_code, headers = api_instance.get_available_filters_with_http_info(organization_id, project_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetAvailableFilters200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_available_filters_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |

### Return type

[**GetAvailableFilters200Response**](GetAvailableFilters200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_cited_sources

> get_cited_sources(organization_id, project_id, date_from, date_to, opts)

Domains and pages the AI answers cited

Minimum role: viewer. The sources the answer engines drew on across a project's AI answers over a date window, ranked by how often they were cited. Per source: citationCount, the total number of citations; distinctResponseCount and distinctQueryCount, how many captured answers and tracked queries it appeared in; avgPosition, its average 1-based rank inside the answers' citation lists, where LOWER is better. A null avgPosition means no citation in the window carried a position, not a rank of zero; a null domain or sampleTitle means the citation never carried one. `total` counts the distinct sources matching the window, before paging. The list is UNFILTERED by ownership: the brand's, competitors' and third-party sources sit in the same ranking. Only the AI answer engines (chatgpt, perplexity, google_ai_overview, google_ai_mode) produce citations, so filtering by google_serp or google_shopping is accepted and returns nothing. Citations still behind an answer engine's redirect (a google.com/goto link, whose URL names the engine rather than the source) are excluded, so a source cited only through such links is absent from this list rather than counted as zero.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d.
opts = {
  engines: ['chatgpt'], # Array<String> | Repeatable, or comma-separated. Only the AI engines carry citations.
  group_by: 'domain', # String | Grain of the roll-up: \"domain\" by host, \"page\" by exact URL.
  limit: 56, # Integer | Page size. A larger value is rejected, never silently reduced.
  offset: 56 # Integer | Number of sources to skip.
}

begin
  # Domains and pages the AI answers cited
  api_instance.get_cited_sources(organization_id, project_id, date_from, date_to, opts)
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_cited_sources: #{e}"
end
```

#### Using the get_cited_sources_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> get_cited_sources_with_http_info(organization_id, project_id, date_from, date_to, opts)

```ruby
begin
  # Domains and pages the AI answers cited
  data, status_code, headers = api_instance.get_cited_sources_with_http_info(organization_id, project_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_cited_sources_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. Only the AI engines carry citations. | [optional] |
| **group_by** | **String** | Grain of the roll-up: \&quot;domain\&quot; by host, \&quot;page\&quot; by exact URL. | [optional][default to &#39;domain&#39;] |
| **limit** | **Integer** | Page size. A larger value is rejected, never silently reduced. | [optional][default to 20] |
| **offset** | **Integer** | Number of sources to skip. | [optional][default to 0] |

### Return type

nil (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## get_cluster_breakdown

> get_cluster_breakdown(organization_id, project_id, date_from, date_to, opts)

Rank-tracking metrics per keyword cluster

Minimum role: viewer. One row per keyword cluster over a date window, with its tracked query and keyword counts, average positions, rates, share of voice and sentiment split. A row whose clusterId is null is the ungrouped bucket: the tracked queries belonging to no cluster. Position metrics are 1-based and LOWER is better; rates, positivityIndex and shareOfVoice are 0-100 percentages where higher is better. A null metric means nothing was captured for that cluster in the window — it is not a zero, and averaging or charting it as one would misstate the period. dataDirtySince is non-null while a recalculation is pending, meaning the numbers predate the latest configuration change.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d.
opts = {
  engines: ['chatgpt'], # Array<String> | Repeatable, or comma-separated.
  countries: ['inner_example'], # Array<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
  query_cluster_ids: ['inner_example'], # Array<String> | Restrict to these clusters. Each must belong to the project.
  include_ungrouped_queries: true # Boolean | Sent alone, returns only the ungrouped bucket rather than adding it to every cluster.
}

begin
  # Rank-tracking metrics per keyword cluster
  api_instance.get_cluster_breakdown(organization_id, project_id, date_from, date_to, opts)
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_cluster_breakdown: #{e}"
end
```

#### Using the get_cluster_breakdown_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> get_cluster_breakdown_with_http_info(organization_id, project_id, date_from, date_to, opts)

```ruby
begin
  # Rank-tracking metrics per keyword cluster
  data, status_code, headers = api_instance.get_cluster_breakdown_with_http_info(organization_id, project_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_cluster_breakdown_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. | [optional] |
| **countries** | [**Array&lt;String&gt;**](String.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **query_cluster_ids** | [**Array&lt;String&gt;**](String.md) | Restrict to these clusters. Each must belong to the project. | [optional] |
| **include_ungrouped_queries** | **Boolean** | Sent alone, returns only the ungrouped bucket rather than adding it to every cluster. | [optional][default to false] |

### Return type

nil (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## get_competitor_co_occurrence

> get_competitor_co_occurrence(organization_id, project_id, date_from, date_to, opts)

Head-to-head record of the brand against each tracked competitor

Minimum role: viewer. Restricted to the AI answers where the brand and a competitor are BOTH mentioned, one row per tracked competitor: sharedResponseCount is how many such answers there are, and brandWins / competitorWins / ties split them by who holds the better (lower) best mention position. winRate is the percentage 0-100 of those answers the brand wins; avgOwnPosition and avgCompetitorPosition are the average best mention position each side held, 1-based, so LOWER is better. exampleQueryText and exampleAiResponseId point at one representative shared answer. Every nullable field means \"not known yet\" rather than zero: a null winRate or average position is the absence of a shared answer in the window, not a record of losing. Tracked competitors only.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d.
opts = {
  engines: ['chatgpt'], # Array<String> | Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence.
  countries: ['inner_example'], # Array<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
  competitor_id: '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids.
}

begin
  # Head-to-head record of the brand against each tracked competitor
  api_instance.get_competitor_co_occurrence(organization_id, project_id, date_from, date_to, opts)
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_competitor_co_occurrence: #{e}"
end
```

#### Using the get_competitor_co_occurrence_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> get_competitor_co_occurrence_with_http_info(organization_id, project_id, date_from, date_to, opts)

```ruby
begin
  # Head-to-head record of the brand against each tracked competitor
  data, status_code, headers = api_instance.get_competitor_co_occurrence_with_http_info(organization_id, project_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_competitor_co_occurrence_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence. | [optional] |
| **countries** | [**Array&lt;String&gt;**](String.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **competitor_id** | **String** | Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids. | [optional] |

### Return type

nil (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## get_mention_mix

> get_mention_mix(organization_id, project_id, date_from, date_to, opts)

Composition of a project brand mentions in AI answers

Minimum role: viewer. Counts of the project brand's own text mentions in AI answers over a date window, grouped three ways: byType (recommendation, comparison, listing, example, reference), byTone (positive, neutral, negative) and byQualifier (direct, conditional — a conditional mention is one the answer hedged with a condition). These are the inputs behind the Share of Voice weighted score. Every bucket is always present and is a plain count, never null: a zero means no mention of that kind was found in the window. The three groupings count the same mentions, so each one sums to the same total. Only the project brand is counted, never a competitor, and only mentions inside the answer text — a citation of the brand's URL is not a mention here. Only AI answer engines produce mentions, so restricting engines to google_serp or google_shopping alone returns all zeros. For the positive/neutral/negative split per engine and per competitor use the sentiment endpoint.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d.
opts = {
  engines: ['chatgpt'], # Array<String> | Repeatable, or comma-separated. Non-AI engines contribute no mentions.
  countries: ['inner_example'] # Array<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
}

begin
  # Composition of a project brand mentions in AI answers
  api_instance.get_mention_mix(organization_id, project_id, date_from, date_to, opts)
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_mention_mix: #{e}"
end
```

#### Using the get_mention_mix_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> get_mention_mix_with_http_info(organization_id, project_id, date_from, date_to, opts)

```ruby
begin
  # Composition of a project brand mentions in AI answers
  data, status_code, headers = api_instance.get_mention_mix_with_http_info(organization_id, project_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_mention_mix_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. Non-AI engines contribute no mentions. | [optional] |
| **countries** | [**Array&lt;String&gt;**](String.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |

### Return type

nil (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## get_mention_samples

> get_mention_samples(organization_id, project_id, date_from, date_to, opts)

Sample of the raw AI mention texts of a project

Minimum role: viewer. A paginated page of the individual mention texts behind the aggregate numbers, for qualitative review and for checking sentiment labels by eye. Each sample carries the mention text, the engine and country it was seen in, the tracked query that produced it, its sentiment and mention type, and mentionPosition — a 1-based rank inside the answer where LOWER is better, always present. `total` counts every mention matching the filters, not the size of the page returned. Only mentions inside the answer text are returned: a citation of the brand URL is not a mention here, and only AI answer engines produce mentions, so restricting engines to google_serp or google_shopping alone returns an empty page rather than an error. Two fields carry a \"not known\" rather than a zero: country is null and queryText is empty when the tracked query behind the mention has since been deleted, and competitorId is null when the mention row stores no competitor id — which is NOT an assertion that the mention is about your own brand, since an untracked competitor also stores none. Read mentionRelation instead: `own` and `tracked-competitor` are what the scraper resolved to a configured entity, `untracked-competitor` is a rival the project does not track, and null means the row predates the field. brandName carries the mentioned brand, and is the only way to name an untracked competitor, which has no competitor id to resolve one from. Omitting the competitorId filter returns exactly the rows with no competitor id stored — that is, own-brand AND untracked-competitor mentions together, not every competitor; pass a competitor UUID to restrict the page to that competitor, and use mentionRelation to separate the rest. For the aggregate positive/neutral/negative split use the sentiment endpoint, and for weighted mention-type counts the mention mix endpoint.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d.
opts = {
  engines: ['chatgpt'], # Array<String> | Repeatable, or comma-separated. Non-AI engines contribute no mentions.
  countries: ['inner_example'], # Array<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
  sentiment: 'positive', # String | Restrict to one sentiment label. Omit for every sentiment.
  mention_type: 'recommendation', # String | Restrict to one mention type. Omit for every type.
  competitor_id: '38400000-8cf0-11bd-b23e-10b96e4ef00d', # String | UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart.
  sort_by: 'recent', # String | recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default.
  limit: 56, # Integer | Page size. A larger value is rejected, never silently reduced.
  offset: 56 # Integer | Number of matching mentions to skip before the page starts.
}

begin
  # Sample of the raw AI mention texts of a project
  api_instance.get_mention_samples(organization_id, project_id, date_from, date_to, opts)
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_mention_samples: #{e}"
end
```

#### Using the get_mention_samples_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> get_mention_samples_with_http_info(organization_id, project_id, date_from, date_to, opts)

```ruby
begin
  # Sample of the raw AI mention texts of a project
  data, status_code, headers = api_instance.get_mention_samples_with_http_info(organization_id, project_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_mention_samples_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. Non-AI engines contribute no mentions. | [optional] |
| **countries** | [**Array&lt;String&gt;**](String.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **sentiment** | **String** | Restrict to one sentiment label. Omit for every sentiment. | [optional] |
| **mention_type** | **String** | Restrict to one mention type. Omit for every type. | [optional] |
| **competitor_id** | **String** | UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart. | [optional] |
| **sort_by** | **String** | recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default. | [optional][default to &#39;recent&#39;] |
| **limit** | **Integer** | Page size. A larger value is rejected, never silently reduced. | [optional][default to 20] |
| **offset** | **Integer** | Number of matching mentions to skip before the page starts. | [optional][default to 0] |

### Return type

nil (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_metric_glossary

> <GetMetricGlossary200Response> get_metric_glossary

Map everyday wording to a metric and the operation that serves it

Static reference, no project data. Each entry gives a metric, the everyday words people use for it, its unit and range, whether higher or lower is better, the operation that returns it, and example questions. Useful when turning a vague or non-technical request into the right call.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new

begin
  # Map everyday wording to a metric and the operation that serves it
  result = api_instance.get_metric_glossary
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_metric_glossary: #{e}"
end
```

#### Using the get_metric_glossary_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetMetricGlossary200Response>, Integer, Hash)> get_metric_glossary_with_http_info

```ruby
begin
  # Map everyday wording to a metric and the operation that serves it
  data, status_code, headers = api_instance.get_metric_glossary_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetMetricGlossary200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_metric_glossary_with_http_info: #{e}"
end
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


## get_organization_overview

> <GetOrganizationOverview200Response> get_organization_overview(organization_id)

Snapshot rank-health board across an organization active projects

Minimum role: viewer. One row per active project — share of voice, mention rate, average mention position, positivity index and tracked-query count — ordered by share of voice, plus an organization-level aggregate of the same metrics. Archived projects are excluded. This is a current-state snapshot and takes no date window; for a date-ranged comparison call the per-project operations (getProjectMetrics, getProjectTimeSeries) for each projectId returned here. Every metric is nullable, and a null means the project has no rank data yet — not a score of zero. Higher is better for shareOfVoice, mentionRate and positivityIndex; avgMentionPosition is a 1-based rank, so LOWER is better.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Snapshot rank-health board across an organization active projects
  result = api_instance.get_organization_overview(organization_id)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_organization_overview: #{e}"
end
```

#### Using the get_organization_overview_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetOrganizationOverview200Response>, Integer, Hash)> get_organization_overview_with_http_info(organization_id)

```ruby
begin
  # Snapshot rank-health board across an organization active projects
  data, status_code, headers = api_instance.get_organization_overview_with_http_info(organization_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetOrganizationOverview200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_organization_overview_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |

### Return type

[**GetOrganizationOverview200Response**](GetOrganizationOverview200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_project_metrics

> get_project_metrics(organization_id, project_id, date_from, date_to, opts)

Headline visibility metrics of a project

Minimum role: viewer. The project overview over a date window: share of voice (own and per competitor), mention / SERP / shopping rates, average and best positions, position stability, the sentiment split and the position-distribution buckets. Positions are 1-based, so a LOWER number is better; rates, the positivity index and share of voice are percentages from 0 to 100, where HIGHER is better. Every `trend*` field is the signed change against the immediately preceding window of the same length: negative means an improved position, positive means an improved rate or score. A null metric means \"not known yet\", never zero: a scalar is null when the window holds no checks at all, and a `trend*` field is null when there is no earlier window to compare against. The counters (`mentionCount`, `*TrackedQueryCount`, `*QueriesWithResult`, `sentiment*` and `mentionTypeCounts`) are genuine zeros instead, so an empty window reads as zero counts with null rates. `dataDirtySince` is non-null while a recalculation is pending, meaning the figures may still move for dates from then on.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d.
opts = {
  engines: ['chatgpt'], # Array<String> | Repeatable, or comma-separated.
  countries: ['inner_example'], # Array<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
  query_cluster_ids: ['inner_example'], # Array<String> | Restrict to these keyword clusters. Each must belong to this project.
  include_ungrouped_queries: true # Boolean | Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster.
}

begin
  # Headline visibility metrics of a project
  api_instance.get_project_metrics(organization_id, project_id, date_from, date_to, opts)
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_project_metrics: #{e}"
end
```

#### Using the get_project_metrics_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> get_project_metrics_with_http_info(organization_id, project_id, date_from, date_to, opts)

```ruby
begin
  # Headline visibility metrics of a project
  data, status_code, headers = api_instance.get_project_metrics_with_http_info(organization_id, project_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_project_metrics_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. | [optional] |
| **countries** | [**Array&lt;String&gt;**](String.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **query_cluster_ids** | [**Array&lt;String&gt;**](String.md) | Restrict to these keyword clusters. Each must belong to this project. | [optional] |
| **include_ungrouped_queries** | **Boolean** | Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster. | [optional][default to false] |

### Return type

nil (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## get_project_sentiment

> get_project_sentiment(organization_id, project_id, date_from, date_to, opts)

Sentiment breakdown of a project brand mentions

Minimum role: viewer. Positive, neutral and negative split of the brand mentions in AI answers over a date window, per engine and per competitor. A null positivityIndex means no mentions were found in the window, which is not the same as a score of zero.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d.
opts = {
  engines: ['chatgpt'], # Array<String> | Repeatable, or comma-separated.
  countries: ['inner_example'], # Array<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
  query_cluster_ids: ['inner_example'], # Array<String> | 
  include_ungrouped_queries: true # Boolean | 
}

begin
  # Sentiment breakdown of a project brand mentions
  api_instance.get_project_sentiment(organization_id, project_id, date_from, date_to, opts)
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_project_sentiment: #{e}"
end
```

#### Using the get_project_sentiment_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> get_project_sentiment_with_http_info(organization_id, project_id, date_from, date_to, opts)

```ruby
begin
  # Sentiment breakdown of a project brand mentions
  data, status_code, headers = api_instance.get_project_sentiment_with_http_info(organization_id, project_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_project_sentiment_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. | [optional] |
| **countries** | [**Array&lt;String&gt;**](String.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **query_cluster_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **include_ungrouped_queries** | **Boolean** |  | [optional][default to false] |

### Return type

nil (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## get_project_time_series

> get_project_time_series(organization_id, project_id, date_from, date_to, opts)

Rank-tracking metrics of a project over time

Minimum role: viewer. One point per bucket over the date window, each carrying the brand metrics and one same-shaped entry per requested competitor. Rank metrics (serp, shopping, mention, link) are 1-based averages where LOWER is better; positivity (0-100), shareOfVoice (0-100), mentionRate (0-100) and serpRate (0-100) are scores where higher is better. Every metric is nullable, and a null means no data was collected for that bucket, which is not the same as a value of zero. A project with no tracked queries returns an empty points list. Prefer weekly or monthly granularity over a long window to keep the response compact.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d.
opts = {
  granularity: 'daily', # String | Bucket size of each point.
  engines: ['chatgpt'], # Array<String> | Repeatable, or comma-separated.
  countries: ['inner_example'], # Array<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
  query_cluster_ids: ['inner_example'], # Array<String> | 
  include_ungrouped_queries: true, # Boolean | On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them.
  competitor_ids: ['inner_example'] # Array<String> | Repeatable, or comma-separated. Each id adds one series under the competitors map of every point.
}

begin
  # Rank-tracking metrics of a project over time
  api_instance.get_project_time_series(organization_id, project_id, date_from, date_to, opts)
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_project_time_series: #{e}"
end
```

#### Using the get_project_time_series_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> get_project_time_series_with_http_info(organization_id, project_id, date_from, date_to, opts)

```ruby
begin
  # Rank-tracking metrics of a project over time
  data, status_code, headers = api_instance.get_project_time_series_with_http_info(organization_id, project_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_project_time_series_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. |  |
| **granularity** | **String** | Bucket size of each point. | [optional][default to &#39;daily&#39;] |
| **engines** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. | [optional] |
| **countries** | [**Array&lt;String&gt;**](String.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **query_cluster_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **include_ungrouped_queries** | **Boolean** | On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them. | [optional][default to false] |
| **competitor_ids** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. Each id adds one series under the competitors map of every point. | [optional] |

### Return type

nil (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## get_query_movers

> get_query_movers(organization_id, project_id, date_from, date_to, opts)

Tracked queries ranked by how much a metric moved

Minimum role: viewer. One row per tracked query — a single engine plus country — carrying its current metric envelope and the signed change against the immediately preceding window of equal length: a 7-day window is compared with the 7 days before it. Every trend delta is signed so that POSITIVE means improved, including the position trends, where the underlying avgSerpPosition / avgShoppingPosition / avgMentionPosition / avgLinkPosition are 1-based ranks and therefore LOWER is better. shareOfVoice and positivityIndex are percentages from 0 to 100, where HIGHER is better. Sorting applies to the trend keys only: sortOrder=desc gives the top gainers, asc the top losers. Every nullable field means \"not known yet\" rather than zero — a null position or shareOfVoice is a query with no data in the window, and a null positivityIndex or trend is a period with no mentions to score, neither of which is a record of losing ground. total counts the tracked queries the filters match, not the rows on this page. dataDirtySince is a date from which the rank data is being recomputed, or null when nothing is pending; while it is non-null the deltas may still move.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d.
opts = {
  engines: ['chatgpt'], # Array<String> | Repeatable, or comma-separated.
  countries: ['inner_example'], # Array<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
  sort_by: 'trend_serp', # String | Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default.
  sort_order: 'asc', # String | desc for the top gainers, asc for the top losers.
  limit: 56, # Integer | Page size. A value above the maximum is rejected, never clamped.
  offset: 56 # Integer | 
}

begin
  # Tracked queries ranked by how much a metric moved
  api_instance.get_query_movers(organization_id, project_id, date_from, date_to, opts)
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_query_movers: #{e}"
end
```

#### Using the get_query_movers_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> get_query_movers_with_http_info(organization_id, project_id, date_from, date_to, opts)

```ruby
begin
  # Tracked queries ranked by how much a metric moved
  data, status_code, headers = api_instance.get_query_movers_with_http_info(organization_id, project_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_query_movers_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. |  |
| **engines** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. | [optional] |
| **countries** | [**Array&lt;String&gt;**](String.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **sort_by** | **String** | Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default. | [optional][default to &#39;trend_share_of_voice&#39;] |
| **sort_order** | **String** | desc for the top gainers, asc for the top losers. | [optional][default to &#39;desc&#39;] |
| **limit** | **Integer** | Page size. A value above the maximum is rejected, never clamped. | [optional][default to 20] |
| **offset** | **Integer** |  | [optional][default to 0] |

### Return type

nil (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## get_share_of_voice_formula

> <GetShareOfVoiceFormula200Response> get_share_of_voice_formula(organization_id, project_id)

The constants behind the Share of Voice score

Minimum role: viewer. Static reference data, the same for every project: the weights and multipliers that turn individual brand mentions into a Share of Voice score. Each mention is worth `mentionTypeWeights[type] * sentimentMultipliers[tone] * (conditional ? conditionalMultiplier : directMultiplier)`, and a competitor's Share of Voice is its share of the summed weights of every brand in the window, as a percentage. mentionTypeWeights is keyed by mention type (recommendation, comparison, listing, example, reference) and sentimentMultipliers by tone (positive, neutral, negative); a negative mention is discounted, not discarded, because it still evidences presence. A conditional mention is one the answer hedged with a condition (\"if you need X\"). Use this to explain a score, not to recompute one: the counts it applies to come from the mention mix endpoint. Every value is always present and is never null.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # The constants behind the Share of Voice score
  result = api_instance.get_share_of_voice_formula(organization_id, project_id)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_share_of_voice_formula: #{e}"
end
```

#### Using the get_share_of_voice_formula_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetShareOfVoiceFormula200Response>, Integer, Hash)> get_share_of_voice_formula_with_http_info(organization_id, project_id)

```ruby
begin
  # The constants behind the Share of Voice score
  data, status_code, headers = api_instance.get_share_of_voice_formula_with_http_info(organization_id, project_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetShareOfVoiceFormula200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_share_of_voice_formula_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |

### Return type

[**GetShareOfVoiceFormula200Response**](GetShareOfVoiceFormula200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_tracked_query_time_series

> get_tracked_query_time_series(organization_id, project_id, tracked_query_id, date_from, date_to, opts)

Rank-tracking time series of a single tracked query

Minimum role: viewer. One point per bucket over the date window, each carrying the brand metrics and one same-shaped entry per requested competitor. Positions (serp, shopping, mention, link) are 1-based, so a LOWER number is better; positivity, shareOfVoice, mentionRate and serpRate are percentages from 0 to 100, where higher is better. Every metric is nullable, and a null means nothing was captured for that entity in that bucket — it is not a zero: a null shareOfVoice means no measurement, a shareOfVoice of 0 means measured and never mentioned. The tracked query fixes its own engine and country, so no engine or country filter is accepted. A non-null dataDirtySince is a timestamp warning that tracked queries were deleted from the project and historical buckets may still include their contributions until the nightly refresh rebuilds them.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
tracked_query_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the project in the path.
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d.
opts = {
  granularity: 'daily', # String | Bucket size. Prefer weekly or monthly for long windows.
  competitor_ids: ['inner_example'] # Array<String> | Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint.
}

begin
  # Rank-tracking time series of a single tracked query
  api_instance.get_tracked_query_time_series(organization_id, project_id, tracked_query_id, date_from, date_to, opts)
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_tracked_query_time_series: #{e}"
end
```

#### Using the get_tracked_query_time_series_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> get_tracked_query_time_series_with_http_info(organization_id, project_id, tracked_query_id, date_from, date_to, opts)

```ruby
begin
  # Rank-tracking time series of a single tracked query
  data, status_code, headers = api_instance.get_tracked_query_time_series_with_http_info(organization_id, project_id, tracked_query_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_tracked_query_time_series_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **tracked_query_id** | **String** | Must belong to the project in the path. |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. |  |
| **granularity** | **String** | Bucket size. Prefer weekly or monthly for long windows. | [optional][default to &#39;daily&#39;] |
| **competitor_ids** | [**Array&lt;String&gt;**](String.md) | Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint. | [optional] |

### Return type

nil (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## get_tracking_coverage

> <GetTrackingCoverage200Response> get_tracking_coverage(organization_id, project_id)

Coverage and staleness of a project tracked queries

Minimum role: viewer. A current-state snapshot answering \"what is stale or not being tracked\": total is every tracked query on the project, active and paused split it by status, neverChecked counts the active queries that have never run, and overdue counts the active queries whose last check is older than their own check-frequency interval (daily, weekly or monthly). neverChecked and overdue are disjoint — a query that has never run is never also counted as overdue — and both ignore paused queries, which are not expected to be checked at all. sample lists up to 20 of the overdue queries, most stale first; it is a sample of overdue only, so it never contains a never-checked query and is empty when overdue is 0. Takes no date window: every count describes the project as it stands right now.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Coverage and staleness of a project tracked queries
  result = api_instance.get_tracking_coverage(organization_id, project_id)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_tracking_coverage: #{e}"
end
```

#### Using the get_tracking_coverage_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetTrackingCoverage200Response>, Integer, Hash)> get_tracking_coverage_with_http_info(organization_id, project_id)

```ruby
begin
  # Coverage and staleness of a project tracked queries
  data, status_code, headers = api_instance.get_tracking_coverage_with_http_info(organization_id, project_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetTrackingCoverage200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->get_tracking_coverage_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |

### Return type

[**GetTrackingCoverage200Response**](GetTrackingCoverage200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_keyword_listings

> <ListKeywordListings200Response> list_keyword_listings(organization_id, project_id, date_from, date_to, opts)

List a project's keywords with their windowed metrics

Minimum role: viewer. One row per distinct keyword text of the project — every tracked query asking that text, on any engine in any country, collapsed into a single row whose variantIds name the tracked queries behind it. Each row carries the metrics of the requested window and a signed trend against the window of equal length immediately before it, where POSITIVE ALWAYS MEANS BETTER whichever direction the metric itself runs. Positions are 1-based and lower is better; rates, positivityIndex and shareOfVoice are 0-100 and higher is better; mentionPositionStability is a day-to-day spread, so lower is steadier. A null metric means nothing was captured for that keyword in the window — it is not a zero. `total` counts the KEYWORDS matching the filters, not the rows on this page and not tracked queries; `totalVariantCount` counts the tracked queries behind the keywords matching every filter EXCEPT `search` — with a text search applied it still counts the project's variants, so do not size a force-check budget from it on a searched page. NEITHER IS THE PROJECT'S TRACKED-QUERY COUNT: the count operation reads the write model, while this listing reads projections refreshed in the background from it, so the numbers legitimately differ while those projections catch up. A project whose cached tracked-query count has not been refreshed yet answers an empty page with total 0 — the same answer as a project with no tracked queries at all — so treat an unexpected empty page right after creating queries as \"not projected yet\", not as \"no data\". dataDirtySince is non-null while a recalculation is pending, meaning the metrics predate the latest configuration change. Filters narrow which VARIANTS count towards a row, so engines, countries, statuses, checkFrequencies and nPassesValues each report what the filters selected rather than everything the keyword has. A filter or sort key this endpoint cannot honour is rejected by name, never ignored, and a limit above the maximum is rejected rather than quietly reduced. This operation answers JSON only: a keyword row carries a nested mentionTypeCounts object, so it is not part of the CSV family.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AnalyticsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
date_from = Date.parse('2013-10-20') # Date | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
date_to = Date.parse('2013-10-20') # Date | Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom.
opts = {
  engines: ['chatgpt'], # Array<String> | Repeatable, or comma-separated. Narrows which variants count towards each row.
  countries: ['inner_example'], # Array<String> | ISO-3166 alpha-2 codes or English names. Must be configured on the project.
  query_cluster_ids: ['inner_example'], # Array<String> | Restrict to keywords with a variant in these clusters. Each must belong to the project.
  include_ungrouped_queries: true, # Boolean | Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection.
  status: 'active', # String | Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \"mixed\".
  check_frequencies: ['daily'], # Array<String> | Repeatable, or comma-separated.
  n_passes: [37], # Array<Integer> | Repeatable, or comma-separated. Restrict to variants configured with these pass counts.
  search: 'search_example', # String | Case-insensitive substring match on the keyword text.
  sort_by: 'keyword', # String | Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default.
  sort_order: 'asc', # String | 
  limit: 56, # Integer | Page size. A larger value is rejected, never silently reduced.
  offset: 56 # Integer | Number of matching keywords to skip before the page starts.
}

begin
  # List a project's keywords with their windowed metrics
  result = api_instance.list_keyword_listings(organization_id, project_id, date_from, date_to, opts)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->list_keyword_listings: #{e}"
end
```

#### Using the list_keyword_listings_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListKeywordListings200Response>, Integer, Hash)> list_keyword_listings_with_http_info(organization_id, project_id, date_from, date_to, opts)

```ruby
begin
  # List a project's keywords with their windowed metrics
  data, status_code, headers = api_instance.list_keyword_listings_with_http_info(organization_id, project_id, date_from, date_to, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListKeywordListings200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling AnalyticsApi->list_keyword_listings_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. |  |
| **date_to** | **Date** | Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom. |  |
| **engines** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. Narrows which variants count towards each row. | [optional] |
| **countries** | [**Array&lt;String&gt;**](String.md) | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] |
| **query_cluster_ids** | [**Array&lt;String&gt;**](String.md) | Restrict to keywords with a variant in these clusters. Each must belong to the project. | [optional] |
| **include_ungrouped_queries** | **Boolean** | Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection. | [optional][default to false] |
| **status** | **String** | Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \&quot;mixed\&quot;. | [optional] |
| **check_frequencies** | [**Array&lt;String&gt;**](String.md) | Repeatable, or comma-separated. | [optional] |
| **n_passes** | [**Array&lt;Integer&gt;**](Integer.md) | Repeatable, or comma-separated. Restrict to variants configured with these pass counts. | [optional] |
| **search** | **String** | Case-insensitive substring match on the keyword text. | [optional] |
| **sort_by** | **String** | Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default. | [optional][default to &#39;keyword&#39;] |
| **sort_order** | **String** |  | [optional][default to &#39;asc&#39;] |
| **limit** | **Integer** | Page size. A larger value is rejected, never silently reduced. | [optional][default to 20] |
| **offset** | **Integer** | Number of matching keywords to skip before the page starts. | [optional][default to 0] |

### Return type

[**ListKeywordListings200Response**](ListKeywordListings200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

