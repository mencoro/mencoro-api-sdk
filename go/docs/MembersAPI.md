# \MembersAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ChangeMemberRole**](MembersAPI.md#ChangeMemberRole) | **Patch** /api/v1/organizations/{organizationId}/members/{memberId} | Change a member role
[**GetMember**](MembersAPI.md#GetMember) | **Get** /api/v1/organizations/{organizationId}/members/{memberId} | Get one organization membership
[**ListMembers**](MembersAPI.md#ListMembers) | **Get** /api/v1/organizations/{organizationId}/members | List an organization&#39;s members
[**ReactivateMember**](MembersAPI.md#ReactivateMember) | **Post** /api/v1/organizations/{organizationId}/members/{memberId}/reactivate | Reactivate a suspended member
[**SuspendMember**](MembersAPI.md#SuspendMember) | **Post** /api/v1/organizations/{organizationId}/members/{memberId}/suspend | Suspend a member



## ChangeMemberRole

> MemberResource ChangeMemberRole(ctx, organizationId, memberId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).ChangeMemberRoleRequest(changeMemberRoleRequest).Execute()

Change a member role



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
	memberId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	xMencoroConfirmation := "xMencoroConfirmation_example" // string | 
	idempotencyKey := "idempotencyKey_example" // string | 
	changeMemberRoleRequest := *openapiclient.NewChangeMemberRoleRequest() // ChangeMemberRoleRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.ChangeMemberRole(context.Background(), organizationId, memberId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).ChangeMemberRoleRequest(changeMemberRoleRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.ChangeMemberRole``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ChangeMemberRole`: MemberResource
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.ChangeMemberRole`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**memberId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiChangeMemberRoleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xMencoroConfirmation** | **string** |  | 
 **idempotencyKey** | **string** |  | 
 **changeMemberRoleRequest** | [**ChangeMemberRoleRequest**](ChangeMemberRoleRequest.md) |  | 

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetMember

> MemberResource GetMember(ctx, organizationId, memberId).Execute()

Get one organization membership



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
	memberId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The membership id, not the user id. Must belong to the organization in the path.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.GetMember(context.Background(), organizationId, memberId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.GetMember``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMember`: MemberResource
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.GetMember`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**memberId** | **string** | The membership id, not the user id. Must belong to the organization in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetMemberRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListMembers

> ListMembers200Response ListMembers(ctx, organizationId).Limit(limit).Offset(offset).Status(status).SortBy(sortBy).SortOrder(sortOrder).Execute()

List an organization's members



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
	status := "status_example" // string | Absent means both states. (optional)
	sortBy := "sortBy_example" // string |  (optional) (default to "joinedAt")
	sortOrder := "sortOrder_example" // string |  (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.ListMembers(context.Background(), organizationId).Limit(limit).Offset(offset).Status(status).SortBy(sortBy).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.ListMembers``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListMembers`: ListMembers200Response
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.ListMembers`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListMembersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** |  | [default to 20]
 **offset** | **int32** |  | [default to 0]
 **status** | **string** | Absent means both states. | 
 **sortBy** | **string** |  | [default to &quot;joinedAt&quot;]
 **sortOrder** | **string** |  | [default to &quot;desc&quot;]

### Return type

[**ListMembers200Response**](ListMembers200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ReactivateMember

> MemberResource ReactivateMember(ctx, organizationId, memberId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).Execute()

Reactivate a suspended member



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
	memberId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	xMencoroConfirmation := "xMencoroConfirmation_example" // string | 
	idempotencyKey := "idempotencyKey_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.ReactivateMember(context.Background(), organizationId, memberId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.ReactivateMember``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ReactivateMember`: MemberResource
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.ReactivateMember`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**memberId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiReactivateMemberRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xMencoroConfirmation** | **string** |  | 
 **idempotencyKey** | **string** |  | 

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SuspendMember

> MemberResource SuspendMember(ctx, organizationId, memberId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).Execute()

Suspend a member



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
	memberId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	xMencoroConfirmation := "xMencoroConfirmation_example" // string | 
	idempotencyKey := "idempotencyKey_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MembersAPI.SuspendMember(context.Background(), organizationId, memberId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MembersAPI.SuspendMember``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SuspendMember`: MemberResource
	fmt.Fprintf(os.Stdout, "Response from `MembersAPI.SuspendMember`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**memberId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiSuspendMemberRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xMencoroConfirmation** | **string** |  | 
 **idempotencyKey** | **string** |  | 

### Return type

[**MemberResource**](MemberResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

