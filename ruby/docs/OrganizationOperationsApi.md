# Mencoro::OrganizationOperationsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**preview_organization_operation**](OrganizationOperationsApi.md#preview_organization_operation) | **POST** /api/v1/organization-operation-previews | Preview an organization operation and obtain a confirmation |


## preview_organization_operation

> <PreviewOrganizationOperation200Response> preview_organization_operation(preview_organization_operation_request)

Preview an organization operation and obtain a confirmation

Organization, member and invitation changes need two calls. This one reports the concrete changes, the side effects, the warnings and the conditions, and returns a confirmation valid for five minutes. Send it back in the X-Mencoro-Confirmation header, together with an Idempotency-Key, on the call that performs the operation. Previewing has no effects of any kind.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::OrganizationOperationsApi.new
preview_organization_operation_request = Mencoro::PreviewOrganizationOperationRequest.new # PreviewOrganizationOperationRequest | 

begin
  # Preview an organization operation and obtain a confirmation
  result = api_instance.preview_organization_operation(preview_organization_operation_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling OrganizationOperationsApi->preview_organization_operation: #{e}"
end
```

#### Using the preview_organization_operation_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PreviewOrganizationOperation200Response>, Integer, Hash)> preview_organization_operation_with_http_info(preview_organization_operation_request)

```ruby
begin
  # Preview an organization operation and obtain a confirmation
  data, status_code, headers = api_instance.preview_organization_operation_with_http_info(preview_organization_operation_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PreviewOrganizationOperation200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling OrganizationOperationsApi->preview_organization_operation_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **preview_organization_operation_request** | [**PreviewOrganizationOperationRequest**](PreviewOrganizationOperationRequest.md) |  |  |

### Return type

[**PreviewOrganizationOperation200Response**](PreviewOrganizationOperation200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

