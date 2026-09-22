# AccountApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMe**](AccountApi.md#getMe) | **GET** /api/v1/me | Get the authenticated identity |
| [**getMeStats**](AccountApi.md#getMeStats) | **GET** /api/v1/me/stats | Counts across everything the key can reach |


<a id="getMe"></a>
# **getMe**
> MeResource getMe()

Get the authenticated identity

Returns the user the API key belongs to, plus the key&#39;s capabilities and scope. Use it to confirm which credential a call runs under.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      MeResource result = apiInstance.getMe();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#getMe");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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
| **200** | The authenticated identity |  -  |
| **403** | The key lacks the read capability |  -  |
| **401** | Missing or invalid API key |  -  |

<a id="getMeStats"></a>
# **getMeStats**
> GetMeStats200Response getMeStats()

Counts across everything the key can reach

Aggregate counts over every organization the key&#39;s owner is an active member of, narrowed to the key&#39;s scope — the same set /api/v1/organizations pages through. &#x60;organizations.total&#x60; is that set&#39;s size; &#x60;projects.total&#x60; and &#x60;projects.active&#x60; count the projects inside it, archived ones included in the total and excluded from the active figure. Every value is an exact count: zero means zero, and no value here is ever null or unknown. Per-organization billing and usage figures are not part of this response; read them from the subscription and entitlements operations instead.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      GetMeStats200Response result = apiInstance.getMeStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#getMeStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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
| **200** | Counts across the organizations the key can reach |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability, or the user it belongs to is no longer active |  -  |

