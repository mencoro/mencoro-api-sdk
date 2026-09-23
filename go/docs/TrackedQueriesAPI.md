# \TrackedQueriesAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddClustersToTrackedQuery**](TrackedQueriesAPI.md#AddClustersToTrackedQuery) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Add a tracked query to clusters
[**BatchChangeTrackedQueriesCheckFrequency**](TrackedQueriesAPI.md#BatchChangeTrackedQueriesCheckFrequency) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/check-frequency | Change how often several tracked queries are checked
[**BatchChangeTrackedQueriesNPasses**](TrackedQueriesAPI.md#BatchChangeTrackedQueriesNPasses) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/passes | Change how many passes several tracked queries run per check
[**BatchCreateTrackedQueries**](TrackedQueriesAPI.md#BatchCreateTrackedQueries) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Create tracked queries
[**BatchForceCheckTrackedQueries**](TrackedQueriesAPI.md#BatchForceCheckTrackedQueries) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check | Check several tracked queries now
[**BatchPauseTrackedQueries**](TrackedQueriesAPI.md#BatchPauseTrackedQueries) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/pause | Pause several tracked queries
[**BatchResumeTrackedQueries**](TrackedQueriesAPI.md#BatchResumeTrackedQueries) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/resume | Resume several tracked queries
[**BulkAddClustersToTrackedQueries**](TrackedQueriesAPI.md#BulkAddClustersToTrackedQueries) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Add many tracked queries to clusters
[**BulkDeleteTrackedQueries**](TrackedQueriesAPI.md#BulkDeleteTrackedQueries) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk-delete | Delete tracked queries
[**BulkRemoveClustersFromTrackedQueries**](TrackedQueriesAPI.md#BulkRemoveClustersFromTrackedQueries) | **Delete** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Remove many tracked queries from clusters
[**ChangeTrackedQueryCheckFrequency**](TrackedQueriesAPI.md#ChangeTrackedQueryCheckFrequency) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/check-frequency | Change how often a tracked query is checked
[**ChangeTrackedQueryNPasses**](TrackedQueriesAPI.md#ChangeTrackedQueryNPasses) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/passes | Change how many passes a tracked query runs per check
[**CountTrackedQueries**](TrackedQueriesAPI.md#CountTrackedQueries) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/count | Count a project&#39;s tracked queries and price checking them
[**ForceCheckAllActiveTrackedQueries**](TrackedQueriesAPI.md#ForceCheckAllActiveTrackedQueries) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check-all | Check every eligible tracked query of a project now
[**GetTrackedQuery**](TrackedQueriesAPI.md#GetTrackedQuery) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId} | Get a tracked query
[**PauseTrackedQuery**](TrackedQueriesAPI.md#PauseTrackedQuery) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/pause | Pause a tracked query
[**RemoveClustersFromTrackedQuery**](TrackedQueriesAPI.md#RemoveClustersFromTrackedQuery) | **Delete** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Remove a tracked query from clusters
[**ReportAiResponse**](TrackedQueriesAPI.md#ReportAiResponse) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/responses/{aiResponseId}/report | Report a problem with a captured AI answer
[**ResumeTrackedQuery**](TrackedQueriesAPI.md#ResumeTrackedQuery) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/resume | Resume a tracked query
[**SearchTrackedQueries**](TrackedQueriesAPI.md#SearchTrackedQueries) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Search a project&#39;s tracked queries
[**SearchTrackedQueryMentionMatches**](TrackedQueriesAPI.md#SearchTrackedQueryMentionMatches) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/mention-matches | List stored mention matches of a tracked query
[**SearchTrackedQuerySerpMatches**](TrackedQueriesAPI.md#SearchTrackedQuerySerpMatches) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/serp-matches | List stored serp matches of a tracked query



## AddClustersToTrackedQuery

> TrackedQueryDetailResource AddClustersToTrackedQuery(ctx, organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).ClusterMembershipRequestData(clusterMembershipRequestData).Execute()

Add a tracked query to clusters



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
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write.
	clusterMembershipRequestData := *openapiclient.NewClusterMembershipRequestData([]string{"QueryClusterIds_example"}) // ClusterMembershipRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.AddClustersToTrackedQuery(context.Background(), organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).ClusterMembershipRequestData(clusterMembershipRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.AddClustersToTrackedQuery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddClustersToTrackedQuery`: TrackedQueryDetailResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.AddClustersToTrackedQuery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** | Must belong to the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddClustersToTrackedQueryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write. | 
 **clusterMembershipRequestData** | [**ClusterMembershipRequestData**](ClusterMembershipRequestData.md) |  | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BatchChangeTrackedQueriesCheckFrequency

> BatchWriteOutcome BatchChangeTrackedQueriesCheckFrequency(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).BatchChangeTrackedQueryCheckFrequencyRequestData(batchChangeTrackedQueryCheckFrequencyRequestData).Execute()

Change how often several tracked queries are checked



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
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
	batchChangeTrackedQueryCheckFrequencyRequestData := *openapiclient.NewBatchChangeTrackedQueryCheckFrequencyRequestData([]string{"Ids_example"}, "CheckFrequency_example") // BatchChangeTrackedQueryCheckFrequencyRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.BatchChangeTrackedQueriesCheckFrequency(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).BatchChangeTrackedQueryCheckFrequencyRequestData(batchChangeTrackedQueryCheckFrequencyRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.BatchChangeTrackedQueriesCheckFrequency``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BatchChangeTrackedQueriesCheckFrequency`: BatchWriteOutcome
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.BatchChangeTrackedQueriesCheckFrequency`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiBatchChangeTrackedQueriesCheckFrequencyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | 
 **batchChangeTrackedQueryCheckFrequencyRequestData** | [**BatchChangeTrackedQueryCheckFrequencyRequestData**](BatchChangeTrackedQueryCheckFrequencyRequestData.md) |  | 

### Return type

[**BatchWriteOutcome**](BatchWriteOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BatchChangeTrackedQueriesNPasses

> BatchWriteOutcome BatchChangeTrackedQueriesNPasses(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).BatchChangeTrackedQueryPassesRequestData(batchChangeTrackedQueryPassesRequestData).Execute()

Change how many passes several tracked queries run per check



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
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
	batchChangeTrackedQueryPassesRequestData := *openapiclient.NewBatchChangeTrackedQueryPassesRequestData([]string{"Ids_example"}, int32(123)) // BatchChangeTrackedQueryPassesRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.BatchChangeTrackedQueriesNPasses(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).BatchChangeTrackedQueryPassesRequestData(batchChangeTrackedQueryPassesRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.BatchChangeTrackedQueriesNPasses``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BatchChangeTrackedQueriesNPasses`: BatchWriteOutcome
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.BatchChangeTrackedQueriesNPasses`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiBatchChangeTrackedQueriesNPassesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | 
 **batchChangeTrackedQueryPassesRequestData** | [**BatchChangeTrackedQueryPassesRequestData**](BatchChangeTrackedQueryPassesRequestData.md) |  | 

### Return type

[**BatchWriteOutcome**](BatchWriteOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BatchCreateTrackedQueries

> BatchCreateTrackedQueriesResultResource BatchCreateTrackedQueries(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).BatchCreateTrackedQueriesRequestData(batchCreateTrackedQueriesRequestData).Execute()

Create tracked queries



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
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of creating anything again.
	batchCreateTrackedQueriesRequestData := *openapiclient.NewBatchCreateTrackedQueriesRequestData([]string{"QueryTexts_example"}, []string{"Engines_example"}, []string{"Countries_example"}, "CheckFrequency_example", int32(123), []string{"QueryClusterIds_example"}) // BatchCreateTrackedQueriesRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.BatchCreateTrackedQueries(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).BatchCreateTrackedQueriesRequestData(batchCreateTrackedQueriesRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.BatchCreateTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BatchCreateTrackedQueries`: BatchCreateTrackedQueriesResultResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.BatchCreateTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiBatchCreateTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | A client-chosen key, unique per operation. Replaying it returns the first answer instead of creating anything again. | 
 **batchCreateTrackedQueriesRequestData** | [**BatchCreateTrackedQueriesRequestData**](BatchCreateTrackedQueriesRequestData.md) |  | 

### Return type

[**BatchCreateTrackedQueriesResultResource**](BatchCreateTrackedQueriesResultResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BatchForceCheckTrackedQueries

> BatchForceCheckTrackedQueries200Response BatchForceCheckTrackedQueries(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).BatchTargetsRequestData(batchTargetsRequestData).Execute()

Check several tracked queries now



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
	idempotencyKey := "idempotencyKey_example" // string | Repeating a request with the same key and the same ids answers with the first attempt's result instead of submitting again.
	batchTargetsRequestData := *openapiclient.NewBatchTargetsRequestData([]string{"Ids_example"}) // BatchTargetsRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.BatchForceCheckTrackedQueries(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).BatchTargetsRequestData(batchTargetsRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.BatchForceCheckTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BatchForceCheckTrackedQueries`: BatchForceCheckTrackedQueries200Response
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.BatchForceCheckTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiBatchForceCheckTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Repeating a request with the same key and the same ids answers with the first attempt&#39;s result instead of submitting again. | 
 **batchTargetsRequestData** | [**BatchTargetsRequestData**](BatchTargetsRequestData.md) |  | 

### Return type

[**BatchForceCheckTrackedQueries200Response**](BatchForceCheckTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BatchPauseTrackedQueries

> BatchPauseTrackedQueries200Response BatchPauseTrackedQueries(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).BatchTargetsRequestData(batchTargetsRequestData).Execute()

Pause several tracked queries



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
	idempotencyKey := "idempotencyKey_example" // string | Repeating a request with the same key and the same ids answers with the first attempt's result.
	batchTargetsRequestData := *openapiclient.NewBatchTargetsRequestData([]string{"Ids_example"}) // BatchTargetsRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.BatchPauseTrackedQueries(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).BatchTargetsRequestData(batchTargetsRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.BatchPauseTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BatchPauseTrackedQueries`: BatchPauseTrackedQueries200Response
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.BatchPauseTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiBatchPauseTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Repeating a request with the same key and the same ids answers with the first attempt&#39;s result. | 
 **batchTargetsRequestData** | [**BatchTargetsRequestData**](BatchTargetsRequestData.md) |  | 

### Return type

[**BatchPauseTrackedQueries200Response**](BatchPauseTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BatchResumeTrackedQueries

> BatchResumeTrackedQueries200Response BatchResumeTrackedQueries(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).BatchTargetsRequestData(batchTargetsRequestData).Execute()

Resume several tracked queries



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
	idempotencyKey := "idempotencyKey_example" // string | Repeating a request with the same key and the same ids answers with the first attempt's result.
	batchTargetsRequestData := *openapiclient.NewBatchTargetsRequestData([]string{"Ids_example"}) // BatchTargetsRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.BatchResumeTrackedQueries(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).BatchTargetsRequestData(batchTargetsRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.BatchResumeTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BatchResumeTrackedQueries`: BatchResumeTrackedQueries200Response
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.BatchResumeTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiBatchResumeTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Repeating a request with the same key and the same ids answers with the first attempt&#39;s result. | 
 **batchTargetsRequestData** | [**BatchTargetsRequestData**](BatchTargetsRequestData.md) |  | 

### Return type

[**BatchResumeTrackedQueries200Response**](BatchResumeTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BulkAddClustersToTrackedQueries

> BulkAddClustersToTrackedQueries200Response BulkAddClustersToTrackedQueries(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).BulkAddClustersToTrackedQueriesRequest(bulkAddClustersToTrackedQueriesRequest).Execute()

Add many tracked queries to clusters



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
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch.
	bulkAddClustersToTrackedQueriesRequest := *openapiclient.NewBulkAddClustersToTrackedQueriesRequest() // BulkAddClustersToTrackedQueriesRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.BulkAddClustersToTrackedQueries(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).BulkAddClustersToTrackedQueriesRequest(bulkAddClustersToTrackedQueriesRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.BulkAddClustersToTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkAddClustersToTrackedQueries`: BulkAddClustersToTrackedQueries200Response
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.BulkAddClustersToTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkAddClustersToTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch. | 
 **bulkAddClustersToTrackedQueriesRequest** | [**BulkAddClustersToTrackedQueriesRequest**](BulkAddClustersToTrackedQueriesRequest.md) |  | 

### Return type

[**BulkAddClustersToTrackedQueries200Response**](BulkAddClustersToTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BulkDeleteTrackedQueries

> BatchWriteOutcome BulkDeleteTrackedQueries(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).BatchTargetsRequestData(batchTargetsRequestData).Execute()

Delete tracked queries



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
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of deleting anything again.
	batchTargetsRequestData := *openapiclient.NewBatchTargetsRequestData([]string{"Ids_example"}) // BatchTargetsRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.BulkDeleteTrackedQueries(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).BatchTargetsRequestData(batchTargetsRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.BulkDeleteTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkDeleteTrackedQueries`: BatchWriteOutcome
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.BulkDeleteTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkDeleteTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | A client-chosen key, unique per operation. Replaying it returns the first answer instead of deleting anything again. | 
 **batchTargetsRequestData** | [**BatchTargetsRequestData**](BatchTargetsRequestData.md) |  | 

### Return type

[**BatchWriteOutcome**](BatchWriteOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BulkRemoveClustersFromTrackedQueries

> BulkRemoveClustersFromTrackedQueries200Response BulkRemoveClustersFromTrackedQueries(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).BulkRemoveClustersFromTrackedQueriesRequest(bulkRemoveClustersFromTrackedQueriesRequest).Execute()

Remove many tracked queries from clusters



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
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch.
	bulkRemoveClustersFromTrackedQueriesRequest := *openapiclient.NewBulkRemoveClustersFromTrackedQueriesRequest() // BulkRemoveClustersFromTrackedQueriesRequest | Required. A DELETE with no body is rejected.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.BulkRemoveClustersFromTrackedQueries(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).BulkRemoveClustersFromTrackedQueriesRequest(bulkRemoveClustersFromTrackedQueriesRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.BulkRemoveClustersFromTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkRemoveClustersFromTrackedQueries`: BulkRemoveClustersFromTrackedQueries200Response
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.BulkRemoveClustersFromTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkRemoveClustersFromTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | A client-chosen key, unique per operation, so a lost response can be retried without repeating the batch. | 
 **bulkRemoveClustersFromTrackedQueriesRequest** | [**BulkRemoveClustersFromTrackedQueriesRequest**](BulkRemoveClustersFromTrackedQueriesRequest.md) | Required. A DELETE with no body is rejected. | 

### Return type

[**BulkRemoveClustersFromTrackedQueries200Response**](BulkRemoveClustersFromTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ChangeTrackedQueryCheckFrequency

> TrackedQueryDetailResource ChangeTrackedQueryCheckFrequency(ctx, organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).ChangeTrackedQueryCheckFrequencyRequestData(changeTrackedQueryCheckFrequencyRequestData).Execute()

Change how often a tracked query is checked



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
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
	changeTrackedQueryCheckFrequencyRequestData := *openapiclient.NewChangeTrackedQueryCheckFrequencyRequestData("CheckFrequency_example") // ChangeTrackedQueryCheckFrequencyRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.ChangeTrackedQueryCheckFrequency(context.Background(), organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).ChangeTrackedQueryCheckFrequencyRequestData(changeTrackedQueryCheckFrequencyRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.ChangeTrackedQueryCheckFrequency``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ChangeTrackedQueryCheckFrequency`: TrackedQueryDetailResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.ChangeTrackedQueryCheckFrequency`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** | Must belong to the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiChangeTrackedQueryCheckFrequencyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | 
 **changeTrackedQueryCheckFrequencyRequestData** | [**ChangeTrackedQueryCheckFrequencyRequestData**](ChangeTrackedQueryCheckFrequencyRequestData.md) |  | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ChangeTrackedQueryNPasses

> TrackedQueryDetailResource ChangeTrackedQueryNPasses(ctx, organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).ChangeTrackedQueryPassesRequestData(changeTrackedQueryPassesRequestData).Execute()

Change how many passes a tracked query runs per check



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
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again.
	changeTrackedQueryPassesRequestData := *openapiclient.NewChangeTrackedQueryPassesRequestData(int32(123)) // ChangeTrackedQueryPassesRequestData | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.ChangeTrackedQueryNPasses(context.Background(), organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).ChangeTrackedQueryPassesRequestData(changeTrackedQueryPassesRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.ChangeTrackedQueryNPasses``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ChangeTrackedQueryNPasses`: TrackedQueryDetailResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.ChangeTrackedQueryNPasses`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** | Must belong to the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiChangeTrackedQueryNPassesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | A client-chosen key, unique per operation. Replaying it returns the first answer instead of applying anything again. | 
 **changeTrackedQueryPassesRequestData** | [**ChangeTrackedQueryPassesRequestData**](ChangeTrackedQueryPassesRequestData.md) |  | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CountTrackedQueries

> TrackedQueryCountResource CountTrackedQueries(ctx, organizationId, projectId).Status(status).Execute()

Count a project's tracked queries and price checking them



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
	status := "status_example" // string | Restrict both numbers to one status. Lower-case; an unknown value is rejected, not ignored. Omitted, every status is counted and priced. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.CountTrackedQueries(context.Background(), organizationId, projectId).Status(status).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.CountTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CountTrackedQueries`: TrackedQueryCountResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.CountTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCountTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **status** | **string** | Restrict both numbers to one status. Lower-case; an unknown value is rejected, not ignored. Omitted, every status is counted and priced. | 

### Return type

[**TrackedQueryCountResource**](TrackedQueryCountResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ForceCheckAllActiveTrackedQueries

> SubmittedChecksResource ForceCheckAllActiveTrackedQueries(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).Execute()

Check every eligible tracked query of a project now



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
	idempotencyKey := "idempotencyKey_example" // string | Repeating a request with the same key answers with the first attempt's result instead of submitting a second wave.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.ForceCheckAllActiveTrackedQueries(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.ForceCheckAllActiveTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ForceCheckAllActiveTrackedQueries`: SubmittedChecksResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.ForceCheckAllActiveTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiForceCheckAllActiveTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Repeating a request with the same key answers with the first attempt&#39;s result instead of submitting a second wave. | 

### Return type

[**SubmittedChecksResource**](SubmittedChecksResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTrackedQuery

> TrackedQueryDetailResource GetTrackedQuery(ctx, organizationId, projectId, trackedQueryId).Execute()

Get a tracked query



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
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.GetTrackedQuery(context.Background(), organizationId, projectId, trackedQueryId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.GetTrackedQuery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTrackedQuery`: TrackedQueryDetailResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.GetTrackedQuery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** | Must belong to the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTrackedQueryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PauseTrackedQuery

> TrackedQueryDetailResource PauseTrackedQuery(ctx, organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).Execute()

Pause a tracked query



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
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.
	idempotencyKey := "idempotencyKey_example" // string | Repeating a request with the same key answers with the first attempt's result instead of pausing again.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.PauseTrackedQuery(context.Background(), organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.PauseTrackedQuery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PauseTrackedQuery`: TrackedQueryDetailResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.PauseTrackedQuery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** | Must belong to the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiPauseTrackedQueryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | Repeating a request with the same key answers with the first attempt&#39;s result instead of pausing again. | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RemoveClustersFromTrackedQuery

> TrackedQueryDetailResource RemoveClustersFromTrackedQuery(ctx, organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).ClusterMembershipRequestData(clusterMembershipRequestData).Execute()

Remove a tracked query from clusters



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
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write.
	clusterMembershipRequestData := *openapiclient.NewClusterMembershipRequestData([]string{"QueryClusterIds_example"}) // ClusterMembershipRequestData | Required. A DELETE with no body is rejected.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.RemoveClustersFromTrackedQuery(context.Background(), organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).ClusterMembershipRequestData(clusterMembershipRequestData).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.RemoveClustersFromTrackedQuery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RemoveClustersFromTrackedQuery`: TrackedQueryDetailResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.RemoveClustersFromTrackedQuery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** | Must belong to the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiRemoveClustersFromTrackedQueryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | A client-chosen key, unique per operation, so a lost response can be retried without repeating the write. | 
 **clusterMembershipRequestData** | [**ClusterMembershipRequestData**](ClusterMembershipRequestData.md) | Required. A DELETE with no body is rejected. | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ReportAiResponse

> AiResponseReportResource ReportAiResponse(ctx, organizationId, projectId, trackedQueryId, aiResponseId).IdempotencyKey(idempotencyKey).ReportAiResponseRequest(reportAiResponseRequest).Execute()

Report a problem with a captured AI answer



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
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.
	aiResponseId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | A capture id from the AI responses listing. Must belong to the tracked query in the path.
	idempotencyKey := "idempotencyKey_example" // string | A client-chosen key, unique per report, so a lost response can be retried without filing the report twice.
	reportAiResponseRequest := *openapiclient.NewReportAiResponseRequest("Type_example") // ReportAiResponseRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.ReportAiResponse(context.Background(), organizationId, projectId, trackedQueryId, aiResponseId).IdempotencyKey(idempotencyKey).ReportAiResponseRequest(reportAiResponseRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.ReportAiResponse``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ReportAiResponse`: AiResponseReportResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.ReportAiResponse`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** | Must belong to the project in the path. | 
**aiResponseId** | **string** | A capture id from the AI responses listing. Must belong to the tracked query in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiReportAiResponseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **idempotencyKey** | **string** | A client-chosen key, unique per report, so a lost response can be retried without filing the report twice. | 
 **reportAiResponseRequest** | [**ReportAiResponseRequest**](ReportAiResponseRequest.md) |  | 

### Return type

[**AiResponseReportResource**](AiResponseReportResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ResumeTrackedQuery

> TrackedQueryDetailResource ResumeTrackedQuery(ctx, organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).Execute()

Resume a tracked query



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
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.
	idempotencyKey := "idempotencyKey_example" // string | Repeating a request with the same key answers with the first attempt's result instead of resuming again.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.ResumeTrackedQuery(context.Background(), organizationId, projectId, trackedQueryId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.ResumeTrackedQuery``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ResumeTrackedQuery`: TrackedQueryDetailResource
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.ResumeTrackedQuery`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** | Must belong to the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiResumeTrackedQueryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | Repeating a request with the same key answers with the first attempt&#39;s result instead of resuming again. | 

### Return type

[**TrackedQueryDetailResource**](TrackedQueryDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SearchTrackedQueries

> SearchTrackedQueries200Response SearchTrackedQueries(ctx, organizationId, projectId).Limit(limit).Offset(offset).Search(search).Status(status).Engines(engines).Countries(countries).SortBy(sortBy).SortOrder(sortOrder).Execute()

Search a project's tracked queries



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
	limit := int32(56) // int32 | Page size. A value above the maximum is rejected, never clamped. (optional) (default to 20)
	offset := int32(56) // int32 |  (optional) (default to 0)
	search := "search_example" // string | Free-text search over the keyword. (optional)
	status := "status_example" // string |  (optional)
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. (optional)
	countries := []string{"Inner_example"} // []string | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
	sortBy := "sortBy_example" // string |  (optional) (default to "queryText")
	sortOrder := "sortOrder_example" // string |  (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.SearchTrackedQueries(context.Background(), organizationId, projectId).Limit(limit).Offset(offset).Search(search).Status(status).Engines(engines).Countries(countries).SortBy(sortBy).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.SearchTrackedQueries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SearchTrackedQueries`: SearchTrackedQueries200Response
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.SearchTrackedQueries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiSearchTrackedQueriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** | Page size. A value above the maximum is rejected, never clamped. | [default to 20]
 **offset** | **int32** |  | [default to 0]
 **search** | **string** | Free-text search over the keyword. | 
 **status** | **string** |  | 
 **engines** | **[]string** | Repeatable, or comma-separated. | 
 **countries** | **[]string** | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | 
 **sortBy** | **string** |  | [default to &quot;queryText&quot;]
 **sortOrder** | **string** |  | [default to &quot;desc&quot;]

### Return type

[**SearchTrackedQueries200Response**](SearchTrackedQueries200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SearchTrackedQueryMentionMatches

> SearchTrackedQueryMentionMatches200Response SearchTrackedQueryMentionMatches(ctx, organizationId, projectId, trackedQueryId).DateFrom(dateFrom).DateTo(dateTo).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()

List stored mention matches of a tracked query



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
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive UTC day; defaults to the retention floor. (optional)
	dateTo := time.Now() // string | Inclusive UTC day. (optional)
	limit := int32(56) // int32 |  (optional) (default to 20)
	offset := int32(56) // int32 |  (optional) (default to 0)
	sortOrder := "sortOrder_example" // string |  (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.SearchTrackedQueryMentionMatches(context.Background(), organizationId, projectId, trackedQueryId).DateFrom(dateFrom).DateTo(dateTo).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.SearchTrackedQueryMentionMatches``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SearchTrackedQueryMentionMatches`: SearchTrackedQueryMentionMatches200Response
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.SearchTrackedQueryMentionMatches`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiSearchTrackedQueryMentionMatchesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **dateFrom** | **string** | Inclusive UTC day; defaults to the retention floor. | 
 **dateTo** | **string** | Inclusive UTC day. | 
 **limit** | **int32** |  | [default to 20]
 **offset** | **int32** |  | [default to 0]
 **sortOrder** | **string** |  | [default to &quot;desc&quot;]

### Return type

[**SearchTrackedQueryMentionMatches200Response**](SearchTrackedQueryMentionMatches200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SearchTrackedQuerySerpMatches

> SearchTrackedQuerySerpMatches200Response SearchTrackedQuerySerpMatches(ctx, organizationId, projectId, trackedQueryId).DateFrom(dateFrom).DateTo(dateTo).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()

List stored serp matches of a tracked query



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
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive UTC day; defaults to the retention floor. (optional)
	dateTo := time.Now() // string | Inclusive UTC day. (optional)
	limit := int32(56) // int32 |  (optional) (default to 20)
	offset := int32(56) // int32 |  (optional) (default to 0)
	sortOrder := "sortOrder_example" // string |  (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TrackedQueriesAPI.SearchTrackedQuerySerpMatches(context.Background(), organizationId, projectId, trackedQueryId).DateFrom(dateFrom).DateTo(dateTo).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TrackedQueriesAPI.SearchTrackedQuerySerpMatches``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SearchTrackedQuerySerpMatches`: SearchTrackedQuerySerpMatches200Response
	fmt.Fprintf(os.Stdout, "Response from `TrackedQueriesAPI.SearchTrackedQuerySerpMatches`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiSearchTrackedQuerySerpMatchesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **dateFrom** | **string** | Inclusive UTC day; defaults to the retention floor. | 
 **dateTo** | **string** | Inclusive UTC day. | 
 **limit** | **int32** |  | [default to 20]
 **offset** | **int32** |  | [default to 0]
 **sortOrder** | **string** |  | [default to &quot;desc&quot;]

### Return type

[**SearchTrackedQuerySerpMatches200Response**](SearchTrackedQuerySerpMatches200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

