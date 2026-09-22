# \ClustersAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApplyClusteringJob**](ClustersAPI.md#ApplyClusteringJob) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs/{jobId}/apply | Apply the result of a clustering job
[**BatchCreateQueryClusters**](ClustersAPI.md#BatchCreateQueryClusters) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/batch | Create several keyword clusters at once
[**CreateQueryCluster**](ClustersAPI.md#CreateQueryCluster) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | Create a keyword cluster
[**DeleteQueryCluster**](ClustersAPI.md#DeleteQueryCluster) | **Delete** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Delete a keyword cluster
[**RenameQueryCluster**](ClustersAPI.md#RenameQueryCluster) | **Patch** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Rename a keyword cluster
[**StartClusteringJob**](ClustersAPI.md#StartClusteringJob) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs | Start a keyword clustering job



## ApplyClusteringJob

> ApplyClusteringJobOutcome ApplyClusteringJob(ctx, organizationId, projectId, jobId).IdempotencyKey(idempotencyKey).Execute()

Apply the result of a clustering job



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
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	jobId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must be a clustering job started for this organization and project.
	idempotencyKey := "idempotencyKey_example" // string | Repeat it to retry a lost response without applying the job twice.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ClustersAPI.ApplyClusteringJob(context.Background(), organizationId, projectId, jobId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ClustersAPI.ApplyClusteringJob``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ApplyClusteringJob`: ApplyClusteringJobOutcome
	fmt.Fprintf(os.Stdout, "Response from `ClustersAPI.ApplyClusteringJob`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**jobId** | **string** | Must be a clustering job started for this organization and project. | 

### Other Parameters

Other parameters are passed through a pointer to a apiApplyClusteringJobRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | Repeat it to retry a lost response without applying the job twice. | 

### Return type

[**ApplyClusteringJobOutcome**](ApplyClusteringJobOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BatchCreateQueryClusters

> BatchCreateQueryClustersOutcome BatchCreateQueryClusters(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).BatchCreateQueryClustersRequestData(batchCreateQueryClustersRequestData).Execute()

Create several keyword clusters at once



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
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | Repeat it to retry a lost response without creating the batch twice.
	batchCreateQueryClustersRequestData := *openapiclient.NewBatchCreateQueryClustersRequestData([]string{"Names_example"}) // BatchCreateQueryClustersRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ClustersAPI.BatchCreateQueryClusters(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).BatchCreateQueryClustersRequestData(batchCreateQueryClustersRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ClustersAPI.BatchCreateQueryClusters``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BatchCreateQueryClusters`: BatchCreateQueryClustersOutcome
	fmt.Fprintf(os.Stdout, "Response from `ClustersAPI.BatchCreateQueryClusters`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiBatchCreateQueryClustersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Repeat it to retry a lost response without creating the batch twice. | 
 **batchCreateQueryClustersRequestData** | [**BatchCreateQueryClustersRequestData**](BatchCreateQueryClustersRequestData.md) |  | 

### Return type

[**BatchCreateQueryClustersOutcome**](BatchCreateQueryClustersOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateQueryCluster

> QueryClusterResource CreateQueryCluster(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).CreateQueryClusterRequest(createQueryClusterRequest).Execute()

Create a keyword cluster



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
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "3f9d2c18-6b4a-4c77-9f10-6f2d5a7c8e21" // string | A token you choose per operation, 8 to 255 printable ASCII characters with no spaces; a UUID is the obvious choice. Repeat it to retry a lost response without creating a second cluster. The key is scoped to your API key, and it is bound to the method, the path and the body of the first attempt: repeating it with anything else changed is refused with 409 rather than replayed.
	createQueryClusterRequest := *openapiclient.NewCreateQueryClusterRequest() // CreateQueryClusterRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ClustersAPI.CreateQueryCluster(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).CreateQueryClusterRequest(createQueryClusterRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ClustersAPI.CreateQueryCluster``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateQueryCluster`: QueryClusterResource
	fmt.Fprintf(os.Stdout, "Response from `ClustersAPI.CreateQueryCluster`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateQueryClusterRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | A token you choose per operation, 8 to 255 printable ASCII characters with no spaces; a UUID is the obvious choice. Repeat it to retry a lost response without creating a second cluster. The key is scoped to your API key, and it is bound to the method, the path and the body of the first attempt: repeating it with anything else changed is refused with 409 rather than replayed. | 
 **createQueryClusterRequest** | [**CreateQueryClusterRequest**](CreateQueryClusterRequest.md) |  | 

### Return type

[**QueryClusterResource**](QueryClusterResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteQueryCluster

> DeleteQueryCluster200Response DeleteQueryCluster(ctx, organizationId, projectId, clusterId).IdempotencyKey(idempotencyKey).Execute()

Delete a keyword cluster



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
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	clusterId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must be a cluster of the project in the path.
	idempotencyKey := "idempotencyKey_example" // string | Repeat it to retry a lost response; a fresh key answers 404 once the cluster is gone.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ClustersAPI.DeleteQueryCluster(context.Background(), organizationId, projectId, clusterId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ClustersAPI.DeleteQueryCluster``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteQueryCluster`: DeleteQueryCluster200Response
	fmt.Fprintf(os.Stdout, "Response from `ClustersAPI.DeleteQueryCluster`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**clusterId** | **string** | Must be a cluster of the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteQueryClusterRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | Repeat it to retry a lost response; a fresh key answers 404 once the cluster is gone. | 

### Return type

[**DeleteQueryCluster200Response**](DeleteQueryCluster200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RenameQueryCluster

> QueryClusterResource RenameQueryCluster(ctx, organizationId, projectId, clusterId).IdempotencyKey(idempotencyKey).CreateQueryClusterRequest(createQueryClusterRequest).Execute()

Rename a keyword cluster



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
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	clusterId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must be a cluster of the project in the path.
	idempotencyKey := "idempotencyKey_example" // string | Repeat it to retry a lost response without renaming twice.
	createQueryClusterRequest := *openapiclient.NewCreateQueryClusterRequest() // CreateQueryClusterRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ClustersAPI.RenameQueryCluster(context.Background(), organizationId, projectId, clusterId).IdempotencyKey(idempotencyKey).CreateQueryClusterRequest(createQueryClusterRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ClustersAPI.RenameQueryCluster``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RenameQueryCluster`: QueryClusterResource
	fmt.Fprintf(os.Stdout, "Response from `ClustersAPI.RenameQueryCluster`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**clusterId** | **string** | Must be a cluster of the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiRenameQueryClusterRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | Repeat it to retry a lost response without renaming twice. | 
 **createQueryClusterRequest** | [**CreateQueryClusterRequest**](CreateQueryClusterRequest.md) |  | 

### Return type

[**QueryClusterResource**](QueryClusterResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartClusteringJob

> AcceptedJobResource StartClusteringJob(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).StartClusteringJobRequestData(startClusteringJobRequestData).Execute()

Start a keyword clustering job



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
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	idempotencyKey := "idempotencyKey_example" // string | Repeat it to retry a lost response without starting a second job.
	startClusteringJobRequestData := *openapiclient.NewStartClusteringJobRequestData([]string{"TrackedQueryIds_example"}, "Mode_example") // StartClusteringJobRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ClustersAPI.StartClusteringJob(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).StartClusteringJobRequestData(startClusteringJobRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ClustersAPI.StartClusteringJob``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StartClusteringJob`: AcceptedJobResource
	fmt.Fprintf(os.Stdout, "Response from `ClustersAPI.StartClusteringJob`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStartClusteringJobRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Repeat it to retry a lost response without starting a second job. | 
 **startClusteringJobRequestData** | [**StartClusteringJobRequestData**](StartClusteringJobRequestData.md) |  | 

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

