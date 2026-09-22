# Mencoro::BillingApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_subscription**](BillingApi.md#get_subscription) | **GET** /api/v1/organizations/{organizationId}/subscription | Get the subscription of an organization |


## get_subscription

> <SubscriptionResource> get_subscription(organization_id)

Get the subscription of an organization

Minimum role: viewer. The most recent subscription contract of the organization, whatever its state: tier, billing interval, check budget and consumption, and the cancellation and grace dates. An organization that has never subscribed answers 200 with \"status\": \"none\" and every other field null - a null is \"not applicable\", never a stand-in for a zero budget or zero consumption. Stripe identifiers, prices and payment methods are not part of this API.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::BillingApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Get the subscription of an organization
  result = api_instance.get_subscription(organization_id)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling BillingApi->get_subscription: #{e}"
end
```

#### Using the get_subscription_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SubscriptionResource>, Integer, Hash)> get_subscription_with_http_info(organization_id)

```ruby
begin
  # Get the subscription of an organization
  data, status_code, headers = api_instance.get_subscription_with_http_info(organization_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SubscriptionResource>
rescue Mencoro::ApiError => e
  puts "Error when calling BillingApi->get_subscription_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

