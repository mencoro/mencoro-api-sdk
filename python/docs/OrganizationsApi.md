# mencoro.OrganizationsApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_organization**](OrganizationsApi.md#archive_organization) | **POST** /api/v1/organizations/{organizationId}/archive | Archive an organization
[**count_organization_tracked_queries**](OrganizationsApi.md#count_organization_tracked_queries) | **GET** /api/v1/organizations/{organizationId}/usage/tracked-queries | Count the tracked queries an organization has configured
[**create_organization**](OrganizationsApi.md#create_organization) | **POST** /api/v1/organizations | Create an organization
[**get_entitlements**](OrganizationsApi.md#get_entitlements) | **GET** /api/v1/organizations/{organizationId}/entitlements | Get an organization&#39;s plan allowance and consumption
[**get_membership_stats**](OrganizationsApi.md#get_membership_stats) | **GET** /api/v1/organizations/{organizationId}/membership-stats | Membership, project and invitation counts for an organization
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /api/v1/organizations/{organizationId} | Get an organization
[**get_organization_projected_monthly_checks**](OrganizationsApi.md#get_organization_projected_monthly_checks) | **GET** /api/v1/organizations/{organizationId}/usage/projected-monthly-checks | Project a month of check consumption from the current tracking configuration
[**get_organization_stats**](OrganizationsApi.md#get_organization_stats) | **GET** /api/v1/organizations/{organizationId}/stats | Headline counts for an organization
[**list_organizations**](OrganizationsApi.md#list_organizations) | **GET** /api/v1/organizations | List accessible organizations
[**restore_organization**](OrganizationsApi.md#restore_organization) | **POST** /api/v1/organizations/{organizationId}/restore | Restore an archived organization
[**update_organization**](OrganizationsApi.md#update_organization) | **PATCH** /api/v1/organizations/{organizationId} | Update an organization profile


# **archive_organization**
> OrganizationResource archive_organization(organization_id, x_mencoro_confirmation, idempotency_key)

Archive an organization

Minimum role: owner. Archiving also archives the active projects of the organization, cancels its pending invitations and cancels its subscription at the end of the current billing period. Those effects are applied by background subscribers, so a 200 means the organization was archived, not that every effect has finished. Preview it first to see exactly what will be touched.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.organization_resource import OrganizationResource
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
    api_instance = mencoro.OrganizationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    x_mencoro_confirmation = 'mencoro_conf_VmajQznkILZjvFf63JexmT1AKX7iYZjOGSrBZYxlUTk' # str | The `confirmation.token` returned by POST /api/v1/organization-operation-previews for this exact action, organization and body. Single use, valid for five minutes, and bound to the effects the preview declared: if the organization gained a project or lost an invitation in between, it is refused with 409 rather than doing more than was agreed. Without it the call answers 428.
    idempotency_key = '5c1b8e42-0d7f-4a93-8c61-9b2e4d0a7f38' # str | Repeat it to retry a lost response. The replay is answered from the record without claiming the confirmation again, so a retry is never refused for presenting a confirmation the first attempt already spent.

    try:
        # Archive an organization
        api_response = api_instance.archive_organization(organization_id, x_mencoro_confirmation, idempotency_key)
        print("The response of OrganizationsApi->archive_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->archive_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **x_mencoro_confirmation** | **str**| The &#x60;confirmation.token&#x60; returned by POST /api/v1/organization-operation-previews for this exact action, organization and body. Single use, valid for five minutes, and bound to the effects the preview declared: if the organization gained a project or lost an invitation in between, it is refused with 409 rather than doing more than was agreed. Without it the call answers 428. | 
 **idempotency_key** | **str**| Repeat it to retry a lost response. The replay is answered from the record without claiming the confirmation again, so a retry is never refused for presenting a confirmation the first attempt already spent. | 

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization in its new state |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the organization:manage capability |  -  |
**404** | No organization the caller can access under this id |  -  |
**409** | The confirmation is invalid, expired, already used, or its declared effects changed; or the status transition is not allowed |  -  |
**428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_organization_tracked_queries**
> TrackedQueryUsageResource count_organization_tracked_queries(organization_id)

Count the tracked queries an organization has configured

Minimum role: viewer. How many tracked queries the organization has configured, counted live in PostgreSQL — the write model — over EVERY project it owns, archived projects included, and over every tracked query in them, active and paused alike. It is deliberately a DIFFERENT number from `aggregate.totalTrackedQueries` in getOrganizationOverview: that one sums a per-project copy held in the Elasticsearch read model and covers ACTIVE projects only, so it excludes archived projects and can lag behind a change that already shows here. Expect the two to disagree and do not treat either as wrong. This figure does reconcile exactly with countTrackedQueries, which counts one project through the same counter in the same store: sum its unfiltered `count` over every project, archived included, and you get this number. For the ACTIVE subset and what it will consume, call getOrganizationProjectedMonthlyChecks, which ranges over the same projects. Do NOT derive the paused count by subtracting one from the other: this number is read live from Postgres while that one is served from a cache invalidated by background subscribers, so the two can disagree while that invalidation catches up and the difference is then a count of nothing. For how many projects this ranges over, read `projects.total` and `projects.active` from getOrganizationStats. The value is never null: 0 means none are configured. This operation takes no query parameters — the population is fixed, and a parameter it cannot honour is rejected with 400 rather than silently ignored.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.tracked_query_usage_resource import TrackedQueryUsageResource
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
    api_instance = mencoro.OrganizationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Count the tracked queries an organization has configured
        api_response = api_instance.count_organization_tracked_queries(organization_id)
        print("The response of OrganizationsApi->count_organization_tracked_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->count_organization_tracked_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 

### Return type

[**TrackedQueryUsageResource**](TrackedQueryUsageResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization&#39;s tracked-query count |  -  |
**400** | A query parameter was sent to an operation that accepts none; the details name it |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization**
> CreateOrganization201Response create_organization(x_mencoro_confirmation, idempotency_key, create_organization_request)

Create an organization

Requires a key scoped to all organizations and the "organization:manage" capability: a key limited to named organizations cannot widen its own reach by creating one. Preview it first and send the confirmation in X-Mencoro-Confirmation together with an Idempotency-Key.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.create_organization201_response import CreateOrganization201Response
from mencoro.models.create_organization_request import CreateOrganizationRequest
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
    api_instance = mencoro.OrganizationsApi(api_client)
    x_mencoro_confirmation = 'x_mencoro_confirmation_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    create_organization_request = mencoro.CreateOrganizationRequest() # CreateOrganizationRequest | 

    try:
        # Create an organization
        api_response = api_instance.create_organization(x_mencoro_confirmation, idempotency_key, create_organization_request)
        print("The response of OrganizationsApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_mencoro_confirmation** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **create_organization_request** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)|  | 

### Return type

[**CreateOrganization201Response**](CreateOrganization201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Organization created. Your owner membership follows asynchronously, so a read immediately afterwards can answer 404 until it lands. |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key is not scoped to all organizations, or lacks \&quot;organization:manage\&quot; |  -  |
**409** | The confirmation is invalid, expired, already used, or its effects changed |  -  |
**428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlements**
> EntitlementsResource get_entitlements(organization_id)

Get an organization's plan allowance and consumption

Minimum role: owner. Returns what the current plan allows, how much of it has been consumed and when the allowance next resets, taken from the most recent subscription contract whether it is running or cancelled. An organization that has never subscribed answers `status: "none"` with every budget and consumption field null — null means "no plan on file, so not known", which is deliberately distinct from a budget or a consumption of zero. Commercial and provider details (prices, Stripe identifiers, internal tier codes) are not part of this contract.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.entitlements_resource import EntitlementsResource
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
    api_instance = mencoro.OrganizationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an organization's plan allowance and consumption
        api_response = api_instance.get_entitlements(organization_id)
        print("The response of OrganizationsApi->get_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 

### Return type

[**EntitlementsResource**](EntitlementsResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization&#39;s allowance and consumption |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller owns under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership_stats**
> GetMembershipStats200Response get_membership_stats(organization_id)

Membership, project and invitation counts for an organization

Minimum role: owner. Pre-computed counts of the organization's members, projects and outstanding invitations, read from a materialized view that is refreshed periodically — `computedAt` says when the snapshot was taken, so a member added since the last refresh is not counted yet. Every count is always an integer and a zero means zero; an organization whose row has not been computed yet answers 404 with code `organization_membership_stats_not_found`, never a body of zeros, so "none" and "not known yet" are never confused. Counts cover the whole organization, active and inactive alike: `totalMembersCount` includes suspended members, and `totalProjectsCount` includes archived projects. `pendingInvitationsCount` counts only invitations that are still pending and not yet expired.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.get_membership_stats200_response import GetMembershipStats200Response
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
    api_instance = mencoro.OrganizationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Membership, project and invitation counts for an organization
        api_response = api_instance.get_membership_stats(organization_id)
        print("The response of OrganizationsApi->get_membership_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_membership_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 

### Return type

[**GetMembershipStats200Response**](GetMembershipStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization&#39;s membership snapshot |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller owns under this id (code &#x60;organization_not_found&#x60;), or the snapshot has not been computed for it yet (code &#x60;organization_membership_stats_not_found&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> OrganizationResource get_organization(organization_id)

Get an organization

Minimum role: viewer. An organization outside the key's scope, or one the caller is not an active member of, answers 404 - the API never confirms that an inaccessible organization exists.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.organization_resource import OrganizationResource
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
    api_instance = mencoro.OrganizationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an organization
        api_response = api_instance.get_organization(organization_id)
        print("The response of OrganizationsApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_projected_monthly_checks**
> ProjectedMonthlyChecksResource get_organization_projected_monthly_checks(organization_id)

Project a month of check consumption from the current tracking configuration

Minimum role: viewer. What the organization's current configuration would consume in a month, in check budget units — the same unit `checkBudget` and `checksAvailable` are counted in by the entitlements operation — so the two are directly comparable when sizing a plan. The arithmetic is published so it can be reproduced rather than trusted: for each ACTIVE tracked query, runs per month (daily 30, weekly 4, monthly 1) multiplied by its nPasses, summed. A weekly query bills 4, not 4.345: a month is modelled as 30 days and 4 weeks, a planning convention rather than a calendar. Take `checkFrequency` and `nPasses` from the tracked-query listing and the arithmetic will match — though the two sides are read from different places and settle at different times: this figure is computed in the Postgres write model and served from a cache that background subscribers invalidate, while that listing reads an Elasticsearch projection. Immediately after a write the two can disagree; neither is wrong, they are catching up. PAUSED queries are excluded from both figures; archived PROJECTS are not — archiving a project does not pause its tracked queries, so they still count here, exactly as they do in countOrganizationTrackedQueries. `activeTrackedQueryCount` describes the same population as that count, minus the paused queries — but do not compute the difference to learn how many are paused: THIS OPERATION IS CACHED and that one is read live, so the two can disagree while the cache is invalidated in the background. This is a projection of the configuration, not a forecast of what will actually be spent: it does not look at the remaining plan budget, does not know which checks will be skipped or retried, and reserves and debits nothing. It is also not the `checkCost` of countTrackedQueries, which prices one round over one project rather than a month over the organization. Both values are never null: 0 means nothing is scheduled. This operation takes no query parameters — the population is fixed, and a parameter it cannot honour is rejected with 400 rather than silently ignored.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.projected_monthly_checks_resource import ProjectedMonthlyChecksResource
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
    api_instance = mencoro.OrganizationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Project a month of check consumption from the current tracking configuration
        api_response = api_instance.get_organization_projected_monthly_checks(organization_id)
        print("The response of OrganizationsApi->get_organization_projected_monthly_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_projected_monthly_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 

### Return type

[**ProjectedMonthlyChecksResource**](ProjectedMonthlyChecksResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The projected monthly checks and the active tracked queries behind them |  -  |
**400** | A query parameter was sent to an operation that accepts none; the details name it |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_stats**
> GetOrganizationStats200Response get_organization_stats(organization_id)

Headline counts for an organization

Minimum role: viewer. Active members, projects (total and active) and pending invitations, in one call. Every value is a count and is always known: 0 means the organization really has none of that thing, and no field is ever null. `members.total` counts ACTIVE memberships only, so a suspended member is not included; `projects.total` counts every project including archived ones, and `projects.active` the non-archived subset. This is a current-state snapshot and takes no date window.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.get_organization_stats200_response import GetOrganizationStats200Response
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
    api_instance = mencoro.OrganizationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Headline counts for an organization
        api_response = api_instance.get_organization_stats(organization_id)
        print("The response of OrganizationsApi->get_organization_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 

### Return type

[**GetOrganizationStats200Response**](GetOrganizationStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization counts |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organizations**
> ListOrganizations200Response list_organizations(limit=limit, offset=offset, search=search, status=status, sort_by=sort_by, sort_order=sort_order)

List accessible organizations

Returns the organizations the key's owner is an active member of, narrowed to the key's scope. A key scoped to all organizations also sees organizations joined after it was created.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.list_organizations200_response import ListOrganizations200Response
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
    api_instance = mencoro.OrganizationsApi(api_client)
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)
    search = 'search_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    sort_by = 'createdAt' # str |  (optional) (default to 'createdAt')
    sort_order = 'desc' # str |  (optional) (default to 'desc')

    try:
        # List accessible organizations
        api_response = api_instance.list_organizations(limit=limit, offset=offset, search=search, status=status, sort_by=sort_by, sort_order=sort_order)
        print("The response of OrganizationsApi->list_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **search** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;createdAt&#39;]
 **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**ListOrganizations200Response**](ListOrganizations200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accessible organizations |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_organization**
> OrganizationResource restore_organization(organization_id, x_mencoro_confirmation, idempotency_key)

Restore an archived organization

Minimum role: owner. Restoring reinstates the projects that were archived as part of archiving this organization - projects archived on their own stay archived - and aborts a pending subscription cancellation. Invitations cancelled by the archive are not reinstated. Preview it first to see which effects are reversible.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.organization_resource import OrganizationResource
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
    api_instance = mencoro.OrganizationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    x_mencoro_confirmation = 'x_mencoro_confirmation_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 

    try:
        # Restore an archived organization
        api_response = api_instance.restore_organization(organization_id, x_mencoro_confirmation, idempotency_key)
        print("The response of OrganizationsApi->restore_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->restore_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **x_mencoro_confirmation** | **str**|  | 
 **idempotency_key** | **str**|  | 

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization in its new state |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the organization:manage capability |  -  |
**404** | No organization the caller can access under this id |  -  |
**409** | The confirmation is invalid, expired, already used, or its declared effects changed; or the status transition is not allowed |  -  |
**428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization**
> OrganizationResource update_organization(organization_id, x_mencoro_confirmation, idempotency_key, update_organization_request)

Update an organization profile

Minimum role: owner. A partial update: omit a field to leave it alone, send it as null to clear it. Preview it first; the confirmation is bound to the current values, so an edit made by somebody else in between invalidates it rather than being silently overwritten. The organization image is deliberately NOT writable here, although the Mencoro app accepts one in the equivalent call: a published JSON API is the wrong place to carry a 10MB base64 blob in a body that also has to be fingerprinted for idempotency and digested for the confirmation. The image stays readable as `imageUrl`; changing it is done in the app.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.organization_resource import OrganizationResource
from mencoro.models.update_organization_request import UpdateOrganizationRequest
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
    api_instance = mencoro.OrganizationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    x_mencoro_confirmation = 'x_mencoro_confirmation_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    update_organization_request = mencoro.UpdateOrganizationRequest() # UpdateOrganizationRequest | 

    try:
        # Update an organization profile
        api_response = api_instance.update_organization(organization_id, x_mencoro_confirmation, idempotency_key, update_organization_request)
        print("The response of OrganizationsApi->update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **x_mencoro_confirmation** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **update_organization_request** | [**UpdateOrganizationRequest**](UpdateOrganizationRequest.md)|  | 

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated organization |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the organization:manage capability |  -  |
**404** | No organization the caller can access under this id |  -  |
**409** | The confirmation is invalid, expired, already used, or the organization changed since the preview |  -  |
**428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

