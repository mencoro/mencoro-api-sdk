# MembersApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeMemberRole**](MembersApi.md#changeMemberRole) | **PATCH** /api/v1/organizations/{organizationId}/members/{memberId} | Change a member role |
| [**getMember**](MembersApi.md#getMember) | **GET** /api/v1/organizations/{organizationId}/members/{memberId} | Get one organization membership |
| [**listMembers**](MembersApi.md#listMembers) | **GET** /api/v1/organizations/{organizationId}/members | List an organization&#39;s members |
| [**reactivateMember**](MembersApi.md#reactivateMember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/reactivate | Reactivate a suspended member |
| [**suspendMember**](MembersApi.md#suspendMember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/suspend | Suspend a member |


<a id="changeMemberRole"></a>
# **changeMemberRole**
> MemberResource changeMemberRole(organizationId, memberId, xMencoroConfirmation, idempotencyKey, changeMemberRoleRequest)

Change a member role

Minimum role: owner. The role of a suspended member cannot be changed, and the last active owner cannot be demoted. Preview it first: the confirmation is bound to the number of active owners, so another owner being suspended in between invalidates it rather than stranding the organization.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID memberId = UUID.randomUUID(); // UUID | 
    String xMencoroConfirmation = "xMencoroConfirmation_example"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | 
    ChangeMemberRoleRequest changeMemberRoleRequest = new ChangeMemberRoleRequest(); // ChangeMemberRoleRequest | 
    try {
      MemberResource result = apiInstance.changeMemberRole(organizationId, memberId, xMencoroConfirmation, idempotencyKey, changeMemberRoleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#changeMemberRole");
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
| **memberId** | **UUID**|  | |
| **xMencoroConfirmation** | **String**|  | |
| **idempotencyKey** | **String**|  | |
| **changeMemberRoleRequest** | [**ChangeMemberRoleRequest**](ChangeMemberRoleRequest.md)|  | |

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

<a id="getMember"></a>
# **getMember**
> MemberResource getMember(organizationId, memberId)

Get one organization membership

Minimum role: owner — the same floor the members listing enforces, because a caller who can page the roster has already seen this record. Returns the facts of one membership: its role, whether it is active or suspended, and when it was joined. It does NOT describe the person behind it: no name, no email address, no phone number and no profile image, so a membership id can never be turned into a contact lookup. The membership is read from PostgreSQL, the same row at the same freshness the listing publishes. A membership belonging to another organization answers 404, exactly as an unknown or malformed id does, so the API never confirms that an inaccessible membership exists; the one 403 is a key without the read capability. The response carries no organizationId — it is the one in the path — and no creation timestamp; joinedAt is the membership fact. No query parameters are accepted.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID memberId = UUID.randomUUID(); // UUID | The membership id, not the user id. Must belong to the organization in the path.
    try {
      MemberResource result = apiInstance.getMember(organizationId, memberId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#getMember");
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
| **memberId** | **UUID**| The membership id, not the user id. Must belong to the organization in the path. | |

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

<a id="listMembers"></a>
# **listMembers**
> ListMembers200Response listMembers(organizationId, limit, offset, status, sortBy, sortOrder)

List an organization&#39;s members

Minimum role: owner. The application exposes this roster twice and the two disagree — its member screen shows it to any viewer, while its non-BFF endpoint requires an owner — so the published API takes the stricter of the two and requires an owner. A membership describes the membership, not the person: names and email addresses are never returned here, and there is no search parameter, because both would turn the roster into a contact export. Omitting \&quot;status\&quot; returns active and suspended memberships alike. Sorting by \&quot;role\&quot; is alphabetical on the role name, not by seniority.Send &#x60;Accept: text/csv&#x60; to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no &#x60;total&#x60;, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with &#x60;&#x3D;&#x60;, &#x60;+&#x60;, &#x60;-&#x60; or &#x60;@&#x60; are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    String status = "active"; // String | Absent means both states.
    String sortBy = "joinedAt"; // String | 
    String sortOrder = "asc"; // String | 
    try {
      ListMembers200Response result = apiInstance.listMembers(organizationId, limit, offset, status, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#listMembers");
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
| **status** | **String**| Absent means both states. | [optional] [enum: active, suspended] |
| **sortBy** | **String**|  | [optional] [default to joinedAt] [enum: joinedAt, role] |
| **sortOrder** | **String**|  | [optional] [default to desc] [enum: asc, desc] |

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

<a id="reactivateMember"></a>
# **reactivateMember**
> MemberResource reactivateMember(organizationId, memberId, xMencoroConfirmation, idempotencyKey)

Reactivate a suspended member

Minimum role: owner. The member keeps the role they had and regains access on their very next request. A member who is already active cannot be reactivated.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID memberId = UUID.randomUUID(); // UUID | 
    String xMencoroConfirmation = "xMencoroConfirmation_example"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | 
    try {
      MemberResource result = apiInstance.reactivateMember(organizationId, memberId, xMencoroConfirmation, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#reactivateMember");
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
| **memberId** | **UUID**|  | |
| **xMencoroConfirmation** | **String**|  | |
| **idempotencyKey** | **String**|  | |

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

<a id="suspendMember"></a>
# **suspendMember**
> MemberResource suspendMember(organizationId, memberId, xMencoroConfirmation, idempotencyKey)

Suspend a member

Minimum role: owner. The member loses access on their very next request, including through any API key they own that is scoped to this organization. The last active owner cannot be suspended.

### Example
```java
// Import classes:
import com.mencoro.api.ApiClient;
import com.mencoro.api.ApiException;
import com.mencoro.api.Configuration;
import com.mencoro.api.auth.*;
import com.mencoro.api.models.*;
import com.mencoro.api.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mencoro.com");
    
    // Configure HTTP bearer authorization: ApiKey
    HttpBearerAuth ApiKey = (HttpBearerAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setBearerToken("BEARER TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | 
    UUID memberId = UUID.randomUUID(); // UUID | 
    String xMencoroConfirmation = "xMencoroConfirmation_example"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | 
    try {
      MemberResource result = apiInstance.suspendMember(organizationId, memberId, xMencoroConfirmation, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#suspendMember");
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
| **memberId** | **UUID**|  | |
| **xMencoroConfirmation** | **String**|  | |
| **idempotencyKey** | **String**|  | |

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

