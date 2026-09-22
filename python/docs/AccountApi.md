# mencoro.AccountApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me**](AccountApi.md#get_me) | **GET** /api/v1/me | Get the authenticated identity
[**get_me_stats**](AccountApi.md#get_me_stats) | **GET** /api/v1/me/stats | Counts across everything the key can reach


# **get_me**
> MeResource get_me()

Get the authenticated identity

Returns the user the API key belongs to, plus the key's capabilities and scope. Use it to confirm which credential a call runs under.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.me_resource import MeResource
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
    api_instance = mencoro.AccountApi(api_client)

    try:
        # Get the authenticated identity
        api_response = api_instance.get_me()
        print("The response of AccountApi->get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_me: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authenticated identity |  -  |
**403** | The key lacks the read capability |  -  |
**401** | Missing or invalid API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_me_stats**
> GetMeStats200Response get_me_stats()

Counts across everything the key can reach

Aggregate counts over every organization the key's owner is an active member of, narrowed to the key's scope — the same set /api/v1/organizations pages through. `organizations.total` is that set's size; `projects.total` and `projects.active` count the projects inside it, archived ones included in the total and excluded from the active figure. Every value is an exact count: zero means zero, and no value here is ever null or unknown. Per-organization billing and usage figures are not part of this response; read them from the subscription and entitlements operations instead.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.get_me_stats200_response import GetMeStats200Response
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
    api_instance = mencoro.AccountApi(api_client)

    try:
        # Counts across everything the key can reach
        api_response = api_instance.get_me_stats()
        print("The response of AccountApi->get_me_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_me_stats: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Counts across the organizations the key can reach |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The key lacks the read capability, or the user it belongs to is no longer active |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

