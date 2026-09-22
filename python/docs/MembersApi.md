# mencoro.MembersApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_member_role**](MembersApi.md#change_member_role) | **PATCH** /api/v1/organizations/{organizationId}/members/{memberId} | Change a member role
[**get_member**](MembersApi.md#get_member) | **GET** /api/v1/organizations/{organizationId}/members/{memberId} | Get one organization membership
[**list_members**](MembersApi.md#list_members) | **GET** /api/v1/organizations/{organizationId}/members | List an organization&#39;s members
[**reactivate_member**](MembersApi.md#reactivate_member) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/reactivate | Reactivate a suspended member
[**suspend_member**](MembersApi.md#suspend_member) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/suspend | Suspend a member


# **change_member_role**
> MemberResource change_member_role(organization_id, member_id, x_mencoro_confirmation, idempotency_key, change_member_role_request)

Change a member role

Minimum role: owner. The role of a suspended member cannot be changed, and the last active owner cannot be demoted. Preview it first: the confirmation is bound to the number of active owners, so another owner being suspended in between invalidates it rather than stranding the organization.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.change_member_role_request import ChangeMemberRoleRequest
from mencoro.models.member_resource import MemberResource
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
    api_instance = mencoro.MembersApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    member_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    x_mencoro_confirmation = 'x_mencoro_confirmation_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    change_member_role_request = mencoro.ChangeMemberRoleRequest() # ChangeMemberRoleRequest | 

    try:
        # Change a member role
        api_response = api_instance.change_member_role(organization_id, member_id, x_mencoro_confirmation, idempotency_key, change_member_role_request)
        print("The response of MembersApi->change_member_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->change_member_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **member_id** | **UUID**|  | 
 **x_mencoro_confirmation** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **change_member_role_request** | [**ChangeMemberRoleRequest**](ChangeMemberRoleRequest.md)|  | 

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The membership in its new state |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the organization:manage capability |  -  |
**404** | No organization or membership the caller can access under these ids |  -  |
**409** | The confirmation is invalid, expired, already used, or its effects changed; the member is suspended; or this is the last active owner |  -  |
**428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member**
> MemberResource get_member(organization_id, member_id)

Get one organization membership

Minimum role: owner — the same floor the members listing enforces, because a caller who can page the roster has already seen this record. Returns the facts of one membership: its role, whether it is active or suspended, and when it was joined. It does NOT describe the person behind it: no name, no email address, no phone number and no profile image, so a membership id can never be turned into a contact lookup. The membership is read from PostgreSQL, the same row at the same freshness the listing publishes. A membership belonging to another organization answers 404, exactly as an unknown or malformed id does, so the API never confirms that an inaccessible membership exists; the one 403 is a key without the read capability. The response carries no organizationId — it is the one in the path — and no creation timestamp; joinedAt is the membership fact. No query parameters are accepted.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.member_resource import MemberResource
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
    api_instance = mencoro.MembersApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    member_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The membership id, not the user id. Must belong to the organization in the path.

    try:
        # Get one organization membership
        api_response = api_instance.get_member(organization_id, member_id)
        print("The response of MembersApi->get_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->get_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **member_id** | **UUID**| The membership id, not the user id. Must belong to the organization in the path. | 

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The membership |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller owns, or no membership of it, under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_members**
> ListMembers200Response list_members(organization_id, limit=limit, offset=offset, status=status, sort_by=sort_by, sort_order=sort_order)

List an organization's members

Minimum role: owner. The application exposes this roster twice and the two disagree — its member screen shows it to any viewer, while its non-BFF endpoint requires an owner — so the published API takes the stricter of the two and requires an owner. A membership describes the membership, not the person: names and email addresses are never returned here, and there is no search parameter, because both would turn the roster into a contact export. Omitting "status" returns active and suspended memberships alike. Sorting by "role" is alphabetical on the role name, not by seniority.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.list_members200_response import ListMembers200Response
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
    api_instance = mencoro.MembersApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)
    status = 'status_example' # str | Absent means both states. (optional)
    sort_by = 'joinedAt' # str |  (optional) (default to 'joinedAt')
    sort_order = 'desc' # str |  (optional) (default to 'desc')

    try:
        # List an organization's members
        api_response = api_instance.list_members(organization_id, limit=limit, offset=offset, status=status, sort_by=sort_by, sort_order=sort_order)
        print("The response of MembersApi->list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->list_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **status** | **str**| Absent means both states. | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;joinedAt&#39;]
 **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**ListMembers200Response**](ListMembers200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization&#39;s memberships |  -  |
**400** | A parameter was rejected; the details name the field. A limit above 100 is refused, not clamped |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller owns under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_member**
> MemberResource reactivate_member(organization_id, member_id, x_mencoro_confirmation, idempotency_key)

Reactivate a suspended member

Minimum role: owner. The member keeps the role they had and regains access on their very next request. A member who is already active cannot be reactivated.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.member_resource import MemberResource
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
    api_instance = mencoro.MembersApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    member_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    x_mencoro_confirmation = 'x_mencoro_confirmation_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 

    try:
        # Reactivate a suspended member
        api_response = api_instance.reactivate_member(organization_id, member_id, x_mencoro_confirmation, idempotency_key)
        print("The response of MembersApi->reactivate_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->reactivate_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **member_id** | **UUID**|  | 
 **x_mencoro_confirmation** | **str**|  | 
 **idempotency_key** | **str**|  | 

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The membership in its new state |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the organization:manage capability |  -  |
**404** | No organization or membership the caller can access under these ids |  -  |
**409** | The confirmation is invalid, expired, already used, or its effects changed; or the member is already active |  -  |
**428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_member**
> MemberResource suspend_member(organization_id, member_id, x_mencoro_confirmation, idempotency_key)

Suspend a member

Minimum role: owner. The member loses access on their very next request, including through any API key they own that is scoped to this organization. The last active owner cannot be suspended.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.member_resource import MemberResource
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
    api_instance = mencoro.MembersApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    member_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    x_mencoro_confirmation = 'x_mencoro_confirmation_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 

    try:
        # Suspend a member
        api_response = api_instance.suspend_member(organization_id, member_id, x_mencoro_confirmation, idempotency_key)
        print("The response of MembersApi->suspend_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembersApi->suspend_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **member_id** | **UUID**|  | 
 **x_mencoro_confirmation** | **str**|  | 
 **idempotency_key** | **str**|  | 

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The membership in its new state |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the organization:manage capability |  -  |
**404** | No organization or membership the caller can access under these ids |  -  |
**409** | The confirmation is invalid, expired, already used, or its effects changed; the member is already suspended; or this is the last active owner |  -  |
**428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

