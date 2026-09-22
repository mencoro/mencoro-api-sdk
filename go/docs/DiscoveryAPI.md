# \DiscoveryAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**StartBrandDiscoveryJob**](DiscoveryAPI.md#StartBrandDiscoveryJob) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/brands | Start a brand discovery job for a project
[**StartBrandNameSuggestionJob**](DiscoveryAPI.md#StartBrandNameSuggestionJob) | **Post** /api/v1/organizations/{organizationId}/brand-name-suggestions | Start a brand-name alias suggestion job
[**StartKeywordDiscoveryJob**](DiscoveryAPI.md#StartKeywordDiscoveryJob) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/keywords | Start a keyword discovery job for a project
[**StartPromptDiscoveryJob**](DiscoveryAPI.md#StartPromptDiscoveryJob) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/prompts | Start a geo prompt discovery job for a project



## StartBrandDiscoveryJob

> AcceptedJobResource StartBrandDiscoveryJob(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).StartBrandDiscoveryJobRequest(startBrandDiscoveryJobRequest).Execute()

Start a brand discovery job for a project



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
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the organization in the path.
	idempotencyKey := "idempotencyKey_example" // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
	startBrandDiscoveryJobRequest := *openapiclient.NewStartBrandDiscoveryJobRequest() // StartBrandDiscoveryJobRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DiscoveryAPI.StartBrandDiscoveryJob(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).StartBrandDiscoveryJobRequest(startBrandDiscoveryJobRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DiscoveryAPI.StartBrandDiscoveryJob``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StartBrandDiscoveryJob`: AcceptedJobResource
	fmt.Fprintf(os.Stdout, "Response from `DiscoveryAPI.StartBrandDiscoveryJob`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** | Must belong to the organization in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiStartBrandDiscoveryJobRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | 
 **startBrandDiscoveryJobRequest** | [**StartBrandDiscoveryJobRequest**](StartBrandDiscoveryJobRequest.md) |  | 

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartBrandNameSuggestionJob

> AcceptedJobResource StartBrandNameSuggestionJob(ctx, organizationId).IdempotencyKey(idempotencyKey).StartBrandNameSuggestionJobRequest(startBrandNameSuggestionJobRequest).Execute()

Start a brand-name alias suggestion job



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
	idempotencyKey := "idempotencyKey_example" // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
	startBrandNameSuggestionJobRequest := *openapiclient.NewStartBrandNameSuggestionJobRequest("Acme", []string{"WebsiteDomains_example"}) // StartBrandNameSuggestionJobRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DiscoveryAPI.StartBrandNameSuggestionJob(context.Background(), organizationId).IdempotencyKey(idempotencyKey).StartBrandNameSuggestionJobRequest(startBrandNameSuggestionJobRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DiscoveryAPI.StartBrandNameSuggestionJob``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StartBrandNameSuggestionJob`: AcceptedJobResource
	fmt.Fprintf(os.Stdout, "Response from `DiscoveryAPI.StartBrandNameSuggestionJob`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStartBrandNameSuggestionJobRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | 
 **startBrandNameSuggestionJobRequest** | [**StartBrandNameSuggestionJobRequest**](StartBrandNameSuggestionJobRequest.md) |  | 

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartKeywordDiscoveryJob

> AcceptedJobResource StartKeywordDiscoveryJob(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).StartKeywordDiscoveryJobRequest(startKeywordDiscoveryJobRequest).Execute()

Start a keyword discovery job for a project



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
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the organization in the path.
	idempotencyKey := "idempotencyKey_example" // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
	startKeywordDiscoveryJobRequest := *openapiclient.NewStartKeywordDiscoveryJobRequest("crm for plumbers, field service software") // StartKeywordDiscoveryJobRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DiscoveryAPI.StartKeywordDiscoveryJob(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).StartKeywordDiscoveryJobRequest(startKeywordDiscoveryJobRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DiscoveryAPI.StartKeywordDiscoveryJob``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StartKeywordDiscoveryJob`: AcceptedJobResource
	fmt.Fprintf(os.Stdout, "Response from `DiscoveryAPI.StartKeywordDiscoveryJob`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** | Must belong to the organization in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiStartKeywordDiscoveryJobRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | 
 **startKeywordDiscoveryJobRequest** | [**StartKeywordDiscoveryJobRequest**](StartKeywordDiscoveryJobRequest.md) |  | 

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartPromptDiscoveryJob

> AcceptedJobResource StartPromptDiscoveryJob(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).StartPromptDiscoveryJobRequest(startPromptDiscoveryJobRequest).Execute()

Start a geo prompt discovery job for a project



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
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the organization in the path.
	idempotencyKey := "idempotencyKey_example" // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
	startPromptDiscoveryJobRequest := *openapiclient.NewStartPromptDiscoveryJobRequest("crm for plumbers, field service software", "ES") // StartPromptDiscoveryJobRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DiscoveryAPI.StartPromptDiscoveryJob(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).StartPromptDiscoveryJobRequest(startPromptDiscoveryJobRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DiscoveryAPI.StartPromptDiscoveryJob``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StartPromptDiscoveryJob`: AcceptedJobResource
	fmt.Fprintf(os.Stdout, "Response from `DiscoveryAPI.StartPromptDiscoveryJob`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** | Must belong to the organization in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiStartPromptDiscoveryJobRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | 
 **startPromptDiscoveryJobRequest** | [**StartPromptDiscoveryJobRequest**](StartPromptDiscoveryJobRequest.md) |  | 

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

