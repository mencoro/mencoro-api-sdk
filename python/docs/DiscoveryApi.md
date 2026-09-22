# mencoro.DiscoveryApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_brand_discovery_job**](DiscoveryApi.md#start_brand_discovery_job) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/brands | Start a brand discovery job for a project
[**start_brand_name_suggestion_job**](DiscoveryApi.md#start_brand_name_suggestion_job) | **POST** /api/v1/organizations/{organizationId}/brand-name-suggestions | Start a brand-name alias suggestion job
[**start_keyword_discovery_job**](DiscoveryApi.md#start_keyword_discovery_job) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/keywords | Start a keyword discovery job for a project
[**start_prompt_discovery_job**](DiscoveryApi.md#start_prompt_discovery_job) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/prompts | Start a geo prompt discovery job for a project


# **start_brand_discovery_job**
> AcceptedJobResource start_brand_discovery_job(organization_id, project_id, idempotency_key, start_brand_discovery_job_request=start_brand_discovery_job_request)

Start a brand discovery job for a project

Minimum role: manager. Starts background discovery of the brands and competitors around a project and answers 202 with the job to poll; it never returns brands inline. The job PROPOSES names: it creates and updates nothing, so neither the brand profile nor the competitor list changes because this endpoint was called. The organization must be active. Unlike keyword and prompt discovery this operation does not require an entitled subscription, matching the application behaviour it mirrors. Ten starts per minute per organization, counted across every key of every member and shared with the same operation in the Mencoro app; a retry carrying an Idempotency-Key already answered is served from the record and does not count. A project whose brand monitoring profile has not been created yet is still accepted and still billed: the job runs grounded on the project name alone, with no website domains, brand names or competitors to work from, and completes normally. Configure the brand profile first if you want the discovery grounded.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.accepted_job_resource import AcceptedJobResource
from mencoro.models.start_brand_discovery_job_request import StartBrandDiscoveryJobRequest
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
    api_instance = mencoro.DiscoveryApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the organization in the path.
    idempotency_key = 'idempotency_key_example' # str | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    start_brand_discovery_job_request = mencoro.StartBrandDiscoveryJobRequest() # StartBrandDiscoveryJobRequest |  (optional)

    try:
        # Start a brand discovery job for a project
        api_response = api_instance.start_brand_discovery_job(organization_id, project_id, idempotency_key, start_brand_discovery_job_request=start_brand_discovery_job_request)
        print("The response of DiscoveryApi->start_brand_discovery_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->start_brand_discovery_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**| Must belong to the organization in the path. | 
 **idempotency_key** | **str**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | 
 **start_brand_discovery_job_request** | [**StartBrandDiscoveryJobRequest**](StartBrandDiscoveryJobRequest.md)|  | [optional] 

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The discovery job was accepted |  -  |
**400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
**429** | The organization exceeded ten brand discovery starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_brand_name_suggestion_job**
> AcceptedJobResource start_brand_name_suggestion_job(organization_id, idempotency_key, start_brand_name_suggestion_job_request)

Start a brand-name alias suggestion job

Minimum role: manager. Starts a background, web-search-grounded job that suggests alias spellings for one entity - a brand, a project or a competitor - described entirely by the body, and answers 202 with the job to poll; it never returns suggestions inline. The entity need not exist: nothing is looked up, nothing is attached and nothing is saved, so the suggestions are the caller's to apply. Names sent in `enteredBrandNames` are excluded from the result. The organization must be active; no subscription is required, matching the application behaviour this mirrors. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.accepted_job_resource import AcceptedJobResource
from mencoro.models.start_brand_name_suggestion_job_request import StartBrandNameSuggestionJobRequest
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
    api_instance = mencoro.DiscoveryApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    start_brand_name_suggestion_job_request = mencoro.StartBrandNameSuggestionJobRequest() # StartBrandNameSuggestionJobRequest | 

    try:
        # Start a brand-name alias suggestion job
        api_response = api_instance.start_brand_name_suggestion_job(organization_id, idempotency_key, start_brand_name_suggestion_job_request)
        print("The response of DiscoveryApi->start_brand_name_suggestion_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->start_brand_name_suggestion_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **idempotency_key** | **str**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | 
 **start_brand_name_suggestion_job_request** | [**StartBrandNameSuggestionJobRequest**](StartBrandNameSuggestionJobRequest.md)|  | 

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The suggestion job was accepted |  -  |
**400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization the caller can access under this id |  -  |
**409** | The organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
**429** | The organization exceeded ten suggestion starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_keyword_discovery_job**
> AcceptedJobResource start_keyword_discovery_job(organization_id, project_id, idempotency_key, start_keyword_discovery_job_request)

Start a keyword discovery job for a project

Minimum role: manager. Starts background keyword discovery from free-text seed input and answers 202 with the job to poll; it never returns keywords inline. The job SUGGESTS keywords - it creates no tracked queries and changes nothing in the project, so a completed job is a list to choose from, not work that has been applied. Queries the project already tracks are excluded from the suggestions automatically; `excludeQueries` adds more on top for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.accepted_job_resource import AcceptedJobResource
from mencoro.models.start_keyword_discovery_job_request import StartKeywordDiscoveryJobRequest
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
    api_instance = mencoro.DiscoveryApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the organization in the path.
    idempotency_key = 'idempotency_key_example' # str | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    start_keyword_discovery_job_request = mencoro.StartKeywordDiscoveryJobRequest() # StartKeywordDiscoveryJobRequest | 

    try:
        # Start a keyword discovery job for a project
        api_response = api_instance.start_keyword_discovery_job(organization_id, project_id, idempotency_key, start_keyword_discovery_job_request)
        print("The response of DiscoveryApi->start_keyword_discovery_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->start_keyword_discovery_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**| Must belong to the organization in the path. | 
 **idempotency_key** | **str**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | 
 **start_keyword_discovery_job_request** | [**StartKeywordDiscoveryJobRequest**](StartKeywordDiscoveryJobRequest.md)|  | 

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The discovery job was accepted |  -  |
**400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
**401** | Missing or invalid API key |  -  |
**402** | The organization has no entitled subscription |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
**429** | The organization exceeded ten discovery starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_prompt_discovery_job**
> AcceptedJobResource start_prompt_discovery_job(organization_id, project_id, idempotency_key, start_prompt_discovery_job_request)

Start a geo prompt discovery job for a project

Minimum role: manager. Starts background discovery of natural-language prompts - the questions an answer engine gets asked - from free-text seed input, and answers 202 with the job to poll; it never returns prompts inline. The job SUGGESTS prompts: it creates no tracked queries and changes nothing in the project. `country` is required here, unlike keyword discovery, because a prompt is a question asked from somewhere and the provider request has no default for it. Queries the project already tracks are excluded automatically; `excludeQueries` adds more for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.accepted_job_resource import AcceptedJobResource
from mencoro.models.start_prompt_discovery_job_request import StartPromptDiscoveryJobRequest
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
    api_instance = mencoro.DiscoveryApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the organization in the path.
    idempotency_key = 'idempotency_key_example' # str | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    start_prompt_discovery_job_request = mencoro.StartPromptDiscoveryJobRequest() # StartPromptDiscoveryJobRequest | 

    try:
        # Start a geo prompt discovery job for a project
        api_response = api_instance.start_prompt_discovery_job(organization_id, project_id, idempotency_key, start_prompt_discovery_job_request)
        print("The response of DiscoveryApi->start_prompt_discovery_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->start_prompt_discovery_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**| Must belong to the organization in the path. | 
 **idempotency_key** | **str**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | 
 **start_prompt_discovery_job_request** | [**StartPromptDiscoveryJobRequest**](StartPromptDiscoveryJobRequest.md)|  | 

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The discovery job was accepted |  -  |
**400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
**401** | Missing or invalid API key |  -  |
**402** | The organization has no entitled subscription |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
**429** | The organization exceeded ten discovery starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

