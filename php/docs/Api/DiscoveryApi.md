# Mencoro\Api\DiscoveryApi

Discovery

All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**startBrandDiscoveryJob()**](DiscoveryApi.md#startBrandDiscoveryJob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/brands | Start a brand discovery job for a project |
| [**startBrandNameSuggestionJob()**](DiscoveryApi.md#startBrandNameSuggestionJob) | **POST** /api/v1/organizations/{organizationId}/brand-name-suggestions | Start a brand-name alias suggestion job |
| [**startKeywordDiscoveryJob()**](DiscoveryApi.md#startKeywordDiscoveryJob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/keywords | Start a keyword discovery job for a project |
| [**startPromptDiscoveryJob()**](DiscoveryApi.md#startPromptDiscoveryJob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/prompts | Start a geo prompt discovery job for a project |


## `startBrandDiscoveryJob()`

```php
startBrandDiscoveryJob($organization_id, $project_id, $idempotency_key, $start_brand_discovery_job_request): \Mencoro\Api\Model\AcceptedJobResource
```

Start a brand discovery job for a project

Minimum role: manager. Starts background discovery of the brands and competitors around a project and answers 202 with the job to poll; it never returns brands inline. The job PROPOSES names: it creates and updates nothing, so neither the brand profile nor the competitor list changes because this endpoint was called. The organization must be active. Unlike keyword and prompt discovery this operation does not require an entitled subscription, matching the application behaviour it mirrors. Ten starts per minute per organization, counted across every key of every member and shared with the same operation in the Mencoro app; a retry carrying an Idempotency-Key already answered is served from the record and does not count. A project whose brand monitoring profile has not been created yet is still accepted and still billed: the job runs grounded on the project name alone, with no website domains, brand names or competitors to work from, and completes normally. Configure the brand profile first if you want the discovery grounded.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\DiscoveryApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string | Must belong to the organization in the path.
$idempotency_key = 'idempotency_key_example'; // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
$start_brand_discovery_job_request = new \Mencoro\Api\Model\StartBrandDiscoveryJobRequest(); // \Mencoro\Api\Model\StartBrandDiscoveryJobRequest

try {
    $result = $apiInstance->startBrandDiscoveryJob($organization_id, $project_id, $idempotency_key, $start_brand_discovery_job_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DiscoveryApi->startBrandDiscoveryJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**| Must belong to the organization in the path. | |
| **idempotency_key** | **string**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | |
| **start_brand_discovery_job_request** | [**\Mencoro\Api\Model\StartBrandDiscoveryJobRequest**](../Model/StartBrandDiscoveryJobRequest.md)|  | [optional] |

### Return type

[**\Mencoro\Api\Model\AcceptedJobResource**](../Model/AcceptedJobResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startBrandNameSuggestionJob()`

```php
startBrandNameSuggestionJob($organization_id, $idempotency_key, $start_brand_name_suggestion_job_request): \Mencoro\Api\Model\AcceptedJobResource
```

Start a brand-name alias suggestion job

Minimum role: manager. Starts a background, web-search-grounded job that suggests alias spellings for one entity - a brand, a project or a competitor - described entirely by the body, and answers 202 with the job to poll; it never returns suggestions inline. The entity need not exist: nothing is looked up, nothing is attached and nothing is saved, so the suggestions are the caller's to apply. Names sent in `enteredBrandNames` are excluded from the result. The organization must be active; no subscription is required, matching the application behaviour this mirrors. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\DiscoveryApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
$start_brand_name_suggestion_job_request = new \Mencoro\Api\Model\StartBrandNameSuggestionJobRequest(); // \Mencoro\Api\Model\StartBrandNameSuggestionJobRequest

try {
    $result = $apiInstance->startBrandNameSuggestionJob($organization_id, $idempotency_key, $start_brand_name_suggestion_job_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DiscoveryApi->startBrandNameSuggestionJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **idempotency_key** | **string**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | |
| **start_brand_name_suggestion_job_request** | [**\Mencoro\Api\Model\StartBrandNameSuggestionJobRequest**](../Model/StartBrandNameSuggestionJobRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\AcceptedJobResource**](../Model/AcceptedJobResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startKeywordDiscoveryJob()`

```php
startKeywordDiscoveryJob($organization_id, $project_id, $idempotency_key, $start_keyword_discovery_job_request): \Mencoro\Api\Model\AcceptedJobResource
```

Start a keyword discovery job for a project

Minimum role: manager. Starts background keyword discovery from free-text seed input and answers 202 with the job to poll; it never returns keywords inline. The job SUGGESTS keywords - it creates no tracked queries and changes nothing in the project, so a completed job is a list to choose from, not work that has been applied. Queries the project already tracks are excluded from the suggestions automatically; `excludeQueries` adds more on top for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\DiscoveryApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string | Must belong to the organization in the path.
$idempotency_key = 'idempotency_key_example'; // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
$start_keyword_discovery_job_request = new \Mencoro\Api\Model\StartKeywordDiscoveryJobRequest(); // \Mencoro\Api\Model\StartKeywordDiscoveryJobRequest

try {
    $result = $apiInstance->startKeywordDiscoveryJob($organization_id, $project_id, $idempotency_key, $start_keyword_discovery_job_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DiscoveryApi->startKeywordDiscoveryJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**| Must belong to the organization in the path. | |
| **idempotency_key** | **string**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | |
| **start_keyword_discovery_job_request** | [**\Mencoro\Api\Model\StartKeywordDiscoveryJobRequest**](../Model/StartKeywordDiscoveryJobRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\AcceptedJobResource**](../Model/AcceptedJobResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startPromptDiscoveryJob()`

```php
startPromptDiscoveryJob($organization_id, $project_id, $idempotency_key, $start_prompt_discovery_job_request): \Mencoro\Api\Model\AcceptedJobResource
```

Start a geo prompt discovery job for a project

Minimum role: manager. Starts background discovery of natural-language prompts - the questions an answer engine gets asked - from free-text seed input, and answers 202 with the job to poll; it never returns prompts inline. The job SUGGESTS prompts: it creates no tracked queries and changes nothing in the project. `country` is required here, unlike keyword discovery, because a prompt is a question asked from somewhere and the provider request has no default for it. Queries the project already tracks are excluded automatically; `excludeQueries` adds more for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\DiscoveryApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string | Must belong to the organization in the path.
$idempotency_key = 'idempotency_key_example'; // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
$start_prompt_discovery_job_request = new \Mencoro\Api\Model\StartPromptDiscoveryJobRequest(); // \Mencoro\Api\Model\StartPromptDiscoveryJobRequest

try {
    $result = $apiInstance->startPromptDiscoveryJob($organization_id, $project_id, $idempotency_key, $start_prompt_discovery_job_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DiscoveryApi->startPromptDiscoveryJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**| Must belong to the organization in the path. | |
| **idempotency_key** | **string**| Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | |
| **start_prompt_discovery_job_request** | [**\Mencoro\Api\Model\StartPromptDiscoveryJobRequest**](../Model/StartPromptDiscoveryJobRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\AcceptedJobResource**](../Model/AcceptedJobResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
