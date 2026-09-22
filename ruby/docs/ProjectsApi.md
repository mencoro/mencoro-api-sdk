# Mencoro::ProjectsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**archive_project**](ProjectsApi.md#archive_project) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/archive | Archive a project |
| [**create_competitor**](ProjectsApi.md#create_competitor) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | Add a competitor to a project |
| [**create_project**](ProjectsApi.md#create_project) | **POST** /api/v1/organizations/{organizationId}/projects | Create a project and the brand monitoring profile its checks run against |
| [**delete_competitor**](ProjectsApi.md#delete_competitor) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Remove a competitor from a project |
| [**get_brand_profile**](ProjectsApi.md#get_brand_profile) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Get a project&#39;s brand monitoring profile |
| [**get_competitor**](ProjectsApi.md#get_competitor) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Get one of a project&#39;s competitors |
| [**get_project**](ProjectsApi.md#get_project) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId} | Get a project and its brand monitoring configuration |
| [**list_competitors**](ProjectsApi.md#list_competitors) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | List the competitors tracked by a project |
| [**list_projects**](ProjectsApi.md#list_projects) | **GET** /api/v1/organizations/{organizationId}/projects | List an organization&#39;s projects |
| [**list_query_clusters**](ProjectsApi.md#list_query_clusters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | List the keyword clusters of a project |
| [**restore_project**](ProjectsApi.md#restore_project) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/restore | Restore an archived project |
| [**update_competitor**](ProjectsApi.md#update_competitor) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Replace a competitor |
| [**update_project**](ProjectsApi.md#update_project) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId} | Rename a project |
| [**update_project_brand_profile**](ProjectsApi.md#update_project_brand_profile) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Replace a project&#39;s brand monitoring profile |


## archive_project

> <ProjectDetailResource> archive_project(organization_id, project_id, idempotency_key)

Archive a project

Minimum role: manager, in an active organization. Requires the \"write\" capability. Archiving stops a project from being modified: its name, brand profile and competitors are refused with 409 until it is restored. What is NOT done: nothing is deleted. Tracked queries, captured responses, mentions and every metric already collected stay exactly as they are, and restoreProject brings the project back with all of it. Archiving is recorded as done by the caller, not by an organization cascade, so restoring the organization later will not restore this project — restore it explicitly. This endpoint takes no body, and one carrying fields is refused. Archiving an already archived project answers 409, unless the call is a retry carrying the key that archived it. Send an Idempotency-Key; a retry with the same key returns the recorded answer.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | 

begin
  # Archive a project
  result = api_instance.archive_project(organization_id, project_id, idempotency_key)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->archive_project: #{e}"
end
```

#### Using the archive_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectDetailResource>, Integer, Hash)> archive_project_with_http_info(organization_id, project_id, idempotency_key)

```ruby
begin
  # Archive a project
  data, status_code, headers = api_instance.archive_project_with_http_info(organization_id, project_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectDetailResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->archive_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **idempotency_key** | **String** |  |  |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## create_competitor

> <CompetitorResource> create_competitor(organization_id, project_id, idempotency_key, create_competitor_request)

Add a competitor to a project

Minimum role: manager, on an active organization and a project that is not archived. Creates one competitor with the domains and brand names its mentions are matched against. Both lists are required and neither may be empty: a competitor that matches on nothing would never be found in an answer. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \"www.\" is dropped. Duplicates are collapsed. The id is assigned by the server and cannot be chosen, and neither the auto-generated brand description nor the internal brand monitoring profile id can be set — sending either is refused as an unknown field. Adding a competitor does NOT re-match the answers already captured: it applies to checks from here on. A project whose brand monitoring profile has not been created yet answers 404. An Idempotency-Key header is required.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the organization in the path.
idempotency_key = 'idempotency_key_example' # String | Unique per attempt. Without it a lost response cannot be retried without risking a second competitor.
create_competitor_request = Mencoro::CreateCompetitorRequest.new # CreateCompetitorRequest | 

begin
  # Add a competitor to a project
  result = api_instance.create_competitor(organization_id, project_id, idempotency_key, create_competitor_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->create_competitor: #{e}"
end
```

#### Using the create_competitor_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CompetitorResource>, Integer, Hash)> create_competitor_with_http_info(organization_id, project_id, idempotency_key, create_competitor_request)

```ruby
begin
  # Add a competitor to a project
  data, status_code, headers = api_instance.create_competitor_with_http_info(organization_id, project_id, idempotency_key, create_competitor_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CompetitorResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->create_competitor_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** | Must belong to the organization in the path. |  |
| **idempotency_key** | **String** | Unique per attempt. Without it a lost response cannot be retried without risking a second competitor. |  |
| **create_competitor_request** | [**CreateCompetitorRequest**](CreateCompetitorRequest.md) |  |  |

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_project

> <ProjectDetailResource> create_project(organization_id, idempotency_key, create_project_request)

Create a project and the brand monitoring profile its checks run against

Minimum role: manager, in an active organization. Requires the \"write\" capability. Creates the project, the brand monitoring profile holding the domains and brand names to watch, and one competitor per entry of `competitors`, in a single call. The project id is minted by the server; a caller-supplied id is rejected as an unknown field. What is NOT done: no tracked queries are created, no check is run and no scraping is scheduled — a new project has nothing collected against it until tracked queries are added. Each website entry may be a full URL or a bare domain: a URL is reduced to its host with any leading \"www.\" removed, so \"https://www.acme.com/pricing\" is stored as \"acme.com\". Duplicate domains and duplicate brand names are collapsed, exactly as the stored value objects do. Send an Idempotency-Key: a retry with the same key and the same body returns this same project instead of creating a second one.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | 
create_project_request = Mencoro::CreateProjectRequest.new({name: 'name_example', website_domains: ['website_domains_example'], brand_names: ['brand_names_example']}) # CreateProjectRequest | 

begin
  # Create a project and the brand monitoring profile its checks run against
  result = api_instance.create_project(organization_id, idempotency_key, create_project_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->create_project: #{e}"
end
```

#### Using the create_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectDetailResource>, Integer, Hash)> create_project_with_http_info(organization_id, idempotency_key, create_project_request)

```ruby
begin
  # Create a project and the brand monitoring profile its checks run against
  data, status_code, headers = api_instance.create_project_with_http_info(organization_id, idempotency_key, create_project_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectDetailResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->create_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **idempotency_key** | **String** |  |  |
| **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md) |  |  |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_competitor

> <CompetitorResource> delete_competitor(organization_id, project_id, competitor_id, idempotency_key)

Remove a competitor from a project

Minimum role: manager, on an active organization and a project that is not archived. Removes the competitor and, asynchronously, every stored mention, search result and shopping result attributed to it, in AI answers and search captures already taken. This is permanent and it changes historical analytics: share of voice and competitor co-occurrence recomputed after the cascade will not include it. A 200 means the competitor is gone; the cascade runs on the event bus and finishes shortly afterwards. The response body is the competitor as it was immediately before removal, because it can no longer be read back. The request takes no body, and sending one is refused. A competitor belonging to another project answers 404, the same answer an unknown id gets. An Idempotency-Key header is required.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the organization in the path.
competitor_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the project in the path.
idempotency_key = 'idempotency_key_example' # String | Unique per attempt. A retry carrying the same key is answered from the record instead of running again.

begin
  # Remove a competitor from a project
  result = api_instance.delete_competitor(organization_id, project_id, competitor_id, idempotency_key)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->delete_competitor: #{e}"
end
```

#### Using the delete_competitor_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CompetitorResource>, Integer, Hash)> delete_competitor_with_http_info(organization_id, project_id, competitor_id, idempotency_key)

```ruby
begin
  # Remove a competitor from a project
  data, status_code, headers = api_instance.delete_competitor_with_http_info(organization_id, project_id, competitor_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CompetitorResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->delete_competitor_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** | Must belong to the organization in the path. |  |
| **competitor_id** | **String** | Must belong to the project in the path. |  |
| **idempotency_key** | **String** | Unique per attempt. A retry carrying the same key is answered from the record instead of running again. |  |

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_brand_profile

> <BrandProfileResource> get_brand_profile(organization_id, project_id)

Get a project's brand monitoring profile

Minimum role: viewer. The brand identity every check of this project is matched against: the tracked brand terms, the website domains, and the generated description of what the brand does. A null description means it has not been generated yet — the generator runs asynchronously after the names or domains change — which is not the same as an empty one. An empty brandNames or websiteDomains array means the profile exists and names nothing; a project whose profile has not been created at all answers 404.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the organization in the path.

begin
  # Get a project's brand monitoring profile
  result = api_instance.get_brand_profile(organization_id, project_id)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->get_brand_profile: #{e}"
end
```

#### Using the get_brand_profile_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BrandProfileResource>, Integer, Hash)> get_brand_profile_with_http_info(organization_id, project_id)

```ruby
begin
  # Get a project's brand monitoring profile
  data, status_code, headers = api_instance.get_brand_profile_with_http_info(organization_id, project_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BrandProfileResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->get_brand_profile_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** | Must belong to the organization in the path. |  |

### Return type

[**BrandProfileResource**](BrandProfileResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_competitor

> <CompetitorResource> get_competitor(organization_id, project_id, competitor_id)

Get one of a project's competitors

Minimum role: viewer. Returns a single competitor of the project, the same projection the competitor listing returns for each of its rows. A competitor belonging to another project answers 404, the same answer an unknown id and a malformed one get, so the API never confirms that a competitor the caller cannot reach exists. A project whose brand monitoring profile has not been created yet has no competitors at all and answers 404 for any competitor id.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the organization in the path.
competitor_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the project in the path.

begin
  # Get one of a project's competitors
  result = api_instance.get_competitor(organization_id, project_id, competitor_id)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->get_competitor: #{e}"
end
```

#### Using the get_competitor_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CompetitorResource>, Integer, Hash)> get_competitor_with_http_info(organization_id, project_id, competitor_id)

```ruby
begin
  # Get one of a project's competitors
  data, status_code, headers = api_instance.get_competitor_with_http_info(organization_id, project_id, competitor_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CompetitorResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->get_competitor_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** | Must belong to the organization in the path. |  |
| **competitor_id** | **String** | Must belong to the project in the path. |  |

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_project

> <ProjectDetailResource> get_project(organization_id, project_id)

Get a project and its brand monitoring configuration

Minimum role: viewer. Returns the project together with the domains and brand names it is monitored for and the competitors it is measured against. A project that exists but belongs to another organization answers 404, never 403. A project that has been created but not yet configured for brand monitoring reports empty `websiteDomains`, `brandNames` and `competitors`. Headline metrics are not part of this response: use `listProjects` for the per-project figures, or `getProjectMetrics` for a window.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 

begin
  # Get a project and its brand monitoring configuration
  result = api_instance.get_project(organization_id, project_id)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->get_project: #{e}"
end
```

#### Using the get_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectDetailResource>, Integer, Hash)> get_project_with_http_info(organization_id, project_id)

```ruby
begin
  # Get a project and its brand monitoring configuration
  data, status_code, headers = api_instance.get_project_with_http_info(organization_id, project_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectDetailResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->get_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_competitors

> <ListCompetitors200Response> list_competitors(organization_id, project_id, opts)

List the competitors tracked by a project

Minimum role: viewer. The competitors configured on the project, one page at a time, with the website domains and brand names each one is matched against. `total` counts every competitor of the project, not the size of this page, so a project with more than `limit` competitors needs `offset` to read them all. Ordering is by id, which for a UUID v7 is roughly creation order, and `sortOrder` chooses its direction; there is no other sort key and no text search, and sending `sortBy` or `search` is rejected rather than ignored. A project whose brand monitoring profile has not been created yet answers 200 with an empty collection, which means \"nothing configured yet\" rather than \"no competitors found\". Internal fields the pipeline writes — the auto-generated brand description used by the mention classifier, and the internal brand monitoring profile id — are not part of this contract.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  limit: 56, # Integer | Page size. A larger value is rejected, never silently reduced.
  offset: 56, # Integer | Number of competitors to skip before the page starts.
  sort_order: 'asc' # String | Direction of the id ordering. An unknown value is rejected, not replaced by the default.
}

begin
  # List the competitors tracked by a project
  result = api_instance.list_competitors(organization_id, project_id, opts)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->list_competitors: #{e}"
end
```

#### Using the list_competitors_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListCompetitors200Response>, Integer, Hash)> list_competitors_with_http_info(organization_id, project_id, opts)

```ruby
begin
  # List the competitors tracked by a project
  data, status_code, headers = api_instance.list_competitors_with_http_info(organization_id, project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListCompetitors200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->list_competitors_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **limit** | **Integer** | Page size. A larger value is rejected, never silently reduced. | [optional][default to 20] |
| **offset** | **Integer** | Number of competitors to skip before the page starts. | [optional][default to 0] |
| **sort_order** | **String** | Direction of the id ordering. An unknown value is rejected, not replaced by the default. | [optional][default to &#39;asc&#39;] |

### Return type

[**ListCompetitors200Response**](ListCompetitors200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## list_projects

> <ListProjects200Response> list_projects(organization_id, opts)

List an organization's projects

Minimum role: viewer. Metrics come from the same read model the application uses, so the figures match what the product shows. A null metric means \"not known yet\", never zero.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  limit: 2, # Integer | Page size. A larger value is rejected, never silently reduced.
  offset: 4, # Integer | Rows to skip before the page starts. Page by advancing it in steps of `limit` until it reaches `total`.
  search: 'search_example', # String | 
  status: 'active', # String | 
  sort_by: 'createdAt', # String | 
  sort_order: 'asc' # String | 
}

begin
  # List an organization's projects
  result = api_instance.list_projects(organization_id, opts)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->list_projects: #{e}"
end
```

#### Using the list_projects_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListProjects200Response>, Integer, Hash)> list_projects_with_http_info(organization_id, opts)

```ruby
begin
  # List an organization's projects
  data, status_code, headers = api_instance.list_projects_with_http_info(organization_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListProjects200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->list_projects_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **limit** | **Integer** | Page size. A larger value is rejected, never silently reduced. | [optional][default to 20] |
| **offset** | **Integer** | Rows to skip before the page starts. Page by advancing it in steps of &#x60;limit&#x60; until it reaches &#x60;total&#x60;. | [optional][default to 0] |
| **search** | **String** |  | [optional] |
| **status** | **String** |  | [optional] |
| **sort_by** | **String** |  | [optional][default to &#39;createdAt&#39;] |
| **sort_order** | **String** |  | [optional][default to &#39;desc&#39;] |

### Return type

[**ListProjects200Response**](ListProjects200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## list_query_clusters

> <ListQueryClusters200Response> list_query_clusters(organization_id, project_id, opts)

List the keyword clusters of a project

Minimum role: viewer. The keyword clusters configured on a project, one page at a time. Each cluster id is exactly what the analytics operations accept in their queryClusterIds filter — pass the id, never the name. Names are unique within a project and are stored lower-cased, so the listing is ordered by name with no ties and paging over it neither repeats nor skips a cluster. `total` counts every cluster in the project, not the size of the page returned. A cluster carries no metrics of its own and no membership count: for the tracked queries inside a cluster, filter the tracked-query operations by its id. An empty list means the project has no clusters configured, which is not an error and is not a statement about whether any data has been collected.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
opts = {
  limit: 56, # Integer | Page size. A larger value is rejected, never silently reduced.
  offset: 56, # Integer | Number of clusters to skip before the page starts.
  sort_order: 'asc' # String | Direction of the name ordering. An unknown value is rejected, not replaced by the default.
}

begin
  # List the keyword clusters of a project
  result = api_instance.list_query_clusters(organization_id, project_id, opts)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->list_query_clusters: #{e}"
end
```

#### Using the list_query_clusters_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ListQueryClusters200Response>, Integer, Hash)> list_query_clusters_with_http_info(organization_id, project_id, opts)

```ruby
begin
  # List the keyword clusters of a project
  data, status_code, headers = api_instance.list_query_clusters_with_http_info(organization_id, project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ListQueryClusters200Response>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->list_query_clusters_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **limit** | **Integer** | Page size. A larger value is rejected, never silently reduced. | [optional][default to 20] |
| **offset** | **Integer** | Number of clusters to skip before the page starts. | [optional][default to 0] |
| **sort_order** | **String** | Direction of the name ordering. An unknown value is rejected, not replaced by the default. | [optional][default to &#39;asc&#39;] |

### Return type

[**ListQueryClusters200Response**](ListQueryClusters200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## restore_project

> <ProjectDetailResource> restore_project(organization_id, project_id, idempotency_key)

Restore an archived project

Minimum role: manager, in an active organization. Requires the \"write\" capability. Brings an archived project back to active, with every tracked query, capture and metric it had when it was archived. What is NOT done: no check is run and no scraping is scheduled as a result — collection resumes on the project's own schedule. Restoring clears the record of who archived the project, so a project restored here is treated as an ordinary active project by any later organization archive. A project archived because its organization was archived cannot be restored on its own: restore the organization, which restores them all. Restoring a project that is already active answers 409, unless the call is a retry carrying the key that restored it. This endpoint takes no body, and one carrying fields is refused. Send an Idempotency-Key; a retry with the same key returns the recorded answer.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | 

begin
  # Restore an archived project
  result = api_instance.restore_project(organization_id, project_id, idempotency_key)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->restore_project: #{e}"
end
```

#### Using the restore_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectDetailResource>, Integer, Hash)> restore_project_with_http_info(organization_id, project_id, idempotency_key)

```ruby
begin
  # Restore an archived project
  data, status_code, headers = api_instance.restore_project_with_http_info(organization_id, project_id, idempotency_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectDetailResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->restore_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **idempotency_key** | **String** |  |  |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_competitor

> <CompetitorResource> update_competitor(organization_id, project_id, competitor_id, idempotency_key, create_competitor_request)

Replace a competitor

Minimum role: manager, on an active organization and a project that is not archived. Replaces the competitor's name, domains and brand names: the lists sent become the lists stored, so a term left out is removed. Both lists are required and neither may be empty — a competitor that matches on nothing would never be found in an answer. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \"www.\" is dropped. Duplicates are collapsed. The auto-generated brand description cannot be set, and sending it is refused as an unknown field. Changing the matching rules does NOT re-match the answers already captured: it applies to checks from here on. A competitor belonging to another project answers 404, the same answer an unknown id gets. An Idempotency-Key header is required.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the organization in the path.
competitor_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the project in the path.
idempotency_key = 'idempotency_key_example' # String | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
create_competitor_request = Mencoro::CreateCompetitorRequest.new # CreateCompetitorRequest | 

begin
  # Replace a competitor
  result = api_instance.update_competitor(organization_id, project_id, competitor_id, idempotency_key, create_competitor_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->update_competitor: #{e}"
end
```

#### Using the update_competitor_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CompetitorResource>, Integer, Hash)> update_competitor_with_http_info(organization_id, project_id, competitor_id, idempotency_key, create_competitor_request)

```ruby
begin
  # Replace a competitor
  data, status_code, headers = api_instance.update_competitor_with_http_info(organization_id, project_id, competitor_id, idempotency_key, create_competitor_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CompetitorResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->update_competitor_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** | Must belong to the organization in the path. |  |
| **competitor_id** | **String** | Must belong to the project in the path. |  |
| **idempotency_key** | **String** | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. |  |
| **create_competitor_request** | [**CreateCompetitorRequest**](CreateCompetitorRequest.md) |  |  |

### Return type

[**CompetitorResource**](CompetitorResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## update_project

> <ProjectDetailResource> update_project(organization_id, project_id, idempotency_key, update_project_request)

Rename a project

Minimum role: manager, in an active organization. Requires the \"write\" capability. `name` is the only writable field and it is required. What is NOT done: the monitored domains and brand names are not touched (use updateProjectBrandProfile) and competitors are not touched, added or removed (use the competitor endpoints). Sending `websiteDomains`, `brandNames` or `competitors` here is refused with the field named, never applied in part and never ignored. Renaming a project changes nothing about the data already collected against it. A project that belongs to another organization answers 404, never 403. An archived project answers 409: restore it first — unless the call is a retry carrying the key of a rename that already succeeded, which is answered from the record whatever the project's state is now. Send an Idempotency-Key; a retry with the same key and body returns the recorded answer.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | 
update_project_request = Mencoro::UpdateProjectRequest.new({name: 'name_example'}) # UpdateProjectRequest | 

begin
  # Rename a project
  result = api_instance.update_project(organization_id, project_id, idempotency_key, update_project_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->update_project: #{e}"
end
```

#### Using the update_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectDetailResource>, Integer, Hash)> update_project_with_http_info(organization_id, project_id, idempotency_key, update_project_request)

```ruby
begin
  # Rename a project
  data, status_code, headers = api_instance.update_project_with_http_info(organization_id, project_id, idempotency_key, update_project_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectDetailResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->update_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** |  |  |
| **idempotency_key** | **String** |  |  |
| **update_project_request** | [**UpdateProjectRequest**](UpdateProjectRequest.md) |  |  |

### Return type

[**ProjectDetailResource**](ProjectDetailResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## update_project_brand_profile

> <BrandProfileResource> update_project_brand_profile(organization_id, project_id, idempotency_key, update_project_brand_profile_request)

Replace a project's brand monitoring profile

Minimum role: manager, on an active organization and a project that is not archived. Replaces the brand terms and website domains every check of this project is matched against: the lists sent become the lists stored, so a term left out is removed. Both lists are required and neither may be empty — a project must keep at least one brand name and one domain to match anything. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \"www.\" is dropped, which is the form the profile is read back in. Duplicates, including two URLs that reduce to the same host, are collapsed. This operation does NOT touch the project name or its competitors, which are separate resources, and it does not regenerate the brand description: that runs asynchronously afterwards, so the description in the response is the one stored at the time of the write. An Idempotency-Key header is required.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::ProjectsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the organization in the path.
idempotency_key = 'idempotency_key_example' # String | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
update_project_brand_profile_request = Mencoro::UpdateProjectBrandProfileRequest.new # UpdateProjectBrandProfileRequest | 

begin
  # Replace a project's brand monitoring profile
  result = api_instance.update_project_brand_profile(organization_id, project_id, idempotency_key, update_project_brand_profile_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->update_project_brand_profile: #{e}"
end
```

#### Using the update_project_brand_profile_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BrandProfileResource>, Integer, Hash)> update_project_brand_profile_with_http_info(organization_id, project_id, idempotency_key, update_project_brand_profile_request)

```ruby
begin
  # Replace a project's brand monitoring profile
  data, status_code, headers = api_instance.update_project_brand_profile_with_http_info(organization_id, project_id, idempotency_key, update_project_brand_profile_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BrandProfileResource>
rescue Mencoro::ApiError => e
  puts "Error when calling ProjectsApi->update_project_brand_profile_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** | Must belong to the organization in the path. |  |
| **idempotency_key** | **String** | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. |  |
| **update_project_brand_profile_request** | [**UpdateProjectBrandProfileRequest**](UpdateProjectBrandProfileRequest.md) |  |  |

### Return type

[**BrandProfileResource**](BrandProfileResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

