# \JobsAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAsyncJob**](JobsAPI.md#GetAsyncJob) | **Get** /api/v1/organizations/{organizationId}/jobs/{jobId} | Get an asynchronous job



## GetAsyncJob

> AsyncJobResource GetAsyncJob(ctx, organizationId, jobId).Execute()

Get an asynchronous job



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
	jobId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must be a job started inside the organization in the path.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.JobsAPI.GetAsyncJob(context.Background(), organizationId, jobId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `JobsAPI.GetAsyncJob``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAsyncJob`: AsyncJobResource
	fmt.Fprintf(os.Stdout, "Response from `JobsAPI.GetAsyncJob`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**jobId** | **string** | Must be a job started inside the organization in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAsyncJobRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**AsyncJobResource**](AsyncJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

