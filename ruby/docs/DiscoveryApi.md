# Mencoro::DiscoveryApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**start_brand_discovery_job**](DiscoveryApi.md#start_brand_discovery_job) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/brands | Start a brand discovery job for a project |
| [**start_brand_name_suggestion_job**](DiscoveryApi.md#start_brand_name_suggestion_job) | **POST** /api/v1/organizations/{organizationId}/brand-name-suggestions | Start a brand-name alias suggestion job |
| [**start_keyword_discovery_job**](DiscoveryApi.md#start_keyword_discovery_job) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/keywords | Start a keyword discovery job for a project |
| [**start_prompt_discovery_job**](DiscoveryApi.md#start_prompt_discovery_job) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/prompts | Start a geo prompt discovery job for a project |


## start_brand_discovery_job

> <AcceptedJobResource> start_brand_discovery_job(organization_id, project_id, idempotency_key, opts)

Start a brand discovery job for a project

Minimum role: manager. Starts background discovery of the brands and competitors around a project and answers 202 with the job to poll; it never returns brands inline. The job PROPOSES names: it creates and updates nothing, so neither the brand profile nor the competitor list changes because this endpoint was called. The organization must be active. Unlike keyword and prompt discovery this operation does not require an entitled subscription, matching the application behaviour it mirrors. Ten starts per minute per organization, counted across every key of every member and shared with the same operation in the Mencoro app; a retry carrying an Idempotency-Key already answered is served from the record and does not count. A project whose brand monitoring profile has not been created yet is still accepted and still billed: the job runs grounded on the project name alone, with no website domains, brand names or competitors to work from, and completes normally. Configure the brand profile first if you want the discovery grounded.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::DiscoveryApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the organization in the path.
idempotency_key = 'idempotency_key_example' # String | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
opts = {
  start_brand_discovery_job_request: Mencoro::StartBrandDiscoveryJobRequest.new # StartBrandDiscoveryJobRequest | 
}

begin
  # Start a brand discovery job for a project
  result = api_instance.start_brand_discovery_job(organization_id, project_id, idempotency_key, opts)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling DiscoveryApi->start_brand_discovery_job: #{e}"
end
```

#### Using the start_brand_discovery_job_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AcceptedJobResource>, Integer, Hash)> start_brand_discovery_job_with_http_info(organization_id, project_id, idempotency_key, opts)

```ruby
begin
  # Start a brand discovery job for a project
  data, status_code, headers = api_instance.start_brand_discovery_job_with_http_info(organization_id, project_id, idempotency_key, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AcceptedJobResource>
rescue Mencoro::ApiError => e
  puts "Error when calling DiscoveryApi->start_brand_discovery_job_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** | Must belong to the organization in the path. |  |
| **idempotency_key** | **String** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. |  |
| **start_brand_discovery_job_request** | [**StartBrandDiscoveryJobRequest**](StartBrandDiscoveryJobRequest.md) |  | [optional] |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## start_brand_name_suggestion_job

> <AcceptedJobResource> start_brand_name_suggestion_job(organization_id, idempotency_key, start_brand_name_suggestion_job_request)

Start a brand-name alias suggestion job

Minimum role: manager. Starts a background, web-search-grounded job that suggests alias spellings for one entity - a brand, a project or a competitor - described entirely by the body, and answers 202 with the job to poll; it never returns suggestions inline. The entity need not exist: nothing is looked up, nothing is attached and nothing is saved, so the suggestions are the caller's to apply. Names sent in `enteredBrandNames` are excluded from the result. The organization must be active; no subscription is required, matching the application behaviour this mirrors. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::DiscoveryApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
idempotency_key = 'idempotency_key_example' # String | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
start_brand_name_suggestion_job_request = Mencoro::StartBrandNameSuggestionJobRequest.new({name: 'Acme', website_domains: ["https: //acme.com"]}) # StartBrandNameSuggestionJobRequest | 

begin
  # Start a brand-name alias suggestion job
  result = api_instance.start_brand_name_suggestion_job(organization_id, idempotency_key, start_brand_name_suggestion_job_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling DiscoveryApi->start_brand_name_suggestion_job: #{e}"
end
```

#### Using the start_brand_name_suggestion_job_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AcceptedJobResource>, Integer, Hash)> start_brand_name_suggestion_job_with_http_info(organization_id, idempotency_key, start_brand_name_suggestion_job_request)

```ruby
begin
  # Start a brand-name alias suggestion job
  data, status_code, headers = api_instance.start_brand_name_suggestion_job_with_http_info(organization_id, idempotency_key, start_brand_name_suggestion_job_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AcceptedJobResource>
rescue Mencoro::ApiError => e
  puts "Error when calling DiscoveryApi->start_brand_name_suggestion_job_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **idempotency_key** | **String** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. |  |
| **start_brand_name_suggestion_job_request** | [**StartBrandNameSuggestionJobRequest**](StartBrandNameSuggestionJobRequest.md) |  |  |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## start_keyword_discovery_job

> <AcceptedJobResource> start_keyword_discovery_job(organization_id, project_id, idempotency_key, start_keyword_discovery_job_request)

Start a keyword discovery job for a project

Minimum role: manager. Starts background keyword discovery from free-text seed input and answers 202 with the job to poll; it never returns keywords inline. The job SUGGESTS keywords - it creates no tracked queries and changes nothing in the project, so a completed job is a list to choose from, not work that has been applied. Queries the project already tracks are excluded from the suggestions automatically; `excludeQueries` adds more on top for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::DiscoveryApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the organization in the path.
idempotency_key = 'idempotency_key_example' # String | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
start_keyword_discovery_job_request = Mencoro::StartKeywordDiscoveryJobRequest.new({input: 'crm for plumbers, field service software'}) # StartKeywordDiscoveryJobRequest | 

begin
  # Start a keyword discovery job for a project
  result = api_instance.start_keyword_discovery_job(organization_id, project_id, idempotency_key, start_keyword_discovery_job_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling DiscoveryApi->start_keyword_discovery_job: #{e}"
end
```

#### Using the start_keyword_discovery_job_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AcceptedJobResource>, Integer, Hash)> start_keyword_discovery_job_with_http_info(organization_id, project_id, idempotency_key, start_keyword_discovery_job_request)

```ruby
begin
  # Start a keyword discovery job for a project
  data, status_code, headers = api_instance.start_keyword_discovery_job_with_http_info(organization_id, project_id, idempotency_key, start_keyword_discovery_job_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AcceptedJobResource>
rescue Mencoro::ApiError => e
  puts "Error when calling DiscoveryApi->start_keyword_discovery_job_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** | Must belong to the organization in the path. |  |
| **idempotency_key** | **String** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. |  |
| **start_keyword_discovery_job_request** | [**StartKeywordDiscoveryJobRequest**](StartKeywordDiscoveryJobRequest.md) |  |  |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## start_prompt_discovery_job

> <AcceptedJobResource> start_prompt_discovery_job(organization_id, project_id, idempotency_key, start_prompt_discovery_job_request)

Start a geo prompt discovery job for a project

Minimum role: manager. Starts background discovery of natural-language prompts - the questions an answer engine gets asked - from free-text seed input, and answers 202 with the job to poll; it never returns prompts inline. The job SUGGESTS prompts: it creates no tracked queries and changes nothing in the project. `country` is required here, unlike keyword discovery, because a prompt is a question asked from somewhere and the provider request has no default for it. Queries the project already tracks are excluded automatically; `excludeQueries` adds more for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::DiscoveryApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must belong to the organization in the path.
idempotency_key = 'idempotency_key_example' # String | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
start_prompt_discovery_job_request = Mencoro::StartPromptDiscoveryJobRequest.new({input: 'crm for plumbers, field service software', country: 'ES'}) # StartPromptDiscoveryJobRequest | 

begin
  # Start a geo prompt discovery job for a project
  result = api_instance.start_prompt_discovery_job(organization_id, project_id, idempotency_key, start_prompt_discovery_job_request)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling DiscoveryApi->start_prompt_discovery_job: #{e}"
end
```

#### Using the start_prompt_discovery_job_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AcceptedJobResource>, Integer, Hash)> start_prompt_discovery_job_with_http_info(organization_id, project_id, idempotency_key, start_prompt_discovery_job_request)

```ruby
begin
  # Start a geo prompt discovery job for a project
  data, status_code, headers = api_instance.start_prompt_discovery_job_with_http_info(organization_id, project_id, idempotency_key, start_prompt_discovery_job_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AcceptedJobResource>
rescue Mencoro::ApiError => e
  puts "Error when calling DiscoveryApi->start_prompt_discovery_job_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **project_id** | **String** | Must belong to the organization in the path. |  |
| **idempotency_key** | **String** | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. |  |
| **start_prompt_discovery_job_request** | [**StartPromptDiscoveryJobRequest**](StartPromptDiscoveryJobRequest.md) |  |  |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

