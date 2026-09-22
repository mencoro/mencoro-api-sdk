# mencoro.CapturesApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_ai_responses**](CapturesApi.md#list_ai_responses) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/ai-responses | List captured AI answers
[**list_search_snapshots**](CapturesApi.md#list_search_snapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/search-snapshots | List captured search-results pages
[**list_shopping_snapshots**](CapturesApi.md#list_shopping_snapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/shopping-snapshots | List captured shopping-results pages


# **list_ai_responses**
> ListAiResponses200Response list_ai_responses(organization_id, project_id, date_from=date_from, date_to=date_to, tracked_query_id=tracked_query_id, engines=engines, limit=limit, offset=offset, sort_order=sort_order)

List captured AI answers

Minimum role: viewer. Every AI answer captured for a project, newest first, one page at a time. This is the evidence under the analytics operations: the full answer text and the sources the engine cited, exactly as captured. Read `unresolved` on a citation before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector, not to the publisher; count the citation, do not credit the site. `passIndex` and `passCount` describe multi-pass sampling: rows sharing a `trackedQueryId` and `capturedAt` are passes of one run, not duplicates, so aggregating across them without dividing by `passCount` double-counts that run. `responseText` is the whole answer, so a page of 100 is a large response — lower `limit` rather than paging blind. Captures are kept for 16 months and purged after that; a `dateFrom` before the window is rejected rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.list_ai_responses200_response import ListAiResponses200Response
from mencoro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mencoro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mencoro.Configuration(
    host = "https://api.mencoro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = mencoro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mencoro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mencoro.CapturesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    date_from = '2013-10-20' # date | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. (optional)
    date_to = '2013-10-20' # date | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional)
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Only captures of this tracked query. Must belong to the project in the path. (optional)
    engines = ['engines_example'] # List[str] | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. (optional)
    limit = 20 # int | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
    offset = 0 # int | Number of captures to skip before the page starts. (optional) (default to 0)
    sort_order = 'desc' # str | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional) (default to 'desc')

    try:
        # List captured AI answers
        api_response = api_instance.list_ai_responses(organization_id, project_id, date_from=date_from, date_to=date_to, tracked_query_id=tracked_query_id, engines=engines, limit=limit, offset=offset, sort_order=sort_order)
        print("The response of CapturesApi->list_ai_responses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapturesApi->list_ai_responses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **date_from** | **date**| Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [optional] 
 **date_to** | **date**| Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] 
 **tracked_query_id** | **UUID**| Only captures of this tracked query. Must belong to the project in the path. | [optional] 
 **engines** | [**List[str]**](str.md)| Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. | [optional] 
 **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20]
 **offset** | **int**| Number of captures to skip before the page starts. | [optional] [default to 0]
 **sort_order** | **str**| Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;desc&#39;]

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
**200** | A page of captured AI answers and the total the filter matches |  -  |
**400** | A filter, pagination or ordering parameter was rejected; the details name the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_search_snapshots**
> ListSearchSnapshots200Response list_search_snapshots(organization_id, project_id, date_from=date_from, date_to=date_to, tracked_query_id=tracked_query_id, limit=limit, offset=offset, sort_order=sort_order)

List captured search-results pages

Minimum role: viewer. Every organic search page captured for a project, newest first, one page at a time. This is what the rank figures in the analytics operations were computed from: the ranked results as they stood at `capturedAt`, not as they stand now. Read `unresolved` on a result before attributing its domain — a true value means the URL is still a redirector and the domain belongs to that redirector; count the result, do not credit the site. `rating` and `ratingVotes` come from a rich-result star rating when Google showed one and are absent far more often than present; their absence says nothing about the page. There is no `engines` filter because every capture here comes from Google SERP. Captures are kept for 16 months and purged after that; a `dateFrom` before the window is rejected rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.list_search_snapshots200_response import ListSearchSnapshots200Response
from mencoro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mencoro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mencoro.Configuration(
    host = "https://api.mencoro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = mencoro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mencoro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mencoro.CapturesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    date_from = '2013-10-20' # date | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. (optional)
    date_to = '2013-10-20' # date | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional)
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Only captures of this tracked query. Must belong to the project in the path. (optional)
    limit = 20 # int | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
    offset = 0 # int | Number of captures to skip before the page starts. (optional) (default to 0)
    sort_order = 'desc' # str | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional) (default to 'desc')

    try:
        # List captured search-results pages
        api_response = api_instance.list_search_snapshots(organization_id, project_id, date_from=date_from, date_to=date_to, tracked_query_id=tracked_query_id, limit=limit, offset=offset, sort_order=sort_order)
        print("The response of CapturesApi->list_search_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapturesApi->list_search_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **date_from** | **date**| Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | [optional] 
 **date_to** | **date**| Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] 
 **tracked_query_id** | **UUID**| Only captures of this tracked query. Must belong to the project in the path. | [optional] 
 **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20]
 **offset** | **int**| Number of captures to skip before the page starts. | [optional] [default to 0]
 **sort_order** | **str**| Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;desc&#39;]

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
**200** | A page of captured search-results pages and the total the filter matches |  -  |
**400** | A filter, pagination or ordering parameter was rejected; the details name the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shopping_snapshots**
> ListShoppingSnapshots200Response list_shopping_snapshots(organization_id, project_id, date_from=date_from, date_to=date_to, tracked_query_id=tracked_query_id, limit=limit, offset=offset, sort_order=sort_order)

List captured shopping-results pages

Minimum role: viewer. Every shopping page captured for a project, newest first, one page at a time: the ranked offers as they stood at `capturedAt`. `price` and `currency` are what the seller showed at that moment — no tax normalisation, no shipping, no conversion — and two offers in one snapshot may carry different currencies, so convert before comparing. `productId` is the marketplace's own identifier for the listing, stable enough to follow one offer across snapshots, and it is not a Mencoro id. Offers turn over far faster than organic results, so two snapshots days apart routinely share none; that is the marketplace behaving normally, not a gap in the capture. Unlike organic results, a shopping offer carries no `unresolved` flag: the capture pipeline does not record one for this surface. Shopping captures are trimmed by the same raw-data purge as AI answers and search pages, so the same retention floor applies: a `dateFrom` before it is refused rather than answered with an empty page. `total` counts every capture the filter matches, not the size of this page.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.list_shopping_snapshots200_response import ListShoppingSnapshots200Response
from mencoro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mencoro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mencoro.Configuration(
    host = "https://api.mencoro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = mencoro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mencoro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mencoro.CapturesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    date_from = '2013-10-20' # date | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. (optional)
    date_to = '2013-10-20' # date | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional)
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Only captures of this tracked query. Must belong to the project in the path. (optional)
    limit = 20 # int | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
    offset = 0 # int | Number of captures to skip before the page starts. (optional) (default to 0)
    sort_order = 'desc' # str | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional) (default to 'desc')

    try:
        # List captured shopping-results pages
        api_response = api_instance.list_shopping_snapshots(organization_id, project_id, date_from=date_from, date_to=date_to, tracked_query_id=tracked_query_id, limit=limit, offset=offset, sort_order=sort_order)
        print("The response of CapturesApi->list_shopping_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapturesApi->list_shopping_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **date_from** | **date**| Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. | [optional] 
 **date_to** | **date**| Inclusive upper bound, widened to 23:59:59 UTC of the named day. | [optional] 
 **tracked_query_id** | **UUID**| Only captures of this tracked query. Must belong to the project in the path. | [optional] 
 **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20]
 **offset** | **int**| Number of captures to skip before the page starts. | [optional] [default to 0]
 **sort_order** | **str**| Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;desc&#39;]

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
**200** | A page of captured shopping-results pages and the total the filter matches |  -  |
**400** | A filter, pagination or ordering parameter was rejected; the details name the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

