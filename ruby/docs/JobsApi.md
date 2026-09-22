# Mencoro::JobsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**get_async_job**](JobsApi.md#get_async_job) | **GET** /api/v1/organizations/{organizationId}/jobs/{jobId} | Get an asynchronous job |


## get_async_job

> <AsyncJobResource> get_async_job(organization_id, job_id)

Get an asynchronous job

Minimum role: manager. The status of one asynchronous job started inside this organization — geo prompt discovery, keyword discovery, query clustering, brand discovery or brand-name suggestion — and, once it has completed, its result. Poll it until `status` is terminal: `completed` or `failed`. A null `result` means the result is not known, either because the job is still in flight or because it failed; it never means the job produced an empty result. A failed job carries no reason: the stored one is an internal exception message, not a published field. A job started by another organization, a job of a type this API does not publish, and a job id that does not exist all answer 404 alike, so the API never confirms that an inaccessible job exists.

### Examples

```ruby
require 'time'
require 'mencoro'
# setup authorization
Mencoro.configure do |config|
  # Configure Bearer authorization: ApiKey
  config.access_token = 'YOUR_BEARER_TOKEN'
end

api_instance = Mencoro::JobsApi.new
organization_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | 
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Must be a job started inside the organization in the path.

begin
  # Get an asynchronous job
  result = api_instance.get_async_job(organization_id, job_id)
  p result
rescue Mencoro::ApiError => e
  puts "Error when calling JobsApi->get_async_job: #{e}"
end
```

#### Using the get_async_job_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AsyncJobResource>, Integer, Hash)> get_async_job_with_http_info(organization_id, job_id)

```ruby
begin
  # Get an asynchronous job
  data, status_code, headers = api_instance.get_async_job_with_http_info(organization_id, job_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AsyncJobResource>
rescue Mencoro::ApiError => e
  puts "Error when calling JobsApi->get_async_job_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | **String** |  |  |
| **job_id** | **String** | Must be a job started inside the organization in the path. |  |

### Return type

[**AsyncJobResource**](AsyncJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

