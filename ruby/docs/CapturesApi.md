# Mencoro::CapturesApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**list_ai_responses**](CapturesApi.md#list_ai_responses) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/ai-responses | List captured AI answers |
| [**list_search_snapshots**](CapturesApi.md#list_search_snapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/search-snapshots | List captured search-results pages |
| [**list_shopping_snapshots**](CapturesApi.md#list_shopping_snapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/shopping-snapshots | List captured shopping-results pages |


## list_ai_responses

> <ListAiResponses200Response> list_ai_responses(organization_id, project_id, opts)

List captured AI answers

Minimum role: viewer. Every AI answer captured for a project, newest first, one page at a time. This is the evidence under the analytics operations: the full answer text and the sources the engine cited, exactly as captured. Read `unresolved` on a citation before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector, not to the publisher; count the citation, do not credit the site. `passIndex` and `passCount` describe multi-pass sampling: rows sharing a `trackedQueryId` and `capturedAt` are passes of one run, not duplicates, so aggregating across them without dividing by `passCount` double-counts that run. `responseText` is the whole answer, so a page of 100 is a large response — lower `limit` rather than paging blind. Captures are kept for 16 months and purged after that; a `dateFrom` before the window is rejected rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::CapturesApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  date_from: Date.parse('2013-10-20'), # Date | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window.
  date_to: Date.parse('2013-10-20'), # Date | Inclusive upper bound, widened to 23:59:59 UTC of the named day.
  tracked_query_id: '38400000-8cf0-11bd-b23e-10b96e4ef00d', # String | Only captures of this tracked query. Must belong to the project in the path.
  engines: ['chatgpt'], # Array<String> | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine.
  limit: 56, # Integer | Page size. A larger value is rejected, never silently reduced.
  offset: 56, # Integer | Number of captures to skip before the page starts.
  sort_order: 'asc' # String | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default.
}

begin
  # List captured AI answers
  result = api_instance.list_ai_responses(organization_id, project_id, opts)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling CapturesApi->list_ai_responses: #{e}"
end
```

#### Using the list_ai_responses_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListAiResponses200Response>, Integer, Hash)> list_ai_responses_with_http_info(organization_id, project_id, opts)

```ruby
begin
  # List captured AI answers
  data, status_code, headers = api_instance.list_ai_responses_with_http_info(organization_id, project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListAiResponses200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling CapturesApi->list_ai_responses_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [optional] |
| **date_to** | **Date** | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] |
| **tracked_query_id** | **String** | Only captures of this tracked query. Must belong to the project in the path. | [optional] |
| **engines** | [**Array&lt;String&gt;**](String.md) | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. | [optional] |
| **limit** | **Integer** | Page size. A larger value is rejected, never silently reduced. | [optional][default to 20] |
| **offset** | **Integer** | Number of captures to skip before the page starts. | [optional][default to 0] |
| **sort_order** | **String** | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional][default to &#39;desc&#39;] |

### Return type

[**ListAiResponses200Response**](ListAiResponses200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_search_snapshots

> <ListSearchSnapshots200Response> list_search_snapshots(organization_id, project_id, opts)

List captured search-results pages

Minimum role: viewer. Every organic search page captured for a project, newest first, one page at a time. This is what the rank figures in the analytics operations were computed from: the ranked results as they stood at `capturedAt`, not as they stand now. Read `unresolved` on a result before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector; count the result, do not credit the site. `rating` and `ratingVotes` come from a rich-result star rating when Google showed one and are absent far more often than present; their absence says nothing about the page. There is no `engines` filter because every capture here comes from Google SERP. Captures are kept for 16 months and purged after that; a `dateFrom` before the window is rejected rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::CapturesApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  date_from: Date.parse('2013-10-20'), # Date | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window.
  date_to: Date.parse('2013-10-20'), # Date | Inclusive upper bound, widened to 23:59:59 UTC of the named day.
  tracked_query_id: '38400000-8cf0-11bd-b23e-10b96e4ef00d', # String | Only captures of this tracked query. Must belong to the project in the path.
  limit: 56, # Integer | Page size. A larger value is rejected, never silently reduced.
  offset: 56, # Integer | Number of captures to skip before the page starts.
  sort_order: 'asc' # String | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default.
}

begin
  # List captured search-results pages
  result = api_instance.list_search_snapshots(organization_id, project_id, opts)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling CapturesApi->list_search_snapshots: #{e}"
end
```

#### Using the list_search_snapshots_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListSearchSnapshots200Response>, Integer, Hash)> list_search_snapshots_with_http_info(organization_id, project_id, opts)

```ruby
begin
  # List captured search-results pages
  data, status_code, headers = api_instance.list_search_snapshots_with_http_info(organization_id, project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListSearchSnapshots200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling CapturesApi->list_search_snapshots_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [optional] |
| **date_to** | **Date** | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] |
| **tracked_query_id** | **String** | Only captures of this tracked query. Must belong to the project in the path. | [optional] |
| **limit** | **Integer** | Page size. A larger value is rejected, never silently reduced. | [optional][default to 20] |
| **offset** | **Integer** | Number of captures to skip before the page starts. | [optional][default to 0] |
| **sort_order** | **String** | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional][default to &#39;desc&#39;] |

### Return type

[**ListSearchSnapshots200Response**](ListSearchSnapshots200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_shopping_snapshots

> <ListShoppingSnapshots200Response> list_shopping_snapshots(organization_id, project_id, opts)

List captured shopping-results pages

Minimum role: viewer. Every shopping page captured for a project, newest first, one page at a time: the ranked offers as they stood at `capturedAt`. `price` and `currency` are what the seller showed at that moment — no tax normalisation, no shipping, no conversion — and two offers in one snapshot may carry different currencies, so convert before comparing. `productId` is the marketplace's own identifier for the listing, stable enough to follow one offer across snapshots, and it is not a Mencoro id. Offers turn over far faster than organic results, so two snapshots days apart routinely share none; that is the marketplace behaving normally, not a gap in the capture. Unlike organic results, a shopping offer carries no `unresolved` flag: the capture pipeline does not record one for this surface. Shopping captures are trimmed by the same raw-data purge as AI answers and search pages, so the same retention floor applies: a `dateFrom` before it is refused rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::CapturesApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  date_from: Date.parse('2013-10-20'), # Date | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture.
  date_to: Date.parse('2013-10-20'), # Date | Inclusive upper bound, widened to 23:59:59 UTC of the named day.
  tracked_query_id: '38400000-8cf0-11bd-b23e-10b96e4ef00d', # String | Only captures of this tracked query. Must belong to the project in the path.
  limit: 56, # Integer | Page size. A larger value is rejected, never silently reduced.
  offset: 56, # Integer | Number of captures to skip before the page starts.
  sort_order: 'asc' # String | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default.
}

begin
  # List captured shopping-results pages
  result = api_instance.list_shopping_snapshots(organization_id, project_id, opts)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling CapturesApi->list_shopping_snapshots: #{e}"
end
```

#### Using the list_shopping_snapshots_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListShoppingSnapshots200Response>, Integer, Hash)> list_shopping_snapshots_with_http_info(organization_id, project_id, opts)

```ruby
begin
  # List captured shopping-results pages
  data, status_code, headers = api_instance.list_shopping_snapshots_with_http_info(organization_id, project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListShoppingSnapshots200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling CapturesApi->list_shopping_snapshots_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **date_from** | **Date** | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. | [optional] |
| **date_to** | **Date** | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] |
| **tracked_query_id** | **String** | Only captures of this tracked query. Must belong to the project in the path. | [optional] |
| **limit** | **Integer** | Page size. A larger value is rejected, never silently reduced. | [optional][default to 20] |
| **offset** | **Integer** | Number of captures to skip before the page starts. | [optional][default to 0] |
| **sort_order** | **String** | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional][default to &#39;desc&#39;] |

### Return type

[**ListShoppingSnapshots200Response**](ListShoppingSnapshots200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

