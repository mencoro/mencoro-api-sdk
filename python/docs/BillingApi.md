# mencoro.BillingApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscription**](BillingApi.md#get_subscription) | **GET** /api/v1/organizations/{organizationId}/subscription | Get the subscription of an organization


# **get_subscription**
> SubscriptionResource get_subscription(organization_id)

Get the subscription of an organization

Minimum role: viewer. The most recent subscription contract of the organization, whatever its state: tier, billing interval, check budget and consumption, and the cancellation and grace dates. An organization that has never subscribed answers 200 with "status": "none" and every other field null - a null is "not applicable", never a stand-in for a zero budget or zero consumption. Stripe identifiers, prices and payment methods are not part of this API.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.subscription_resource import SubscriptionResource
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
    api_instance = mencoro.BillingApi(api_client)
    organization_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get the subscription of an organization
        api_response = api_instance.get_subscription(organization_id)
        print("The response of BillingApi->get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **UUID**|  | 

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
**200** | The subscription contract, or the \&quot;none\&quot; state |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability |  -  |
**404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

