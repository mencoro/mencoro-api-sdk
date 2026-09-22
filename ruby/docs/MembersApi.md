# Mencoro::MembersApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**change_member_role**](MembersApi.md#change_member_role) | **PATCH** /api/v1/organizations/{organizationId}/members/{memberId} | Change a member role |
| [**get_member**](MembersApi.md#get_member) | **GET** /api/v1/organizations/{organizationId}/members/{memberId} | Get one organization membership |
| [**list_members**](MembersApi.md#list_members) | **GET** /api/v1/organizations/{organizationId}/members | List an organization&#39;s members |
| [**reactivate_member**](MembersApi.md#reactivate_member) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/reactivate | Reactivate a suspended member |
| [**suspend_member**](MembersApi.md#suspend_member) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/suspend | Suspend a member |


## change_member_role

> <MemberResource> change_member_role(organization_id, member_id, x_mencoro_confirmation, idempotency_key, change_member_role_request)

Change a member role

Minimum role: owner. The role of a suspended member cannot be changed, and the last active owner cannot be demoted. Preview it first: the confirmation is bound to the number of active owners, so another owner being suspended in between invalidates it rather than stranding the organization.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::MembersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
member_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
x_mencoro_confirmation = 'x_mencoro_confirmation_example' # String | 
idempotency_key = 'idempotency_key_example' # String | 
change_member_role_request = Mencoro::ChangeMemberRoleRequest.new # ChangeMemberRoleRequest | 

begin
  # Change a member role
  result = api_instance.change_member_role(organization_id, member_id, x_mencoro_confirmation, idempotency_key, change_member_role_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling MembersApi->change_member_role: #{e}"
end
```

#### Using the change_member_role_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MemberResource>, Integer, Hash)> change_member_role_with_http_info(organization_id, member_id, x_mencoro_confirmation, idempotency_key, change_member_role_request)

```ruby
begin
  # Change a member role
  data, status_code, headers = api_instance.change_member_role_with_http_info(organization_id, member_id, x_mencoro_confirmation, idempotency_key, change_member_role_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MemberResource>
rescue Mencoro::ApiError => e
  puts "Error when calling MembersApi->change_member_role_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **member_id** | **String** |  |  |
| **x_mencoro_confirmation** | **String** |  |  |
| **idempotency_key** | **String** |  |  |
| **change_member_role_request** | [**ChangeMemberRoleRequest**](ChangeMemberRoleRequest.md) |  |  |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get_member

> <MemberResource> get_member(organization_id, member_id)

Get one organization membership

Minimum role: owner — the same floor the members listing enforces, because a caller who can page the roster has already seen this record. Returns the facts of one membership: its role, whether it is active or suspended, and when it was joined. It does NOT describe the person behind it: no name, no email address, no phone number and no profile image, so a membership id can never be turned into a contact lookup. The membership is read from PostgreSQL, the same row at the same freshness the listing publishes. A membership belonging to another organization answers 404, exactly as an unknown or malformed id does, so the API never confirms that an inaccessible membership exists; the one 403 is a key without the read capability. The response carries no organizationId — it is the one in the path — and no creation timestamp; joinedAt is the membership fact. No query parameters are accepted.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::MembersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
member_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | The membership id, not the user id. Must belong to the organization in the path.

begin
  # Get one organization membership
  result = api_instance.get_member(organization_id, member_id)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling MembersApi->get_member: #{e}"
end
```

#### Using the get_member_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MemberResource>, Integer, Hash)> get_member_with_http_info(organization_id, member_id)

```ruby
begin
  # Get one organization membership
  data, status_code, headers = api_instance.get_member_with_http_info(organization_id, member_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MemberResource>
rescue Mencoro::ApiError => e
  puts "Error when calling MembersApi->get_member_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **member_id** | **String** | The membership id, not the user id. Must belong to the organization in the path. |  |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_members

> <ListMembers200Response> list_members(organization_id, opts)

List an organization's members

Minimum role: owner. The application exposes this roster twice and the two disagree — its member screen shows it to any viewer, while its non-BFF endpoint requires an owner — so the published API takes the stricter of the two and requires an owner. A membership describes the membership, not the person: names and email addresses are never returned here, and there is no search parameter, because both would turn the roster into a contact export. Omitting \"status\" returns active and suspended memberships alike. Sorting by \"role\" is alphabetical on the role name, not by seniority.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::MembersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  limit: 56, # Integer | 
  offset: 56, # Integer | 
  status: 'active', # String | Absent means both states.
  sort_by: 'joinedAt', # String | 
  sort_order: 'asc' # String | 
}

begin
  # List an organization's members
  result = api_instance.list_members(organization_id, opts)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling MembersApi->list_members: #{e}"
end
```

#### Using the list_members_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListMembers200Response>, Integer, Hash)> list_members_with_http_info(organization_id, opts)

```ruby
begin
  # List an organization's members
  data, status_code, headers = api_instance.list_members_with_http_info(organization_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListMembers200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling MembersApi->list_members_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **limit** | **Integer** |  | [optional][default to 20] |
| **offset** | **Integer** |  | [optional][default to 0] |
| **status** | **String** | Absent means both states. | [optional] |
| **sort_by** | **String** |  | [optional][default to &#39;joinedAt&#39;] |
| **sort_order** | **String** |  | [optional][default to &#39;desc&#39;] |

### Return type

[**ListMembers200Response**](ListMembers200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## reactivate_member

> <MemberResource> reactivate_member(organization_id, member_id, x_mencoro_confirmation, idempotency_key)

Reactivate a suspended member

Minimum role: owner. The member keeps the role they had and regains access on their very next request. A member who is already active cannot be reactivated.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::MembersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
member_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
x_mencoro_confirmation = 'x_mencoro_confirmation_example' # String | 
idempotency_key = 'idempotency_key_example' # String | 

begin
  # Reactivate a suspended member
  result = api_instance.reactivate_member(organization_id, member_id, x_mencoro_confirmation, idempotency_key)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling MembersApi->reactivate_member: #{e}"
end
```

#### Using the reactivate_member_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MemberResource>, Integer, Hash)> reactivate_member_with_http_info(organization_id, member_id, x_mencoro_confirmation, idempotency_key)

```ruby
begin
  # Reactivate a suspended member
  data, status_code, headers = api_instance.reactivate_member_with_http_info(organization_id, member_id, x_mencoro_confirmation, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MemberResource>
rescue Mencoro::ApiError => e
  puts "Error when calling MembersApi->reactivate_member_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **member_id** | **String** |  |  |
| **x_mencoro_confirmation** | **String** |  |  |
| **idempotency_key** | **String** |  |  |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suspend_member

> <MemberResource> suspend_member(organization_id, member_id, x_mencoro_confirmation, idempotency_key)

Suspend a member

Minimum role: owner. The member loses access on their very next request, including through any API key they own that is scoped to this organization. The last active owner cannot be suspended.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::MembersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
member_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
x_mencoro_confirmation = 'x_mencoro_confirmation_example' # String | 
idempotency_key = 'idempotency_key_example' # String | 

begin
  # Suspend a member
  result = api_instance.suspend_member(organization_id, member_id, x_mencoro_confirmation, idempotency_key)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling MembersApi->suspend_member: #{e}"
end
```

#### Using the suspend_member_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MemberResource>, Integer, Hash)> suspend_member_with_http_info(organization_id, member_id, x_mencoro_confirmation, idempotency_key)

```ruby
begin
  # Suspend a member
  data, status_code, headers = api_instance.suspend_member_with_http_info(organization_id, member_id, x_mencoro_confirmation, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MemberResource>
rescue Mencoro::ApiError => e
  puts "Error when calling MembersApi->suspend_member_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **member_id** | **String** |  |  |
| **x_mencoro_confirmation** | **String** |  |  |
| **idempotency_key** | **String** |  |  |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

