# Mencoro\Api\BillingApi

Billing

All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getSubscription()**](BillingApi.md#getSubscription) | **GET** /api/v1/organizations/{organizationId}/subscription | Get the subscription of an organization |


## `getSubscription()`

```php
getSubscription($organization_id): \Mencoro\Api\Model\SubscriptionResource
```

Get the subscription of an organization

Minimum role: viewer. The most recent subscription contract of the organization, whatever its state: tier, billing interval, check budget and consumption, and the cancellation and grace dates. An organization that has never subscribed answers 200 with \"status\": \"none\" and every other field null - a null is \"not applicable\", never a stand-in for a zero budget or zero consumption. Stripe identifiers, prices and payment methods are not part of this API.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\BillingApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string

try {
    $result = $apiInstance->getSubscription($organization_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BillingApi->getSubscription: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\SubscriptionResource**](../Model/SubscriptionResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
