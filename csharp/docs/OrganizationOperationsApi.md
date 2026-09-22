# Mencoro.Api.Api.OrganizationOperationsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**PreviewOrganizationOperation**](OrganizationOperationsApi.md#previeworganizationoperation) | **POST** /api/v1/organization-operation-previews | Preview an organization operation and obtain a confirmation |

<a id="previeworganizationoperation"></a>
# **PreviewOrganizationOperation**
> PreviewOrganizationOperation200Response PreviewOrganizationOperation (PreviewOrganizationOperationRequest previewOrganizationOperationRequest)

Preview an organization operation and obtain a confirmation

Organization, member and invitation changes need two calls. This one reports the concrete changes, the side effects, the warnings and the conditions, and returns a confirmation valid for five minutes. Send it back in the X-Mencoro-Confirmation header, together with an Idempotency-Key, on the call that performs the operation. Previewing has no effects of any kind.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class PreviewOrganizationOperationExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationOperationsApi(httpClient, config, httpClientHandler);
            var previewOrganizationOperationRequest = new PreviewOrganizationOperationRequest(); // PreviewOrganizationOperationRequest | 

            try
            {
                // Preview an organization operation and obtain a confirmation
                PreviewOrganizationOperation200Response result = apiInstance.PreviewOrganizationOperation(previewOrganizationOperationRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationOperationsApi.PreviewOrganizationOperation: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the PreviewOrganizationOperationWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Preview an organization operation and obtain a confirmation
    ApiResponse<PreviewOrganizationOperation200Response> response = apiInstance.PreviewOrganizationOperationWithHttpInfo(previewOrganizationOperationRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationOperationsApi.PreviewOrganizationOperationWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **previewOrganizationOperationRequest** | [**PreviewOrganizationOperationRequest**](PreviewOrganizationOperationRequest.md) |  |  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

