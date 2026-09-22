# \OrganizationOperationsAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**PreviewOrganizationOperation**](OrganizationOperationsAPI.md#PreviewOrganizationOperation) | **Post** /api/v1/organization-operation-previews | Preview an organization operation and obtain a confirmation



## PreviewOrganizationOperation

> PreviewOrganizationOperation200Response PreviewOrganizationOperation(ctx).PreviewOrganizationOperationRequest(previewOrganizationOperationRequest).Execute()

Preview an organization operation and obtain a confirmation



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
	previewOrganizationOperationRequest := *openapiclient.NewPreviewOrganizationOperationRequest() // PreviewOrganizationOperationRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OrganizationOperationsAPI.PreviewOrganizationOperation(context.Background()).PreviewOrganizationOperationRequest(previewOrganizationOperationRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OrganizationOperationsAPI.PreviewOrganizationOperation``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PreviewOrganizationOperation`: PreviewOrganizationOperation200Response
	fmt.Fprintf(os.Stdout, "Response from `OrganizationOperationsAPI.PreviewOrganizationOperation`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPreviewOrganizationOperationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **previewOrganizationOperationRequest** | [**PreviewOrganizationOperationRequest**](PreviewOrganizationOperationRequest.md) |  | 

### Return type

[**PreviewOrganizationOperation200Response**](PreviewOrganizationOperation200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

