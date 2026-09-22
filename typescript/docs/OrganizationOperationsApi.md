# OrganizationOperationsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**previewOrganizationOperation**](OrganizationOperationsApi.md#previeworganizationoperationoperation) | **POST** /api/v1/organization-operation-previews | Preview an organization operation and obtain a confirmation |



## previewOrganizationOperation

> PreviewOrganizationOperation200Response previewOrganizationOperation(previewOrganizationOperationRequest)

Preview an organization operation and obtain a confirmation

Organization, member and invitation changes need two calls. This one reports the concrete changes, the side effects, the warnings and the conditions, and returns a confirmation valid for five minutes. Send it back in the X-Mencoro-Confirmation header, together with an Idempotency-Key, on the call that performs the operation. Previewing has no effects of any kind.

### Example

```ts
import {
  Configuration,
  OrganizationOperationsApi,
} from '@mencoro/api';
import type { PreviewOrganizationOperationOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new OrganizationOperationsApi(config);

  const body = {
    // PreviewOrganizationOperationRequest
    previewOrganizationOperationRequest: {"action":"archiveOrganization","organizationId":"0193c4f0-11aa-7b22-9d33-4e5f60718293"},
  } satisfies PreviewOrganizationOperationOperationRequest;

  try {
    const data = await api.previewOrganizationOperation(body);
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
| **previewOrganizationOperationRequest** | [PreviewOrganizationOperationRequest](PreviewOrganizationOperationRequest.md) |  | |

### Return type

[**PreviewOrganizationOperation200Response**](PreviewOrganizationOperation200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | What the operation would do, plus a confirmation |  -  |
| **401** | Missing or invalid API key |  -  |
| **400** | Unknown action, or a payload the operation does not accept |  -  |
| **403** | The key lacks a required capability, or its scope is too narrow |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

