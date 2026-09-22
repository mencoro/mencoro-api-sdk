# InvitationsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelInvitation**](InvitationsApi.md#cancelinvitation) | **POST** /api/v1/organizations/{organizationId}/invitations/{invitationId}/cancel | Cancel a pending invitation |
| [**createInvitation**](InvitationsApi.md#createinvitationoperation) | **POST** /api/v1/organizations/{organizationId}/invitations | Invite somebody to an organization |
| [**listInvitations**](InvitationsApi.md#listinvitations) | **GET** /api/v1/organizations/{organizationId}/invitations | List an organization\&#39;s invitations |



## cancelInvitation

> InvitationResource cancelInvitation(organizationId, invitationId, xMencoroConfirmation, idempotencyKey)

Cancel a pending invitation

Minimum role: owner. The link already emailed to the invitee stops working. Only a pending invitation can be cancelled; one that was accepted, rejected or has expired is refused.

### Example

```ts
import {
  Configuration,
  InvitationsApi,
} from '@mencoro/api';
import type { CancelInvitationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new InvitationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    invitationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    xMencoroConfirmation: xMencoroConfirmation_example,
    // string
    idempotencyKey: idempotencyKey_example,
  } satisfies CancelInvitationRequest;

  try {
    const data = await api.cancelInvitation(body);
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
| **invitationId** | `string` |  | [Defaults to `undefined`] |
| **xMencoroConfirmation** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |

### Return type

[**InvitationResource**](InvitationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The invitation in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization or invitation the caller can access under these ids |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed; or the invitation is not pending |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createInvitation

> CreateInvitation200Response createInvitation(organizationId, xMencoroConfirmation, idempotencyKey, createInvitationRequest)

Invite somebody to an organization

Minimum role: owner. Sends an invitation email that expires after 14 days. If the address already belongs to an active member the call succeeds and creates nothing - answered as 200 with created&#x3D;false rather than 201, so a client can tell the two apart. Preview it first; the preview says which of the two will happen.

### Example

```ts
import {
  Configuration,
  InvitationsApi,
} from '@mencoro/api';
import type { CreateInvitationOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new InvitationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    xMencoroConfirmation: xMencoroConfirmation_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // CreateInvitationRequest
    createInvitationRequest: ...,
  } satisfies CreateInvitationOperationRequest;

  try {
    const data = await api.createInvitation(body);
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
| **xMencoroConfirmation** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **createInvitationRequest** | [CreateInvitationRequest](CreateInvitationRequest.md) |  | |

### Return type

[**CreateInvitation200Response**](CreateInvitation200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


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

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listInvitations

> ListInvitations200Response listInvitations(organizationId, limit, offset, search, status, sortBy, sortOrder)

List an organization\&#39;s invitations

Minimum role: owner. Returns the invitations issued for this organization, in every state. The invitation token is never returned. &#x60;status&#x60; matches the stored state, so an invitation that has passed its &#x60;expiresAt&#x60; is still listed as pending until it is transitioned; compare &#x60;expiresAt&#x60; to decide. Rows are ordered by the chosen sort field, and invitations sharing the same value keep no guaranteed relative order across pages.Send &#x60;Accept: text/csv&#x60; to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no &#x60;total&#x60;, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with &#x60;&#x3D;&#x60;, &#x60;+&#x60;, &#x60;-&#x60; or &#x60;@&#x60; are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```ts
import {
  Configuration,
  InvitationsApi,
} from '@mencoro/api';
import type { ListInvitationsRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new InvitationsApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number (optional)
    limit: 56,
    // number (optional)
    offset: 56,
    // string | Matches part of the invited email address. (optional)
    search: search_example,
    // 'pending' | 'accepted' | 'rejected' | 'expired' | 'cancelled' | Absent means every state. (optional)
    status: status_example,
    // 'createdAt' | 'expiresAt' (optional)
    sortBy: sortBy_example,
    // 'asc' | 'desc' (optional)
    sortOrder: sortOrder_example,
  } satisfies ListInvitationsRequest;

  try {
    const data = await api.listInvitations(body);
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
| **search** | `string` | Matches part of the invited email address. | [Optional] [Defaults to `undefined`] |
| **status** | `pending`, `accepted`, `rejected`, `expired`, `cancelled` | Absent means every state. | [Optional] [Defaults to `undefined`] [Enum: pending, accepted, rejected, expired, cancelled] |
| **sortBy** | `createdAt`, `expiresAt` |  | [Optional] [Defaults to `&#39;createdAt&#39;`] [Enum: createdAt, expiresAt] |
| **sortOrder** | `asc`, `desc` |  | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**ListInvitations200Response**](ListInvitations200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization\&#39;s invitations |  -  |
| **400** | A parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller owns under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

