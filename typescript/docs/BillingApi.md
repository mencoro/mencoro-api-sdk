# BillingApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSubscription**](BillingApi.md#getsubscription) | **GET** /api/v1/organizations/{organizationId}/subscription | Get the subscription of an organization |



## getSubscription

> SubscriptionResource getSubscription(organizationId)

Get the subscription of an organization

Minimum role: viewer. The most recent subscription contract of the organization, whatever its state: tier, billing interval, check budget and consumption, and the cancellation and grace dates. An organization that has never subscribed answers 200 with \&quot;status\&quot;: \&quot;none\&quot; and every other field null - a null is \&quot;not applicable\&quot;, never a stand-in for a zero budget or zero consumption. Stripe identifiers, prices and payment methods are not part of this API.

### Example

```ts
import {
  Configuration,
  BillingApi,
} from '@mencoro/api';
import type { GetSubscriptionRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new BillingApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetSubscriptionRequest;

  try {
    const data = await api.getSubscription(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The subscription contract, or the \&quot;none\&quot; state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

