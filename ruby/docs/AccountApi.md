# Mencoro::AccountApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_me**](AccountApi.md#get_me) | **GET** /api/v1/me | Get the authenticated identity |
| [**get_me_stats**](AccountApi.md#get_me_stats) | **GET** /api/v1/me/stats | Counts across everything the key can reach |


## get_me

> <MeResource> get_me

Get the authenticated identity

Returns the user the API key belongs to, plus the key's capabilities and scope. Use it to confirm which credential a call runs under.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AccountApi.new

begin
  # Get the authenticated identity
  result = api_instance.get_me
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling AccountApi->get_me: #{e}"
end
```

#### Using the get_me_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MeResource>, Integer, Hash)> get_me_with_http_info

```ruby
begin
  # Get the authenticated identity
  data, status_code, headers = api_instance.get_me_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MeResource>
rescue Mencoro::ApiError => e
  puts "Error when calling AccountApi->get_me_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**MeResource**](MeResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_me_stats

> <GetMeStats200Response> get_me_stats

Counts across everything the key can reach

Aggregate counts over every organization the key's owner is an active member of, narrowed to the key's scope — the same set /api/v1/organizations pages through. `organizations.total` is that set's size; `projects.total` and `projects.active` count the projects inside it, archived ones included in the total and excluded from the active figure. Every value is an exact count: zero means zero, and no value here is ever null or unknown. Per-organization billing and usage figures are not part of this response; read them from the subscription and entitlements operations instead.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::AccountApi.new

begin
  # Counts across everything the key can reach
  result = api_instance.get_me_stats
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling AccountApi->get_me_stats: #{e}"
end
```

#### Using the get_me_stats_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<GetMeStats200Response>, Integer, Hash)> get_me_stats_with_http_info

```ruby
begin
  # Counts across everything the key can reach
  data, status_code, headers = api_instance.get_me_stats_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <GetMeStats200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling AccountApi->get_me_stats_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMeStats200Response**](GetMeStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

