# OrganizationOperationsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**previewOrganizationOperation**](OrganizationOperationsApi.md#previewOrganizationOperation) | **POST** /api/v1/organization-operation-previews | Preview an organization operation and obtain a confirmation |


<a id="previewOrganizationOperation"></a>
# **previewOrganizationOperation**
> PreviewOrganizationOperation200Response previewOrganizationOperation(previewOrganizationOperationRequest)

Preview an organization operation and obtain a confirmation

Organization, member and invitation changes need two calls. This one reports the concrete changes, the side effects, the warnings and the conditions, and returns a confirmation valid for five minutes. Send it back in the X-Mencoro-Confirmation header, together with an Idempotency-Key, on the call that performs the operation. Previewing has no effects of any kind.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.OrganizationOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    OrganizationOperationsApi apiInstance = new OrganizationOperationsApi(defaultClient);
    PreviewOrganizationOperationRequest previewOrganizationOperationRequest = new PreviewOrganizationOperationRequest(); // PreviewOrganizationOperationRequest | 
    try {
      PreviewOrganizationOperation200Response result = apiInstance.previewOrganizationOperation(previewOrganizationOperationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationOperationsApi#previewOrganizationOperation");
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
| **previewOrganizationOperationRequest** | [**PreviewOrganizationOperationRequest**](PreviewOrganizationOperationRequest.md)|  | |

### Return type

[**PreviewOrganizationOperation200Response**](PreviewOrganizationOperation200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | What the operation would do, plus a confirmation |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | Unknown action, or a payload the operation does not accept |  -  |
| **403** | The key lacks a required capability, or its scope is too narrow |  -  |
| **404** | No organization the caller can access under this id |  -  |

