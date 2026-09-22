# InvitationsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelInvitation**](InvitationsApi.md#cancelInvitation) | **POST** /api/v1/organizations/{organizationId}/invitations/{invitationId}/cancel | Cancel a pending invitation |
| [**createInvitation**](InvitationsApi.md#createInvitation) | **POST** /api/v1/organizations/{organizationId}/invitations | Invite somebody to an organization |
| [**listInvitations**](InvitationsApi.md#listInvitations) | **GET** /api/v1/organizations/{organizationId}/invitations | List an organization&#39;s invitations |


<a id="cancelInvitation"></a>
# **cancelInvitation**
> InvitationResource cancelInvitation(organizationId, invitationId, xMencoroConfirmation, idempotencyKey)

Cancel a pending invitation

Minimum role: owner. The link already emailed to the invitee stops working. Only a pending invitation can be cancelled; one that was accepted, rejected or has expired is refused.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.InvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    InvitationsApi apiInstance = new InvitationsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID invitationId = UUID.randomUUID(); // UUID | 
    String xMencoroConfirmation = "xMencoroConfirmation_example"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | 
    try {
      InvitationResource result = apiInstance.cancelInvitation(organizationId, invitationId, xMencoroConfirmation, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitationsApi#cancelInvitation");
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
| **invitationId** | **UUID**|  | |
| **xMencoroConfirmation** | **String**|  | |
| **idempotencyKey** | **String**|  | |

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

<a id="createInvitation"></a>
# **createInvitation**
> CreateInvitation200Response createInvitation(organizationId, xMencoroConfirmation, idempotencyKey, createInvitationRequest)

Invite somebody to an organization

Minimum role: owner. Sends an invitation email that expires after 14 days. If the address already belongs to an active member the call succeeds and creates nothing - answered as 200 with created&#x3D;false rather than 201, so a client can tell the two apart. Preview it first; the preview says which of the two will happen.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.InvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    InvitationsApi apiInstance = new InvitationsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    String xMencoroConfirmation = "xMencoroConfirmation_example"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | 
    CreateInvitationRequest createInvitationRequest = new CreateInvitationRequest(); // CreateInvitationRequest | 
    try {
      CreateInvitation200Response result = apiInstance.createInvitation(organizationId, xMencoroConfirmation, idempotencyKey, createInvitationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitationsApi#createInvitation");
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
| **xMencoroConfirmation** | **String**|  | |
| **idempotencyKey** | **String**|  | |
| **createInvitationRequest** | [**CreateInvitationRequest**](CreateInvitationRequest.md)|  | |

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

<a id="listInvitations"></a>
# **listInvitations**
> ListInvitations200Response listInvitations(organizationId, limit, offset, search, status, sortBy, sortOrder)

List an organization&#39;s invitations

Minimum role: owner. Returns the invitations issued for this organization, in every state. The invitation token is never returned. &#x60;status&#x60; matches the stored state, so an invitation that has passed its &#x60;expiresAt&#x60; is still listed as pending until it is transitioned; compare &#x60;expiresAt&#x60; to decide. Rows are ordered by the chosen sort field, and invitations sharing the same value keep no guaranteed relative order across pages.Send &#x60;Accept: text/csv&#x60; to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no &#x60;total&#x60;, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with &#x60;&#x3D;&#x60;, &#x60;+&#x60;, &#x60;-&#x60; or &#x60;@&#x60; are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.InvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    InvitationsApi apiInstance = new InvitationsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    String search = "search_example"; // String | Matches part of the invited email address.
    String status = "pending"; // String | Absent means every state.
    String sortBy = "createdAt"; // String | 
    String sortOrder = "asc"; // String | 
    try {
      ListInvitations200Response result = apiInstance.listInvitations(organizationId, limit, offset, search, status, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitationsApi#listInvitations");
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
| **limit** | **Integer**|  | [optional] [default to 20] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **search** | **String**| Matches part of the invited email address. | [optional] |
| **status** | **String**| Absent means every state. | [optional] [enum: pending, accepted, rejected, expired, cancelled] |
| **sortBy** | **String**|  | [optional] [default to createdAt] [enum: createdAt, expiresAt] |
| **sortOrder** | **String**|  | [optional] [default to desc] [enum: asc, desc] |

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

