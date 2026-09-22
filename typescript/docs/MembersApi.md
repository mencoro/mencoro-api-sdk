# MembersApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeMemberRole**](MembersApi.md#changememberroleoperation) | **PATCH** /api/v1/organizations/{organizationId}/members/{memberId} | Change a member role |
| [**getMember**](MembersApi.md#getmember) | **GET** /api/v1/organizations/{organizationId}/members/{memberId} | Get one organization membership |
| [**listMembers**](MembersApi.md#listmembers) | **GET** /api/v1/organizations/{organizationId}/members | List an organization\&#39;s members |
| [**reactivateMember**](MembersApi.md#reactivatemember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/reactivate | Reactivate a suspended member |
| [**suspendMember**](MembersApi.md#suspendmember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/suspend | Suspend a member |



## changeMemberRole

> MemberResource changeMemberRole(organizationId, memberId, xMencoroConfirmation, idempotencyKey, changeMemberRoleRequest)

Change a member role

Minimum role: owner. The role of a suspended member cannot be changed, and the last active owner cannot be demoted. Preview it first: the confirmation is bound to the number of active owners, so another owner being suspended in between invalidates it rather than stranding the organization.

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mencoro/api';
import type { ChangeMemberRoleOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    memberId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    xMencoroConfirmation: xMencoroConfirmation_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // ChangeMemberRoleRequest
    changeMemberRoleRequest: ...,
  } satisfies ChangeMemberRoleOperationRequest;

  try {
    const data = await api.changeMemberRole(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **memberId** | `string` |  | [Defaults to `undefined`] |
| **xMencoroConfirmation** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **changeMemberRoleRequest** | [ChangeMemberRoleRequest](ChangeMemberRoleRequest.md) |  | |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The membership in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization or membership the caller can access under these ids |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed; the member is suspended; or this is the last active owner |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getMember

> MemberResource getMember(organizationId, memberId)

Get one organization membership

Minimum role: owner — the same floor the members listing enforces, because a caller who can page the roster has already seen this record. Returns the facts of one membership: its role, whether it is active or suspended, and when it was joined. It does NOT describe the person behind it: no name, no email address, no phone number and no profile image, so a membership id can never be turned into a contact lookup. The membership is read from PostgreSQL, the same row at the same freshness the listing publishes. A membership belonging to another organization answers 404, exactly as an unknown or malformed id does, so the API never confirms that an inaccessible membership exists; the one 403 is a key without the read capability. The response carries no organizationId — it is the one in the path — and no creation timestamp; joinedAt is the membership fact. No query parameters are accepted.

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mencoro/api';
import type { GetMemberRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | The membership id, not the user id. Must belong to the organization in the path.
    memberId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetMemberRequest;

  try {
    const data = await api.getMember(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **memberId** | `string` | The membership id, not the user id. Must belong to the organization in the path. | [Defaults to `undefined`] |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The membership |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller owns, or no membership of it, under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listMembers

> ListMembers200Response listMembers(organizationId, limit, offset, status, sortBy, sortOrder)

List an organization\&#39;s members

Minimum role: owner. The application exposes this roster twice and the two disagree — its member screen shows it to any viewer, while its non-BFF endpoint requires an owner — so the published API takes the stricter of the two and requires an owner. A membership describes the membership, not the person: names and email addresses are never returned here, and there is no search parameter, because both would turn the roster into a contact export. Omitting \&quot;status\&quot; returns active and suspended memberships alike. Sorting by \&quot;role\&quot; is alphabetical on the role name, not by seniority.Send &#x60;Accept: text/csv&#x60; to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no &#x60;total&#x60;, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with &#x60;&#x3D;&#x60;, &#x60;+&#x60;, &#x60;-&#x60; or &#x60;@&#x60; are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mencoro/api';
import type { ListMembersRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number (optional)
    limit: 56,
    // number (optional)
    offset: 56,
    // 'active' | 'suspended' | Absent means both states. (optional)
    status: status_example,
    // 'joinedAt' | 'role' (optional)
    sortBy: sortBy_example,
    // 'asc' | 'desc' (optional)
    sortOrder: sortOrder_example,
  } satisfies ListMembersRequest;

  try {
    const data = await api.listMembers(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `20`] |
| **offset** | `number` |  | [Optional] [Defaults to `0`] |
| **status** | `active`, `suspended` | Absent means both states. | [Optional] [Defaults to `undefined`] [Enum: active, suspended] |
| **sortBy** | `joinedAt`, `role` |  | [Optional] [Defaults to `&#39;joinedAt&#39;`] [Enum: joinedAt, role] |
| **sortOrder** | `asc`, `desc` |  | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**ListMembers200Response**](ListMembers200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization\&#39;s memberships |  -  |
| **400** | A parameter was rejected; the details name the field. A limit above 100 is refused, not clamped |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller owns under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## reactivateMember

> MemberResource reactivateMember(organizationId, memberId, xMencoroConfirmation, idempotencyKey)

Reactivate a suspended member

Minimum role: owner. The member keeps the role they had and regains access on their very next request. A member who is already active cannot be reactivated.

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mencoro/api';
import type { ReactivateMemberRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    memberId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    xMencoroConfirmation: xMencoroConfirmation_example,
    // string
    idempotencyKey: idempotencyKey_example,
  } satisfies ReactivateMemberRequest;

  try {
    const data = await api.reactivateMember(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **memberId** | `string` |  | [Defaults to `undefined`] |
| **xMencoroConfirmation** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The membership in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization or membership the caller can access under these ids |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed; or the member is already active |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## suspendMember

> MemberResource suspendMember(organizationId, memberId, xMencoroConfirmation, idempotencyKey)

Suspend a member

Minimum role: owner. The member loses access on their very next request, including through any API key they own that is scoped to this organization. The last active owner cannot be suspended.

### Example

```ts
import {
  Configuration,
  MembersApi,
} from '@mencoro/api';
import type { SuspendMemberRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new MembersApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    memberId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    xMencoroConfirmation: xMencoroConfirmation_example,
    // string
    idempotencyKey: idempotencyKey_example,
  } satisfies SuspendMemberRequest;

  try {
    const data = await api.suspendMember(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **memberId** | `string` |  | [Defaults to `undefined`] |
| **xMencoroConfirmation** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The membership in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization or membership the caller can access under these ids |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed; the member is already suspended; or this is the last active owner |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

