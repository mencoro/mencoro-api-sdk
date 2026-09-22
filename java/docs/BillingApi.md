# BillingApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSubscription**](BillingApi.md#getSubscription) | **GET** /api/v1/organizations/{organizationId}/subscription | Get the subscription of an organization |


<a id="getSubscription"></a>
# **getSubscription**
> SubscriptionResource getSubscription(organizationId)

Get the subscription of an organization

Minimum role: viewer. The most recent subscription contract of the organization, whatever its state: tier, billing interval, check budget and consumption, and the cancellation and grace dates. An organization that has never subscribed answers 200 with \&quot;status\&quot;: \&quot;none\&quot; and every other field null - a null is \&quot;not applicable\&quot;, never a stand-in for a zero budget or zero consumption. Stripe identifiers, prices and payment methods are not part of this API.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    try {
      SubscriptionResource result = apiInstance.getSubscription(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#getSubscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | **UUID**|  | |

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The subscription contract, or the \&quot;none\&quot; state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

