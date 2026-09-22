# DiscoveryApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**startBrandDiscoveryJob**](DiscoveryApi.md#startBrandDiscoveryJob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/brands | Start a brand discovery job for a project |
| [**startBrandNameSuggestionJob**](DiscoveryApi.md#startBrandNameSuggestionJob) | **POST** /api/v1/organizations/{organizationId}/brand-name-suggestions | Start a brand-name alias suggestion job |
| [**startKeywordDiscoveryJob**](DiscoveryApi.md#startKeywordDiscoveryJob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/keywords | Start a keyword discovery job for a project |
| [**startPromptDiscoveryJob**](DiscoveryApi.md#startPromptDiscoveryJob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/prompts | Start a geo prompt discovery job for a project |


<a id="startBrandDiscoveryJob"></a>
# **startBrandDiscoveryJob**
> AcceptedJobResource startBrandDiscoveryJob(organizationId, projectId, idempotencyKey, startBrandDiscoveryJobRequest)

Start a brand discovery job for a project

Minimum role: manager. Starts background discovery of the brands and competitors around a project and answers 202 with the job to poll; it never returns brands inline. The job PROPOSES names: it creates and updates nothing, so neither the brand profile nor the competitor list changes because this endpoint was called. The organization must be active. Unlike keyword and prompt discovery this operation does not require an entitled subscription, matching the application behaviour it mirrors. Ten starts per minute per organization, counted across every key of every member and shared with the same operation in the Mencoro app; a retry carrying an Idempotency-Key already answered is served from the record and does not count. A project whose brand monitoring profile has not been created yet is still accepted and still billed: the job runs grounded on the project name alone, with no website domains, brand names or competitors to work from, and completes normally. Configure the brand profile first if you want the discovery grounded.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.DiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    DiscoveryApi apiInstance = new DiscoveryApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | Must belong to the organization in the path.
    String idempotencyKey = "idempotencyKey_example"; // String | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    StartBrandDiscoveryJobRequest startBrandDiscoveryJobRequest = new StartBrandDiscoveryJobRequest(); // StartBrandDiscoveryJobRequest | 
    try {
      AcceptedJobResource result = apiInstance.startBrandDiscoveryJob(organizationId, projectId, idempotencyKey, startBrandDiscoveryJobRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryApi#startBrandDiscoveryJob");
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
| **projectId** | **UUID**| Must belong to the organization in the path. | |
| **idempotencyKey** | **String**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | |
| **startBrandDiscoveryJobRequest** | [**StartBrandDiscoveryJobRequest**](StartBrandDiscoveryJobRequest.md)|  | [optional] |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The discovery job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten brand discovery starts per minute, or the key exceeded its request budget |  -  |

<a id="startBrandNameSuggestionJob"></a>
# **startBrandNameSuggestionJob**
> AcceptedJobResource startBrandNameSuggestionJob(organizationId, idempotencyKey, startBrandNameSuggestionJobRequest)

Start a brand-name alias suggestion job

Minimum role: manager. Starts a background, web-search-grounded job that suggests alias spellings for one entity - a brand, a project or a competitor - described entirely by the body, and answers 202 with the job to poll; it never returns suggestions inline. The entity need not exist: nothing is looked up, nothing is attached and nothing is saved, so the suggestions are the caller&#39;s to apply. Names sent in &#x60;enteredBrandNames&#x60; are excluded from the result. The organization must be active; no subscription is required, matching the application behaviour this mirrors. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.DiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    DiscoveryApi apiInstance = new DiscoveryApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    String idempotencyKey = "idempotencyKey_example"; // String | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    StartBrandNameSuggestionJobRequest startBrandNameSuggestionJobRequest = new StartBrandNameSuggestionJobRequest(); // StartBrandNameSuggestionJobRequest | 
    try {
      AcceptedJobResource result = apiInstance.startBrandNameSuggestionJob(organizationId, idempotencyKey, startBrandNameSuggestionJobRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryApi#startBrandNameSuggestionJob");
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
| **idempotencyKey** | **String**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | |
| **startBrandNameSuggestionJobRequest** | [**StartBrandNameSuggestionJobRequest**](StartBrandNameSuggestionJobRequest.md)|  | |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The suggestion job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten suggestion starts per minute, or the key exceeded its request budget |  -  |

<a id="startKeywordDiscoveryJob"></a>
# **startKeywordDiscoveryJob**
> AcceptedJobResource startKeywordDiscoveryJob(organizationId, projectId, idempotencyKey, startKeywordDiscoveryJobRequest)

Start a keyword discovery job for a project

Minimum role: manager. Starts background keyword discovery from free-text seed input and answers 202 with the job to poll; it never returns keywords inline. The job SUGGESTS keywords - it creates no tracked queries and changes nothing in the project, so a completed job is a list to choose from, not work that has been applied. Queries the project already tracks are excluded from the suggestions automatically; &#x60;excludeQueries&#x60; adds more on top for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.DiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    DiscoveryApi apiInstance = new DiscoveryApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | Must belong to the organization in the path.
    String idempotencyKey = "idempotencyKey_example"; // String | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    StartKeywordDiscoveryJobRequest startKeywordDiscoveryJobRequest = new StartKeywordDiscoveryJobRequest(); // StartKeywordDiscoveryJobRequest | 
    try {
      AcceptedJobResource result = apiInstance.startKeywordDiscoveryJob(organizationId, projectId, idempotencyKey, startKeywordDiscoveryJobRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryApi#startKeywordDiscoveryJob");
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
| **projectId** | **UUID**| Must belong to the organization in the path. | |
| **idempotencyKey** | **String**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | |
| **startKeywordDiscoveryJobRequest** | [**StartKeywordDiscoveryJobRequest**](StartKeywordDiscoveryJobRequest.md)|  | |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The discovery job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **402** | The organization has no entitled subscription |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten discovery starts per minute, or the key exceeded its request budget |  -  |

<a id="startPromptDiscoveryJob"></a>
# **startPromptDiscoveryJob**
> AcceptedJobResource startPromptDiscoveryJob(organizationId, projectId, idempotencyKey, startPromptDiscoveryJobRequest)

Start a geo prompt discovery job for a project

Minimum role: manager. Starts background discovery of natural-language prompts - the questions an answer engine gets asked - from free-text seed input, and answers 202 with the job to poll; it never returns prompts inline. The job SUGGESTS prompts: it creates no tracked queries and changes nothing in the project. &#x60;country&#x60; is required here, unlike keyword discovery, because a prompt is a question asked from somewhere and the provider request has no default for it. Queries the project already tracks are excluded automatically; &#x60;excludeQueries&#x60; adds more for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.DiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    DiscoveryApi apiInstance = new DiscoveryApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | Must belong to the organization in the path.
    String idempotencyKey = "idempotencyKey_example"; // String | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    StartPromptDiscoveryJobRequest startPromptDiscoveryJobRequest = new StartPromptDiscoveryJobRequest(); // StartPromptDiscoveryJobRequest | 
    try {
      AcceptedJobResource result = apiInstance.startPromptDiscoveryJob(organizationId, projectId, idempotencyKey, startPromptDiscoveryJobRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryApi#startPromptDiscoveryJob");
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
| **projectId** | **UUID**| Must belong to the organization in the path. | |
| **idempotencyKey** | **String**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | |
| **startPromptDiscoveryJobRequest** | [**StartPromptDiscoveryJobRequest**](StartPromptDiscoveryJobRequest.md)|  | |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The discovery job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **402** | The organization has no entitled subscription |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten discovery starts per minute, or the key exceeded its request budget |  -  |

