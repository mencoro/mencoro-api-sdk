# Mencoro\Api\AccountApi

Account

All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getMe()**](AccountApi.md#getMe) | **GET** /api/v1/me | Get the authenticated identity |
| [**getMeStats()**](AccountApi.md#getMeStats) | **GET** /api/v1/me/stats | Counts across everything the key can reach |


## `getMe()`

```php
getMe(): \Mencoro\Api\Model\MeResource
```

Get the authenticated identity

Returns the user the API key belongs to, plus the key's capabilities and scope. Use it to confirm which credential a call runs under.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AccountApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getMe();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountApi->getMe: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\Mencoro\Api\Model\MeResource**](../Model/MeResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMeStats()`

```php
getMeStats(): \Mencoro\Api\Model\GetMeStats200Response
```

Counts across everything the key can reach

Aggregate counts over every organization the key's owner is an active member of, narrowed to the key's scope — the same set /api/v1/organizations pages through. `organizations.total` is that set's size; `projects.total` and `projects.active` count the projects inside it, archived ones included in the total and excluded from the active figure. Every value is an exact count: zero means zero, and no value here is ever null or unknown. Per-organization billing and usage figures are not part of this response; read them from the subscription and entitlements operations instead.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AccountApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getMeStats();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountApi->getMeStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\Mencoro\Api\Model\GetMeStats200Response**](../Model/GetMeStats200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
