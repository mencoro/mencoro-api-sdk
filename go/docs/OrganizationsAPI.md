# \OrganizationsAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ArchiveOrganization**](OrganizationsAPI.md#ArchiveOrganization) | **Post** /api/v1/organizations/{organizationId}/archive | Archive an organization
[**CountOrganizationTrackedQueries**](OrganizationsAPI.md#CountOrganizationTrackedQueries) | **Get** /api/v1/organizations/{organizationId}/usage/tracked-queries | Count the tracked queries an organization has configured
[**CreateOrganization**](OrganizationsAPI.md#CreateOrganization) | **Post** /api/v1/organizations | Create an organization
[**GetEntitlements**](OrganizationsAPI.md#GetEntitlements) | **Get** /api/v1/organizations/{organizationId}/entitlements | Get an organization&#39;s plan allowance and consumption
[**GetMembershipStats**](OrganizationsAPI.md#GetMembershipStats) | **Get** /api/v1/organizations/{organizationId}/membership-stats | Membership, project and invitation counts for an organization
[**GetOrganization**](OrganizationsAPI.md#GetOrganization) | **Get** /api/v1/organizations/{organizationId} | Get an organization
[**GetOrganizationProjectedMonthlyChecks**](OrganizationsAPI.md#GetOrganizationProjectedMonthlyChecks) | **Get** /api/v1/organizations/{organizationId}/usage/projected-monthly-checks | Project a month of check consumption from the current tracking configuration
[**GetOrganizationStats**](OrganizationsAPI.md#GetOrganizationStats) | **Get** /api/v1/organizations/{organizationId}/stats | Headline counts for an organization
[**ListOrganizations**](OrganizationsAPI.md#ListOrganizations) | **Get** /api/v1/organizations | List accessible organizations
[**RestoreOrganization**](OrganizationsAPI.md#RestoreOrganization) | **Post** /api/v1/organizations/{organizationId}/restore | Restore an archived organization
[**UpdateOrganization**](OrganizationsAPI.md#UpdateOrganization) | **Patch** /api/v1/organizations/{organizationId} | Update an organization profile



## ArchiveOrganization

> OrganizationResource ArchiveOrganization(ctx, organizationId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).Execute()

Archive an organization



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
	xMencoroConfirmation := "mencoro_conf_VmajQznkILZjvFf63JexmT1AKX7iYZjOGSrBZYxlUTk" // string | The `confirmation.token` returned by POST /api/v1/organization-operation-previews for this exact action, organization and body. Single use, valid for five minutes, and bound to the effects the preview declared: if the organization gained a project or lost an invitation in between, it is refused with 409 rather than doing more than was agreed. Without it the call answers 428.
	idempotencyKey := "5c1b8e42-0d7f-4a93-8c61-9b2e4d0a7f38" // string | Repeat it to retry a lost response. The replay is answered from the record without claiming the confirmation again, so a retry is never refused for presenting a confirmation the first attempt already spent.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.ArchiveOrganization(context.Background(), organizationId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.ArchiveOrganization``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArchiveOrganization`: OrganizationResource
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.ArchiveOrganization`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiArchiveOrganizationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xMencoroConfirmation** | **string** | The &#x60;confirmation.token&#x60; returned by POST /api/v1/organization-operation-previews for this exact action, organization and body. Single use, valid for five minutes, and bound to the effects the preview declared: if the organization gained a project or lost an invitation in between, it is refused with 409 rather than doing more than was agreed. Without it the call answers 428. | 
 **idempotencyKey** | **string** | Repeat it to retry a lost response. The replay is answered from the record without claiming the confirmation again, so a retry is never refused for presenting a confirmation the first attempt already spent. | 

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CountOrganizationTrackedQueries

> TrackedQueryUsageResource CountOrganizationTrackedQueries(ctx, organizationId).Execute()

Count the tracked queries an organization has configured



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.CountOrganizationTrackedQueries(context.Background(), organizationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.CountOrganizationTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CountOrganizationTrackedQueries`: TrackedQueryUsageResource
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.CountOrganizationTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCountOrganizationTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**TrackedQueryUsageResource**](TrackedQueryUsageResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateOrganization

> CreateOrganization201Response CreateOrganization(ctx).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).CreateOrganizationRequest(createOrganizationRequest).Execute()

Create an organization



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
	xMencoroConfirmation := "xMencoroConfirmation_example" // string | 
	idempotencyKey := "idempotencyKey_example" // string | 
	createOrganizationRequest := *openapiclient.NewCreateOrganizationRequest() // CreateOrganizationRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.CreateOrganization(context.Background()).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).CreateOrganizationRequest(createOrganizationRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.CreateOrganization``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateOrganization`: CreateOrganization201Response
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.CreateOrganization`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateOrganizationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xMencoroConfirmation** | **string** |  | 
 **idempotencyKey** | **string** |  | 
 **createOrganizationRequest** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md) |  | 

### Return type

[**CreateOrganization201Response**](CreateOrganization201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetEntitlements

> EntitlementsResource GetEntitlements(ctx, organizationId).Execute()

Get an organization's plan allowance and consumption



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.GetEntitlements(context.Background(), organizationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.GetEntitlements``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetEntitlements`: EntitlementsResource
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.GetEntitlements`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetEntitlementsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**EntitlementsResource**](EntitlementsResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetMembershipStats

> GetMembershipStats200Response GetMembershipStats(ctx, organizationId).Execute()

Membership, project and invitation counts for an organization



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.GetMembershipStats(context.Background(), organizationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.GetMembershipStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMembershipStats`: GetMembershipStats200Response
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.GetMembershipStats`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetMembershipStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetMembershipStats200Response**](GetMembershipStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetOrganization

> OrganizationResource GetOrganization(ctx, organizationId).Execute()

Get an organization



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.GetOrganization(context.Background(), organizationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.GetOrganization``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetOrganization`: OrganizationResource
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.GetOrganization`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetOrganizationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetOrganizationProjectedMonthlyChecks

> ProjectedMonthlyChecksResource GetOrganizationProjectedMonthlyChecks(ctx, organizationId).Execute()

Project a month of check consumption from the current tracking configuration



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.GetOrganizationProjectedMonthlyChecks(context.Background(), organizationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.GetOrganizationProjectedMonthlyChecks``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetOrganizationProjectedMonthlyChecks`: ProjectedMonthlyChecksResource
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.GetOrganizationProjectedMonthlyChecks`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetOrganizationProjectedMonthlyChecksRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ProjectedMonthlyChecksResource**](ProjectedMonthlyChecksResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetOrganizationStats

> GetOrganizationStats200Response GetOrganizationStats(ctx, organizationId).Execute()

Headline counts for an organization



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.GetOrganizationStats(context.Background(), organizationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.GetOrganizationStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetOrganizationStats`: GetOrganizationStats200Response
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.GetOrganizationStats`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetOrganizationStatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetOrganizationStats200Response**](GetOrganizationStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListOrganizations

> ListOrganizations200Response ListOrganizations(ctx).Limit(limit).Offset(offset).Search(search).Status(status).SortBy(sortBy).SortOrder(sortOrder).Execute()

List accessible organizations



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
	limit := int32(56) // int32 |  (optional) (default to 20)
	offset := int32(56) // int32 |  (optional) (default to 0)
	search := "search_example" // string |  (optional)
	status := "status_example" // string |  (optional)
	sortBy := "sortBy_example" // string |  (optional) (default to "createdAt")
	sortOrder := "sortOrder_example" // string |  (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.ListOrganizations(context.Background()).Limit(limit).Offset(offset).Search(search).Status(status).SortBy(sortBy).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.ListOrganizations``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListOrganizations`: ListOrganizations200Response
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.ListOrganizations`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListOrganizationsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** |  | [default to 20]
 **offset** | **int32** |  | [default to 0]
 **search** | **string** |  | 
 **status** | **string** |  | 
 **sortBy** | **string** |  | [default to &quot;createdAt&quot;]
 **sortOrder** | **string** |  | [default to &quot;desc&quot;]

### Return type

[**ListOrganizations200Response**](ListOrganizations200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreOrganization

> OrganizationResource RestoreOrganization(ctx, organizationId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).Execute()

Restore an archived organization



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.RestoreOrganization(context.Background(), organizationId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.RestoreOrganization``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreOrganization`: OrganizationResource
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.RestoreOrganization`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreOrganizationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xMencoroConfirmation** | **string** |  | 
 **idempotencyKey** | **string** |  | 

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateOrganization

> OrganizationResource UpdateOrganization(ctx, organizationId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).UpdateOrganizationRequest(updateOrganizationRequest).Execute()

Update an organization profile



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
	updateOrganizationRequest := *openapiclient.NewUpdateOrganizationRequest() // UpdateOrganizationRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationsAPI.UpdateOrganization(context.Background(), organizationId).XMencoroConfirmation(xMencoroConfirmation).IdempotencyKey(idempotencyKey).UpdateOrganizationRequest(updateOrganizationRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsAPI.UpdateOrganization``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateOrganization`: OrganizationResource
	fmt.Fprintf(os.Stdout, "Response from `OrganizationsAPI.UpdateOrganization`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateOrganizationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xMencoroConfirmation** | **string** |  | 
 **idempotencyKey** | **string** |  | 
 **updateOrganizationRequest** | [**UpdateOrganizationRequest**](UpdateOrganizationRequest.md) |  | 

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

