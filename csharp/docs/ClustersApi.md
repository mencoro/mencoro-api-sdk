# Mencoro.Api.Api.ClustersApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ApplyClusteringJob**](ClustersApi.md#applyclusteringjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs/{jobId}/apply | Apply the result of a clustering job |
| [**BatchCreateQueryClusters**](ClustersApi.md#batchcreatequeryclusters) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/batch | Create several keyword clusters at once |
| [**CreateQueryCluster**](ClustersApi.md#createquerycluster) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | Create a keyword cluster |
| [**DeleteQueryCluster**](ClustersApi.md#deletequerycluster) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Delete a keyword cluster |
| [**GetQueryCluster**](ClustersApi.md#getquerycluster) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Get one of a project&#39;s keyword clusters |
| [**RenameQueryCluster**](ClustersApi.md#renamequerycluster) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Rename a keyword cluster |
| [**StartClusteringJob**](ClustersApi.md#startclusteringjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs | Start a keyword clustering job |

<a id="applyclusteringjob"></a>
# **ApplyClusteringJob**
> ApplyClusteringJobOutcome ApplyClusteringJob (Guid organizationId, Guid projectId, Guid jobId, string idempotencyKey)

Apply the result of a clustering job

Minimum role: manager. Writes a completed clustering job onto the tracked queries it was computed for: it creates the clusters the job proposed that the project does not have yet, then assigns each tracked query according to the merge mode the job was started with — fill_gaps leaves already grouped queries alone, add_on_top only adds, full_regroup replaces a query's clusters with the proposed set and therefore REMOVES clusters that are not in it — but only for a tracked query the job actually returned an assignment for. A tracked query the job was started over and produced no assignment for is listed under `unassigned` and left exactly as it was, under every mode; it is not treated as \"belongs to no cluster\" and is never stripped. That matters most with restrictToExistingClusters, where the model is expected to return nothing for queries that fit no existing cluster. The body must be empty: the assignments, the target tracked queries and the mode all come from the job, so this call cannot apply something the job did not produce. Synchronous and partially successful — always 200, with each tracked query under `successful` or `failed`, and nothing rolled back because one failed. A job that is not completed, or one that produced no assignments, is refused with 409. Requires the write capability and an Idempotency-Key header; repeating the key returns the first answer rather than applying twice.

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
    public class ApplyClusteringJobExample
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
            var apiInstance = new ClustersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var jobId = "jobId_example";  // Guid | Must be a clustering job started for this organization and project.
            var idempotencyKey = "idempotencyKey_example";  // string | Repeat it to retry a lost response without applying the job twice.

            try
            {
                // Apply the result of a clustering job
                ApplyClusteringJobOutcome result = apiInstance.ApplyClusteringJob(organizationId, projectId, jobId, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ClustersApi.ApplyClusteringJob: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ApplyClusteringJobWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Apply the result of a clustering job
    ApiResponse<ApplyClusteringJobOutcome> response = apiInstance.ApplyClusteringJobWithHttpInfo(organizationId, projectId, jobId, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ClustersApi.ApplyClusteringJobWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **jobId** | **Guid** | Must be a clustering job started for this organization and project. |  |
| **idempotencyKey** | **string** | Repeat it to retry a lost response without applying the job twice. |  |

### Return type

[**ApplyClusteringJobOutcome**](ApplyClusteringJobOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | What was written; read &#x60;failed&#x60; rather than inferring success from the status |  -  |
| **400** | A body was sent, or the Idempotency-Key header is missing; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or clustering job the caller can access under these ids |  -  |
| **409** | The job is not completed, produced nothing that can be applied, the organization is archived, the project is archived, or the idempotency key was reused for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="batchcreatequeryclusters"></a>
# **BatchCreateQueryClusters**
> BatchCreateQueryClustersOutcome BatchCreateQueryClusters (Guid organizationId, Guid projectId, string idempotencyKey, BatchCreateQueryClustersRequestData batchCreateQueryClustersRequestData)

Create several keyword clusters at once

Minimum role: manager. Creates up to 100 empty keyword clusters in one call. Names are trimmed and lower-cased and repeated names in the body are collapsed before anything is written. Partial success: the answer is always 200 and reports every name under `successful` or under `failed` — a name already taken in the project fails with query_cluster_name_already_exists and is NOT resolved to the existing cluster, while the other names are still created. Nothing is rolled back because one name failed. The clusters are created empty; no tracked query is assigned to them. The organization must not be archived; an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

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
    public class BatchCreateQueryClustersExample
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
            var apiInstance = new ClustersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | Repeat it to retry a lost response without creating the batch twice.
            var batchCreateQueryClustersRequestData = new BatchCreateQueryClustersRequestData(); // BatchCreateQueryClustersRequestData | 

            try
            {
                // Create several keyword clusters at once
                BatchCreateQueryClustersOutcome result = apiInstance.BatchCreateQueryClusters(organizationId, projectId, idempotencyKey, batchCreateQueryClustersRequestData);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ClustersApi.BatchCreateQueryClusters: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the BatchCreateQueryClustersWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Create several keyword clusters at once
    ApiResponse<BatchCreateQueryClustersOutcome> response = apiInstance.BatchCreateQueryClustersWithHttpInfo(organizationId, projectId, idempotencyKey, batchCreateQueryClustersRequestData);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ClustersApi.BatchCreateQueryClustersWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **idempotencyKey** | **string** | Repeat it to retry a lost response without creating the batch twice. |  |
| **batchCreateQueryClustersRequestData** | [**BatchCreateQueryClustersRequestData**](BatchCreateQueryClustersRequestData.md) |  |  |

### Return type

[**BatchCreateQueryClustersOutcome**](BatchCreateQueryClustersOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-name results; read &#x60;failed&#x60; rather than inferring success from the status |  -  |
| **400** | The body was rejected, or the Idempotency-Key header is missing; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The organization is archived, or the idempotency key was reused for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="createquerycluster"></a>
# **CreateQueryCluster**
> QueryClusterResource CreateQueryCluster (Guid organizationId, Guid projectId, string idempotencyKey, CreateQueryClusterRequest createQueryClusterRequest)

Create a keyword cluster

Minimum role: manager. Creates one empty keyword cluster in the project. The name is trimmed and lower-cased before it is stored, and it must be unique within the project: a name that already exists is refused with 409 and nothing is merged into the existing cluster. The cluster starts with no tracked queries in it — this operation does not assign anything to it. The organization must not be archived; an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

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
    public class CreateQueryClusterExample
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
            var apiInstance = new ClustersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var idempotencyKey = 3f9d2c18-6b4a-4c77-9f10-6f2d5a7c8e21;  // string | A token you choose per operation, 8 to 255 printable ASCII characters with no spaces; a UUID is the obvious choice. Repeat it to retry a lost response without creating a second cluster. The key is scoped to your API key, and it is bound to the method, the path and the body of the first attempt: repeating it with anything else changed is refused with 409 rather than replayed.
            var createQueryClusterRequest = new CreateQueryClusterRequest(); // CreateQueryClusterRequest | 

            try
            {
                // Create a keyword cluster
                QueryClusterResource result = apiInstance.CreateQueryCluster(organizationId, projectId, idempotencyKey, createQueryClusterRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ClustersApi.CreateQueryCluster: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the CreateQueryClusterWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Create a keyword cluster
    ApiResponse<QueryClusterResource> response = apiInstance.CreateQueryClusterWithHttpInfo(organizationId, projectId, idempotencyKey, createQueryClusterRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ClustersApi.CreateQueryClusterWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **idempotencyKey** | **string** | A token you choose per operation, 8 to 255 printable ASCII characters with no spaces; a UUID is the obvious choice. Repeat it to retry a lost response without creating a second cluster. The key is scoped to your API key, and it is bound to the method, the path and the body of the first attempt: repeating it with anything else changed is refused with 409 rather than replayed. |  |
| **createQueryClusterRequest** | [**CreateQueryClusterRequest**](CreateQueryClusterRequest.md) |  |  |

### Return type

[**QueryClusterResource**](QueryClusterResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The cluster that was created |  -  |
| **400** | The body was rejected, or the Idempotency-Key header is missing; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | A cluster with this name already exists in the project, the organization is archived, the project is archived, or the idempotency key was reused for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="deletequerycluster"></a>
# **DeleteQueryCluster**
> DeleteQueryCluster200Response DeleteQueryCluster (Guid organizationId, Guid projectId, Guid clusterId, string idempotencyKey)

Delete a keyword cluster

Minimum role: manager. Deletes one keyword cluster. The tracked queries that were in it are NOT deleted: they are unassigned from this cluster and keep every other cluster they belong to. Analytics filtered by this cluster id return nothing afterwards, including for dates before the deletion, because that filter reads current membership. This cannot be undone — recreating a cluster with the same name produces a new id and an empty cluster. The organization must not be archived, and neither must the project: an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

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
    public class DeleteQueryClusterExample
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
            var apiInstance = new ClustersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var clusterId = "clusterId_example";  // Guid | Must be a cluster of the project in the path.
            var idempotencyKey = "idempotencyKey_example";  // string | Repeat it to retry a lost response; a fresh key answers 404 once the cluster is gone.

            try
            {
                // Delete a keyword cluster
                DeleteQueryCluster200Response result = apiInstance.DeleteQueryCluster(organizationId, projectId, clusterId, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ClustersApi.DeleteQueryCluster: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DeleteQueryClusterWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Delete a keyword cluster
    ApiResponse<DeleteQueryCluster200Response> response = apiInstance.DeleteQueryClusterWithHttpInfo(organizationId, projectId, clusterId, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ClustersApi.DeleteQueryClusterWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **clusterId** | **Guid** | Must be a cluster of the project in the path. |  |
| **idempotencyKey** | **string** | Repeat it to retry a lost response; a fresh key answers 404 once the cluster is gone. |  |

### Return type

[**DeleteQueryCluster200Response**](DeleteQueryCluster200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster was deleted |  -  |
| **400** | A body was sent, or the Idempotency-Key header is missing; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or cluster the caller can access under these ids |  -  |
| **409** | The organization is archived, or the idempotency key was reused for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getquerycluster"></a>
# **GetQueryCluster**
> QueryClusterResource GetQueryCluster (Guid organizationId, Guid projectId, Guid clusterId)

Get one of a project's keyword clusters

Minimum role: viewer. Returns a single keyword cluster of the project, the same projection the cluster listing returns for each of its rows. A cluster belonging to another project answers 404, the same answer an unknown id and a malformed one get, so the API never confirms that a cluster the caller cannot reach exists.

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
    public class GetQueryClusterExample
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
            var apiInstance = new ClustersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | Must belong to the organization in the path.
            var clusterId = "clusterId_example";  // Guid | Must be a cluster of the project in the path.

            try
            {
                // Get one of a project's keyword clusters
                QueryClusterResource result = apiInstance.GetQueryCluster(organizationId, projectId, clusterId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ClustersApi.GetQueryCluster: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetQueryClusterWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get one of a project's keyword clusters
    ApiResponse<QueryClusterResource> response = apiInstance.GetQueryClusterWithHttpInfo(organizationId, projectId, clusterId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ClustersApi.GetQueryClusterWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** | Must belong to the organization in the path. |  |
| **clusterId** | **Guid** | Must be a cluster of the project in the path. |  |

### Return type

[**QueryClusterResource**](QueryClusterResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The keyword cluster |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization, project or cluster the caller can access under these ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="renamequerycluster"></a>
# **RenameQueryCluster**
> QueryClusterResource RenameQueryCluster (Guid organizationId, Guid projectId, Guid clusterId, string idempotencyKey, CreateQueryClusterRequest createQueryClusterRequest)

Rename a keyword cluster

Minimum role: manager. Changes the name of one keyword cluster and nothing else: the tracked queries assigned to it are untouched, and its id does not change, so nothing a client stored breaks. The new name is trimmed and lower-cased and must be unique within the project; a collision is refused with 409. Renaming to the name the cluster already has is accepted and is a no-op. The organization must not be archived; an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

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
    public class RenameQueryClusterExample
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
            var apiInstance = new ClustersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var clusterId = "clusterId_example";  // Guid | Must be a cluster of the project in the path.
            var idempotencyKey = "idempotencyKey_example";  // string | Repeat it to retry a lost response without renaming twice.
            var createQueryClusterRequest = new CreateQueryClusterRequest(); // CreateQueryClusterRequest | 

            try
            {
                // Rename a keyword cluster
                QueryClusterResource result = apiInstance.RenameQueryCluster(organizationId, projectId, clusterId, idempotencyKey, createQueryClusterRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ClustersApi.RenameQueryCluster: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the RenameQueryClusterWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Rename a keyword cluster
    ApiResponse<QueryClusterResource> response = apiInstance.RenameQueryClusterWithHttpInfo(organizationId, projectId, clusterId, idempotencyKey, createQueryClusterRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ClustersApi.RenameQueryClusterWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **clusterId** | **Guid** | Must be a cluster of the project in the path. |  |
| **idempotencyKey** | **string** | Repeat it to retry a lost response without renaming twice. |  |
| **createQueryClusterRequest** | [**CreateQueryClusterRequest**](CreateQueryClusterRequest.md) |  |  |

### Return type

[**QueryClusterResource**](QueryClusterResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster in its new state |  -  |
| **400** | The body was rejected, or the Idempotency-Key header is missing; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or cluster the caller can access under these ids |  -  |
| **409** | Another cluster in the project already has this name, the organization is archived, the project is archived, or the idempotency key was reused for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="startclusteringjob"></a>
# **StartClusteringJob**
> AcceptedJobResource StartClusteringJob (Guid organizationId, Guid projectId, string idempotencyKey, StartClusteringJobRequestData startClusteringJobRequestData)

Start a keyword clustering job

Minimum role: manager. Asks the clustering service to propose keyword clusters for up to 500 tracked queries of the project, and answers 202 with the job to poll — the work runs in the background and a 202 says it was accepted, never that it succeeded. THE JOB WRITES NOTHING: it produces a proposal, and nothing changes until it is applied through the apply operation, which is a separate call. Duplicate query texts within the selection are sent once. Requires an entitled subscription (402 otherwise) and the organization must be active and the project not archived. Rate limited to 10 starts per minute per organization, shared with the same operation in the web application. Requires the write capability and an Idempotency-Key header; repeating the key returns the first job rather than starting a second.

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
    public class StartClusteringJobExample
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
            var apiInstance = new ClustersApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var projectId = "projectId_example";  // Guid | 
            var idempotencyKey = "idempotencyKey_example";  // string | Repeat it to retry a lost response without starting a second job.
            var startClusteringJobRequestData = new StartClusteringJobRequestData(); // StartClusteringJobRequestData | 

            try
            {
                // Start a keyword clustering job
                AcceptedJobResource result = apiInstance.StartClusteringJob(organizationId, projectId, idempotencyKey, startClusteringJobRequestData);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ClustersApi.StartClusteringJob: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the StartClusteringJobWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Start a keyword clustering job
    ApiResponse<AcceptedJobResource> response = apiInstance.StartClusteringJobWithHttpInfo(organizationId, projectId, idempotencyKey, startClusteringJobRequestData);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ClustersApi.StartClusteringJobWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **projectId** | **Guid** |  |  |
| **idempotencyKey** | **string** | Repeat it to retry a lost response without starting a second job. |  |
| **startClusteringJobRequestData** | [**StartClusteringJobRequestData**](StartClusteringJobRequestData.md) |  |  |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The job was accepted; poll trackingUrl until its status is terminal |  -  |
| **400** | The body was rejected, or the Idempotency-Key header is missing; the details name the field |  -  |
| **401** | Missing or invalid API key |  -  |
| **402** | The organization has no entitled subscription |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization, project or tracked query the caller can access under these ids |  -  |
| **409** | The organization is archived, the project is archived, there is nothing to cluster, or the idempotency key was reused for a different request, a concurrent request with the same key is still running, or a previous attempt with it ended without a known outcome |  -  |
| **429** | More than 10 clustering starts in a minute for this organization; Retry-After says when to try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

