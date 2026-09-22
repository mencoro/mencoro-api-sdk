# Mencoro::InvitationsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**cancel_invitation**](InvitationsApi.md#cancel_invitation) | **POST** /api/v1/organizations/{organizationId}/invitations/{invitationId}/cancel | Cancel a pending invitation |
| [**create_invitation**](InvitationsApi.md#create_invitation) | **POST** /api/v1/organizations/{organizationId}/invitations | Invite somebody to an organization |
| [**list_invitations**](InvitationsApi.md#list_invitations) | **GET** /api/v1/organizations/{organizationId}/invitations | List an organization&#39;s invitations |


## cancel_invitation

> <InvitationResource> cancel_invitation(organization_id, invitation_id, x_mencoro_confirmation, idempotency_key)

Cancel a pending invitation

Minimum role: owner. The link already emailed to the invitee stops working. Only a pending invitation can be cancelled; one that was accepted, rejected or has expired is refused.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::InvitationsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
invitation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
x_mencoro_confirmation = 'x_mencoro_confirmation_example' # String | 
idempotency_key = 'idempotency_key_example' # String | 

begin
  # Cancel a pending invitation
  result = api_instance.cancel_invitation(organization_id, invitation_id, x_mencoro_confirmation, idempotency_key)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling InvitationsApi->cancel_invitation: #{e}"
end
```

#### Using the cancel_invitation_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InvitationResource>, Integer, Hash)> cancel_invitation_with_http_info(organization_id, invitation_id, x_mencoro_confirmation, idempotency_key)

```ruby
begin
  # Cancel a pending invitation
  data, status_code, headers = api_instance.cancel_invitation_with_http_info(organization_id, invitation_id, x_mencoro_confirmation, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InvitationResource>
rescue Mencoro::ApiError => e
  puts "Error when calling InvitationsApi->cancel_invitation_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **invitation_id** | **String** |  |  |
| **x_mencoro_confirmation** | **String** |  |  |
| **idempotency_key** | **String** |  |  |

### Return type

[**InvitationResource**](InvitationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## create_invitation

> <CreateInvitation200Response> create_invitation(organization_id, x_mencoro_confirmation, idempotency_key, create_invitation_request)

Invite somebody to an organization

Minimum role: owner. Sends an invitation email that expires after 14 days. If the address already belongs to an active member the call succeeds and creates nothing - answered as 200 with created=false rather than 201, so a client can tell the two apart. Preview it first; the preview says which of the two will happen.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::InvitationsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
x_mencoro_confirmation = 'x_mencoro_confirmation_example' # String | 
idempotency_key = 'idempotency_key_example' # String | 
create_invitation_request = Mencoro::CreateInvitationRequest.new # CreateInvitationRequest | 

begin
  # Invite somebody to an organization
  result = api_instance.create_invitation(organization_id, x_mencoro_confirmation, idempotency_key, create_invitation_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling InvitationsApi->create_invitation: #{e}"
end
```

#### Using the create_invitation_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CreateInvitation200Response>, Integer, Hash)> create_invitation_with_http_info(organization_id, x_mencoro_confirmation, idempotency_key, create_invitation_request)

```ruby
begin
  # Invite somebody to an organization
  data, status_code, headers = api_instance.create_invitation_with_http_info(organization_id, x_mencoro_confirmation, idempotency_key, create_invitation_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CreateInvitation200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling InvitationsApi->create_invitation_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **x_mencoro_confirmation** | **String** |  |  |
| **idempotency_key** | **String** |  |  |
| **create_invitation_request** | [**CreateInvitationRequest**](CreateInvitationRequest.md) |  |  |

### Return type

[**CreateInvitation200Response**](CreateInvitation200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## list_invitations

> <ListInvitations200Response> list_invitations(organization_id, opts)

List an organization's invitations

Minimum role: owner. Returns the invitations issued for this organization, in every state. The invitation token is never returned. `status` matches the stored state, so an invitation that has passed its `expiresAt` is still listed as pending until it is transitioned; compare `expiresAt` to decide. Rows are ordered by the chosen sort field, and invitations sharing the same value keep no guaranteed relative order across pages.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::InvitationsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  limit: 56, # Integer | 
  offset: 56, # Integer | 
  search: 'search_example', # String | Matches part of the invited email address.
  status: 'pending', # String | Absent means every state.
  sort_by: 'createdAt', # String | 
  sort_order: 'asc' # String | 
}

begin
  # List an organization's invitations
  result = api_instance.list_invitations(organization_id, opts)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling InvitationsApi->list_invitations: #{e}"
end
```

#### Using the list_invitations_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListInvitations200Response>, Integer, Hash)> list_invitations_with_http_info(organization_id, opts)

```ruby
begin
  # List an organization's invitations
  data, status_code, headers = api_instance.list_invitations_with_http_info(organization_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListInvitations200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling InvitationsApi->list_invitations_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **limit** | **Integer** |  | [optional][default to 20] |
| **offset** | **Integer** |  | [optional][default to 0] |
| **search** | **String** | Matches part of the invited email address. | [optional] |
| **status** | **String** | Absent means every state. | [optional] |
| **sort_by** | **String** |  | [optional][default to &#39;createdAt&#39;] |
| **sort_order** | **String** |  | [optional][default to &#39;desc&#39;] |

### Return type

[**ListInvitations200Response**](ListInvitations200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

