# CapturesApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listAiResponses**](CapturesApi.md#listairesponses) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/ai-responses | List captured AI answers |
| [**listSearchSnapshots**](CapturesApi.md#listsearchsnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/search-snapshots | List captured search-results pages |
| [**listShoppingSnapshots**](CapturesApi.md#listshoppingsnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/shopping-snapshots | List captured shopping-results pages |



## listAiResponses

> ListAiResponses200Response listAiResponses(organizationId, projectId, dateFrom, dateTo, trackedQueryId, engines, limit, offset, sortOrder)

List captured AI answers

Minimum role: viewer. Every AI answer captured for a project, newest first, one page at a time. This is the evidence under the analytics operations: the full answer text and the sources the engine cited, exactly as captured. Read &#x60;unresolved&#x60; on a citation before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector, not to the publisher; count the citation, do not credit the site. &#x60;passIndex&#x60; and &#x60;passCount&#x60; describe multi-pass sampling: rows sharing a &#x60;trackedQueryId&#x60; and &#x60;capturedAt&#x60; are passes of one run, not duplicates, so aggregating across them without dividing by &#x60;passCount&#x60; double-counts that run. &#x60;responseText&#x60; is the whole answer, so a page of 100 is a large response — lower &#x60;limit&#x60; rather than paging blind. Captures are kept for 16 months and purged after that; a &#x60;dateFrom&#x60; before the window is rejected rather than answered with an empty page. &#x60;total&#x60; counts every capture the filter matches, not the size of this page.

### Example

```ts
import {
  Configuration,
  CapturesApi,
} from '@mencoro/api';
import type { ListAiResponsesRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CapturesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. (optional)
    dateFrom: 2013-10-20,
    // Date | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional)
    dateTo: 2013-10-20,
    // string | Only captures of this tracked query. Must belong to the project in the path. (optional)
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Array<'chatgpt' | 'perplexity' | 'google_ai_overview' | 'google_ai_mode'> | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. (optional)
    engines: ...,
    // number | Page size. A larger value is rejected, never silently reduced. (optional)
    limit: 56,
    // number | Number of captures to skip before the page starts. (optional)
    offset: 56,
    // 'asc' | 'desc' | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional)
    sortOrder: sortOrder_example,
  } satisfies ListAiResponsesRequest;

  try {
    const data = await api.listAiResponses(body);
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
| **dateFrom** | `Date` | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [Optional] [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [Optional] [Defaults to `undefined`] |
| **trackedQueryId** | `string` | Only captures of this tracked query. Must belong to the project in the path. | [Optional] [Defaults to `undefined`] |
| **engines** | `chatgpt`, `perplexity`, `google_ai_overview`, `google_ai_mode` | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. | [Optional] [Enum: chatgpt, perplexity, google_ai_overview, google_ai_mode] |
| **limit** | `number` | Page size. A larger value is rejected, never silently reduced. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Number of captures to skip before the page starts. | [Optional] [Defaults to `0`] |
| **sortOrder** | `asc`, `desc` | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**ListAiResponses200Response**](ListAiResponses200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of captured AI answers and the total the filter matches |  -  |
| **400** | A filter, pagination or ordering parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSearchSnapshots

> ListSearchSnapshots200Response listSearchSnapshots(organizationId, projectId, dateFrom, dateTo, trackedQueryId, limit, offset, sortOrder)

List captured search-results pages

Minimum role: viewer. Every organic search page captured for a project, newest first, one page at a time. This is what the rank figures in the analytics operations were computed from: the ranked results as they stood at &#x60;capturedAt&#x60;, not as they stand now. Read &#x60;unresolved&#x60; on a result before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector; count the result, do not credit the site. &#x60;rating&#x60; and &#x60;ratingVotes&#x60; come from a rich-result star rating when Google showed one and are absent far more often than present; their absence says nothing about the page. There is no &#x60;engines&#x60; filter because every capture here comes from Google SERP. Captures are kept for 16 months and purged after that; a &#x60;dateFrom&#x60; before the window is rejected rather than answered with an empty page. &#x60;total&#x60; counts every capture the filter matches, not the size of this page.

### Example

```ts
import {
  Configuration,
  CapturesApi,
} from '@mencoro/api';
import type { ListSearchSnapshotsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CapturesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. (optional)
    dateFrom: 2013-10-20,
    // Date | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional)
    dateTo: 2013-10-20,
    // string | Only captures of this tracked query. Must belong to the project in the path. (optional)
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Page size. A larger value is rejected, never silently reduced. (optional)
    limit: 56,
    // number | Number of captures to skip before the page starts. (optional)
    offset: 56,
    // 'asc' | 'desc' | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional)
    sortOrder: sortOrder_example,
  } satisfies ListSearchSnapshotsRequest;

  try {
    const data = await api.listSearchSnapshots(body);
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
| **dateFrom** | `Date` | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [Optional] [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [Optional] [Defaults to `undefined`] |
| **trackedQueryId** | `string` | Only captures of this tracked query. Must belong to the project in the path. | [Optional] [Defaults to `undefined`] |
| **limit** | `number` | Page size. A larger value is rejected, never silently reduced. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Number of captures to skip before the page starts. | [Optional] [Defaults to `0`] |
| **sortOrder** | `asc`, `desc` | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**ListSearchSnapshots200Response**](ListSearchSnapshots200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of captured search-results pages and the total the filter matches |  -  |
| **400** | A filter, pagination or ordering parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listShoppingSnapshots

> ListShoppingSnapshots200Response listShoppingSnapshots(organizationId, projectId, dateFrom, dateTo, trackedQueryId, limit, offset, sortOrder)

List captured shopping-results pages

Minimum role: viewer. Every shopping page captured for a project, newest first, one page at a time: the ranked offers as they stood at &#x60;capturedAt&#x60;. &#x60;price&#x60; and &#x60;currency&#x60; are what the seller showed at that moment — no tax normalisation, no shipping, no conversion — and two offers in one snapshot may carry different currencies, so convert before comparing. &#x60;productId&#x60; is the marketplace\&#39;s own identifier for the listing, stable enough to follow one offer across snapshots, and it is not a Mencoro id. Offers turn over far faster than organic results, so two snapshots days apart routinely share none; that is the marketplace behaving normally, not a gap in the capture. Unlike organic results, a shopping offer carries no &#x60;unresolved&#x60; flag: the capture pipeline does not record one for this surface. Shopping captures are trimmed by the same raw-data purge as AI answers and search pages, so the same retention floor applies: a &#x60;dateFrom&#x60; before it is refused rather than answered with an empty page. &#x60;total&#x60; counts every capture the filter matches, not the size of this page.

### Example

```ts
import {
  Configuration,
  CapturesApi,
} from '@mencoro/api';
import type { ListShoppingSnapshotsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new CapturesApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // Date | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. (optional)
    dateFrom: 2013-10-20,
    // Date | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional)
    dateTo: 2013-10-20,
    // string | Only captures of this tracked query. Must belong to the project in the path. (optional)
    trackedQueryId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Page size. A larger value is rejected, never silently reduced. (optional)
    limit: 56,
    // number | Number of captures to skip before the page starts. (optional)
    offset: 56,
    // 'asc' | 'desc' | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional)
    sortOrder: sortOrder_example,
  } satisfies ListShoppingSnapshotsRequest;

  try {
    const data = await api.listShoppingSnapshots(body);
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
| **dateFrom** | `Date` | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. | [Optional] [Defaults to `undefined`] |
| **dateTo** | `Date` | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [Optional] [Defaults to `undefined`] |
| **trackedQueryId** | `string` | Only captures of this tracked query. Must belong to the project in the path. | [Optional] [Defaults to `undefined`] |
| **limit** | `number` | Page size. A larger value is rejected, never silently reduced. | [Optional] [Defaults to `20`] |
| **offset** | `number` | Number of captures to skip before the page starts. | [Optional] [Defaults to `0`] |
| **sortOrder** | `asc`, `desc` | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**ListShoppingSnapshots200Response**](ListShoppingSnapshots200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of captured shopping-results pages and the total the filter matches |  -  |
| **400** | A filter, pagination or ordering parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

