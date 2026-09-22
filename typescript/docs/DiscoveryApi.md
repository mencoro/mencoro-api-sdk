# DiscoveryApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**startBrandDiscoveryJob**](DiscoveryApi.md#startbranddiscoveryjoboperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/brands | Start a brand discovery job for a project |
| [**startBrandNameSuggestionJob**](DiscoveryApi.md#startbrandnamesuggestionjoboperation) | **POST** /api/v1/organizations/{organizationId}/brand-name-suggestions | Start a brand-name alias suggestion job |
| [**startKeywordDiscoveryJob**](DiscoveryApi.md#startkeyworddiscoveryjoboperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/keywords | Start a keyword discovery job for a project |
| [**startPromptDiscoveryJob**](DiscoveryApi.md#startpromptdiscoveryjoboperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/prompts | Start a geo prompt discovery job for a project |



## startBrandDiscoveryJob

> AcceptedJobResource startBrandDiscoveryJob(organizationId, projectId, idempotencyKey, startBrandDiscoveryJobRequest)

Start a brand discovery job for a project

Minimum role: manager. Starts background discovery of the brands and competitors around a project and answers 202 with the job to poll; it never returns brands inline. The job PROPOSES names: it creates and updates nothing, so neither the brand profile nor the competitor list changes because this endpoint was called. The organization must be active. Unlike keyword and prompt discovery this operation does not require an entitled subscription, matching the application behaviour it mirrors. Ten starts per minute per organization, counted across every key of every member and shared with the same operation in the Mencoro app; a retry carrying an Idempotency-Key already answered is served from the record and does not count. A project whose brand monitoring profile has not been created yet is still accepted and still billed: the job runs grounded on the project name alone, with no website domains, brand names or competitors to work from, and completes normally. Configure the brand profile first if you want the discovery grounded.

### Example

```ts
import {
  Configuration,
  DiscoveryApi,
} from '@mencoro/api';
import type { StartBrandDiscoveryJobOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DiscoveryApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the organization in the path.
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    idempotencyKey: idempotencyKey_example,
    // StartBrandDiscoveryJobRequest (optional)
    startBrandDiscoveryJobRequest: ...,
  } satisfies StartBrandDiscoveryJobOperationRequest;

  try {
    const data = await api.startBrandDiscoveryJob(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **projectId** | `string` | Must belong to the organization in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | [Defaults to `undefined`] |
| **startBrandDiscoveryJobRequest** | [StartBrandDiscoveryJobRequest](StartBrandDiscoveryJobRequest.md) |  | [Optional] |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The discovery job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten brand discovery starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## startBrandNameSuggestionJob

> AcceptedJobResource startBrandNameSuggestionJob(organizationId, idempotencyKey, startBrandNameSuggestionJobRequest)

Start a brand-name alias suggestion job

Minimum role: manager. Starts a background, web-search-grounded job that suggests alias spellings for one entity - a brand, a project or a competitor - described entirely by the body, and answers 202 with the job to poll; it never returns suggestions inline. The entity need not exist: nothing is looked up, nothing is attached and nothing is saved, so the suggestions are the caller\&#39;s to apply. Names sent in &#x60;enteredBrandNames&#x60; are excluded from the result. The organization must be active; no subscription is required, matching the application behaviour this mirrors. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count.

### Example

```ts
import {
  Configuration,
  DiscoveryApi,
} from '@mencoro/api';
import type { StartBrandNameSuggestionJobOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DiscoveryApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    idempotencyKey: idempotencyKey_example,
    // StartBrandNameSuggestionJobRequest
    startBrandNameSuggestionJobRequest: ...,
  } satisfies StartBrandNameSuggestionJobOperationRequest;

  try {
    const data = await api.startBrandNameSuggestionJob(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | [Defaults to `undefined`] |
| **startBrandNameSuggestionJobRequest** | [StartBrandNameSuggestionJobRequest](StartBrandNameSuggestionJobRequest.md) |  | |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The suggestion job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten suggestion starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## startKeywordDiscoveryJob

> AcceptedJobResource startKeywordDiscoveryJob(organizationId, projectId, idempotencyKey, startKeywordDiscoveryJobRequest)

Start a keyword discovery job for a project

Minimum role: manager. Starts background keyword discovery from free-text seed input and answers 202 with the job to poll; it never returns keywords inline. The job SUGGESTS keywords - it creates no tracked queries and changes nothing in the project, so a completed job is a list to choose from, not work that has been applied. Queries the project already tracks are excluded from the suggestions automatically; &#x60;excludeQueries&#x60; adds more on top for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Example

```ts
import {
  Configuration,
  DiscoveryApi,
} from '@mencoro/api';
import type { StartKeywordDiscoveryJobOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DiscoveryApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the organization in the path.
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    idempotencyKey: idempotencyKey_example,
    // StartKeywordDiscoveryJobRequest
    startKeywordDiscoveryJobRequest: ...,
  } satisfies StartKeywordDiscoveryJobOperationRequest;

  try {
    const data = await api.startKeywordDiscoveryJob(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **projectId** | `string` | Must belong to the organization in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | [Defaults to `undefined`] |
| **startKeywordDiscoveryJobRequest** | [StartKeywordDiscoveryJobRequest](StartKeywordDiscoveryJobRequest.md) |  | |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The discovery job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **402** | The organization has no entitled subscription |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten discovery starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## startPromptDiscoveryJob

> AcceptedJobResource startPromptDiscoveryJob(organizationId, projectId, idempotencyKey, startPromptDiscoveryJobRequest)

Start a geo prompt discovery job for a project

Minimum role: manager. Starts background discovery of natural-language prompts - the questions an answer engine gets asked - from free-text seed input, and answers 202 with the job to poll; it never returns prompts inline. The job SUGGESTS prompts: it creates no tracked queries and changes nothing in the project. &#x60;country&#x60; is required here, unlike keyword discovery, because a prompt is a question asked from somewhere and the provider request has no default for it. Queries the project already tracks are excluded automatically; &#x60;excludeQueries&#x60; adds more for this run only. The organization must be active and hold an entitled subscription, because the run spends provider budget. Ten starts per minute per organization, counted across every key of every member; a retry carrying an Idempotency-Key already answered is served from the record and does not count. Run tuning is not exposed: the discovery fan-out uses provider defaults.

### Example

```ts
import {
  Configuration,
  DiscoveryApi,
} from '@mencoro/api';
import type { StartPromptDiscoveryJobOperationRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DiscoveryApi(config);

  const body = {
    // string
    organizationId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Must belong to the organization in the path.
    projectId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one.
    idempotencyKey: idempotencyKey_example,
    // StartPromptDiscoveryJobRequest
    startPromptDiscoveryJobRequest: ...,
  } satisfies StartPromptDiscoveryJobOperationRequest;

  try {
    const data = await api.startPromptDiscoveryJob(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **organizationId** | `string` |  | [Defaults to `undefined`] |
| **projectId** | `string` | Must belong to the organization in the path. | [Defaults to `undefined`] |
| **idempotencyKey** | `string` | Repeat it to retry a start whose response was lost; the same key returns the same job instead of starting a second one. | [Defaults to `undefined`] |
| **startPromptDiscoveryJobRequest** | [StartPromptDiscoveryJobRequest](StartPromptDiscoveryJobRequest.md) |  | |

### Return type

[**AcceptedJobResource**](AcceptedJobResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The discovery job was accepted |  -  |
| **400** | The body is not a JSON object, names an unknown field, or fails validation; or the Idempotency-Key header is missing |  -  |
| **401** | Missing or invalid API key |  -  |
| **402** | The organization has no entitled subscription |  -  |
| **403** | The key lacks the write capability |  -  |
| **404** | No organization or project the caller can access under these ids |  -  |
| **409** | The project is archived, or the organization is archived, or the Idempotency-Key was already used for a different request, or a previous attempt with it ended without a known outcome |  -  |
| **429** | The organization exceeded ten discovery starts per minute, or the key exceeded its request budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

