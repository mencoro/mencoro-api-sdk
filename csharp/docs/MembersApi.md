# Mencoro.Api.Api.MembersApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ChangeMemberRole**](MembersApi.md#changememberrole) | **PATCH** /api/v1/organizations/{organizationId}/members/{memberId} | Change a member role |
| [**GetMember**](MembersApi.md#getmember) | **GET** /api/v1/organizations/{organizationId}/members/{memberId} | Get one organization membership |
| [**ListMembers**](MembersApi.md#listmembers) | **GET** /api/v1/organizations/{organizationId}/members | List an organization&#39;s members |
| [**ReactivateMember**](MembersApi.md#reactivatemember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/reactivate | Reactivate a suspended member |
| [**SuspendMember**](MembersApi.md#suspendmember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/suspend | Suspend a member |

<a id="changememberrole"></a>
# **ChangeMemberRole**
> MemberResource ChangeMemberRole (Guid organizationId, Guid memberId, string xMencoroConfirmation, string idempotencyKey, ChangeMemberRoleRequest changeMemberRoleRequest)

Change a member role

Minimum role: owner. The role of a suspended member cannot be changed, and the last active owner cannot be demoted. Preview it first: the confirmation is bound to the number of active owners, so another owner being suspended in between invalidates it rather than stranding the organization.

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
    public class ChangeMemberRoleExample
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
            var apiInstance = new MembersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var memberId = "memberId_example";  // Guid | 
            var xMencoroConfirmation = "xMencoroConfirmation_example";  // string | 
            var idempotencyKey = "idempotencyKey_example";  // string | 
            var changeMemberRoleRequest = new ChangeMemberRoleRequest(); // ChangeMemberRoleRequest | 

            try
            {
                // Change a member role
                MemberResource result = apiInstance.ChangeMemberRole(organizationId, memberId, xMencoroConfirmation, idempotencyKey, changeMemberRoleRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MembersApi.ChangeMemberRole: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ChangeMemberRoleWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Change a member role
    ApiResponse<MemberResource> response = apiInstance.ChangeMemberRoleWithHttpInfo(organizationId, memberId, xMencoroConfirmation, idempotencyKey, changeMemberRoleRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MembersApi.ChangeMemberRoleWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **memberId** | **Guid** |  |  |
| **xMencoroConfirmation** | **string** |  |  |
| **idempotencyKey** | **string** |  |  |
| **changeMemberRoleRequest** | [**ChangeMemberRoleRequest**](ChangeMemberRoleRequest.md) |  |  |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The membership in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization or membership the caller can access under these ids |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed; the member is suspended; or this is the last active owner |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getmember"></a>
# **GetMember**
> MemberResource GetMember (Guid organizationId, Guid memberId)

Get one organization membership

Minimum role: owner — the same floor the members listing enforces, because a caller who can page the roster has already seen this record. Returns the facts of one membership: its role, whether it is active or suspended, and when it was joined. It does NOT describe the person behind it: no name, no email address, no phone number and no profile image, so a membership id can never be turned into a contact lookup. The membership is read from PostgreSQL, the same row at the same freshness the listing publishes. A membership belonging to another organization answers 404, exactly as an unknown or malformed id does, so the API never confirms that an inaccessible membership exists; the one 403 is a key without the read capability. The response carries no organizationId — it is the one in the path — and no creation timestamp; joinedAt is the membership fact. No query parameters are accepted.

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
    public class GetMemberExample
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
            var apiInstance = new MembersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var memberId = "memberId_example";  // Guid | The membership id, not the user id. Must belong to the organization in the path.

            try
            {
                // Get one organization membership
                MemberResource result = apiInstance.GetMember(organizationId, memberId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MembersApi.GetMember: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetMemberWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get one organization membership
    ApiResponse<MemberResource> response = apiInstance.GetMemberWithHttpInfo(organizationId, memberId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MembersApi.GetMemberWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **memberId** | **Guid** | The membership id, not the user id. Must belong to the organization in the path. |  |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The membership |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller owns, or no membership of it, under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listmembers"></a>
# **ListMembers**
> ListMembers200Response ListMembers (Guid organizationId, int? limit = null, int? offset = null, string? status = null, string? sortBy = null, string? sortOrder = null)

List an organization's members

Minimum role: owner. The application exposes this roster twice and the two disagree — its member screen shows it to any viewer, while its non-BFF endpoint requires an owner — so the published API takes the stricter of the two and requires an owner. A membership describes the membership, not the person: names and email addresses are never returned here, and there is no search parameter, because both would turn the roster into a contact export. Omitting \"status\" returns active and suspended memberships alike. Sorting by \"role\" is alphabetical on the role name, not by seniority.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

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
    public class ListMembersExample
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
            var apiInstance = new MembersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var limit = 20;  // int? |  (optional)  (default to 20)
            var offset = 0;  // int? |  (optional)  (default to 0)
            var status = "active";  // string? | Absent means both states. (optional) 
            var sortBy = "joinedAt";  // string? |  (optional)  (default to joinedAt)
            var sortOrder = "asc";  // string? |  (optional)  (default to desc)

            try
            {
                // List an organization's members
                ListMembers200Response result = apiInstance.ListMembers(organizationId, limit, offset, status, sortBy, sortOrder);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MembersApi.ListMembers: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListMembersWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List an organization's members
    ApiResponse<ListMembers200Response> response = apiInstance.ListMembersWithHttpInfo(organizationId, limit, offset, status, sortBy, sortOrder);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MembersApi.ListMembersWithHttpInfo: " + e.Message);
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
| **status** | **string?** | Absent means both states. | [optional]  |
| **sortBy** | **string?** |  | [optional] [default to joinedAt] |
| **sortOrder** | **string?** |  | [optional] [default to desc] |

### Return type

[**ListMembers200Response**](ListMembers200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization&#39;s memberships |  -  |
| **400** | A parameter was rejected; the details name the field. A limit above 100 is refused, not clamped |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller owns under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="reactivatemember"></a>
# **ReactivateMember**
> MemberResource ReactivateMember (Guid organizationId, Guid memberId, string xMencoroConfirmation, string idempotencyKey)

Reactivate a suspended member

Minimum role: owner. The member keeps the role they had and regains access on their very next request. A member who is already active cannot be reactivated.

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
    public class ReactivateMemberExample
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
            var apiInstance = new MembersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var memberId = "memberId_example";  // Guid | 
            var xMencoroConfirmation = "xMencoroConfirmation_example";  // string | 
            var idempotencyKey = "idempotencyKey_example";  // string | 

            try
            {
                // Reactivate a suspended member
                MemberResource result = apiInstance.ReactivateMember(organizationId, memberId, xMencoroConfirmation, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MembersApi.ReactivateMember: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ReactivateMemberWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Reactivate a suspended member
    ApiResponse<MemberResource> response = apiInstance.ReactivateMemberWithHttpInfo(organizationId, memberId, xMencoroConfirmation, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MembersApi.ReactivateMemberWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **memberId** | **Guid** |  |  |
| **xMencoroConfirmation** | **string** |  |  |
| **idempotencyKey** | **string** |  |  |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The membership in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization or membership the caller can access under these ids |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed; or the member is already active |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="suspendmember"></a>
# **SuspendMember**
> MemberResource SuspendMember (Guid organizationId, Guid memberId, string xMencoroConfirmation, string idempotencyKey)

Suspend a member

Minimum role: owner. The member loses access on their very next request, including through any API key they own that is scoped to this organization. The last active owner cannot be suspended.

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
    public class SuspendMemberExample
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
            var apiInstance = new MembersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var memberId = "memberId_example";  // Guid | 
            var xMencoroConfirmation = "xMencoroConfirmation_example";  // string | 
            var idempotencyKey = "idempotencyKey_example";  // string | 

            try
            {
                // Suspend a member
                MemberResource result = apiInstance.SuspendMember(organizationId, memberId, xMencoroConfirmation, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MembersApi.SuspendMember: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the SuspendMemberWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Suspend a member
    ApiResponse<MemberResource> response = apiInstance.SuspendMemberWithHttpInfo(organizationId, memberId, xMencoroConfirmation, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MembersApi.SuspendMemberWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **memberId** | **Guid** |  |  |
| **xMencoroConfirmation** | **string** |  |  |
| **idempotencyKey** | **string** |  |  |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The membership in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization or membership the caller can access under these ids |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed; the member is already suspended; or this is the last active owner |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

