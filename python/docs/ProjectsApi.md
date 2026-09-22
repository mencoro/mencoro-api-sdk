# mencoro.ProjectsApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_project**](ProjectsApi.md#archive_project) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/archive | Archive a project
[**create_competitor**](ProjectsApi.md#create_competitor) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | Add a competitor to a project
[**create_project**](ProjectsApi.md#create_project) | **POST** /api/v1/organizations/{organizationId}/projects | Create a project and the brand monitoring profile its checks run against
[**delete_competitor**](ProjectsApi.md#delete_competitor) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Remove a competitor from a project
[**get_brand_profile**](ProjectsApi.md#get_brand_profile) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Get a project&#39;s brand monitoring profile
[**get_competitor**](ProjectsApi.md#get_competitor) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Get one of a project&#39;s competitors
[**get_project**](ProjectsApi.md#get_project) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId} | Get a project and its brand monitoring configuration
[**list_competitors**](ProjectsApi.md#list_competitors) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | List the competitors tracked by a project
[**list_projects**](ProjectsApi.md#list_projects) | **GET** /api/v1/organizations/{organizationId}/projects | List an organization&#39;s projects
[**list_query_clusters**](ProjectsApi.md#list_query_clusters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | List the keyword clusters of a project
[**restore_project**](ProjectsApi.md#restore_project) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/restore | Restore an archived project
[**update_competitor**](ProjectsApi.md#update_competitor) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Replace a competitor
[**update_project**](ProjectsApi.md#update_project) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId} | Rename a project
[**update_project_brand_profile**](ProjectsApi.md#update_project_brand_profile) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Replace a project&#39;s brand monitoring profile


# **archive_project**
> ProjectDetailResource archive_project(organization_id, project_id, idempotency_key)

Archive a project

Minimum role: manager, in an active organization. Requires the "write" capability. Archiving stops a project from being modified: its name, brand profile and competitors are refused with 409 until it is restored. What is NOT done: nothing is deleted. Tracked queries, captured responses, mentions and every metric already collected stay exactly as they are, and restoreProject brings the project back with all of it. Archiving is recorded as done by the caller, not by an organization cascade, so restoring the organization later will not restore this project — restore it explicitly. This endpoint takes no body, and one carrying fields is refused. Archiving an already archived project answers 409, unless the call is a retry carrying the key that archived it. Send an Idempotency-Key; a retry with the same key returns the recorded answer.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.project_detail_resource import ProjectDetailResource
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | 

    try:
        # Archive a project
        api_response = api_instance.archive_project(organization_id, project_id, idempotency_key)
        print("The response of ProjectsApi->archive_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->archive_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**|  | 

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project in its new state |  -  |
**400** | A body was sent, or the Idempotency-Key was rejected |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The project is already archived, the organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_competitor**
> CompetitorResource create_competitor(organization_id, project_id, idempotency_key, create_competitor_request)

Add a competitor to a project

Minimum role: manager, on an active organization and a project that is not archived. Creates one competitor with the domains and brand names its mentions are matched against. Both lists are required and neither may be empty: a competitor that matches on nothing would never be found in an answer. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading "www." is dropped. Duplicates are collapsed. The id is assigned by the server and cannot be chosen, and neither the auto-generated brand description nor the internal brand monitoring profile id can be set — sending either is refused as an unknown field. Adding a competitor does NOT re-match the answers already captured: it applies to checks from here on. A project whose brand monitoring profile has not been created yet answers 404. An Idempotency-Key header is required.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.competitor_resource import CompetitorResource
from mencoro.models.create_competitor_request import CreateCompetitorRequest
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the organization in the path.
    idempotency_key = 'idempotency_key_example' # str | Unique per attempt. Without it a lost response cannot be retried without risking a second competitor.
    create_competitor_request = mencoro.CreateCompetitorRequest() # CreateCompetitorRequest | 

    try:
        # Add a competitor to a project
        api_response = api_instance.create_competitor(organization_id, project_id, idempotency_key, create_competitor_request)
        print("The response of ProjectsApi->create_competitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_competitor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**| Must belong to the organization in the path. | 
 **idempotency_key** | **str**| Unique per attempt. Without it a lost response cannot be retried without risking a second competitor. | 
 **create_competitor_request** | [**CreateCompetitorRequest**](CreateCompetitorRequest.md)|  | 

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The competitor as stored |  -  |
**400** | The body failed validation, or the Idempotency-Key header is missing |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids, or the project has no brand monitoring profile |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> ProjectDetailResource create_project(organization_id, idempotency_key, create_project_request)

Create a project and the brand monitoring profile its checks run against

Minimum role: manager, in an active organization. Requires the "write" capability. Creates the project, the brand monitoring profile holding the domains and brand names to watch, and one competitor per entry of `competitors`, in a single call. The project id is minted by the server; a caller-supplied id is rejected as an unknown field. What is NOT done: no tracked queries are created, no check is run and no scraping is scheduled — a new project has nothing collected against it until tracked queries are added. Each website entry may be a full URL or a bare domain: a URL is reduced to its host with any leading "www." removed, so "https://www.acme.com/pricing" is stored as "acme.com". Duplicate domains and duplicate brand names are collapsed, exactly as the stored value objects do. Send an Idempotency-Key: a retry with the same key and the same body returns this same project instead of creating a second one.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.create_project_request import CreateProjectRequest
from mencoro.models.project_detail_resource import ProjectDetailResource
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | 
    create_project_request = mencoro.CreateProjectRequest() # CreateProjectRequest | 

    try:
        # Create a project and the brand monitoring profile its checks run against
        api_response = api_instance.create_project(organization_id, idempotency_key, create_project_request)
        print("The response of ProjectsApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **idempotency_key** | **str**|  | 
 **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | 

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created project and its brand monitoring configuration |  -  |
**400** | The body or the Idempotency-Key was rejected; &#x60;details&#x60; names every field at fault |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization the caller can access under this id |  -  |
**409** | The organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_competitor**
> CompetitorResource delete_competitor(organization_id, project_id, competitor_id, idempotency_key)

Remove a competitor from a project

Minimum role: manager, on an active organization and a project that is not archived. Removes the competitor and, asynchronously, every stored mention, search result and shopping result attributed to it, in AI answers and search captures already taken. This is permanent and it changes historical analytics: share of voice and competitor co-occurrence recomputed after the cascade will not include it. A 200 means the competitor is gone; the cascade runs on the event bus and finishes shortly afterwards. The response body is the competitor as it was immediately before removal, because it can no longer be read back. The request takes no body, and sending one is refused. A competitor belonging to another project answers 404, the same answer an unknown id gets. An Idempotency-Key header is required.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.competitor_resource import CompetitorResource
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the organization in the path.
    competitor_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.
    idempotency_key = 'idempotency_key_example' # str | Unique per attempt. A retry carrying the same key is answered from the record instead of running again.

    try:
        # Remove a competitor from a project
        api_response = api_instance.delete_competitor(organization_id, project_id, competitor_id, idempotency_key)
        print("The response of ProjectsApi->delete_competitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_competitor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**| Must belong to the organization in the path. | 
 **competitor_id** | **UUID**| Must belong to the project in the path. | 
 **idempotency_key** | **str**| Unique per attempt. A retry carrying the same key is answered from the record instead of running again. | 

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The competitor as it was immediately before removal |  -  |
**400** | A body was sent, or the Idempotency-Key header is missing |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization, project or competitor the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was reused for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand_profile**
> BrandProfileResource get_brand_profile(organization_id, project_id)

Get a project's brand monitoring profile

Minimum role: viewer. The brand identity every check of this project is matched against: the tracked brand terms, the website domains, and the generated description of what the brand does. A null description means it has not been generated yet — the generator runs asynchronously after the names or domains change — which is not the same as an empty one. An empty brandNames or websiteDomains array means the profile exists and names nothing; a project whose profile has not been created at all answers 404.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.brand_profile_resource import BrandProfileResource
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the organization in the path.

    try:
        # Get a project's brand monitoring profile
        api_response = api_instance.get_brand_profile(organization_id, project_id)
        print("The response of ProjectsApi->get_brand_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_brand_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**| Must belong to the organization in the path. | 

### Return type

[**BrandProfileResource**](BrandProfileResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project&#39;s brand monitoring profile |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization or project the caller can access under these ids, or the project has no brand profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_competitor**
> CompetitorResource get_competitor(organization_id, project_id, competitor_id)

Get one of a project's competitors

Minimum role: viewer. Returns a single competitor of the project, the same projection the competitor listing returns for each of its rows. A competitor belonging to another project answers 404, the same answer an unknown id and a malformed one get, so the API never confirms that a competitor the caller cannot reach exists. A project whose brand monitoring profile has not been created yet has no competitors at all and answers 404 for any competitor id.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.competitor_resource import CompetitorResource
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the organization in the path.
    competitor_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.

    try:
        # Get one of a project's competitors
        api_response = api_instance.get_competitor(organization_id, project_id, competitor_id)
        print("The response of ProjectsApi->get_competitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_competitor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**| Must belong to the organization in the path. | 
 **competitor_id** | **UUID**| Must belong to the project in the path. | 

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The competitor |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization, project or competitor the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectDetailResource get_project(organization_id, project_id)

Get a project and its brand monitoring configuration

Minimum role: viewer. Returns the project together with the domains and brand names it is monitored for and the competitors it is measured against. A project that exists but belongs to another organization answers 404, never 403. A project that has been created but not yet configured for brand monitoring reports empty `websiteDomains`, `brandNames` and `competitors`. Headline metrics are not part of this response: use `listProjects` for the per-project figures, or `getProjectMetrics` for a window.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.project_detail_resource import ProjectDetailResource
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a project and its brand monitoring configuration
        api_response = api_instance.get_project(organization_id, project_id)
        print("The response of ProjectsApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project and its brand monitoring configuration |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller can access under this id, or no project with this id inside it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_competitors**
> ListCompetitors200Response list_competitors(organization_id, project_id, limit=limit, offset=offset, sort_order=sort_order)

List the competitors tracked by a project

Minimum role: viewer. The competitors configured on the project, one page at a time, with the website domains and brand names each one is matched against. `total` counts every competitor of the project, not the size of this page, so a project with more than `limit` competitors needs `offset` to read them all. Ordering is by id, which for a UUID v7 is roughly creation order, and `sortOrder` chooses its direction; there is no other sort key and no text search, and sending `sortBy` or `search` is rejected rather than ignored. A project whose brand monitoring profile has not been created yet answers 200 with an empty collection, which means "nothing configured yet" rather than "no competitors found". Internal fields the pipeline writes — the auto-generated brand description used by the mention classifier, and the internal brand monitoring profile id — are not part of this contract.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.list_competitors200_response import ListCompetitors200Response
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    limit = 20 # int | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
    offset = 0 # int | Number of competitors to skip before the page starts. (optional) (default to 0)
    sort_order = 'asc' # str | Direction of the id ordering. An unknown value is rejected, not replaced by the default. (optional) (default to 'asc')

    try:
        # List the competitors tracked by a project
        api_response = api_instance.list_competitors(organization_id, project_id, limit=limit, offset=offset, sort_order=sort_order)
        print("The response of ProjectsApi->list_competitors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->list_competitors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20]
 **offset** | **int**| Number of competitors to skip before the page starts. | [optional] [default to 0]
 **sort_order** | **str**| Direction of the id ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;asc&#39;]

### Return type

[**ListCompetitors200Response**](ListCompetitors200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project&#39;s competitors |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ListProjects200Response list_projects(organization_id, limit=limit, offset=offset, search=search, status=status, sort_by=sort_by, sort_order=sort_order)

List an organization's projects

Minimum role: viewer. Metrics come from the same read model the application uses, so the figures match what the product shows. A null metric means "not known yet", never zero.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.list_projects200_response import ListProjects200Response
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    limit = 20 # int | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
    offset = 0 # int | Rows to skip before the page starts. Page by advancing it in steps of `limit` until it reaches `total`. (optional) (default to 0)
    search = 'search_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    sort_by = 'createdAt' # str |  (optional) (default to 'createdAt')
    sort_order = 'desc' # str |  (optional) (default to 'desc')

    try:
        # List an organization's projects
        api_response = api_instance.list_projects(organization_id, limit=limit, offset=offset, search=search, status=status, sort_by=sort_by, sort_order=sort_order)
        print("The response of ProjectsApi->list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->list_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20]
 **offset** | **int**| Rows to skip before the page starts. Page by advancing it in steps of &#x60;limit&#x60; until it reaches &#x60;total&#x60;. | [optional] [default to 0]
 **search** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;createdAt&#39;]
 **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**ListProjects200Response**](ListProjects200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization&#39;s projects |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_query_clusters**
> ListQueryClusters200Response list_query_clusters(organization_id, project_id, limit=limit, offset=offset, sort_order=sort_order)

List the keyword clusters of a project

Minimum role: viewer. The keyword clusters configured on a project, one page at a time. Each cluster id is exactly what the analytics operations accept in their queryClusterIds filter — pass the id, never the name. Names are unique within a project and are stored lower-cased, so the listing is ordered by name with no ties and paging over it neither repeats nor skips a cluster. `total` counts every cluster in the project, not the size of the page returned. A cluster carries no metrics of its own and no membership count: for the tracked queries inside a cluster, filter the tracked-query operations by its id. An empty list means the project has no clusters configured, which is not an error and is not a statement about whether any data has been collected.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.list_query_clusters200_response import ListQueryClusters200Response
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    limit = 20 # int | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
    offset = 0 # int | Number of clusters to skip before the page starts. (optional) (default to 0)
    sort_order = 'asc' # str | Direction of the name ordering. An unknown value is rejected, not replaced by the default. (optional) (default to 'asc')

    try:
        # List the keyword clusters of a project
        api_response = api_instance.list_query_clusters(organization_id, project_id, limit=limit, offset=offset, sort_order=sort_order)
        print("The response of ProjectsApi->list_query_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->list_query_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20]
 **offset** | **int**| Number of clusters to skip before the page starts. | [optional] [default to 0]
 **sort_order** | **str**| Direction of the name ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;asc&#39;]

### Return type

[**ListQueryClusters200Response**](ListQueryClusters200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of the project&#39;s keyword clusters and the total in the project |  -  |
**400** | A pagination or ordering parameter was rejected; the details name the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_project**
> ProjectDetailResource restore_project(organization_id, project_id, idempotency_key)

Restore an archived project

Minimum role: manager, in an active organization. Requires the "write" capability. Brings an archived project back to active, with every tracked query, capture and metric it had when it was archived. What is NOT done: no check is run and no scraping is scheduled as a result — collection resumes on the project's own schedule. Restoring clears the record of who archived the project, so a project restored here is treated as an ordinary active project by any later organization archive. A project archived because its organization was archived cannot be restored on its own: restore the organization, which restores them all. Restoring a project that is already active answers 409, unless the call is a retry carrying the key that restored it. This endpoint takes no body, and one carrying fields is refused. Send an Idempotency-Key; a retry with the same key returns the recorded answer.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.project_detail_resource import ProjectDetailResource
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | 

    try:
        # Restore an archived project
        api_response = api_instance.restore_project(organization_id, project_id, idempotency_key)
        print("The response of ProjectsApi->restore_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->restore_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**|  | 

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project in its new state |  -  |
**400** | A body was sent, or the Idempotency-Key was rejected |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The project is not archived, the organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_competitor**
> CompetitorResource update_competitor(organization_id, project_id, competitor_id, idempotency_key, create_competitor_request)

Replace a competitor

Minimum role: manager, on an active organization and a project that is not archived. Replaces the competitor's name, domains and brand names: the lists sent become the lists stored, so a term left out is removed. Both lists are required and neither may be empty — a competitor that matches on nothing would never be found in an answer. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading "www." is dropped. Duplicates are collapsed. The auto-generated brand description cannot be set, and sending it is refused as an unknown field. Changing the matching rules does NOT re-match the answers already captured: it applies to checks from here on. A competitor belonging to another project answers 404, the same answer an unknown id gets. An Idempotency-Key header is required.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.competitor_resource import CompetitorResource
from mencoro.models.create_competitor_request import CreateCompetitorRequest
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the organization in the path.
    competitor_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.
    idempotency_key = 'idempotency_key_example' # str | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
    create_competitor_request = mencoro.CreateCompetitorRequest() # CreateCompetitorRequest | 

    try:
        # Replace a competitor
        api_response = api_instance.update_competitor(organization_id, project_id, competitor_id, idempotency_key, create_competitor_request)
        print("The response of ProjectsApi->update_competitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_competitor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**| Must belong to the organization in the path. | 
 **competitor_id** | **UUID**| Must belong to the project in the path. | 
 **idempotency_key** | **str**| Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. | 
 **create_competitor_request** | [**CreateCompetitorRequest**](CreateCompetitorRequest.md)|  | 

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The competitor as stored |  -  |
**400** | The body failed validation, or the Idempotency-Key header is missing |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization, project or competitor the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> ProjectDetailResource update_project(organization_id, project_id, idempotency_key, update_project_request)

Rename a project

Minimum role: manager, in an active organization. Requires the "write" capability. `name` is the only writable field and it is required. What is NOT done: the monitored domains and brand names are not touched (use updateProjectBrandProfile) and competitors are not touched, added or removed (use the competitor endpoints). Sending `websiteDomains`, `brandNames` or `competitors` here is refused with the field named, never applied in part and never ignored. Renaming a project changes nothing about the data already collected against it. A project that belongs to another organization answers 404, never 403. An archived project answers 409: restore it first — unless the call is a retry carrying the key of a rename that already succeeded, which is answered from the record whatever the project's state is now. Send an Idempotency-Key; a retry with the same key and body returns the recorded answer.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.project_detail_resource import ProjectDetailResource
from mencoro.models.update_project_request import UpdateProjectRequest
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | 
    update_project_request = mencoro.UpdateProjectRequest() # UpdateProjectRequest | 

    try:
        # Rename a project
        api_response = api_instance.update_project(organization_id, project_id, idempotency_key, update_project_request)
        print("The response of ProjectsApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**|  | 
 **update_project_request** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | 

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project in its new state |  -  |
**400** | The body or the Idempotency-Key was rejected; &#x60;details&#x60; names every field at fault |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The project is archived, the organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_brand_profile**
> BrandProfileResource update_project_brand_profile(organization_id, project_id, idempotency_key, update_project_brand_profile_request)

Replace a project's brand monitoring profile

Minimum role: manager, on an active organization and a project that is not archived. Replaces the brand terms and website domains every check of this project is matched against: the lists sent become the lists stored, so a term left out is removed. Both lists are required and neither may be empty — a project must keep at least one brand name and one domain to match anything. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading "www." is dropped, which is the form the profile is read back in. Duplicates, including two URLs that reduce to the same host, are collapsed. This operation does NOT touch the project name or its competitors, which are separate resources, and it does not regenerate the brand description: that runs asynchronously afterwards, so the description in the response is the one stored at the time of the write. An Idempotency-Key header is required.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.brand_profile_resource import BrandProfileResource
from mencoro.models.update_project_brand_profile_request import UpdateProjectBrandProfileRequest
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
    api_instance = mencoro.ProjectsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the organization in the path.
    idempotency_key = 'idempotency_key_example' # str | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
    update_project_brand_profile_request = mencoro.UpdateProjectBrandProfileRequest() # UpdateProjectBrandProfileRequest | 

    try:
        # Replace a project's brand monitoring profile
        api_response = api_instance.update_project_brand_profile(organization_id, project_id, idempotency_key, update_project_brand_profile_request)
        print("The response of ProjectsApi->update_project_brand_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project_brand_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**| Must belong to the organization in the path. | 
 **idempotency_key** | **str**| Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. | 
 **update_project_brand_profile_request** | [**UpdateProjectBrandProfileRequest**](UpdateProjectBrandProfileRequest.md)|  | 

### Return type

[**BrandProfileResource**](BrandProfileResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The profile as stored |  -  |
**400** | The body failed validation, or the Idempotency-Key header is missing |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids, or the project has no brand profile |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

