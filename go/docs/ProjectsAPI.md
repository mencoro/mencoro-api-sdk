# \ProjectsAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ArchiveProject**](ProjectsAPI.md#ArchiveProject) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/archive | Archive a project
[**CreateCompetitor**](ProjectsAPI.md#CreateCompetitor) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | Add a competitor to a project
[**CreateProject**](ProjectsAPI.md#CreateProject) | **Post** /api/v1/organizations/{organizationId}/projects | Create a project and the brand monitoring profile its checks run against
[**DeleteCompetitor**](ProjectsAPI.md#DeleteCompetitor) | **Delete** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Remove a competitor from a project
[**GetBrandProfile**](ProjectsAPI.md#GetBrandProfile) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Get a project&#39;s brand monitoring profile
[**GetProject**](ProjectsAPI.md#GetProject) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId} | Get a project and its brand monitoring configuration
[**ListCompetitors**](ProjectsAPI.md#ListCompetitors) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | List the competitors tracked by a project
[**ListProjects**](ProjectsAPI.md#ListProjects) | **Get** /api/v1/organizations/{organizationId}/projects | List an organization&#39;s projects
[**ListQueryClusters**](ProjectsAPI.md#ListQueryClusters) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | List the keyword clusters of a project
[**RestoreProject**](ProjectsAPI.md#RestoreProject) | **Post** /api/v1/organizations/{organizationId}/projects/{projectId}/restore | Restore an archived project
[**UpdateCompetitor**](ProjectsAPI.md#UpdateCompetitor) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Replace a competitor
[**UpdateProject**](ProjectsAPI.md#UpdateProject) | **Patch** /api/v1/organizations/{organizationId}/projects/{projectId} | Rename a project
[**UpdateProjectBrandProfile**](ProjectsAPI.md#UpdateProjectBrandProfile) | **Put** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Replace a project&#39;s brand monitoring profile



## ArchiveProject

> ProjectDetailResource ArchiveProject(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).Execute()

Archive a project



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
	idempotencyKey := "idempotencyKey_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.ArchiveProject(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.ArchiveProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArchiveProject`: ProjectDetailResource
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.ArchiveProject`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiArchiveProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  | 

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateCompetitor

> CompetitorResource CreateCompetitor(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).CreateCompetitorRequest(createCompetitorRequest).Execute()

Add a competitor to a project



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
	idempotencyKey := "idempotencyKey_example" // string | Unique per attempt. Without it a lost response cannot be retried without risking a second competitor.
	createCompetitorRequest := *openapiclient.NewCreateCompetitorRequest() // CreateCompetitorRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.CreateCompetitor(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).CreateCompetitorRequest(createCompetitorRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.CreateCompetitor``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateCompetitor`: CompetitorResource
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.CreateCompetitor`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** | Must belong to the organization in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateCompetitorRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Unique per attempt. Without it a lost response cannot be retried without risking a second competitor. | 
 **createCompetitorRequest** | [**CreateCompetitorRequest**](CreateCompetitorRequest.md) |  | 

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateProject

> ProjectDetailResource CreateProject(ctx, organizationId).IdempotencyKey(idempotencyKey).CreateProjectRequest(createProjectRequest).Execute()

Create a project and the brand monitoring profile its checks run against



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
	idempotencyKey := "idempotencyKey_example" // string | 
	createProjectRequest := *openapiclient.NewCreateProjectRequest("Name_example", []string{"WebsiteDomains_example"}, []string{"BrandNames_example"}) // CreateProjectRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.CreateProject(context.Background(), organizationId).IdempotencyKey(idempotencyKey).CreateProjectRequest(createProjectRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.CreateProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateProject`: ProjectDetailResource
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.CreateProject`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** |  | 
 **createProjectRequest** | [**CreateProjectRequest**](CreateProjectRequest.md) |  | 

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteCompetitor

> CompetitorResource DeleteCompetitor(ctx, organizationId, projectId, competitorId).IdempotencyKey(idempotencyKey).Execute()

Remove a competitor from a project



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
	competitorId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.
	idempotencyKey := "idempotencyKey_example" // string | Unique per attempt. A retry carrying the same key is answered from the record instead of running again.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.DeleteCompetitor(context.Background(), organizationId, projectId, competitorId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.DeleteCompetitor``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteCompetitor`: CompetitorResource
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.DeleteCompetitor`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** | Must belong to the organization in the path. | 
**competitorId** | **string** | Must belong to the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteCompetitorRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | Unique per attempt. A retry carrying the same key is answered from the record instead of running again. | 

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetBrandProfile

> BrandProfileResource GetBrandProfile(ctx, organizationId, projectId).Execute()

Get a project's brand monitoring profile



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.GetBrandProfile(context.Background(), organizationId, projectId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.GetBrandProfile``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBrandProfile`: BrandProfileResource
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.GetBrandProfile`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** | Must belong to the organization in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetBrandProfileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**BrandProfileResource**](BrandProfileResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProject

> ProjectDetailResource GetProject(ctx, organizationId, projectId).Execute()

Get a project and its brand monitoring configuration



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.GetProject(context.Background(), organizationId, projectId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.GetProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetProject`: ProjectDetailResource
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.GetProject`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListCompetitors

> ListCompetitors200Response ListCompetitors(ctx, organizationId, projectId).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()

List the competitors tracked by a project



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
	limit := int32(56) // int32 | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
	offset := int32(56) // int32 | Number of competitors to skip before the page starts. (optional) (default to 0)
	sortOrder := "sortOrder_example" // string | Direction of the id ordering. An unknown value is rejected, not replaced by the default. (optional) (default to "asc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.ListCompetitors(context.Background(), organizationId, projectId).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.ListCompetitors``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListCompetitors`: ListCompetitors200Response
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.ListCompetitors`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListCompetitorsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** | Page size. A larger value is rejected, never silently reduced. | [default to 20]
 **offset** | **int32** | Number of competitors to skip before the page starts. | [default to 0]
 **sortOrder** | **string** | Direction of the id ordering. An unknown value is rejected, not replaced by the default. | [default to &quot;asc&quot;]

### Return type

[**ListCompetitors200Response**](ListCompetitors200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListProjects

> ListProjects200Response ListProjects(ctx, organizationId).Limit(limit).Offset(offset).Search(search).Status(status).SortBy(sortBy).SortOrder(sortOrder).Execute()

List an organization's projects



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
	limit := int32(2) // int32 | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
	offset := int32(4) // int32 | Rows to skip before the page starts. Page by advancing it in steps of `limit` until it reaches `total`. (optional) (default to 0)
	search := "search_example" // string |  (optional)
	status := "status_example" // string |  (optional)
	sortBy := "sortBy_example" // string |  (optional) (default to "createdAt")
	sortOrder := "sortOrder_example" // string |  (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.ListProjects(context.Background(), organizationId).Limit(limit).Offset(offset).Search(search).Status(status).SortBy(sortBy).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.ListProjects``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListProjects`: ListProjects200Response
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.ListProjects`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListProjectsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** | Page size. A larger value is rejected, never silently reduced. | [default to 20]
 **offset** | **int32** | Rows to skip before the page starts. Page by advancing it in steps of &#x60;limit&#x60; until it reaches &#x60;total&#x60;. | [default to 0]
 **search** | **string** |  | 
 **status** | **string** |  | 
 **sortBy** | **string** |  | [default to &quot;createdAt&quot;]
 **sortOrder** | **string** |  | [default to &quot;desc&quot;]

### Return type

[**ListProjects200Response**](ListProjects200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListQueryClusters

> ListQueryClusters200Response ListQueryClusters(ctx, organizationId, projectId).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()

List the keyword clusters of a project



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
	limit := int32(56) // int32 | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
	offset := int32(56) // int32 | Number of clusters to skip before the page starts. (optional) (default to 0)
	sortOrder := "sortOrder_example" // string | Direction of the name ordering. An unknown value is rejected, not replaced by the default. (optional) (default to "asc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.ListQueryClusters(context.Background(), organizationId, projectId).Limit(limit).Offset(offset).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.ListQueryClusters``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListQueryClusters`: ListQueryClusters200Response
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.ListQueryClusters`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListQueryClustersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** | Page size. A larger value is rejected, never silently reduced. | [default to 20]
 **offset** | **int32** | Number of clusters to skip before the page starts. | [default to 0]
 **sortOrder** | **string** | Direction of the name ordering. An unknown value is rejected, not replaced by the default. | [default to &quot;asc&quot;]

### Return type

[**ListQueryClusters200Response**](ListQueryClusters200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreProject

> ProjectDetailResource RestoreProject(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).Execute()

Restore an archived project



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
	idempotencyKey := "idempotencyKey_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.RestoreProject(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.RestoreProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreProject`: ProjectDetailResource
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.RestoreProject`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  | 

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateCompetitor

> CompetitorResource UpdateCompetitor(ctx, organizationId, projectId, competitorId).IdempotencyKey(idempotencyKey).CreateCompetitorRequest(createCompetitorRequest).Execute()

Replace a competitor



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
	competitorId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.
	idempotencyKey := "idempotencyKey_example" // string | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
	createCompetitorRequest := *openapiclient.NewCreateCompetitorRequest() // CreateCompetitorRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.UpdateCompetitor(context.Background(), organizationId, projectId, competitorId).IdempotencyKey(idempotencyKey).CreateCompetitorRequest(createCompetitorRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.UpdateCompetitor``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateCompetitor`: CompetitorResource
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.UpdateCompetitor`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** | Must belong to the organization in the path. | 
**competitorId** | **string** | Must belong to the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateCompetitorRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. | 
 **createCompetitorRequest** | [**CreateCompetitorRequest**](CreateCompetitorRequest.md) |  | 

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateProject

> ProjectDetailResource UpdateProject(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).UpdateProjectRequest(updateProjectRequest).Execute()

Rename a project



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
	idempotencyKey := "idempotencyKey_example" // string | 
	updateProjectRequest := *openapiclient.NewUpdateProjectRequest("Name_example") // UpdateProjectRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.UpdateProject(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).UpdateProjectRequest(updateProjectRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.UpdateProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateProject`: ProjectDetailResource
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.UpdateProject`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  | 
 **updateProjectRequest** | [**UpdateProjectRequest**](UpdateProjectRequest.md) |  | 

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateProjectBrandProfile

> BrandProfileResource UpdateProjectBrandProfile(ctx, organizationId, projectId).IdempotencyKey(idempotencyKey).UpdateProjectBrandProfileRequest(updateProjectBrandProfileRequest).Execute()

Replace a project's brand monitoring profile



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
	idempotencyKey := "idempotencyKey_example" // string | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
	updateProjectBrandProfileRequest := *openapiclient.NewUpdateProjectBrandProfileRequest() // UpdateProjectBrandProfileRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ProjectsAPI.UpdateProjectBrandProfile(context.Background(), organizationId, projectId).IdempotencyKey(idempotencyKey).UpdateProjectBrandProfileRequest(updateProjectBrandProfileRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ProjectsAPI.UpdateProjectBrandProfile``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateProjectBrandProfile`: BrandProfileResource
	fmt.Fprintf(os.Stdout, "Response from `ProjectsAPI.UpdateProjectBrandProfile`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** | Must belong to the organization in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateProjectBrandProfileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. | 
 **updateProjectBrandProfileRequest** | [**UpdateProjectBrandProfileRequest**](UpdateProjectBrandProfileRequest.md) |  | 

### Return type

[**BrandProfileResource**](BrandProfileResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

