# \AccountAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetMe**](AccountAPI.md#GetMe) | **Get** /api/v1/me | Get the authenticated identity
[**GetMeStats**](AccountAPI.md#GetMeStats) | **Get** /api/v1/me/stats | Counts across everything the key can reach



## GetMe

> MeResource GetMe(ctx).Execute()

Get the authenticated identity



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccountAPI.GetMe(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccountAPI.GetMe``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMe`: MeResource
	fmt.Fprintf(os.Stdout, "Response from `AccountAPI.GetMe`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetMeRequest struct via the builder pattern


### Return type

[**MeResource**](MeResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetMeStats

> GetMeStats200Response GetMeStats(ctx).Execute()

Counts across everything the key can reach



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccountAPI.GetMeStats(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccountAPI.GetMeStats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMeStats`: GetMeStats200Response
	fmt.Fprintf(os.Stdout, "Response from `AccountAPI.GetMeStats`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetMeStatsRequest struct via the builder pattern


### Return type

[**GetMeStats200Response**](GetMeStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

