# Mencoro\Api\ProjectsApi

Projects

All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**archiveProject()**](ProjectsApi.md#archiveProject) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/archive | Archive a project |
| [**createCompetitor()**](ProjectsApi.md#createCompetitor) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | Add a competitor to a project |
| [**createProject()**](ProjectsApi.md#createProject) | **POST** /api/v1/organizations/{organizationId}/projects | Create a project and the brand monitoring profile its checks run against |
| [**deleteCompetitor()**](ProjectsApi.md#deleteCompetitor) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Remove a competitor from a project |
| [**getBrandProfile()**](ProjectsApi.md#getBrandProfile) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Get a project&#39;s brand monitoring profile |
| [**getCompetitor()**](ProjectsApi.md#getCompetitor) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Get one of a project&#39;s competitors |
| [**getProject()**](ProjectsApi.md#getProject) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId} | Get a project and its brand monitoring configuration |
| [**listCompetitors()**](ProjectsApi.md#listCompetitors) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | List the competitors tracked by a project |
| [**listProjects()**](ProjectsApi.md#listProjects) | **GET** /api/v1/organizations/{organizationId}/projects | List an organization&#39;s projects |
| [**listQueryClusters()**](ProjectsApi.md#listQueryClusters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | List the keyword clusters of a project |
| [**restoreProject()**](ProjectsApi.md#restoreProject) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/restore | Restore an archived project |
| [**updateCompetitor()**](ProjectsApi.md#updateCompetitor) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Replace a competitor |
| [**updateProject()**](ProjectsApi.md#updateProject) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId} | Rename a project |
| [**updateProjectBrandProfile()**](ProjectsApi.md#updateProjectBrandProfile) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Replace a project&#39;s brand monitoring profile |


## `archiveProject()`

```php
archiveProject($organization_id, $project_id, $idempotency_key): \Mencoro\Api\Model\ProjectDetailResource
```

Archive a project

Minimum role: manager, in an active organization. Requires the \"write\" capability. Archiving stops a project from being modified: its name, brand profile and competitors are refused with 409 until it is restored. What is NOT done: nothing is deleted. Tracked queries, captured responses, mentions and every metric already collected stay exactly as they are, and restoreProject brings the project back with all of it. Archiving is recorded as done by the caller, not by an organization cascade, so restoring the organization later will not restore this project — restore it explicitly. This endpoint takes no body, and one carrying fields is refused. Archiving an already archived project answers 409, unless the call is a retry carrying the key that archived it. Send an Idempotency-Key; a retry with the same key returns the recorded answer.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string

try {
    $result = $apiInstance->archiveProject($organization_id, $project_id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->archiveProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\ProjectDetailResource**](../Model/ProjectDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createCompetitor()`

```php
createCompetitor($organization_id, $project_id, $idempotency_key, $create_competitor_request): \Mencoro\Api\Model\CompetitorResource
```

Add a competitor to a project

Minimum role: manager, on an active organization and a project that is not archived. Creates one competitor with the domains and brand names its mentions are matched against. Both lists are required and neither may be empty: a competitor that matches on nothing would never be found in an answer. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \"www.\" is dropped. Duplicates are collapsed. The id is assigned by the server and cannot be chosen, and neither the auto-generated brand description nor the internal brand monitoring profile id can be set — sending either is refused as an unknown field. Adding a competitor does NOT re-match the answers already captured: it applies to checks from here on. A project whose brand monitoring profile has not been created yet answers 404. An Idempotency-Key header is required.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string | Must belong to the organization in the path.
$idempotency_key = 'idempotency_key_example'; // string | Unique per attempt. Without it a lost response cannot be retried without risking a second competitor.
$create_competitor_request = new \Mencoro\Api\Model\CreateCompetitorRequest(); // \Mencoro\Api\Model\CreateCompetitorRequest

try {
    $result = $apiInstance->createCompetitor($organization_id, $project_id, $idempotency_key, $create_competitor_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->createCompetitor: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**| Must belong to the organization in the path. | |
| **idempotency_key** | **string**| Unique per attempt. Without it a lost response cannot be retried without risking a second competitor. | |
| **create_competitor_request** | [**\Mencoro\Api\Model\CreateCompetitorRequest**](../Model/CreateCompetitorRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\CompetitorResource**](../Model/CompetitorResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createProject()`

```php
createProject($organization_id, $idempotency_key, $create_project_request): \Mencoro\Api\Model\ProjectDetailResource
```

Create a project and the brand monitoring profile its checks run against

Minimum role: manager, in an active organization. Requires the \"write\" capability. Creates the project, the brand monitoring profile holding the domains and brand names to watch, and one competitor per entry of `competitors`, in a single call. The project id is minted by the server; a caller-supplied id is rejected as an unknown field. What is NOT done: no tracked queries are created, no check is run and no scraping is scheduled — a new project has nothing collected against it until tracked queries are added. Each website entry may be a full URL or a bare domain: a URL is reduced to its host with any leading \"www.\" removed, so \"https://www.acme.com/pricing\" is stored as \"acme.com\". Duplicate domains and duplicate brand names are collapsed, exactly as the stored value objects do. Send an Idempotency-Key: a retry with the same key and the same body returns this same project instead of creating a second one.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string
$create_project_request = new \Mencoro\Api\Model\CreateProjectRequest(); // \Mencoro\Api\Model\CreateProjectRequest

try {
    $result = $apiInstance->createProject($organization_id, $idempotency_key, $create_project_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->createProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **idempotency_key** | **string**|  | |
| **create_project_request** | [**\Mencoro\Api\Model\CreateProjectRequest**](../Model/CreateProjectRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\ProjectDetailResource**](../Model/ProjectDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteCompetitor()`

```php
deleteCompetitor($organization_id, $project_id, $competitor_id, $idempotency_key): \Mencoro\Api\Model\CompetitorResource
```

Remove a competitor from a project

Minimum role: manager, on an active organization and a project that is not archived. Removes the competitor and, asynchronously, every stored mention, search result and shopping result attributed to it, in AI answers and search captures already taken. This is permanent and it changes historical analytics: share of voice and competitor co-occurrence recomputed after the cascade will not include it. A 200 means the competitor is gone; the cascade runs on the event bus and finishes shortly afterwards. The response body is the competitor as it was immediately before removal, because it can no longer be read back. The request takes no body, and sending one is refused. A competitor belonging to another project answers 404, the same answer an unknown id gets. An Idempotency-Key header is required.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string | Must belong to the organization in the path.
$competitor_id = 'competitor_id_example'; // string | Must belong to the project in the path.
$idempotency_key = 'idempotency_key_example'; // string | Unique per attempt. A retry carrying the same key is answered from the record instead of running again.

try {
    $result = $apiInstance->deleteCompetitor($organization_id, $project_id, $competitor_id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->deleteCompetitor: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**| Must belong to the organization in the path. | |
| **competitor_id** | **string**| Must belong to the project in the path. | |
| **idempotency_key** | **string**| Unique per attempt. A retry carrying the same key is answered from the record instead of running again. | |

### Return type

[**\Mencoro\Api\Model\CompetitorResource**](../Model/CompetitorResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getBrandProfile()`

```php
getBrandProfile($organization_id, $project_id): \Mencoro\Api\Model\BrandProfileResource
```

Get a project's brand monitoring profile

Minimum role: viewer. The brand identity every check of this project is matched against: the tracked brand terms, the website domains, and the generated description of what the brand does. A null description means it has not been generated yet — the generator runs asynchronously after the names or domains change — which is not the same as an empty one. An empty brandNames or websiteDomains array means the profile exists and names nothing; a project whose profile has not been created at all answers 404.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string | Must belong to the organization in the path.

try {
    $result = $apiInstance->getBrandProfile($organization_id, $project_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->getBrandProfile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**| Must belong to the organization in the path. | |

### Return type

[**\Mencoro\Api\Model\BrandProfileResource**](../Model/BrandProfileResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCompetitor()`

```php
getCompetitor($organization_id, $project_id, $competitor_id): \Mencoro\Api\Model\CompetitorResource
```

Get one of a project's competitors

Minimum role: viewer. Returns a single competitor of the project, the same projection the competitor listing returns for each of its rows. A competitor belonging to another project answers 404, the same answer an unknown id and a malformed one get, so the API never confirms that a competitor the caller cannot reach exists. A project whose brand monitoring profile has not been created yet has no competitors at all and answers 404 for any competitor id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string | Must belong to the organization in the path.
$competitor_id = 'competitor_id_example'; // string | Must belong to the project in the path.

try {
    $result = $apiInstance->getCompetitor($organization_id, $project_id, $competitor_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->getCompetitor: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**| Must belong to the organization in the path. | |
| **competitor_id** | **string**| Must belong to the project in the path. | |

### Return type

[**\Mencoro\Api\Model\CompetitorResource**](../Model/CompetitorResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getProject()`

```php
getProject($organization_id, $project_id): \Mencoro\Api\Model\ProjectDetailResource
```

Get a project and its brand monitoring configuration

Minimum role: viewer. Returns the project together with the domains and brand names it is monitored for and the competitors it is measured against. A project that exists but belongs to another organization answers 404, never 403. A project that has been created but not yet configured for brand monitoring reports empty `websiteDomains`, `brandNames` and `competitors`. Headline metrics are not part of this response: use `listProjects` for the per-project figures, or `getProjectMetrics` for a window.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string

try {
    $result = $apiInstance->getProject($organization_id, $project_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->getProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\ProjectDetailResource**](../Model/ProjectDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listCompetitors()`

```php
listCompetitors($organization_id, $project_id, $limit, $offset, $sort_order): \Mencoro\Api\Model\ListCompetitors200Response
```

List the competitors tracked by a project

Minimum role: viewer. The competitors configured on the project, one page at a time, with the website domains and brand names each one is matched against. `total` counts every competitor of the project, not the size of this page, so a project with more than `limit` competitors needs `offset` to read them all. Ordering is by id, which for a UUID v7 is roughly creation order, and `sortOrder` chooses its direction; there is no other sort key and no text search, and sending `sortBy` or `search` is rejected rather than ignored. A project whose brand monitoring profile has not been created yet answers 200 with an empty collection, which means \"nothing configured yet\" rather than \"no competitors found\". Internal fields the pipeline writes — the auto-generated brand description used by the mention classifier, and the internal brand monitoring profile id — are not part of this contract.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$limit = 20; // int | Page size. A larger value is rejected, never silently reduced.
$offset = 0; // int | Number of competitors to skip before the page starts.
$sort_order = 'asc'; // string | Direction of the id ordering. An unknown value is rejected, not replaced by the default.

try {
    $result = $apiInstance->listCompetitors($organization_id, $project_id, $limit, $offset, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->listCompetitors: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int**| Number of competitors to skip before the page starts. | [optional] [default to 0] |
| **sort_order** | **string**| Direction of the id ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;asc&#39;] |

### Return type

[**\Mencoro\Api\Model\ListCompetitors200Response**](../Model/ListCompetitors200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listProjects()`

```php
listProjects($organization_id, $limit, $offset, $search, $status, $sort_by, $sort_order): \Mencoro\Api\Model\ListProjects200Response
```

List an organization's projects

Minimum role: viewer. Metrics come from the same read model the application uses, so the figures match what the product shows. A null metric means \"not known yet\", never zero.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$limit = 2; // int | Page size. A larger value is rejected, never silently reduced.
$offset = 4; // int | Rows to skip before the page starts. Page by advancing it in steps of `limit` until it reaches `total`.
$search = 'search_example'; // string
$status = 'status_example'; // string
$sort_by = 'createdAt'; // string
$sort_order = 'desc'; // string

try {
    $result = $apiInstance->listProjects($organization_id, $limit, $offset, $search, $status, $sort_by, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->listProjects: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int**| Rows to skip before the page starts. Page by advancing it in steps of &#x60;limit&#x60; until it reaches &#x60;total&#x60;. | [optional] [default to 0] |
| **search** | **string**|  | [optional] |
| **status** | **string**|  | [optional] |
| **sort_by** | **string**|  | [optional] [default to &#39;createdAt&#39;] |
| **sort_order** | **string**|  | [optional] [default to &#39;desc&#39;] |

### Return type

[**\Mencoro\Api\Model\ListProjects200Response**](../Model/ListProjects200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listQueryClusters()`

```php
listQueryClusters($organization_id, $project_id, $limit, $offset, $sort_order): \Mencoro\Api\Model\ListQueryClusters200Response
```

List the keyword clusters of a project

Minimum role: viewer. The keyword clusters configured on a project, one page at a time. Each cluster id is exactly what the analytics operations accept in their queryClusterIds filter — pass the id, never the name. Names are unique within a project and are stored lower-cased, so the listing is ordered by name with no ties and paging over it neither repeats nor skips a cluster. `total` counts every cluster in the project, not the size of the page returned. A cluster carries no metrics of its own and no membership count: for the tracked queries inside a cluster, filter the tracked-query operations by its id. An empty list means the project has no clusters configured, which is not an error and is not a statement about whether any data has been collected.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. A list-valued field is joined into one cell with `; ` as a display projection — parse the JSON if you need the structure. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$limit = 20; // int | Page size. A larger value is rejected, never silently reduced.
$offset = 0; // int | Number of clusters to skip before the page starts.
$sort_order = 'asc'; // string | Direction of the name ordering. An unknown value is rejected, not replaced by the default.

try {
    $result = $apiInstance->listQueryClusters($organization_id, $project_id, $limit, $offset, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->listQueryClusters: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **limit** | **int**| Page size. A larger value is rejected, never silently reduced. | [optional] [default to 20] |
| **offset** | **int**| Number of clusters to skip before the page starts. | [optional] [default to 0] |
| **sort_order** | **string**| Direction of the name ordering. An unknown value is rejected, not replaced by the default. | [optional] [default to &#39;asc&#39;] |

### Return type

[**\Mencoro\Api\Model\ListQueryClusters200Response**](../Model/ListQueryClusters200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `restoreProject()`

```php
restoreProject($organization_id, $project_id, $idempotency_key): \Mencoro\Api\Model\ProjectDetailResource
```

Restore an archived project

Minimum role: manager, in an active organization. Requires the \"write\" capability. Brings an archived project back to active, with every tracked query, capture and metric it had when it was archived. What is NOT done: no check is run and no scraping is scheduled as a result — collection resumes on the project's own schedule. Restoring clears the record of who archived the project, so a project restored here is treated as an ordinary active project by any later organization archive. A project archived because its organization was archived cannot be restored on its own: restore the organization, which restores them all. Restoring a project that is already active answers 409, unless the call is a retry carrying the key that restored it. This endpoint takes no body, and one carrying fields is refused. Send an Idempotency-Key; a retry with the same key returns the recorded answer.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string

try {
    $result = $apiInstance->restoreProject($organization_id, $project_id, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->restoreProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\ProjectDetailResource**](../Model/ProjectDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateCompetitor()`

```php
updateCompetitor($organization_id, $project_id, $competitor_id, $idempotency_key, $create_competitor_request): \Mencoro\Api\Model\CompetitorResource
```

Replace a competitor

Minimum role: manager, on an active organization and a project that is not archived. Replaces the competitor's name, domains and brand names: the lists sent become the lists stored, so a term left out is removed. Both lists are required and neither may be empty — a competitor that matches on nothing would never be found in an answer. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \"www.\" is dropped. Duplicates are collapsed. The auto-generated brand description cannot be set, and sending it is refused as an unknown field. Changing the matching rules does NOT re-match the answers already captured: it applies to checks from here on. A competitor belonging to another project answers 404, the same answer an unknown id gets. An Idempotency-Key header is required.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string | Must belong to the organization in the path.
$competitor_id = 'competitor_id_example'; // string | Must belong to the project in the path.
$idempotency_key = 'idempotency_key_example'; // string | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
$create_competitor_request = new \Mencoro\Api\Model\CreateCompetitorRequest(); // \Mencoro\Api\Model\CreateCompetitorRequest

try {
    $result = $apiInstance->updateCompetitor($organization_id, $project_id, $competitor_id, $idempotency_key, $create_competitor_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->updateCompetitor: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**| Must belong to the organization in the path. | |
| **competitor_id** | **string**| Must belong to the project in the path. | |
| **idempotency_key** | **string**| Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. | |
| **create_competitor_request** | [**\Mencoro\Api\Model\CreateCompetitorRequest**](../Model/CreateCompetitorRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\CompetitorResource**](../Model/CompetitorResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateProject()`

```php
updateProject($organization_id, $project_id, $idempotency_key, $update_project_request): \Mencoro\Api\Model\ProjectDetailResource
```

Rename a project

Minimum role: manager, in an active organization. Requires the \"write\" capability. `name` is the only writable field and it is required. What is NOT done: the monitored domains and brand names are not touched (use updateProjectBrandProfile) and competitors are not touched, added or removed (use the competitor endpoints). Sending `websiteDomains`, `brandNames` or `competitors` here is refused with the field named, never applied in part and never ignored. Renaming a project changes nothing about the data already collected against it. A project that belongs to another organization answers 404, never 403. An archived project answers 409: restore it first — unless the call is a retry carrying the key of a rename that already succeeded, which is answered from the record whatever the project's state is now. Send an Idempotency-Key; a retry with the same key and body returns the recorded answer.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string
$idempotency_key = 'idempotency_key_example'; // string
$update_project_request = new \Mencoro\Api\Model\UpdateProjectRequest(); // \Mencoro\Api\Model\UpdateProjectRequest

try {
    $result = $apiInstance->updateProject($organization_id, $project_id, $idempotency_key, $update_project_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->updateProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**|  | |
| **idempotency_key** | **string**|  | |
| **update_project_request** | [**\Mencoro\Api\Model\UpdateProjectRequest**](../Model/UpdateProjectRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\ProjectDetailResource**](../Model/ProjectDetailResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateProjectBrandProfile()`

```php
updateProjectBrandProfile($organization_id, $project_id, $idempotency_key, $update_project_brand_profile_request): \Mencoro\Api\Model\BrandProfileResource
```

Replace a project's brand monitoring profile

Minimum role: manager, on an active organization and a project that is not archived. Replaces the brand terms and website domains every check of this project is matched against: the lists sent become the lists stored, so a term left out is removed. Both lists are required and neither may be empty — a project must keep at least one brand name and one domain to match anything. A domain may be sent as a full URL or as a bare host; a URL is reduced to its host and a leading \"www.\" is dropped, which is the form the profile is read back in. Duplicates, including two URLs that reduce to the same host, are collapsed. This operation does NOT touch the project name or its competitors, which are separate resources, and it does not regenerate the brand description: that runs asynchronously afterwards, so the description in the response is the one stored at the time of the write. An Idempotency-Key header is required.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\ProjectsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$project_id = 'project_id_example'; // string | Must belong to the organization in the path.
$idempotency_key = 'idempotency_key_example'; // string | Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again.
$update_project_brand_profile_request = new \Mencoro\Api\Model\UpdateProjectBrandProfileRequest(); // \Mencoro\Api\Model\UpdateProjectBrandProfileRequest

try {
    $result = $apiInstance->updateProjectBrandProfile($organization_id, $project_id, $idempotency_key, $update_project_brand_profile_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProjectsApi->updateProjectBrandProfile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **project_id** | **string**| Must belong to the organization in the path. | |
| **idempotency_key** | **string**| Unique per attempt. A retry carrying the same key and the same body is answered from the record instead of running again. | |
| **update_project_brand_profile_request** | [**\Mencoro\Api\Model\UpdateProjectBrandProfileRequest**](../Model/UpdateProjectBrandProfileRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\BrandProfileResource**](../Model/BrandProfileResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
