# Mencoro\Api\CapturesApi

Captures

All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listAiResponses()**](CapturesApi.md#listAiResponses) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/ai-responses | List captured AI answers |
| [**listSearchSnapshots()**](CapturesApi.md#listSearchSnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/search-snapshots | List captured search-results pages |
| [**listShoppingSnapshots()**](CapturesApi.md#listShoppingSnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/shopping-snapshots | List captured shopping-results pages |


## `listAiResponses()`

```php
listAiResponses($organization_id, $project_id, $date_from, $date_to, $tracked_query_id, $engines, $limit, $offset, $sort_order): \Mencoro\Api\Model\ListAiResponses200Response
```

List captured AI answers

Minimum role: viewer. Every AI answer captured for a project, newest first, one page at a time. This is the evidence under the analytics operations: the full answer text and the sources the engine cited, exactly as captured. Read `unresolved` on a citation before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector, not to the publisher; count the citation, do not credit the site. `passIndex` and `passCount` describe multi-pass sampling: rows sharing a `trackedQueryId` and `capturedAt` are passes of one run, not duplicates, so aggregating across them without dividing by `passCount` double-counts that run. `responseText` is the whole answer, so a page of 100 is a large response — lower `limit` rather than paging blind. Captures are kept for 16 months and purged after that; a `dateFrom` before the window is rejected rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\CapturesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive upper bound, widened to 23:59:59 UTC of the named day.
$tracked_query_id = 'tracked_query_id_example'; // string | Only captures of this tracked query. Must belong to the project in the path.
$engines = array('engines_example'); // string[] | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine.
$limit = 20; // int | Page size. A larger value is rejected, never silently reduced.
$offset = 0; // int | Number of captures to skip before the page starts.
$sort_order = 'desc'; // string | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default.

try {
    $result = $apiInstance->listAiResponses($organization_id, $project_id, $date_from, $date_to, $tracked_query_id, $engines, $limit, $offset, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CapturesApi->listAiResponses: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [optional] |
| **date_to** | **\DateTime**| Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] |
| **tracked_query_id** | **string**| Only captures of this tracked query. Must belong to the project in the path. | [optional] |
| **engines** | [**string[]**](../Model/string.md)| Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. | [optional] |
| **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int**| Number of captures to skip before the page starts. | [optional] [default to 0] |
| **sort_order** | **string**| Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;desc&#39;] |

### Return type

[**\Mencoro\Api\Model\ListAiResponses200Response**](../Model/ListAiResponses200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listSearchSnapshots()`

```php
listSearchSnapshots($organization_id, $project_id, $date_from, $date_to, $tracked_query_id, $limit, $offset, $sort_order): \Mencoro\Api\Model\ListSearchSnapshots200Response
```

List captured search-results pages

Minimum role: viewer. Every organic search page captured for a project, newest first, one page at a time. This is what the rank figures in the analytics operations were computed from: the ranked results as they stood at `capturedAt`, not as they stand now. Read `unresolved` on a result before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector; count the result, do not credit the site. `rating` and `ratingVotes` come from a rich-result star rating when Google showed one and are absent far more often than present; their absence says nothing about the page. There is no `engines` filter because every capture here comes from Google SERP. Captures are kept for 16 months and purged after that; a `dateFrom` before the window is rejected rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\CapturesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive upper bound, widened to 23:59:59 UTC of the named day.
$tracked_query_id = 'tracked_query_id_example'; // string | Only captures of this tracked query. Must belong to the project in the path.
$limit = 20; // int | Page size. A larger value is rejected, never silently reduced.
$offset = 0; // int | Number of captures to skip before the page starts.
$sort_order = 'desc'; // string | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default.

try {
    $result = $apiInstance->listSearchSnapshots($organization_id, $project_id, $date_from, $date_to, $tracked_query_id, $limit, $offset, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CapturesApi->listSearchSnapshots: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [optional] |
| **date_to** | **\DateTime**| Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] |
| **tracked_query_id** | **string**| Only captures of this tracked query. Must belong to the project in the path. | [optional] |
| **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int**| Number of captures to skip before the page starts. | [optional] [default to 0] |
| **sort_order** | **string**| Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;desc&#39;] |

### Return type

[**\Mencoro\Api\Model\ListSearchSnapshots200Response**](../Model/ListSearchSnapshots200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listShoppingSnapshots()`

```php
listShoppingSnapshots($organization_id, $project_id, $date_from, $date_to, $tracked_query_id, $limit, $offset, $sort_order): \Mencoro\Api\Model\ListShoppingSnapshots200Response
```

List captured shopping-results pages

Minimum role: viewer. Every shopping page captured for a project, newest first, one page at a time: the ranked offers as they stood at `capturedAt`. `price` and `currency` are what the seller showed at that moment — no tax normalisation, no shipping, no conversion — and two offers in one snapshot may carry different currencies, so convert before comparing. `productId` is the marketplace's own identifier for the listing, stable enough to follow one offer across snapshots, and it is not a Mencoro id. Offers turn over far faster than organic results, so two snapshots days apart routinely share none; that is the marketplace behaving normally, not a gap in the capture. Unlike organic results, a shopping offer carries no `unresolved` flag: the capture pipeline does not record one for this surface. Shopping captures are trimmed by the same raw-data purge as AI answers and search pages, so the same retention floor applies: a `dateFrom` before it is refused rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\CapturesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$date_from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture.
$date_to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive upper bound, widened to 23:59:59 UTC of the named day.
$tracked_query_id = 'tracked_query_id_example'; // string | Only captures of this tracked query. Must belong to the project in the path.
$limit = 20; // int | Page size. A larger value is rejected, never silently reduced.
$offset = 0; // int | Number of captures to skip before the page starts.
$sort_order = 'desc'; // string | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default.

try {
    $result = $apiInstance->listShoppingSnapshots($organization_id, $project_id, $date_from, $date_to, $tracked_query_id, $limit, $offset, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CapturesApi->listShoppingSnapshots: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **date_from** | **\DateTime**| Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. | [optional] |
| **date_to** | **\DateTime**| Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] |
| **tracked_query_id** | **string**| Only captures of this tracked query. Must belong to the project in the path. | [optional] |
| **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int**| Number of captures to skip before the page starts. | [optional] [default to 0] |
| **sort_order** | **string**| Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;desc&#39;] |

### Return type

[**\Mencoro\Api\Model\ListShoppingSnapshots200Response**](../Model/ListShoppingSnapshots200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
