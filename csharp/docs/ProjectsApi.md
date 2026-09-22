# Mencoro.Api.Api.ProjectsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ArchiveProject**](ProjectsApi.md#archiveproject) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/archive | Archive a project |
| [**CreateCompetitor**](ProjectsApi.md#createcompetitor) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | Add a competitor to a project |
| [**CreateProject**](ProjectsApi.md#createproject) | **POST** /api/v1/organizations/{organizationId}/projects | Create a project and the brand monitoring profile its checks run against |
| [**DeleteCompetitor**](ProjectsApi.md#deletecompetitor) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Remove a competitor from a project |
| [**GetBrandProfile**](ProjectsApi.md#getbrandprofile) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Get a project&#39;s brand monitoring profile |
| [**GetProject**](ProjectsApi.md#getproject) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId} | Get a project and its brand monitoring configuration |
| [**ListCompetitors**](ProjectsApi.md#listcompetitors) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | List the competitors tracked by a project |
| [**ListProjects**](ProjectsApi.md#listprojects) | **GET** /api/v1/organizations/{organizationId}/projects | List an organization&#39;s projects |
| [**ListQueryClusters**](ProjectsApi.md#listqueryclusters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | List the keyword clusters of a project |
| [**RestoreProject**](ProjectsApi.md#restoreproject) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/restore | Restore an archived project |
| [**UpdateCompetitor**](ProjectsApi.md#updatecompetitor) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Replace a competitor |
| [**UpdateProject**](ProjectsApi.md#updateproject) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId} | Rename a project |
| [**UpdateProjectBrandProfile**](ProjectsApi.md#updateprojectbrandprofile) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Replace a project&#39;s brand monitoring profile |

<a id="archiveproject"></a>
# **ArchiveProject**
> ProjectDetailResource ArchiveProject (Guid organizationId, Guid projectId, string idempotencyKey)

Archive a project

Minimum role: manager, in an active organization. Requires the \"write\" capability. Archiving stops a project from being modified: its name, brand profile and competitors are refused with 409 until it is restored. What is NOT done: nothing is deleted. Tracked queries, captured responses, mentions and every metric already collected stay exactly as they are, and restoreProject brings the project back with all of it. Archiving is recorded as done by the caller, not by an organization cascade, so restoring the organization later will not restore this project — restore it explicitly. This endpoint takes no body, and one carrying fields is refused. Archiving an already archived project answers 409, unless the call is a retry carrying the key that archived it. Send an Idempotency-Key; a retry with the same key returns the recorded answer.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class ArchiveProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | 

            try
            {
                // Archive a project
                ProjectDetailResource result = apiInstance.ArchiveProject(organizationId, projectId, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.ArchiveProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ArchiveProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Archive a project
    ApiResponse<ProjectDetailResource> response = apiInstance.ArchiveProjectWithHttpInfo(organizationId, projectId, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.ArchiveProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **idempotencyKey** | **string** |  |  |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project in its new state |  -  |
| **400** | A body was sent, or the Idempotency-Key was rejected |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is already archived, the organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="createcompetitor"></a>
# **CreateCompetitor**
> CompetitorResource CreateCompetitor (Guid organizationId, Guid projectId, string idempotencyKey, CreateCompetitorRequest createCompetitorRequest)

Add a competitor to a project

Minimum role: manager, on an active organization and a project that is not archived. Creates one competitor with the domains and brand names its mentions are matched against. Both lists are required and neither may be empty: a competitor that matches on nothing would never be found in an answer. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \"www.\" is dropped. Duplicates are collapsed. The id is assigned by the server and cannot be chosen, and neither the auto-generated brand description nor the internal brand monitoring profile id can be set — sending either is refused as an unknown field. Adding a competitor does NOT re-match the answers already captured: it applies to checks from here on. A project whose brand monitoring profile has not been created yet answers 404. An Idempotency-Key header is required.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class CreateCompetitorExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | Must belong to the organization in the path.
            var idempotencyKey = "idempotencyKey_example";  // string | Unique per attempt. Without it a lost response cannot be retried without risking a second competitor.
            var createCompetitorRequest = new CreateCompetitorRequest(); // CreateCompetitorRequest | 

            try
            {
                // Add a competitor to a project
                CompetitorResource result = apiInstance.CreateCompetitor(organizationId, projectId, idempotencyKey, createCompetitorRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.CreateCompetitor: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the CreateCompetitorWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Add a competitor to a project
    ApiResponse<CompetitorResource> response = apiInstance.CreateCompetitorWithHttpInfo(organizationId, projectId, idempotencyKey, createCompetitorRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.CreateCompetitorWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** | Must belong to the organization in the path. |  |
| **idempotencyKey** | **string** | Unique per attempt. Without it a lost response cannot be retried without risking a second competitor. |  |
| **createCompetitorRequest** | [**CreateCompetitorRequest**](CreateCompetitorRequest.md) |  |  |

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The competitor as stored |  -  |
| **400** | The body failed validation, or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids, or the project has no brand monitoring profile |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="createproject"></a>
# **CreateProject**
> ProjectDetailResource CreateProject (Guid organizationId, string idempotencyKey, CreateProjectRequest createProjectRequest)

Create a project and the brand monitoring profile its checks run against

Minimum role: manager, in an active organization. Requires the \"write\" capability. Creates the project, the brand monitoring profile holding the domains and brand names to watch, and one competitor per entry of `competitors`, in a single call. The project id is minted by the server; a caller-supplied id is rejected as an unknown field. What is NOT done: no tracked queries are created, no check is run and no scraping is scheduled — a new project has nothing collected against it until tracked queries are added. Each website entry may be a full URL or a bare domain: a URL is reduced to its host with any leading \"www.\" removed, so \"https://www.acme.com/pricing\" is stored as \"acme.com\". Duplicate domains and duplicate brand names are collapsed, exactly as the stored value objects do. Send an Idempotency-Key: a retry with the same key and the same body returns this same project instead of creating a second one.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class CreateProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | 
            var createProjectRequest = new CreateProjectRequest(); // CreateProjectRequest | 

            try
            {
                // Create a project and the brand monitoring profile its checks run against
                ProjectDetailResource result = apiInstance.CreateProject(organizationId, idempotencyKey, createProjectRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.CreateProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the CreateProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Create a project and the brand monitoring profile its checks run against
    ApiResponse<ProjectDetailResource> response = apiInstance.CreateProjectWithHttpInfo(organizationId, idempotencyKey, createProjectRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.CreateProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **idempotencyKey** | **string** |  |  |
| **createProjectRequest** | [**CreateProjectRequest**](CreateProjectRequest.md) |  |  |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created project and its brand monitoring configuration |  -  |
| **400** | The body or the Idempotency-Key was rejected; &#x60;details&#x60; names every field at fault |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="deletecompetitor"></a>
# **DeleteCompetitor**
> CompetitorResource DeleteCompetitor (Guid organizationId, Guid projectId, Guid competitorId, string idempotencyKey)

Remove a competitor from a project

Minimum role: manager, on an active organization and a project that is not archived. Removes the competitor and, asynchronously, every stored mention, search result and shopping result attributed to it, in AI answers and search captures already taken. This is permanent and it changes historical analytics: share of voice and competitor co-occurrence recomputed after the cascade will not include it. A 200 means the competitor is gone; the cascade runs on the event bus and finishes shortly afterwards. The response body is the competitor as it was immediately before removal, because it can no longer be read back. The request takes no body, and sending one is refused. A competitor belonging to another project answers 404, the same answer an unknown id gets. An Idempotency-Key header is required.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class DeleteCompetitorExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | Must belong to the organization in the path.
            var competitorId = "competitorId_example";  // Guid | Must belong to the project in the path.
            var idempotencyKey = "idempotencyKey_example";  // string | Unique per attempt. A retry carrying the same key is answered from the record instead of running again.

            try
            {
                // Remove a competitor from a project
                CompetitorResource result = apiInstance.DeleteCompetitor(organizationId, projectId, competitorId, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.DeleteCompetitor: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DeleteCompetitorWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Remove a competitor from a project
    ApiResponse<CompetitorResource> response = apiInstance.DeleteCompetitorWithHttpInfo(organizationId, projectId, competitorId, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.DeleteCompetitorWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** | Must belong to the organization in the path. |  |
| **competitorId** | **Guid** | Must belong to the project in the path. |  |
| **idempotencyKey** | **string** | Unique per attempt. A retry carrying the same key is answered from the record instead of running again. |  |

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The competitor as it was immediately before removal |  -  |
| **400** | A body was sent, or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or competitor the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was reused for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getbrandprofile"></a>
# **GetBrandProfile**
> BrandProfileResource GetBrandProfile (Guid organizationId, Guid projectId)

Get a project's brand monitoring profile

Minimum role: viewer. The brand identity every check of this project is matched against: the tracked brand terms, the website domains, and the generated description of what the brand does. A null description means it has not been generated yet — the generator runs asynchronously after the names or domains change — which is not the same as an empty one. An empty brandNames or websiteDomains array means the profile exists and names nothing; a project whose profile has not been created at all answers 404.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class GetBrandProfileExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | Must belong to the organization in the path.

            try
            {
                // Get a project's brand monitoring profile
                BrandProfileResource result = apiInstance.GetBrandProfile(organizationId, projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.GetBrandProfile: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetBrandProfileWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get a project's brand monitoring profile
    ApiResponse<BrandProfileResource> response = apiInstance.GetBrandProfileWithHttpInfo(organizationId, projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.GetBrandProfileWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** | Must belong to the organization in the path. |  |

### Return type

[**BrandProfileResource**](BrandProfileResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project&#39;s brand monitoring profile |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids, or the project has no brand profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getproject"></a>
# **GetProject**
> ProjectDetailResource GetProject (Guid organizationId, Guid projectId)

Get a project and its brand monitoring configuration

Minimum role: viewer. Returns the project together with the domains and brand names it is monitored for and the competitors it is measured against. A project that exists but belongs to another organization answers 404, never 403. A project that has been created but not yet configured for brand monitoring reports empty `websiteDomains`, `brandNames` and `competitors`. Headline metrics are not part of this response: use `listProjects` for the per-project figures, or `getProjectMetrics` for a window.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class GetProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 

            try
            {
                // Get a project and its brand monitoring configuration
                ProjectDetailResource result = apiInstance.GetProject(organizationId, projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.GetProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get a project and its brand monitoring configuration
    ApiResponse<ProjectDetailResource> response = apiInstance.GetProjectWithHttpInfo(organizationId, projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.GetProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project and its brand monitoring configuration |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id, or no project with this id inside it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listcompetitors"></a>
# **ListCompetitors**
> ListCompetitors200Response ListCompetitors (Guid organizationId, Guid projectId, int? limit = null, int? offset = null, string? sortOrder = null)

List the competitors tracked by a project

Minimum role: viewer. The competitors configured on the project, one page at a time, with the website domains and brand names each one is matched against. `total` counts every competitor of the project, not the size of this page, so a project with more than `limit` competitors needs `offset` to read them all. Ordering is by id, which for a UUID v7 is roughly creation order, and `sortOrder` chooses its direction; there is no other sort key and no text search, and sending `sortBy` or `search` is rejected rather than ignored. A project whose brand monitoring profile has not been created yet answers 200 with an empty collection, which means \"nothing configured yet\" rather than \"no competitors found\". Internal fields the pipeline writes — the auto-generated brand description used by the mention classifier, and the internal brand monitoring profile id — are not part of this contract.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class ListCompetitorsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var limit = 20;  // int? | Page size. A larger value is rejected, never silently reduced. (optional)  (default to 20)
            var offset = 0;  // int? | Number of competitors to skip before the page starts. (optional)  (default to 0)
            var sortOrder = "asc";  // string? | Direction of the id ordering. An unknown value is rejected, not replaced by the default. (optional)  (default to asc)

            try
            {
                // List the competitors tracked by a project
                ListCompetitors200Response result = apiInstance.ListCompetitors(organizationId, projectId, limit, offset, sortOrder);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.ListCompetitors: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListCompetitorsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List the competitors tracked by a project
    ApiResponse<ListCompetitors200Response> response = apiInstance.ListCompetitorsWithHttpInfo(organizationId, projectId, limit, offset, sortOrder);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.ListCompetitorsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **limit** | **int?** | Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int?** | Number of competitors to skip before the page starts. | [optional] [default to 0] |
| **sortOrder** | **string?** | Direction of the id ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to asc] |

### Return type

[**ListCompetitors200Response**](ListCompetitors200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project&#39;s competitors |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listprojects"></a>
# **ListProjects**
> ListProjects200Response ListProjects (Guid organizationId, int? limit = null, int? offset = null, string? search = null, string? status = null, string? sortBy = null, string? sortOrder = null)

List an organization's projects

Minimum role: viewer. Metrics come from the same read model the application uses, so the figures match what the product shows. A null metric means \"not known yet\", never zero.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class ListProjectsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var limit = 2;  // int? | Page size. A larger value is rejected, never silently reduced. (optional)  (default to 20)
            var offset = 4;  // int? | Rows to skip before the page starts. Page by advancing it in steps of `limit` until it reaches `total`. (optional)  (default to 0)
            var search = "search_example";  // string? |  (optional) 
            var status = "active";  // string? |  (optional) 
            var sortBy = "createdAt";  // string? |  (optional)  (default to createdAt)
            var sortOrder = "asc";  // string? |  (optional)  (default to desc)

            try
            {
                // List an organization's projects
                ListProjects200Response result = apiInstance.ListProjects(organizationId, limit, offset, search, status, sortBy, sortOrder);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.ListProjects: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListProjectsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List an organization's projects
    ApiResponse<ListProjects200Response> response = apiInstance.ListProjectsWithHttpInfo(organizationId, limit, offset, search, status, sortBy, sortOrder);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.ListProjectsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **limit** | **int?** | Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int?** | Rows to skip before the page starts. Page by advancing it in steps of &#x60;limit&#x60; until it reaches &#x60;total&#x60;. | [optional] [default to 0] |
| **search** | **string?** |  | [optional]  |
| **status** | **string?** |  | [optional]  |
| **sortBy** | **string?** |  | [optional] [default to createdAt] |
| **sortOrder** | **string?** |  | [optional] [default to desc] |

### Return type

[**ListProjects200Response**](ListProjects200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization&#39;s projects |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listqueryclusters"></a>
# **ListQueryClusters**
> ListQueryClusters200Response ListQueryClusters (Guid organizationId, Guid projectId, int? limit = null, int? offset = null, string? sortOrder = null)

List the keyword clusters of a project

Minimum role: viewer. The keyword clusters configured on a project, one page at a time. Each cluster id is exactly what the analytics operations accept in their queryClusterIds filter — pass the id, never the name. Names are unique within a project and are stored lower-cased, so the listing is ordered by name with no ties and paging over it neither repeats nor skips a cluster. `total` counts every cluster in the project, not the size of the page returned. A cluster carries no metrics of its own and no membership count: for the tracked queries inside a cluster, filter the tracked-query operations by its id. An empty list means the project has no clusters configured, which is not an error and is not a statement about whether any data has been collected.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class ListQueryClustersExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var limit = 20;  // int? | Page size. A larger value is rejected, never silently reduced. (optional)  (default to 20)
            var offset = 0;  // int? | Number of clusters to skip before the page starts. (optional)  (default to 0)
            var sortOrder = "asc";  // string? | Direction of the name ordering. An unknown value is rejected, not replaced by the default. (optional)  (default to asc)

            try
            {
                // List the keyword clusters of a project
                ListQueryClusters200Response result = apiInstance.ListQueryClusters(organizationId, projectId, limit, offset, sortOrder);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.ListQueryClusters: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListQueryClustersWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List the keyword clusters of a project
    ApiResponse<ListQueryClusters200Response> response = apiInstance.ListQueryClustersWithHttpInfo(organizationId, projectId, limit, offset, sortOrder);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.ListQueryClustersWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **limit** | **int?** | Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int?** | Number of clusters to skip before the page starts. | [optional] [default to 0] |
| **sortOrder** | **string?** | Direction of the name ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to asc] |

### Return type

[**ListQueryClusters200Response**](ListQueryClusters200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of the project&#39;s keyword clusters and the total in the project |  -  |
| **400** | A pagination or ordering parameter was rejected; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="restoreproject"></a>
# **RestoreProject**
> ProjectDetailResource RestoreProject (Guid organizationId, Guid projectId, string idempotencyKey)

Restore an archived project

Minimum role: manager, in an active organization. Requires the \"write\" capability. Brings an archived project back to active, with every tracked query, capture and metric it had when it was archived. What is NOT done: no check is run and no scraping is scheduled as a result — collection resumes on the project's own schedule. Restoring clears the record of who archived the project, so a project restored here is treated as an ordinary active project by any later organization archive. A project archived because its organization was archived cannot be restored on its own: restore the organization, which restores them all. Restoring a project that is already active answers 409, unless the call is a retry carrying the key that restored it. This endpoint takes no body, and one carrying fields is refused. Send an Idempotency-Key; a retry with the same key returns the recorded answer.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class RestoreProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | 

            try
            {
                // Restore an archived project
                ProjectDetailResource result = apiInstance.RestoreProject(organizationId, projectId, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.RestoreProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the RestoreProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Restore an archived project
    ApiResponse<ProjectDetailResource> response = apiInstance.RestoreProjectWithHttpInfo(organizationId, projectId, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.RestoreProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **idempotencyKey** | **string** |  |  |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project in its new state |  -  |
| **400** | A body was sent, or the Idempotency-Key was rejected |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is not archived, the organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="updatecompetitor"></a>
# **UpdateCompetitor**
> CompetitorResource UpdateCompetitor (Guid organizationId, Guid projectId, Guid competitorId, string idempotencyKey, CreateCompetitorRequest createCompetitorRequest)

Replace a competitor

Minimum role: manager, on an active organization and a project that is not archived. Replaces the competitor's name, domains and brand names: the lists sent become the lists stored, so a term left out is removed. Both lists are required and neither may be empty — a competitor that matches on nothing would never be found in an answer. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \"www.\" is dropped. Duplicates are collapsed. The auto-generated brand description cannot be set, and sending it is refused as an unknown field. Changing the matching rules does NOT re-match the answers already captured: it applies to checks from here on. A competitor belonging to another project answers 404, the same answer an unknown id gets. An Idempotency-Key header is required.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class UpdateCompetitorExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | Must belong to the organization in the path.
            var competitorId = "competitorId_example";  // Guid | Must belong to the project in the path.
            var idempotencyKey = "idempotencyKey_example";  // string | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
            var createCompetitorRequest = new CreateCompetitorRequest(); // CreateCompetitorRequest | 

            try
            {
                // Replace a competitor
                CompetitorResource result = apiInstance.UpdateCompetitor(organizationId, projectId, competitorId, idempotencyKey, createCompetitorRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.UpdateCompetitor: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateCompetitorWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Replace a competitor
    ApiResponse<CompetitorResource> response = apiInstance.UpdateCompetitorWithHttpInfo(organizationId, projectId, competitorId, idempotencyKey, createCompetitorRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.UpdateCompetitorWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** | Must belong to the organization in the path. |  |
| **competitorId** | **Guid** | Must belong to the project in the path. |  |
| **idempotencyKey** | **string** | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. |  |
| **createCompetitorRequest** | [**CreateCompetitorRequest**](CreateCompetitorRequest.md) |  |  |

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The competitor as stored |  -  |
| **400** | The body failed validation, or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or competitor the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="updateproject"></a>
# **UpdateProject**
> ProjectDetailResource UpdateProject (Guid organizationId, Guid projectId, string idempotencyKey, UpdateProjectRequest updateProjectRequest)

Rename a project

Minimum role: manager, in an active organization. Requires the \"write\" capability. `name` is the only writable field and it is required. What is NOT done: the monitored domains and brand names are not touched (use updateProjectBrandProfile) and competitors are not touched, added or removed (use the competitor endpoints). Sending `websiteDomains`, `brandNames` or `competitors` here is refused with the field named, never applied in part and never ignored. Renaming a project changes nothing about the data already collected against it. A project that belongs to another organization answers 404, never 403. An archived project answers 409: restore it first — unless the call is a retry carrying the key of a rename that already succeeded, which is answered from the record whatever the project's state is now. Send an Idempotency-Key; a retry with the same key and body returns the recorded answer.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class UpdateProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | 
            var updateProjectRequest = new UpdateProjectRequest(); // UpdateProjectRequest | 

            try
            {
                // Rename a project
                ProjectDetailResource result = apiInstance.UpdateProject(organizationId, projectId, idempotencyKey, updateProjectRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.UpdateProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Rename a project
    ApiResponse<ProjectDetailResource> response = apiInstance.UpdateProjectWithHttpInfo(organizationId, projectId, idempotencyKey, updateProjectRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.UpdateProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **idempotencyKey** | **string** |  |  |
| **updateProjectRequest** | [**UpdateProjectRequest**](UpdateProjectRequest.md) |  |  |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project in its new state |  -  |
| **400** | The body or the Idempotency-Key was rejected; &#x60;details&#x60; names every field at fault |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, the organization is archived, the idempotency key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="updateprojectbrandprofile"></a>
# **UpdateProjectBrandProfile**
> BrandProfileResource UpdateProjectBrandProfile (Guid organizationId, Guid projectId, string idempotencyKey, UpdateProjectBrandProfileRequest updateProjectBrandProfileRequest)

Replace a project's brand monitoring profile

Minimum role: manager, on an active organization and a project that is not archived. Replaces the brand terms and website domains every check of this project is matched against: the lists sent become the lists stored, so a term left out is removed. Both lists are required and neither may be empty — a project must keep at least one brand name and one domain to match anything. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \"www.\" is dropped, which is the form the profile is read back in. Duplicates, including two URLs that reduce to the same host, are collapsed. This operation does NOT touch the project name or its competitors, which are separate resources, and it does not regenerate the brand description: that runs asynchronously afterwards, so the description in the response is the one stored at the time of the write. An Idempotency-Key header is required.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class UpdateProjectBrandProfileExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new ProjectsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | Must belong to the organization in the path.
            var idempotencyKey = "idempotencyKey_example";  // string | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
            var updateProjectBrandProfileRequest = new UpdateProjectBrandProfileRequest(); // UpdateProjectBrandProfileRequest | 

            try
            {
                // Replace a project's brand monitoring profile
                BrandProfileResource result = apiInstance.UpdateProjectBrandProfile(organizationId, projectId, idempotencyKey, updateProjectBrandProfileRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectsApi.UpdateProjectBrandProfile: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateProjectBrandProfileWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Replace a project's brand monitoring profile
    ApiResponse<BrandProfileResource> response = apiInstance.UpdateProjectBrandProfileWithHttpInfo(organizationId, projectId, idempotencyKey, updateProjectBrandProfileRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectsApi.UpdateProjectBrandProfileWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** | Must belong to the organization in the path. |  |
| **idempotencyKey** | **string** | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. |  |
| **updateProjectBrandProfileRequest** | [**UpdateProjectBrandProfileRequest**](UpdateProjectBrandProfileRequest.md) |  |  |

### Return type

[**BrandProfileResource**](BrandProfileResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The profile as stored |  -  |
| **400** | The body failed validation, or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids, or the project has no brand profile |  -  |
| **409** | The organization is archived, the project is archived, or the idempotency key was reused for a different body, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

