# \CapturesAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ListAiResponses**](CapturesAPI.md#ListAiResponses) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/ai-responses | List captured AI answers
[**ListSearchSnapshots**](CapturesAPI.md#ListSearchSnapshots) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/search-snapshots | List captured search-results pages
[**ListShoppingSnapshots**](CapturesAPI.md#ListShoppingSnapshots) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/shopping-snapshots | List captured shopping-results pages



## ListAiResponses

> ListAiResponses200Response ListAiResponses(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).TrackedQueryId(trackedQueryId).Engines(engines).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()

List captured AI answers



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. (optional)
	dateTo := time.Now() // string | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional)
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Only captures of this tracked query. Must belong to the project in the path. (optional)
	engines := []string{"Engines_example"} // []string | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. (optional)
	limit := int32(56) // int32 | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
	offset := int32(56) // int32 | Number of captures to skip before the page starts. (optional) (default to 0)
	sortOrder := "sortOrder_example" // string | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CapturesAPI.ListAiResponses(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).TrackedQueryId(trackedQueryId).Engines(engines).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CapturesAPI.ListAiResponses``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListAiResponses`: ListAiResponses200Response
	fmt.Fprintf(os.Stdout, "Response from `CapturesAPI.ListAiResponses`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListAiResponsesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | 
 **dateTo** | **string** | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | 
 **trackedQueryId** | **string** | Only captures of this tracked query. Must belong to the project in the path. | 
 **engines** | **[]string** | Only captures from these AI engines. Repeat the parameter or pass a comma-separated list. An empty filter means every engine. | 
 **limit** | **int32** | Page size. A larger value is rejected, never silently reduced. | [default to 20]
 **offset** | **int32** | Number of captures to skip before the page starts. | [default to 0]
 **sortOrder** | **string** | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [default to &quot;desc&quot;]

### Return type

[**ListAiResponses200Response**](ListAiResponses200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSearchSnapshots

> ListSearchSnapshots200Response ListSearchSnapshots(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).TrackedQueryId(trackedQueryId).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()

List captured search-results pages



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. (optional)
	dateTo := time.Now() // string | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional)
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Only captures of this tracked query. Must belong to the project in the path. (optional)
	limit := int32(56) // int32 | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
	offset := int32(56) // int32 | Number of captures to skip before the page starts. (optional) (default to 0)
	sortOrder := "sortOrder_example" // string | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CapturesAPI.ListSearchSnapshots(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).TrackedQueryId(trackedQueryId).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CapturesAPI.ListSearchSnapshots``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSearchSnapshots`: ListSearchSnapshots200Response
	fmt.Fprintf(os.Stdout, "Response from `CapturesAPI.ListSearchSnapshots`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListSearchSnapshotsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive lower bound, widened to 00:00:00 UTC of the named day. Must be inside the retention window. | 
 **dateTo** | **string** | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | 
 **trackedQueryId** | **string** | Only captures of this tracked query. Must belong to the project in the path. | 
 **limit** | **int32** | Page size. A larger value is rejected, never silently reduced. | [default to 20]
 **offset** | **int32** | Number of captures to skip before the page starts. | [default to 0]
 **sortOrder** | **string** | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [default to &quot;desc&quot;]

### Return type

[**ListSearchSnapshots200Response**](ListSearchSnapshots200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListShoppingSnapshots

> ListShoppingSnapshots200Response ListShoppingSnapshots(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).TrackedQueryId(trackedQueryId).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()

List captured shopping-results pages



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. (optional)
	dateTo := time.Now() // string | Inclusive upper bound, widened to 23:59:59 UTC of the named day. (optional)
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Only captures of this tracked query. Must belong to the project in the path. (optional)
	limit := int32(56) // int32 | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
	offset := int32(56) // int32 | Number of captures to skip before the page starts. (optional) (default to 0)
	sortOrder := "sortOrder_example" // string | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CapturesAPI.ListShoppingSnapshots(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).TrackedQueryId(trackedQueryId).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CapturesAPI.ListShoppingSnapshots``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListShoppingSnapshots`: ListShoppingSnapshots200Response
	fmt.Fprintf(os.Stdout, "Response from `CapturesAPI.ListShoppingSnapshots`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListShoppingSnapshotsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive lower bound, widened to 00:00:00 UTC of the named day. A date before the retention floor is refused rather than answered with an empty page: shopping captures are aged out by the raw-data purge like every other capture. | 
 **dateTo** | **string** | Inclusive upper bound, widened to 23:59:59 UTC of the named day. | 
 **trackedQueryId** | **string** | Only captures of this tracked query. Must belong to the project in the path. | 
 **limit** | **int32** | Page size. A larger value is rejected, never silently reduced. | [default to 20]
 **offset** | **int32** | Number of captures to skip before the page starts. | [default to 0]
 **sortOrder** | **string** | Direction of the capture-time ordering. An unknown value is rejected, not replaced by the default. | [default to &quot;desc&quot;]

### Return type

[**ListShoppingSnapshots200Response**](ListShoppingSnapshots200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

