# Mencoro::ClustersApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**apply_clustering_job**](ClustersApi.md#apply_clustering_job) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs/{jobId}/apply | Apply the result of a clustering job |
| [**batch_create_query_clusters**](ClustersApi.md#batch_create_query_clusters) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/batch | Create several keyword clusters at once |
| [**create_query_cluster**](ClustersApi.md#create_query_cluster) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | Create a keyword cluster |
| [**delete_query_cluster**](ClustersApi.md#delete_query_cluster) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Delete a keyword cluster |
| [**rename_query_cluster**](ClustersApi.md#rename_query_cluster) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Rename a keyword cluster |
| [**start_clustering_job**](ClustersApi.md#start_clustering_job) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs | Start a keyword clustering job |


## apply_clustering_job

> <ApplyClusteringJobOutcome> apply_clustering_job(organization_id, project_id, job_id, idempotency_key)

Apply the result of a clustering job

Minimum role: manager. Writes a completed clustering job onto the tracked queries it was computed for: it creates the clusters the job proposed that the project does not have yet, then assigns each tracked query according to the merge mode the job was started with — fill_gaps leaves already grouped queries alone, add_on_top only adds, full_regroup replaces a query's clusters with the proposed set and therefore REMOVES clusters that are not in it — but only for a tracked query the job actually returned an assignment for. A tracked query the job was started over and produced no assignment for is listed under `unassigned` and left exactly as it was, under every mode; it is not treated as \"belongs to no cluster\" and is never stripped. That matters most with restrictToExistingClusters, where the model is expected to return nothing for queries that fit no existing cluster. The body must be empty: the assignments, the target tracked queries and the mode all come from the job, so this call cannot apply something the job did not produce. Synchronous and partially successful — always 200, with each tracked query under `successful` or `failed`, and nothing rolled back because one failed. A job that is not completed, or one that produced no assignments, is refused with 409. Requires the write capability and an Idempotency-Key header; repeating the key returns the first answer rather than applying twice.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ClustersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must be a clustering job started for this organization and project.
idempotency_key = 'idempotency_key_example' # String | Repeat it to retry a lost response without applying the job twice.

begin
  # Apply the result of a clustering job
  result = api_instance.apply_clustering_job(organization_id, project_id, job_id, idempotency_key)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->apply_clustering_job: #{e}"
end
```

#### Using the apply_clustering_job_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ApplyClusteringJobOutcome>, Integer, Hash)> apply_clustering_job_with_http_info(organization_id, project_id, job_id, idempotency_key)

```ruby
begin
  # Apply the result of a clustering job
  data, status_code, headers = api_instance.apply_clustering_job_with_http_info(organization_id, project_id, job_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ApplyClusteringJobOutcome>
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->apply_clustering_job_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **job_id** | **String** | Must be a clustering job started for this organization and project. |  |
| **idempotency_key** | **String** | Repeat it to retry a lost response without applying the job twice. |  |

### Return type

[**ApplyClusteringJobOutcome**](ApplyClusteringJobOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## batch_create_query_clusters

> <BatchCreateQueryClustersOutcome> batch_create_query_clusters(organization_id, project_id, idempotency_key, batch_create_query_clusters_request_data)

Create several keyword clusters at once

Minimum role: manager. Creates up to 100 empty keyword clusters in one call. Names are trimmed and lower-cased and repeated names in the body are collapsed before anything is written. Partial success: the answer is always 200 and reports every name under `successful` or under `failed` — a name already taken in the project fails with query_cluster_name_already_exists and is NOT resolved to the existing cluster, while the other names are still created. Nothing is rolled back because one name failed. The clusters are created empty; no tracked query is assigned to them. The organization must not be archived; an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ClustersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | Repeat it to retry a lost response without creating the batch twice.
batch_create_query_clusters_request_data = Mencoro::BatchCreateQueryClustersRequestData.new({names: ['names_example']}) # BatchCreateQueryClustersRequestData | 

begin
  # Create several keyword clusters at once
  result = api_instance.batch_create_query_clusters(organization_id, project_id, idempotency_key, batch_create_query_clusters_request_data)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->batch_create_query_clusters: #{e}"
end
```

#### Using the batch_create_query_clusters_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BatchCreateQueryClustersOutcome>, Integer, Hash)> batch_create_query_clusters_with_http_info(organization_id, project_id, idempotency_key, batch_create_query_clusters_request_data)

```ruby
begin
  # Create several keyword clusters at once
  data, status_code, headers = api_instance.batch_create_query_clusters_with_http_info(organization_id, project_id, idempotency_key, batch_create_query_clusters_request_data)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BatchCreateQueryClustersOutcome>
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->batch_create_query_clusters_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **idempotency_key** | **String** | Repeat it to retry a lost response without creating the batch twice. |  |
| **batch_create_query_clusters_request_data** | [**BatchCreateQueryClustersRequestData**](BatchCreateQueryClustersRequestData.md) |  |  |

### Return type

[**BatchCreateQueryClustersOutcome**](BatchCreateQueryClustersOutcome.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_query_cluster

> <QueryClusterResource> create_query_cluster(organization_id, project_id, idempotency_key, create_query_cluster_request)

Create a keyword cluster

Minimum role: manager. Creates one empty keyword cluster in the project. The name is trimmed and lower-cased before it is stored, and it must be unique within the project: a name that already exists is refused with 409 and nothing is merged into the existing cluster. The cluster starts with no tracked queries in it — this operation does not assign anything to it. The organization must not be archived; an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ClustersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = '3f9d2c18-6b4a-4c77-9f10-6f2d5a7c8e21' # String | A token you choose per operation, 8 to 255 printable ASCII characters with no spaces; a UUID is the obvious choice. Repeat it to retry a lost response without creating a second cluster. The key is scoped to your API key, and it is bound to the method, the path and the body of the first attempt: repeating it with anything else changed is refused with 409 rather than replayed.
create_query_cluster_request = Mencoro::CreateQueryClusterRequest.new # CreateQueryClusterRequest | 

begin
  # Create a keyword cluster
  result = api_instance.create_query_cluster(organization_id, project_id, idempotency_key, create_query_cluster_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->create_query_cluster: #{e}"
end
```

#### Using the create_query_cluster_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<QueryClusterResource>, Integer, Hash)> create_query_cluster_with_http_info(organization_id, project_id, idempotency_key, create_query_cluster_request)

```ruby
begin
  # Create a keyword cluster
  data, status_code, headers = api_instance.create_query_cluster_with_http_info(organization_id, project_id, idempotency_key, create_query_cluster_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <QueryClusterResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->create_query_cluster_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **idempotency_key** | **String** | A token you choose per operation, 8 to 255 printable ASCII characters with no spaces; a UUID is the obvious choice. Repeat it to retry a lost response without creating a second cluster. The key is scoped to your API key, and it is bound to the method, the path and the body of the first attempt: repeating it with anything else changed is refused with 409 rather than replayed. |  |
| **create_query_cluster_request** | [**CreateQueryClusterRequest**](CreateQueryClusterRequest.md) |  |  |

### Return type

[**QueryClusterResource**](QueryClusterResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_query_cluster

> <DeleteQueryCluster200Response> delete_query_cluster(organization_id, project_id, cluster_id, idempotency_key)

Delete a keyword cluster

Minimum role: manager. Deletes one keyword cluster. The tracked queries that were in it are NOT deleted: they are unassigned from this cluster and keep every other cluster they belong to. Analytics filtered by this cluster id return nothing afterwards, including for dates before the deletion, because that filter reads current membership. This cannot be undone — recreating a cluster with the same name produces a new id and an empty cluster. The organization must not be archived, and neither must the project: an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ClustersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must be a cluster of the project in the path.
idempotency_key = 'idempotency_key_example' # String | Repeat it to retry a lost response; a fresh key answers 404 once the cluster is gone.

begin
  # Delete a keyword cluster
  result = api_instance.delete_query_cluster(organization_id, project_id, cluster_id, idempotency_key)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->delete_query_cluster: #{e}"
end
```

#### Using the delete_query_cluster_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DeleteQueryCluster200Response>, Integer, Hash)> delete_query_cluster_with_http_info(organization_id, project_id, cluster_id, idempotency_key)

```ruby
begin
  # Delete a keyword cluster
  data, status_code, headers = api_instance.delete_query_cluster_with_http_info(organization_id, project_id, cluster_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DeleteQueryCluster200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->delete_query_cluster_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **cluster_id** | **String** | Must be a cluster of the project in the path. |  |
| **idempotency_key** | **String** | Repeat it to retry a lost response; a fresh key answers 404 once the cluster is gone. |  |

### Return type

[**DeleteQueryCluster200Response**](DeleteQueryCluster200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rename_query_cluster

> <QueryClusterResource> rename_query_cluster(organization_id, project_id, cluster_id, idempotency_key, create_query_cluster_request)

Rename a keyword cluster

Minimum role: manager. Changes the name of one keyword cluster and nothing else: the tracked queries assigned to it are untouched, and its id does not change, so nothing a client stored breaks. The new name is trimmed and lower-cased and must be unique within the project; a collision is refused with 409. Renaming to the name the cluster already has is accepted and is a no-op. The organization must not be archived; an archived project IS refused with 409, stricter than the Mencoro app, which lets cluster writes into one. Requires the write capability and an Idempotency-Key header.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ClustersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
cluster_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must be a cluster of the project in the path.
idempotency_key = 'idempotency_key_example' # String | Repeat it to retry a lost response without renaming twice.
create_query_cluster_request = Mencoro::CreateQueryClusterRequest.new # CreateQueryClusterRequest | 

begin
  # Rename a keyword cluster
  result = api_instance.rename_query_cluster(organization_id, project_id, cluster_id, idempotency_key, create_query_cluster_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->rename_query_cluster: #{e}"
end
```

#### Using the rename_query_cluster_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<QueryClusterResource>, Integer, Hash)> rename_query_cluster_with_http_info(organization_id, project_id, cluster_id, idempotency_key, create_query_cluster_request)

```ruby
begin
  # Rename a keyword cluster
  data, status_code, headers = api_instance.rename_query_cluster_with_http_info(organization_id, project_id, cluster_id, idempotency_key, create_query_cluster_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <QueryClusterResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->rename_query_cluster_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **cluster_id** | **String** | Must be a cluster of the project in the path. |  |
| **idempotency_key** | **String** | Repeat it to retry a lost response without renaming twice. |  |
| **create_query_cluster_request** | [**CreateQueryClusterRequest**](CreateQueryClusterRequest.md) |  |  |

### Return type

[**QueryClusterResource**](QueryClusterResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## start_clustering_job

> <AcceptedJobResource> start_clustering_job(organization_id, project_id, idempotency_key, start_clustering_job_request_data)

Start a keyword clustering job

Minimum role: manager. Asks the clustering service to propose keyword clusters for up to 500 tracked queries of the project, and answers 202 with the job to poll — the work runs in the background and a 202 says it was accepted, never that it succeeded. THE JOB WRITES NOTHING: it produces a proposal, and nothing changes until it is applied through the apply operation, which is a separate call. Duplicate query texts within the selection are sent once. Requires an entitled subscription (402 otherwise) and the organization must be active and the project not archived. Rate limited to 10 starts per minute per organization, shared with the same operation in the web application. Requires the write capability and an Idempotency-Key header; repeating the key returns the first job rather than starting a second.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ClustersApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | Repeat it to retry a lost response without starting a second job.
start_clustering_job_request_data = Mencoro::StartClusteringJobRequestData.new({tracked_query_ids: ['tracked_query_ids_example'], mode: 'fill_gaps'}) # StartClusteringJobRequestData | 

begin
  # Start a keyword clustering job
  result = api_instance.start_clustering_job(organization_id, project_id, idempotency_key, start_clustering_job_request_data)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->start_clustering_job: #{e}"
end
```

#### Using the start_clustering_job_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AcceptedJobResource>, Integer, Hash)> start_clustering_job_with_http_info(organization_id, project_id, idempotency_key, start_clustering_job_request_data)

```ruby
begin
  # Start a keyword clustering job
  data, status_code, headers = api_instance.start_clustering_job_with_http_info(organization_id, project_id, idempotency_key, start_clustering_job_request_data)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AcceptedJobResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ClustersApi->start_clustering_job_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **idempotency_key** | **String** | Repeat it to retry a lost response without starting a second job. |  |
| **start_clustering_job_request_data** | [**StartClusteringJobRequestData**](StartClusteringJobRequestData.md) |  |  |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

