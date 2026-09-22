# mencoro.InvitationsApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_invitation**](InvitationsApi.md#cancel_invitation) | **POST** /api/v1/organizations/{organizationId}/invitations/{invitationId}/cancel | Cancel a pending invitation
[**create_invitation**](InvitationsApi.md#create_invitation) | **POST** /api/v1/organizations/{organizationId}/invitations | Invite somebody to an organization
[**list_invitations**](InvitationsApi.md#list_invitations) | **GET** /api/v1/organizations/{organizationId}/invitations | List an organization&#39;s invitations


# **cancel_invitation**
> InvitationResource cancel_invitation(organization_id, invitation_id, x_mencoro_confirmation, idempotency_key)

Cancel a pending invitation

Minimum role: owner. The link already emailed to the invitee stops working. Only a pending invitation can be cancelled; one that was accepted, rejected or has expired is refused.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.invitation_resource import InvitationResource
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
    api_instance = mencoro.InvitationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    invitation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    x_mencoro_confirmation = 'x_mencoro_confirmation_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 

    try:
        # Cancel a pending invitation
        api_response = api_instance.cancel_invitation(organization_id, invitation_id, x_mencoro_confirmation, idempotency_key)
        print("The response of InvitationsApi->cancel_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->cancel_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **invitation_id** | **UUID**|  | 
 **x_mencoro_confirmation** | **str**|  | 
 **idempotency_key** | **str**|  | 

### Return type

[**InvitationResource**](InvitationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The invitation in its new state |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the organization:manage capability |  -  |
**404** | No organization or invitation the caller can access under these ids |  -  |
**409** | The confirmation is invalid, expired, already used, or its effects changed; or the invitation is not pending |  -  |
**428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invitation**
> CreateInvitation200Response create_invitation(organization_id, x_mencoro_confirmation, idempotency_key, create_invitation_request)

Invite somebody to an organization

Minimum role: owner. Sends an invitation email that expires after 14 days. If the address already belongs to an active member the call succeeds and creates nothing - answered as 200 with created=false rather than 201, so a client can tell the two apart. Preview it first; the preview says which of the two will happen.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.create_invitation200_response import CreateInvitation200Response
from mencoro.models.create_invitation_request import CreateInvitationRequest
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
    api_instance = mencoro.InvitationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    x_mencoro_confirmation = 'x_mencoro_confirmation_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    create_invitation_request = mencoro.CreateInvitationRequest() # CreateInvitationRequest | 

    try:
        # Invite somebody to an organization
        api_response = api_instance.create_invitation(organization_id, x_mencoro_confirmation, idempotency_key, create_invitation_request)
        print("The response of InvitationsApi->create_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->create_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **x_mencoro_confirmation** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **create_invitation_request** | [**CreateInvitationRequest**](CreateInvitationRequest.md)|  | 

### Return type

[**CreateInvitation200Response**](CreateInvitation200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The invitation that was created. &#x60;created&#x60; is true; branch on it rather than on the status code, so one code path handles both answers. |  -  |
**200** | Nothing was created because the address already belongs to an active member. Not an error: the end state the caller asked for already holds. |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the organization:manage capability |  -  |
**404** | No organization the caller can access under this id |  -  |
**409** | The confirmation is invalid, expired, already used, or its effects changed; or a pending invitation already exists for this address |  -  |
**428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invitations**
> ListInvitations200Response list_invitations(organization_id, limit=limit, offset=offset, search=search, status=status, sort_by=sort_by, sort_order=sort_order)

List an organization's invitations

Minimum role: owner. Returns the invitations issued for this organization, in every state. The invitation token is never returned. `status` matches the stored state, so an invitation that has passed its `expiresAt` is still listed as pending until it is transitioned; compare `expiresAt` to decide. Rows are ordered by the chosen sort field, and invitations sharing the same value keep no guaranteed relative order across pages.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.list_invitations200_response import ListInvitations200Response
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
    api_instance = mencoro.InvitationsApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)
    search = 'search_example' # str | Matches part of the invited email address. (optional)
    status = 'status_example' # str | Absent means every state. (optional)
    sort_by = 'createdAt' # str |  (optional) (default to 'createdAt')
    sort_order = 'desc' # str |  (optional) (default to 'desc')

    try:
        # List an organization's invitations
        api_response = api_instance.list_invitations(organization_id, limit=limit, offset=offset, search=search, status=status, sort_by=sort_by, sort_order=sort_order)
        print("The response of InvitationsApi->list_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->list_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **search** | **str**| Matches part of the invited email address. | [optional] 
 **status** | **str**| Absent means every state. | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;createdAt&#39;]
 **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**ListInvitations200Response**](ListInvitations200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization&#39;s invitations |  -  |
**400** | A parameter was rejected; the details name the field |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller owns under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

