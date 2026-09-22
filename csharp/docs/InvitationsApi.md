# Mencoro.Api.Api.InvitationsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CancelInvitation**](InvitationsApi.md#cancelinvitation) | **POST** /api/v1/organizations/{organizationId}/invitations/{invitationId}/cancel | Cancel a pending invitation |
| [**CreateInvitation**](InvitationsApi.md#createinvitation) | **POST** /api/v1/organizations/{organizationId}/invitations | Invite somebody to an organization |
| [**ListInvitations**](InvitationsApi.md#listinvitations) | **GET** /api/v1/organizations/{organizationId}/invitations | List an organization&#39;s invitations |

<a id="cancelinvitation"></a>
# **CancelInvitation**
> InvitationResource CancelInvitation (Guid organizationId, Guid invitationId, string xMencoroConfirmation, string idempotencyKey)

Cancel a pending invitation

Minimum role: owner. The link already emailed to the invitee stops working. Only a pending invitation can be cancelled; one that was accepted, rejected or has expired is refused.

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
    public class CancelInvitationExample
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
            var apiInstance = new InvitationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var invitationId = "invitationId_example";  // Guid | 
            var xMencoroConfirmation = "xMencoroConfirmation_example";  // string | 
            var idempotencyKey = "idempotencyKey_example";  // string | 

            try
            {
                // Cancel a pending invitation
                InvitationResource result = apiInstance.CancelInvitation(organizationId, invitationId, xMencoroConfirmation, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling InvitationsApi.CancelInvitation: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the CancelInvitationWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Cancel a pending invitation
    ApiResponse<InvitationResource> response = apiInstance.CancelInvitationWithHttpInfo(organizationId, invitationId, xMencoroConfirmation, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling InvitationsApi.CancelInvitationWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **invitationId** | **Guid** |  |  |
| **xMencoroConfirmation** | **string** |  |  |
| **idempotencyKey** | **string** |  |  |

### Return type

[**InvitationResource**](InvitationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The invitation in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization or invitation the caller can access under these ids |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed; or the invitation is not pending |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="createinvitation"></a>
# **CreateInvitation**
> CreateInvitation200Response CreateInvitation (Guid organizationId, string xMencoroConfirmation, string idempotencyKey, CreateInvitationRequest createInvitationRequest)

Invite somebody to an organization

Minimum role: owner. Sends an invitation email that expires after 14 days. If the address already belongs to an active member the call succeeds and creates nothing - answered as 200 with created=false rather than 201, so a client can tell the two apart. Preview it first; the preview says which of the two will happen.

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
    public class CreateInvitationExample
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
            var apiInstance = new InvitationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var xMencoroConfirmation = "xMencoroConfirmation_example";  // string | 
            var idempotencyKey = "idempotencyKey_example";  // string | 
            var createInvitationRequest = new CreateInvitationRequest(); // CreateInvitationRequest | 

            try
            {
                // Invite somebody to an organization
                CreateInvitation200Response result = apiInstance.CreateInvitation(organizationId, xMencoroConfirmation, idempotencyKey, createInvitationRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling InvitationsApi.CreateInvitation: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the CreateInvitationWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Invite somebody to an organization
    ApiResponse<CreateInvitation200Response> response = apiInstance.CreateInvitationWithHttpInfo(organizationId, xMencoroConfirmation, idempotencyKey, createInvitationRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling InvitationsApi.CreateInvitationWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **xMencoroConfirmation** | **string** |  |  |
| **idempotencyKey** | **string** |  |  |
| **createInvitationRequest** | [**CreateInvitationRequest**](CreateInvitationRequest.md) |  |  |

### Return type

[**CreateInvitation200Response**](CreateInvitation200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The invitation that was created. &#x60;created&#x60; is true; branch on it rather than on the status code, so one code path handles both answers. |  -  |
| **200** | Nothing was created because the address already belongs to an active member. Not an error: the end state the caller asked for already holds. |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed; or a pending invitation already exists for this address |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listinvitations"></a>
# **ListInvitations**
> ListInvitations200Response ListInvitations (Guid organizationId, int? limit = null, int? offset = null, string? search = null, string? status = null, string? sortBy = null, string? sortOrder = null)

List an organization's invitations

Minimum role: owner. Returns the invitations issued for this organization, in every state. The invitation token is never returned. `status` matches the stored state, so an invitation that has passed its `expiresAt` is still listed as pending until it is transitioned; compare `expiresAt` to decide. Rows are ordered by the chosen sort field, and invitations sharing the same value keep no guaranteed relative order across pages.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

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
    public class ListInvitationsExample
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
            var apiInstance = new InvitationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var limit = 20;  // int? |  (optional)  (default to 20)
            var offset = 0;  // int? |  (optional)  (default to 0)
            var search = "search_example";  // string? | Matches part of the invited email address. (optional) 
            var status = "pending";  // string? | Absent means every state. (optional) 
            var sortBy = "createdAt";  // string? |  (optional)  (default to createdAt)
            var sortOrder = "asc";  // string? |  (optional)  (default to desc)

            try
            {
                // List an organization's invitations
                ListInvitations200Response result = apiInstance.ListInvitations(organizationId, limit, offset, search, status, sortBy, sortOrder);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling InvitationsApi.ListInvitations: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListInvitationsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List an organization's invitations
    ApiResponse<ListInvitations200Response> response = apiInstance.ListInvitationsWithHttpInfo(organizationId, limit, offset, search, status, sortBy, sortOrder);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling InvitationsApi.ListInvitationsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **limit** | **int?** |  | [optional] [default to 20] |
| **offset** | **int?** |  | [optional] [default to 0] |
| **search** | **string?** | Matches part of the invited email address. | [optional]  |
| **status** | **string?** | Absent means every state. | [optional]  |
| **sortBy** | **string?** |  | [optional] [default to createdAt] |
| **sortOrder** | **string?** |  | [optional] [default to desc] |

### Return type

[**ListInvitations200Response**](ListInvitations200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization&#39;s invitations |  -  |
| **400** | A parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller owns under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

