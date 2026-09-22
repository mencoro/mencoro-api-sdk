# AccountApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMe**](AccountApi.md#getme) | **GET** /api/v1/me | Get the authenticated identity |
| [**getMeStats**](AccountApi.md#getmestats) | **GET** /api/v1/me/stats | Counts across everything the key can reach |



## getMe

> MeResource getMe()

Get the authenticated identity

Returns the user the API key belongs to, plus the key\&#39;s capabilities and scope. Use it to confirm which credential a call runs under.

### Example

```ts
import {
  Configuration,
  AccountApi,
} from '@mencoro/api';
import type { GetMeRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AccountApi(config);

  try {
    const data = await api.getMe();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**MeResource**](MeResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The authenticated identity |  -  |
| **403** | The key lacks the read capability |  -  |
| **401** | Missing or invalid API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getMeStats

> GetMeStats200Response getMeStats()

Counts across everything the key can reach

Aggregate counts over every organization the key\&#39;s owner is an active member of, narrowed to the key\&#39;s scope — the same set /api/v1/organizations pages through. &#x60;organizations.total&#x60; is that set\&#39;s size; &#x60;projects.total&#x60; and &#x60;projects.active&#x60; count the projects inside it, archived ones included in the total and excluded from the active figure. Every value is an exact count: zero means zero, and no value here is ever null or unknown. Per-organization billing and usage figures are not part of this response; read them from the subscription and entitlements operations instead.

### Example

```ts
import {
  Configuration,
  AccountApi,
} from '@mencoro/api';
import type { GetMeStatsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AccountApi(config);

  try {
    const data = await api.getMeStats();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMeStats200Response**](GetMeStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Counts across the organizations the key can reach |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability, or the user it belongs to is no longer active |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

