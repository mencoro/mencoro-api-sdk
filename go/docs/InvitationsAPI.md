# \InvitationsAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CancelInvitation**](InvitationsAPI.md#CancelInvitation) | **Post** /api/v1/organizations/{organizationId}/invitations/{invitationId}/cancel | Cancel a pending invitation
[**CreateInvitation**](InvitationsAPI.md#CreateInvitation) | **Post** /api/v1/organizations/{organizationId}/invitations | Invite somebody to an organization
[**ListInvitations**](InvitationsAPI.md#ListInvitations) | **Get** /api/v1/organizations/{organizationId}/invitations | List an organization&#39;s invitations



## CancelInvitation

> InvitationResource CancelInvitation(ctx, organizationId, invitationId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).Execute()

Cancel a pending invitation



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	invitationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	xMencoroConfirmation := "xMencoroConfirmation_example" // string | 
	idempotencyKey := "idempotencyKey_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InvitationsAPI.CancelInvitation(context.Background(), organizationId, invitationId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InvitationsAPI.CancelInvitation``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CancelInvitation`: InvitationResource
	fmt.Fprintf(os.Stdout, "Response from `InvitationsAPI.CancelInvitation`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**invitationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCancelInvitationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xMencoroConfirmation** | **string** |  | 
 **idempotencyKey** | **string** |  | 

### Return type

[**InvitationResource**](InvitationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateInvitation

> CreateInvitation200Response CreateInvitation(ctx, organizationId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).CreateInvitationRequest(createInvitationRequest).Execute()

Invite somebody to an organization



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	xMencoroConfirmation := "xMencoroConfirmation_example" // string | 
	idempotencyKey := "idempotencyKey_example" // string | 
	createInvitationRequest := *openapiclient.NewCreateInvitationRequest() // CreateInvitationRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InvitationsAPI.CreateInvitation(context.Background(), organizationId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).CreateInvitationRequest(createInvitationRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InvitationsAPI.CreateInvitation``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateInvitation`: CreateInvitation200Response
	fmt.Fprintf(os.Stdout, "Response from `InvitationsAPI.CreateInvitation`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateInvitationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xMencoroConfirmation** | **string** |  | 
 **idempotencyKey** | **string** |  | 
 **createInvitationRequest** | [**CreateInvitationRequest**](CreateInvitationRequest.md) |  | 

### Return type

[**CreateInvitation200Response**](CreateInvitation200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListInvitations

> ListInvitations200Response ListInvitations(ctx, organizationId).Limit(limit).Offset(offset).Search(search).Status(status).SortBy(sortBy).SortOrder(sortOrder).Execute()

List an organization's invitations



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	limit := int32(56) // int32 |  (optional) (default to 20)
	offset := int32(56) // int32 |  (optional) (default to 0)
	search := "search_example" // string | Matches part of the invited email address. (optional)
	status := "status_example" // string | Absent means every state. (optional)
	sortBy := "sortBy_example" // string |  (optional) (default to "createdAt")
	sortOrder := "sortOrder_example" // string |  (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InvitationsAPI.ListInvitations(context.Background(), organizationId).Limit(limit).Offset(offset).Search(search).Status(status).SortBy(sortBy).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InvitationsAPI.ListInvitations``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListInvitations`: ListInvitations200Response
	fmt.Fprintf(os.Stdout, "Response from `InvitationsAPI.ListInvitations`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListInvitationsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** |  | [default to 20]
 **offset** | **int32** |  | [default to 0]
 **search** | **string** | Matches part of the invited email address. | 
 **status** | **string** | Absent means every state. | 
 **sortBy** | **string** |  | [default to &quot;createdAt&quot;]
 **sortOrder** | **string** |  | [default to &quot;desc&quot;]

### Return type

[**ListInvitations200Response**](ListInvitations200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

