# mencoro.TrackedQueriesApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_clusters_to_tracked_query**](TrackedQueriesApi.md#add_clusters_to_tracked_query) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Add a tracked query to clusters
[**batch_change_tracked_queries_check_frequency**](TrackedQueriesApi.md#batch_change_tracked_queries_check_frequency) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/check-frequency | Change how often several tracked queries are checked
[**batch_change_tracked_queries_n_passes**](TrackedQueriesApi.md#batch_change_tracked_queries_n_passes) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/passes | Change how many passes several tracked queries run per check
[**batch_create_tracked_queries**](TrackedQueriesApi.md#batch_create_tracked_queries) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Create tracked queries
[**batch_force_check_tracked_queries**](TrackedQueriesApi.md#batch_force_check_tracked_queries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check | Check several tracked queries now
[**batch_pause_tracked_queries**](TrackedQueriesApi.md#batch_pause_tracked_queries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/pause | Pause several tracked queries
[**batch_resume_tracked_queries**](TrackedQueriesApi.md#batch_resume_tracked_queries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/resume | Resume several tracked queries
[**bulk_add_clusters_to_tracked_queries**](TrackedQueriesApi.md#bulk_add_clusters_to_tracked_queries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Add many tracked queries to clusters
[**bulk_delete_tracked_queries**](TrackedQueriesApi.md#bulk_delete_tracked_queries) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk-delete | Delete tracked queries
[**bulk_remove_clusters_from_tracked_queries**](TrackedQueriesApi.md#bulk_remove_clusters_from_tracked_queries) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Remove many tracked queries from clusters
[**change_tracked_query_check_frequency**](TrackedQueriesApi.md#change_tracked_query_check_frequency) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/check-frequency | Change how often a tracked query is checked
[**change_tracked_query_n_passes**](TrackedQueriesApi.md#change_tracked_query_n_passes) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/passes | Change how many passes a tracked query runs per check
[**count_tracked_queries**](TrackedQueriesApi.md#count_tracked_queries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/count | Count a project&#39;s tracked queries and price checking them
[**force_check_all_active_tracked_queries**](TrackedQueriesApi.md#force_check_all_active_tracked_queries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check-all | Check every eligible tracked query of a project now
[**get_tracked_query**](TrackedQueriesApi.md#get_tracked_query) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId} | Get a tracked query
[**pause_tracked_query**](TrackedQueriesApi.md#pause_tracked_query) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/pause | Pause a tracked query
[**remove_clusters_from_tracked_query**](TrackedQueriesApi.md#remove_clusters_from_tracked_query) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Remove a tracked query from clusters
[**report_ai_response**](TrackedQueriesApi.md#report_ai_response) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/responses/{aiResponseId}/report | Report a problem with a captured AI answer
[**resume_tracked_query**](TrackedQueriesApi.md#resume_tracked_query) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/resume | Resume a tracked query
[**search_tracked_queries**](TrackedQueriesApi.md#search_tracked_queries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Search a project&#39;s tracked queries
[**search_tracked_query_mention_matches**](TrackedQueriesApi.md#search_tracked_query_mention_matches) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/mention-matches | List stored mention matches of a tracked query
[**search_tracked_query_serp_matches**](TrackedQueriesApi.md#search_tracked_query_serp_matches) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/serp-matches | List stored serp matches of a tracked query


# **add_clusters_to_tracked_query**
> TrackedQueryDetailResource add_clusters_to_tracked_query(organization_id, project_id, tracked_query_id, idempotency_key, cluster_membership_request_data)

Add a tracked query to clusters

Minimum role: manager. Adds the tracked query to every cluster named in "queryClusterIds" and answers with the query in its new state. Membership is a set: a cluster the query already belongs to is skipped, not reported as an error, and the response still lists it. Clusters the query belongs to and this call does not name are left alone — this adds, it does not replace the membership. Every cluster must belong to the project in the path; one that does not is rejected with its field named, and nothing is written. The "Idempotency-Key" header is required, and a repeat of the same key and body returns the recorded answer without adding anything again.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.cluster_membership_request_data import ClusterMembershipRequestData
from mencoro.models.tracked_query_detail_resource import TrackedQueryDetailResource
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write.
    cluster_membership_request_data = mencoro.ClusterMembershipRequestData() # ClusterMembershipRequestData | 

    try:
        # Add a tracked query to clusters
        api_response = api_instance.add_clusters_to_tracked_query(organization_id, project_id, tracked_query_id, idempotency_key, cluster_membership_request_data)
        print("The response of TrackedQueriesApi->add_clusters_to_tracked_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->add_clusters_to_tracked_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **tracked_query_id** | **UUID**| Must belong to the project in the path. | 
 **idempotency_key** | **str**| A client-chosen key, unique per operation, so a lost response can be retried without repeating the write. | 
 **cluster_membership_request_data** | [**ClusterMembershipRequestData**](ClusterMembershipRequestData.md)|  | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tracked query, including the clusters it now belongs to |  -  |
**400** | The body was rejected: an unknown field, a malformed cluster id, a cluster outside this project, or a missing Idempotency-Key |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization, project or tracked query the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, the idempotency key was reused for a different body, or a cluster was deleted between validation and the write, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_change_tracked_queries_check_frequency**
> BatchWriteOutcome batch_change_tracked_queries_check_frequency(organization_id, project_id, idempotency_key, batch_change_tracked_query_check_frequency_request_data)

Change how often several tracked queries are checked

Minimum role: manager. Sets the same check frequency on every tracked query named in `ids`, at most 100 distinct ids per call. The organization must be active and the project must not be archived. Partial success: an id that is not a tracked query of this project — unknown, malformed, already deleted, or belonging to somewhere else — is reported under `failed` with `tracked_query_not_found` while the rest are changed, and the call still answers 200. Nothing is rolled back because an item failed. Setting the frequency a query already has is accepted and changes nothing. This does NOT run a check and does not reschedule one already in flight. It never changes more than the ids it is given: there is no "change everything matching a filter" mode. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.batch_change_tracked_query_check_frequency_request_data import BatchChangeTrackedQueryCheckFrequencyRequestData
from mencoro.models.batch_write_outcome import BatchWriteOutcome
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
    batch_change_tracked_query_check_frequency_request_data = mencoro.BatchChangeTrackedQueryCheckFrequencyRequestData() # BatchChangeTrackedQueryCheckFrequencyRequestData | 

    try:
        # Change how often several tracked queries are checked
        api_response = api_instance.batch_change_tracked_queries_check_frequency(organization_id, project_id, idempotency_key, batch_change_tracked_query_check_frequency_request_data)
        print("The response of TrackedQueriesApi->batch_change_tracked_queries_check_frequency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->batch_change_tracked_queries_check_frequency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | 
 **batch_change_tracked_query_check_frequency_request_data** | [**BatchChangeTrackedQueryCheckFrequencyRequestData**](BatchChangeTrackedQueryCheckFrequencyRequestData.md)|  | 

### Return type

[**BatchWriteOutcome**](BatchWriteOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-id results. Read &#x60;failed&#x60;: a non-empty &#x60;failed&#x60; with a 200 is the normal partial-success answer. |  -  |
**400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_change_tracked_queries_n_passes**
> BatchWriteOutcome batch_change_tracked_queries_n_passes(organization_id, project_id, idempotency_key, batch_change_tracked_query_passes_request_data)

Change how many passes several tracked queries run per check

Minimum role: manager. Sets the same passes-per-check on every tracked query named in `ids`, at most 100 distinct ids per call. The organization must be active and the project must not be archived. Partial success, and two distinct reasons appear under `failed`: an id that is not a tracked query of this project answers `tracked_query_not_found`, and a `google_serp` or `google_shopping` query asked for more than one pass answers `n_passes_not_supported_for_engine` — those engines run a single pass. Both leave the rest of the batch changed and the call still answers 200. Setting the value back to 1 is always allowed, so a batch that lowers sampling never fails on engine grounds. This does NOT run a check and does not change history already captured. More passes cost proportionally more of the plan's check budget. It never changes more than the ids it is given: there is no "change everything matching a filter" mode. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.batch_change_tracked_query_passes_request_data import BatchChangeTrackedQueryPassesRequestData
from mencoro.models.batch_write_outcome import BatchWriteOutcome
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
    batch_change_tracked_query_passes_request_data = mencoro.BatchChangeTrackedQueryPassesRequestData() # BatchChangeTrackedQueryPassesRequestData | 

    try:
        # Change how many passes several tracked queries run per check
        api_response = api_instance.batch_change_tracked_queries_n_passes(organization_id, project_id, idempotency_key, batch_change_tracked_query_passes_request_data)
        print("The response of TrackedQueriesApi->batch_change_tracked_queries_n_passes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->batch_change_tracked_queries_n_passes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | 
 **batch_change_tracked_query_passes_request_data** | [**BatchChangeTrackedQueryPassesRequestData**](BatchChangeTrackedQueryPassesRequestData.md)|  | 

### Return type

[**BatchWriteOutcome**](BatchWriteOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-id results. Read &#x60;failed&#x60;: a non-empty &#x60;failed&#x60; with a 200 is the normal partial-success answer. |  -  |
**400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_create_tracked_queries**
> BatchCreateTrackedQueriesResultResource batch_create_tracked_queries(organization_id, project_id, idempotency_key, batch_create_tracked_queries_request_data)

Create tracked queries

Minimum role: manager. Creates the cross product of `queryTexts` x `engines` x `countries`: three texts, two engines and two countries create twelve tracked queries, not three. At most 100 combinations per call. The organization must be active and the project must not be archived. Partial success: the response lists, per combination, either the id it was created under or why nothing was created for it, and the status code never reports item-level outcomes. A combination the project already tracks is NOT created again and NOT re-identified — it appears under `failed` with `tracked_query_already_exists`, keeps the id it already had, and has any `queryClusterIds` in this request merged into it. Query text is normalised before it is compared and stored (lower-cased, whitespace collapsed, leading list markers stripped), so two texts differing only in those respects are one tracked query: the first of them owns the outcome and every later one appears under `failed` with `duplicate_combination_in_request`, naming the entry it repeats. `nPasses` applies to AI engines only: `google_serp` and `google_shopping` rows are always created with one pass, whatever is sent. Google AI Mode is unavailable in a few countries and those combinations are reported under `failed` rather than created. Creating a tracked query does not run a check: the first check happens on the normal schedule for the `checkFrequency` chosen. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without creating anything again.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.batch_create_tracked_queries_request_data import BatchCreateTrackedQueriesRequestData
from mencoro.models.batch_create_tracked_queries_result_resource import BatchCreateTrackedQueriesResultResource
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per operation. Replaying it returns the first answer instead of creating anything again.
    batch_create_tracked_queries_request_data = mencoro.BatchCreateTrackedQueriesRequestData() # BatchCreateTrackedQueriesRequestData | 

    try:
        # Create tracked queries
        api_response = api_instance.batch_create_tracked_queries(organization_id, project_id, idempotency_key, batch_create_tracked_queries_request_data)
        print("The response of TrackedQueriesApi->batch_create_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->batch_create_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of creating anything again. | 
 **batch_create_tracked_queries_request_data** | [**BatchCreateTrackedQueriesRequestData**](BatchCreateTrackedQueriesRequestData.md)|  | 

### Return type

[**BatchCreateTrackedQueriesResultResource**](BatchCreateTrackedQueriesResultResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-combination results. Read &#x60;failed&#x60;: a non-empty &#x60;failed&#x60; with a 200 is the normal partial-success answer. |  -  |
**400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization, project or query cluster the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |
**422** | A query cluster exists but belongs to another project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_force_check_tracked_queries**
> BatchForceCheckTrackedQueries200Response batch_force_check_tracked_queries(organization_id, project_id, idempotency_key, batch_targets_request_data)

Check several tracked queries now

Minimum role: manager. Asks for a fresh check of up to 100 named tracked queries straight away, ignoring how recently each was last checked. Answers 200 with per-item results and NO job id: a check that is already in flight for a query is reused rather than started again, so there is no id this operation could hand back that is guaranteed to exist. Follow progress on the tracked query itself — its lastCheckedAt advances when the check completes. A successful item means the check was accepted for submission with budget available for it at that moment; it does not mean the check has run. A checked query costs one budget unit per pass (nPasses), and items that do not fit the remaining budget are reported as failed with `check_budget_forecast_exhausted`, or `subscription_not_found` when the organization has no entitled subscription — they are never reported as successful. That budget figure is a forecast for this batch, and a pessimistic one: a tracked query already being checked is joined to the check in flight and costs nothing, but it is still debited here, so an item refused this way may have fitted. Resubmit it in a later batch rather than treating the refusal as a statement about your subscription. A paused query is reported as failed with `tracked_query_already_paused`: paused queries are never checked. An id that is not a tracked query of this project is reported as failed with `tracked_query_not_found`, exactly as an id that does not exist. Requires an Idempotency-Key header; a retry must repeat the same ids in the same order.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.batch_force_check_tracked_queries200_response import BatchForceCheckTrackedQueries200Response
from mencoro.models.batch_targets_request_data import BatchTargetsRequestData
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | Repeating a request with the same key and the same ids answers with the first attempt's result instead of submitting again.
    batch_targets_request_data = mencoro.BatchTargetsRequestData() # BatchTargetsRequestData | 

    try:
        # Check several tracked queries now
        api_response = api_instance.batch_force_check_tracked_queries(organization_id, project_id, idempotency_key, batch_targets_request_data)
        print("The response of TrackedQueriesApi->batch_force_check_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->batch_force_check_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**| Repeating a request with the same key and the same ids answers with the first attempt&#39;s result instead of submitting again. | 
 **batch_targets_request_data** | [**BatchTargetsRequestData**](BatchTargetsRequestData.md)|  | 

### Return type

[**BatchForceCheckTrackedQueries200Response**](BatchForceCheckTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-item results. &#x60;failed&#x60; is always present, empty list included: read it rather than inferring success from the status. |  -  |
**400** | The Idempotency-Key header is missing, the body carried an unknown field, or \&quot;ids\&quot; was absent, malformed or larger than 100 distinct entries |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pause_tracked_queries**
> BatchPauseTrackedQueries200Response batch_pause_tracked_queries(organization_id, project_id, idempotency_key, batch_targets_request_data)

Pause several tracked queries

Minimum role: manager. Pauses up to 100 tracked queries of one project, each independently. Always answers 200 when the batch itself was processed: read `failed` to find out which items were not paused, never the status code. Items are never rolled back because a later one failed. An id that is already paused is reported as successful — pausing asserts a state, not a transition. An id that is not a tracked query of this project is reported as failed with `tracked_query_not_found`, exactly as an id that does not exist at all, and nothing is written for it. Pausing does not cancel a check that is already running. Requires an Idempotency-Key header; a retry must repeat the same ids in the same order to be recognised as a retry rather than refused as a reused key.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.batch_pause_tracked_queries200_response import BatchPauseTrackedQueries200Response
from mencoro.models.batch_targets_request_data import BatchTargetsRequestData
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | Repeating a request with the same key and the same ids answers with the first attempt's result.
    batch_targets_request_data = mencoro.BatchTargetsRequestData() # BatchTargetsRequestData | 

    try:
        # Pause several tracked queries
        api_response = api_instance.batch_pause_tracked_queries(organization_id, project_id, idempotency_key, batch_targets_request_data)
        print("The response of TrackedQueriesApi->batch_pause_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->batch_pause_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**| Repeating a request with the same key and the same ids answers with the first attempt&#39;s result. | 
 **batch_targets_request_data** | [**BatchTargetsRequestData**](BatchTargetsRequestData.md)|  | 

### Return type

[**BatchPauseTrackedQueries200Response**](BatchPauseTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-item results. &#x60;failed&#x60; is always present, empty list included: read it rather than inferring success from the status. |  -  |
**400** | The Idempotency-Key header is missing, the body carried an unknown field, or \&quot;ids\&quot; was absent, malformed or larger than 100 distinct entries |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_resume_tracked_queries**
> BatchResumeTrackedQueries200Response batch_resume_tracked_queries(organization_id, project_id, idempotency_key, batch_targets_request_data)

Resume several tracked queries

Minimum role: manager. Puts up to 100 paused tracked queries of one project back under the scheduler, each independently. Always answers 200 when the batch itself was processed: read `failed` to find out which items were not resumed, never the status code. Items are never rolled back because a later one failed. An id that is already active is reported as successful — resuming asserts a state, not a transition. An id that is not a tracked query of this project is reported as failed with `tracked_query_not_found`, exactly as an id that does not exist at all, and nothing is written for it. No check is run by this operation and nothing is back-filled for the time the queries spent paused. Requires an Idempotency-Key header; a retry must repeat the same ids in the same order to be recognised as a retry rather than refused as a reused key.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.batch_resume_tracked_queries200_response import BatchResumeTrackedQueries200Response
from mencoro.models.batch_targets_request_data import BatchTargetsRequestData
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | Repeating a request with the same key and the same ids answers with the first attempt's result.
    batch_targets_request_data = mencoro.BatchTargetsRequestData() # BatchTargetsRequestData | 

    try:
        # Resume several tracked queries
        api_response = api_instance.batch_resume_tracked_queries(organization_id, project_id, idempotency_key, batch_targets_request_data)
        print("The response of TrackedQueriesApi->batch_resume_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->batch_resume_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**| Repeating a request with the same key and the same ids answers with the first attempt&#39;s result. | 
 **batch_targets_request_data** | [**BatchTargetsRequestData**](BatchTargetsRequestData.md)|  | 

### Return type

[**BatchResumeTrackedQueries200Response**](BatchResumeTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-item results. &#x60;failed&#x60; is always present, empty list included: read it rather than inferring success from the status. |  -  |
**400** | The Idempotency-Key header is missing, the body carried an unknown field, or \&quot;ids\&quot; was absent, malformed or larger than 100 distinct entries |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_add_clusters_to_tracked_queries**
> BulkAddClustersToTrackedQueries200Response bulk_add_clusters_to_tracked_queries(organization_id, project_id, idempotency_key, bulk_add_clusters_to_tracked_queries_request)

Add many tracked queries to clusters

Minimum role: manager. Adds every tracked query named in "ids" to every cluster named in "queryClusterIds". At most 100 distinct tracked queries per call; duplicates in "ids" are collapsed. Partial success: the answer is 200 with a per-item "successful" and "failed" list even when some items failed, nothing is rolled back, and an id that is not a tracked query of this project is reported as a failed item rather than dropped. Clusters not named are left alone — this adds, it does not replace membership. Every cluster must belong to the project in the path; one that does not is rejected with its field named and nothing is written at all. The "Idempotency-Key" header is required, and a repeat of the same key and body returns the recorded answer without running the batch again.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.bulk_add_clusters_to_tracked_queries200_response import BulkAddClustersToTrackedQueries200Response
from mencoro.models.bulk_add_clusters_to_tracked_queries_request import BulkAddClustersToTrackedQueriesRequest
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch.
    bulk_add_clusters_to_tracked_queries_request = mencoro.BulkAddClustersToTrackedQueriesRequest() # BulkAddClustersToTrackedQueriesRequest | 

    try:
        # Add many tracked queries to clusters
        api_response = api_instance.bulk_add_clusters_to_tracked_queries(organization_id, project_id, idempotency_key, bulk_add_clusters_to_tracked_queries_request)
        print("The response of TrackedQueriesApi->bulk_add_clusters_to_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->bulk_add_clusters_to_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**| A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch. | 
 **bulk_add_clusters_to_tracked_queries_request** | [**BulkAddClustersToTrackedQueriesRequest**](BulkAddClustersToTrackedQueriesRequest.md)|  | 

### Return type

[**BulkAddClustersToTrackedQueries200Response**](BulkAddClustersToTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-item results. Read \&quot;failed\&quot;: a 200 does not mean every item succeeded. |  -  |
**400** | The body was rejected: an unknown field, a malformed or missing id, more than 100 distinct ids, a cluster outside this project, or a missing Idempotency-Key |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_tracked_queries**
> BatchWriteOutcome bulk_delete_tracked_queries(organization_id, project_id, idempotency_key, batch_targets_request_data)

Delete tracked queries

Minimum role: manager. Permanently deletes the tracked queries named in `ids`, at most 100 distinct ids per call. The organization must be active and the project must not be archived. Deletion is hard and cannot be undone: the tracked query is removed along with its captured answers, matches, search pages and rank history, and any check already in flight for it is cancelled. Those cascades run in the background, so a 200 means the tracked queries were deleted, not that every derived record has finished being purged. Partial success: an id that is not a tracked query of this project — unknown, malformed, already deleted, or belonging to somewhere else — is reported under `failed` with `tracked_query_not_found` while the rest are deleted. It never deletes more than the ids it is given: there is no "delete everything matching a filter" mode. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without deleting anything again.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.batch_targets_request_data import BatchTargetsRequestData
from mencoro.models.batch_write_outcome import BatchWriteOutcome
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per operation. Replaying it returns the first answer instead of deleting anything again.
    batch_targets_request_data = mencoro.BatchTargetsRequestData() # BatchTargetsRequestData | 

    try:
        # Delete tracked queries
        api_response = api_instance.bulk_delete_tracked_queries(organization_id, project_id, idempotency_key, batch_targets_request_data)
        print("The response of TrackedQueriesApi->bulk_delete_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->bulk_delete_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of deleting anything again. | 
 **batch_targets_request_data** | [**BatchTargetsRequestData**](BatchTargetsRequestData.md)|  | 

### Return type

[**BatchWriteOutcome**](BatchWriteOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-id results. Read &#x60;failed&#x60;: a non-empty &#x60;failed&#x60; with a 200 is the normal partial-success answer. |  -  |
**400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_remove_clusters_from_tracked_queries**
> BulkRemoveClustersFromTrackedQueries200Response bulk_remove_clusters_from_tracked_queries(organization_id, project_id, idempotency_key, bulk_remove_clusters_from_tracked_queries_request)

Remove many tracked queries from clusters

Minimum role: manager. Removes every tracked query named in "ids" from every cluster named in "queryClusterIds". At most 100 distinct tracked queries per call; duplicates in "ids" are collapsed. Partial success: the answer is 200 with a per-item "successful" and "failed" list even when some items failed, nothing is rolled back, and an id that is not a tracked query of this project is reported as a failed item rather than dropped. Neither the clusters nor the tracked queries are deleted: only the membership between them. Every cluster must belong to the project in the path; one that does not is rejected with its field named and nothing is written at all. NOTE: this DELETE requires a request body — some HTTP client libraries and proxies strip bodies from DELETE, and a stripped body is refused with a validation error rather than interpreted as "remove everything". The "Idempotency-Key" header is required, and a repeat of the same key and body returns the recorded answer without running the batch again.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.bulk_remove_clusters_from_tracked_queries200_response import BulkRemoveClustersFromTrackedQueries200Response
from mencoro.models.bulk_remove_clusters_from_tracked_queries_request import BulkRemoveClustersFromTrackedQueriesRequest
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch.
    bulk_remove_clusters_from_tracked_queries_request = mencoro.BulkRemoveClustersFromTrackedQueriesRequest() # BulkRemoveClustersFromTrackedQueriesRequest | Required. A DELETE with no body is rejected.

    try:
        # Remove many tracked queries from clusters
        api_response = api_instance.bulk_remove_clusters_from_tracked_queries(organization_id, project_id, idempotency_key, bulk_remove_clusters_from_tracked_queries_request)
        print("The response of TrackedQueriesApi->bulk_remove_clusters_from_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->bulk_remove_clusters_from_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**| A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch. | 
 **bulk_remove_clusters_from_tracked_queries_request** | [**BulkRemoveClustersFromTrackedQueriesRequest**](BulkRemoveClustersFromTrackedQueriesRequest.md)| Required. A DELETE with no body is rejected. | 

### Return type

[**BulkRemoveClustersFromTrackedQueries200Response**](BulkRemoveClustersFromTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Per-item results. Read \&quot;failed\&quot;: a 200 does not mean every item succeeded. |  -  |
**400** | The body was rejected or missing: an unknown field, a malformed or missing id, more than 100 distinct ids, a cluster outside this project, a stripped DELETE body, or a missing Idempotency-Key |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_tracked_query_check_frequency**
> TrackedQueryDetailResource change_tracked_query_check_frequency(organization_id, project_id, tracked_query_id, idempotency_key, change_tracked_query_check_frequency_request_data)

Change how often a tracked query is checked

Minimum role: manager. Sets how often one tracked query is checked while it is active. The organization must be active and the project must not be archived. Setting the frequency it already has is accepted and changes nothing. This does NOT run a check, does not backfill history, and does not reschedule a check already in flight: the new cadence applies from the next time the query is considered. A paused query keeps the setting but is not checked until it is resumed. A tracked query belonging to another project answers 404, the same answer an unknown id gets. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.change_tracked_query_check_frequency_request_data import ChangeTrackedQueryCheckFrequencyRequestData
from mencoro.models.tracked_query_detail_resource import TrackedQueryDetailResource
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
    change_tracked_query_check_frequency_request_data = mencoro.ChangeTrackedQueryCheckFrequencyRequestData() # ChangeTrackedQueryCheckFrequencyRequestData | 

    try:
        # Change how often a tracked query is checked
        api_response = api_instance.change_tracked_query_check_frequency(organization_id, project_id, tracked_query_id, idempotency_key, change_tracked_query_check_frequency_request_data)
        print("The response of TrackedQueriesApi->change_tracked_query_check_frequency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->change_tracked_query_check_frequency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **tracked_query_id** | **UUID**| Must belong to the project in the path. | 
 **idempotency_key** | **str**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | 
 **change_tracked_query_check_frequency_request_data** | [**ChangeTrackedQueryCheckFrequencyRequestData**](ChangeTrackedQueryCheckFrequencyRequestData.md)|  | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tracked query in its new state |  -  |
**400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization, project or tracked query the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_tracked_query_n_passes**
> TrackedQueryDetailResource change_tracked_query_n_passes(organization_id, project_id, tracked_query_id, idempotency_key, change_tracked_query_passes_request_data)

Change how many passes a tracked query runs per check

Minimum role: manager. Sets how many times one tracked query is asked per check. AI engines are not deterministic, so several passes are averaged; `google_serp` and `google_shopping` run a single pass and refuse any value above one with 409 `n_passes_not_supported_for_engine`. Setting the value back to 1 is always allowed. The organization must be active and the project must not be archived. Setting the value it already has is accepted and changes nothing. This does NOT run a check and does not change history already captured: it applies from the next check. More passes cost proportionally more of the plan's check budget. A tracked query belonging to another project answers 404, the same answer an unknown id gets. The Idempotency-Key header is required; a retry with the same key and the same body returns this same answer without applying anything again.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.change_tracked_query_passes_request_data import ChangeTrackedQueryPassesRequestData
from mencoro.models.tracked_query_detail_resource import TrackedQueryDetailResource
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
    change_tracked_query_passes_request_data = mencoro.ChangeTrackedQueryPassesRequestData() # ChangeTrackedQueryPassesRequestData | 

    try:
        # Change how many passes a tracked query runs per check
        api_response = api_instance.change_tracked_query_n_passes(organization_id, project_id, tracked_query_id, idempotency_key, change_tracked_query_passes_request_data)
        print("The response of TrackedQueriesApi->change_tracked_query_n_passes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->change_tracked_query_n_passes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **tracked_query_id** | **UUID**| Must belong to the project in the path. | 
 **idempotency_key** | **str**| A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | 
 **change_tracked_query_passes_request_data** | [**ChangeTrackedQueryPassesRequestData**](ChangeTrackedQueryPassesRequestData.md)|  | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tracked query in its new state |  -  |
**400** | The body was rejected, or the Idempotency-Key header is missing; &#x60;details&#x60; names the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization, project or tracked query the caller can access under these ids |  -  |
**409** | The engine runs a single pass and cannot take more; or the organization or project is archived; or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_tracked_queries**
> TrackedQueryCountResource count_tracked_queries(organization_id, project_id, status=status)

Count a project's tracked queries and price checking them

Minimum role: viewer. Two numbers about one project: how many tracked queries it holds, and what force-checking that same set would cost. Omit `status` to count every tracked query whatever its status; send `active` or `paused` to count and price only those. `checkCost` is a PRICED DRY RUN expressed in check budget units — one unit per pass, the same unit the plan allowance is counted in, so it is directly comparable with `checksAvailable` from the entitlements operation — and it is the sum of each matched tracked query's configured passes. Asking reserves nothing, debits nothing and starts no check. It is deliberately NOT a forecast of what the check-all operation will consume: that operation skips paused queries, skips a query whose check is already pending or running, re-runs a check awaiting retry without charging for it again, and stops at whatever budget is left — none of which is subtracted here. Count with `status=active` for the figure closest to a full check-all. Both numbers are read from the write model, so a tracked query created moments ago is already in them; that is why they can be AHEAD of the `total` returned by the tracked-queries listing, which counts a search projection, and ahead of the keyword listings, which read projections refreshed in the background. Summing the unfiltered count over every project of an organization, archived projects included, reproduces countOrganizationTrackedQueries, which counts through the same counter in the same store. An archived project still answers, because this is a read, but no check can be submitted there while it stays archived, so its cost is hypothetical. For a month of scheduled rounds across the whole organization instead of one round over one project, read getOrganizationProjectedMonthlyChecks. No monetary amount is published or implied: the cost of a check is published only in budget units.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.tracked_query_count_resource import TrackedQueryCountResource
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    status = 'status_example' # str | Restrict both numbers to one status. Lower-case; an unknown value is rejected, not ignored. Omitted, every status is counted and priced. (optional)

    try:
        # Count a project's tracked queries and price checking them
        api_response = api_instance.count_tracked_queries(organization_id, project_id, status=status)
        print("The response of TrackedQueriesApi->count_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->count_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **status** | **str**| Restrict both numbers to one status. Lower-case; an unknown value is rejected, not ignored. Omitted, every status is counted and priced. | [optional] 

### Return type

[**TrackedQueryCountResource**](TrackedQueryCountResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tracked query count and the budget cost of checking that set |  -  |
**400** | The status parameter was rejected; the details name the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_check_all_active_tracked_queries**
> SubmittedChecksResource force_check_all_active_tracked_queries(organization_id, project_id, idempotency_key)

Check every eligible tracked query of a project now

Minimum role: manager. Submits a fresh check for every eligible tracked query of the project, ignoring how recently each was last checked, least-recently-checked first, and at most 1000 tracked queries per call. Eligible is narrower than active: a paused query is skipped, and so is one whose check is already pending or running for the same engine. A query whose check is awaiting a retry is included and, WHEN THE ENGINE HAS NOT CHANGED SINCE, costs nothing extra, because its first submission already paid for it; if the engine did change, the pending run is replaced and the replacement is paid for. What is left is trimmed to what the organization's remaining check budget can pay for — a check costs one budget unit per pass. While a subscription is cancelled but still inside its paid grace window nothing is submitted at all and `submitted` is 0; name the queries explicitly through the check operation to run them in that window. CALLING AGAIN DOES NOT CONTINUE WHERE THIS CALL STOPPED: submissions are handed to a worker, and a tracked query stops being selected only once that worker has started its check, so a second call made before the queue drains selects and submits the same tracked queries again. That is safe while the first check is still running — the duplicate is collapsed, and nothing is checked or charged twice — but a check that has already finished is run again and charged again, because this operation ignores staleness by design. To cover a project with more than 1000 eligible tracked queries, wait for the submitted wave to be picked up — each tracked query's lastCheckedAt advances when its check completes — and call again then. The response lists the tracked queries submitted and carries NO job id: a check already in flight is reused rather than started again, so no id could be guaranteed to exist. Submission is accepted, not completed: a listed tracked query can still lose the last budget units to another caller before the worker reaches it. The request takes no body, and any field sent is rejected. Requires an Idempotency-Key header.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.submitted_checks_resource import SubmittedChecksResource
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    idempotency_key = 'idempotency_key_example' # str | Repeating a request with the same key answers with the first attempt's result instead of submitting a second wave.

    try:
        # Check every eligible tracked query of a project now
        api_response = api_instance.force_check_all_active_tracked_queries(organization_id, project_id, idempotency_key)
        print("The response of TrackedQueriesApi->force_check_all_active_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->force_check_all_active_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **idempotency_key** | **str**| Repeating a request with the same key answers with the first attempt&#39;s result instead of submitting a second wave. | 

### Return type

[**SubmittedChecksResource**](SubmittedChecksResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tracked queries submitted for a check |  -  |
**400** | The Idempotency-Key header is missing or malformed, or the request carried a body |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |
**409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracked_query**
> TrackedQueryDetailResource get_tracked_query(organization_id, project_id, tracked_query_id)

Get a tracked query

Minimum role: viewer. The configuration of one tracked query: the text sent to the engine, the engine, locale and country it is asked in, the clusters it belongs to, and how often it is checked. A lastCheckedAt of null means no check has completed yet — it is not a check that found nothing. A tracked query belonging to another project answers 404, the same answer an unknown id gets, so the API never confirms that an inaccessible tracked query exists. Rank positions, share of voice and sentiment are not part of this response: they belong to a date window and are served by the analytics endpoints.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.tracked_query_detail_resource import TrackedQueryDetailResource
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.

    try:
        # Get a tracked query
        api_response = api_instance.get_tracked_query(organization_id, project_id, tracked_query_id)
        print("The response of TrackedQueriesApi->get_tracked_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->get_tracked_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **tracked_query_id** | **UUID**| Must belong to the project in the path. | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tracked query |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization, project or tracked query the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_tracked_query**
> TrackedQueryDetailResource pause_tracked_query(organization_id, project_id, tracked_query_id, idempotency_key)

Pause a tracked query

Minimum role: manager. Stops the scheduler from checking this tracked query; it keeps its configuration, its clusters and every result already collected, and nothing is deleted. Pausing a query that is already paused succeeds and answers the same body — this is a PUT asserting a state, not a transition, so it is safe to repeat. It does NOT cancel a check that is already running: a check in flight when the pause lands still completes and still consumes the budget unit it reserved. The request takes no body, and any field sent is rejected. Requires an Idempotency-Key header.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.tracked_query_detail_resource import TrackedQueryDetailResource
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.
    idempotency_key = 'idempotency_key_example' # str | Repeating a request with the same key answers with the first attempt's result instead of pausing again.

    try:
        # Pause a tracked query
        api_response = api_instance.pause_tracked_query(organization_id, project_id, tracked_query_id, idempotency_key)
        print("The response of TrackedQueriesApi->pause_tracked_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->pause_tracked_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **tracked_query_id** | **UUID**| Must belong to the project in the path. | 
 **idempotency_key** | **str**| Repeating a request with the same key answers with the first attempt&#39;s result instead of pausing again. | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tracked query, paused |  -  |
**400** | The Idempotency-Key header is missing or malformed, or the request carried a body |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization, project or tracked query the caller can access under these ids |  -  |
**409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_clusters_from_tracked_query**
> TrackedQueryDetailResource remove_clusters_from_tracked_query(organization_id, project_id, tracked_query_id, idempotency_key, cluster_membership_request_data)

Remove a tracked query from clusters

Minimum role: manager. Removes the tracked query from every cluster named in "queryClusterIds" and answers with the query in its new state. A cluster the query does not belong to is skipped, not reported as an error. Neither the clusters nor the tracked query are deleted: only the membership between them. Every cluster must belong to the project in the path. NOTE: this DELETE requires a request body — some HTTP client libraries and proxies strip bodies from DELETE, and a stripped body is refused with a validation error rather than interpreted as "remove all clusters". The "Idempotency-Key" header is required, and a repeat of the same key and body returns the recorded answer without removing anything again.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.cluster_membership_request_data import ClusterMembershipRequestData
from mencoro.models.tracked_query_detail_resource import TrackedQueryDetailResource
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write.
    cluster_membership_request_data = mencoro.ClusterMembershipRequestData() # ClusterMembershipRequestData | Required. A DELETE with no body is rejected.

    try:
        # Remove a tracked query from clusters
        api_response = api_instance.remove_clusters_from_tracked_query(organization_id, project_id, tracked_query_id, idempotency_key, cluster_membership_request_data)
        print("The response of TrackedQueriesApi->remove_clusters_from_tracked_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->remove_clusters_from_tracked_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **tracked_query_id** | **UUID**| Must belong to the project in the path. | 
 **idempotency_key** | **str**| A client-chosen key, unique per operation, so a lost response can be retried without repeating the write. | 
 **cluster_membership_request_data** | [**ClusterMembershipRequestData**](ClusterMembershipRequestData.md)| Required. A DELETE with no body is rejected. | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tracked query, including the clusters it still belongs to |  -  |
**400** | The body was rejected or missing: an unknown field, a malformed cluster id, a cluster outside this project, a stripped DELETE body, or a missing Idempotency-Key |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization, project or tracked query the caller can access under these ids |  -  |
**409** | The organization is archived, the project is archived, the idempotency key was reused for a different body, or a cluster was deleted between validation and the write, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_ai_response**
> AiResponseReportResource report_ai_response(organization_id, project_id, tracked_query_id, ai_response_id, idempotency_key, report_ai_response_request)

Report a problem with a captured AI answer

Minimum role: viewer — deliberately lower than the other tracked-query writes, because a report changes nothing a viewer cannot already read. The key still needs the "write" capability. The report is forwarded to the team that reviews the scrape run behind the capture; it does not change the capture, the tracked query, or any metric derived from them, and nothing in this API will show the report afterwards. A 200 means the report was accepted for review, not that anything was corrected, and there is no identifier to poll. A capture that belongs to another tracked query or project answers 404, the same answer an unknown id gets. A capture that cannot be routed back to its scrape run answers 409 "ai_check_session_unavailable", and it cannot be reported. That code covers two moments, which behave differently for your key: when the capture carries no scrape run at all the refusal is decided BEFORE anything is sent, so the idempotency key is left unused and the same key answers the same way however often it is presented; when the review system itself rejects the run — its own retention having elapsed — the refusal comes after the forward was attempted, so the key is spent like any outcome we cannot confirm. You can tell them apart without guessing: retry the same key, and a reply of "operation_outcome_uncertain" means the refusal came from the review system. Delivery is at-most-once: the "Idempotency-Key" header is required and a repeat of the same key and body returns the recorded answer, but a delivery whose outcome is unknown refuses replay on that key rather than risk filing the report twice.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.ai_response_report_resource import AiResponseReportResource
from mencoro.models.report_ai_response_request import ReportAiResponseRequest
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.
    ai_response_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | A capture id from the AI responses listing. Must belong to the tracked query in the path.
    idempotency_key = 'idempotency_key_example' # str | A client-chosen key, unique per report, so a lost response can be retried without filing the report twice.
    report_ai_response_request = mencoro.ReportAiResponseRequest() # ReportAiResponseRequest | 

    try:
        # Report a problem with a captured AI answer
        api_response = api_instance.report_ai_response(organization_id, project_id, tracked_query_id, ai_response_id, idempotency_key, report_ai_response_request)
        print("The response of TrackedQueriesApi->report_ai_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->report_ai_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **tracked_query_id** | **UUID**| Must belong to the project in the path. | 
 **ai_response_id** | **UUID**| A capture id from the AI responses listing. Must belong to the tracked query in the path. | 
 **idempotency_key** | **str**| A client-chosen key, unique per report, so a lost response can be retried without filing the report twice. | 
 **report_ai_response_request** | [**ReportAiResponseRequest**](ReportAiResponseRequest.md)|  | 

### Return type

[**AiResponseReportResource**](AiResponseReportResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The report as accepted, in its normalised form |  -  |
**400** | The body was rejected: an unknown field, a missing or unsupported \&quot;type\&quot;, an over-long comment or brand name, or a missing Idempotency-Key |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization, project, tracked query or capture the caller can access under these ids |  -  |
**409** | The organization is archived, the capture can no longer be routed back to its scrape run, the idempotency key was reused for a different body, or a previous attempt with this key ended with an unknown outcome |  -  |
**502** | The review system could not be reached or refused the forward. Whether the report was filed is UNKNOWN: delivery is at-most-once and the failure can happen after the report was recorded upstream. This idempotency key will not replay; retrying with a new key may file the report twice. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_tracked_query**
> TrackedQueryDetailResource resume_tracked_query(organization_id, project_id, tracked_query_id, idempotency_key)

Resume a tracked query

Minimum role: manager. Puts a paused tracked query back under the scheduler. Resuming a query that is already active succeeds and answers the same body — this is a PUT asserting a state, not a transition. It does NOT run a check: the query is checked when it next falls due under its own checkFrequency, and results collected while it was paused are unaffected. Nothing is back-filled for the time it spent paused. The request takes no body, and any field sent is rejected. Requires an Idempotency-Key header.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.tracked_query_detail_resource import TrackedQueryDetailResource
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Must belong to the project in the path.
    idempotency_key = 'idempotency_key_example' # str | Repeating a request with the same key answers with the first attempt's result instead of resuming again.

    try:
        # Resume a tracked query
        api_response = api_instance.resume_tracked_query(organization_id, project_id, tracked_query_id, idempotency_key)
        print("The response of TrackedQueriesApi->resume_tracked_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->resume_tracked_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **tracked_query_id** | **UUID**| Must belong to the project in the path. | 
 **idempotency_key** | **str**| Repeating a request with the same key answers with the first attempt&#39;s result instead of resuming again. | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tracked query, active |  -  |
**400** | The Idempotency-Key header is missing or malformed, or the request carried a body |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the write capability |  -  |
**404** | No organization, project or tracked query the caller can access under these ids |  -  |
**409** | The organization or the project is archived, or the idempotency key was already used for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tracked_queries**
> SearchTrackedQueries200Response search_tracked_queries(organization_id, project_id, limit=limit, offset=offset, search=search, status=status, engines=engines, countries=countries, sort_by=sort_by, sort_order=sort_order)

Search a project's tracked queries

Minimum role: viewer. One row per tracked query — a single keyword on a single engine in a single country — carrying the metrics of its most recent completed check. Filter by status, engine, country and a free-text search over the keyword, and sort by any of the returned metrics. Positions (lastSerpPosition, lastMentionPosition, lastLinkPosition, lastShoppingPosition) are 1-based ranks, so LOWER is better; lastShareOfVoice and lastPositivityIndex are percentages from 0 to 100, where HIGHER is better. Every nullable field means "not known yet" rather than zero: a null position is a query with no data for that surface, a null lastPositivityIndex is a check with no mentions to score, and a null lastCheckedAt is a query that has never been checked — none of them is a score of zero. This listing reads a projection refreshed by background subscribers, not the write model, so a tracked query created or changed moments ago may not appear here yet or may still show its previous settings. It catches up on its own; nothing is lost. If you need to read back what you just wrote, the creation response carries the new ids and the single tracked-query operation reads the write model directly. total counts the tracked queries the filters match, not the rows on this page. A limit above the maximum is rejected, never clamped, and a filter this endpoint does not support is rejected rather than ignored.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.search_tracked_queries200_response import SearchTrackedQueries200Response
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    limit = 20 # int | Page size. A value above the maximum is rejected, never clamped. (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)
    search = 'search_example' # str | Free-text search over the keyword. (optional)
    status = 'status_example' # str |  (optional)
    engines = ['engines_example'] # List[str] | Repeatable, or comma-separated. (optional)
    countries = ['countries_example'] # List[str] | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
    sort_by = 'queryText' # str |  (optional) (default to 'queryText')
    sort_order = 'desc' # str |  (optional) (default to 'desc')

    try:
        # Search a project's tracked queries
        api_response = api_instance.search_tracked_queries(organization_id, project_id, limit=limit, offset=offset, search=search, status=status, engines=engines, countries=countries, sort_by=sort_by, sort_order=sort_order)
        print("The response of TrackedQueriesApi->search_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->search_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **limit** | **int**| Page size. A value above the maximum is rejected, never clamped. | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **search** | **str**| Free-text search over the keyword. | [optional] 
 **status** | **str**|  | [optional] 
 **engines** | [**List[str]**](str.md)| Repeatable, or comma-separated. | [optional] 
 **countries** | [**List[str]**](str.md)| ISO-3166 alpha-2 codes or English names. Must be configured on the project. | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;queryText&#39;]
 **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**SearchTrackedQueries200Response**](SearchTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project&#39;s tracked queries |  -  |
**400** | A filter or page bound was rejected; the details name the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tracked_query_mention_matches**
> SearchTrackedQueryMentionMatches200Response search_tracked_query_mention_matches(organization_id, project_id, tracked_query_id, date_from=date_from, date_to=date_to, limit=limit, offset=offset, sort_order=sort_order)

List stored mention matches of a tracked query

Minimum role: viewer. Text mentions across own brand and tracked or untracked competitors. Citation-only rows are excluded before pagination. Read mentionRelation to distinguish own brand from untracked competitors; a null competitorId alone does not classify the mention. Newest first by detection time, with an id tie-break. Dates cover whole UTC days. Only the retained 16-month window is readable, including when dateFrom is omitted. Unknown filters are rejected. The total counts all matching rows before pagination. Send Accept: text/csv for the same bounded page and filters as CSV, with formula-safe cells and no total.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.search_tracked_query_mention_matches200_response import SearchTrackedQueryMentionMatches200Response
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    date_from = '2013-10-20' # date | Inclusive UTC day; defaults to the retention floor. (optional)
    date_to = '2013-10-20' # date | Inclusive UTC day. (optional)
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)
    sort_order = 'desc' # str |  (optional) (default to 'desc')

    try:
        # List stored mention matches of a tracked query
        api_response = api_instance.search_tracked_query_mention_matches(organization_id, project_id, tracked_query_id, date_from=date_from, date_to=date_to, limit=limit, offset=offset, sort_order=sort_order)
        print("The response of TrackedQueriesApi->search_tracked_query_mention_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->search_tracked_query_mention_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **tracked_query_id** | **UUID**|  | 
 **date_from** | **date**| Inclusive UTC day; defaults to the retention floor. | [optional] 
 **date_to** | **date**| Inclusive UTC day. | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**SearchTrackedQueryMentionMatches200Response**](SearchTrackedQueryMentionMatches200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored matches and total under the same filters |  -  |
**400** | Invalid or unsupported query parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | Organization, project or tracked query is not accessible |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tracked_query_serp_matches**
> SearchTrackedQuerySerpMatches200Response search_tracked_query_serp_matches(organization_id, project_id, tracked_query_id, date_from=date_from, date_to=date_to, limit=limit, offset=offset, sort_order=sort_order)

List stored serp matches of a tracked query

Minimum role: viewer. Stored organic-search matches with the competitor attribution and position recorded at detection time. A null competitorId identifies the own-brand match. These are historical matches, not a reclassification using the current brand profile. Newest first by detection time, with an id tie-break. Dates cover whole UTC days. Only the retained 16-month window is readable, including when dateFrom is omitted. Unknown filters are rejected. The total counts all matching rows before pagination. Send Accept: text/csv for the same bounded page and filters as CSV, with formula-safe cells and no total.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.search_tracked_query_serp_matches200_response import SearchTrackedQuerySerpMatches200Response
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
    api_instance = mencoro.TrackedQueriesApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tracked_query_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    date_from = '2013-10-20' # date | Inclusive UTC day; defaults to the retention floor. (optional)
    date_to = '2013-10-20' # date | Inclusive UTC day. (optional)
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)
    sort_order = 'desc' # str |  (optional) (default to 'desc')

    try:
        # List stored serp matches of a tracked query
        api_response = api_instance.search_tracked_query_serp_matches(organization_id, project_id, tracked_query_id, date_from=date_from, date_to=date_to, limit=limit, offset=offset, sort_order=sort_order)
        print("The response of TrackedQueriesApi->search_tracked_query_serp_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackedQueriesApi->search_tracked_query_serp_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **project_id** | **UUID**|  | 
 **tracked_query_id** | **UUID**|  | 
 **date_from** | **date**| Inclusive UTC day; defaults to the retention floor. | [optional] 
 **date_to** | **date**| Inclusive UTC day. | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**SearchTrackedQuerySerpMatches200Response**](SearchTrackedQuerySerpMatches200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored matches and total under the same filters |  -  |
**400** | Invalid or unsupported query parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | Organization, project or tracked query is not accessible |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

