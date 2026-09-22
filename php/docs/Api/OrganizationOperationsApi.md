# Mencoro\Api\OrganizationOperationsApi



All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**previewOrganizationOperation()**](OrganizationOperationsApi.md#previewOrganizationOperation) | **POST** /api/v1/organization-operation-previews | Preview an organization operation and obtain a confirmation |


## `previewOrganizationOperation()`

```php
previewOrganizationOperation($preview_organization_operation_request): \Mencoro\Api\Model\PreviewOrganizationOperation200Response
```

Preview an organization operation and obtain a confirmation

Organization, member and invitation changes need two calls. This one reports the concrete changes, the side effects, the warnings and the conditions, and returns a confirmation valid for five minutes. Send it back in the X-Mencoro-Confirmation header, together with an Idempotency-Key, on the call that performs the operation. Previewing has no effects of any kind.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\OrganizationOperationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$preview_organization_operation_request = {"action":"archiveOrganization","organizationId":"0193c4f0-11aa-7b22-9d33-4e5f60718293"}; // \Mencoro\Api\Model\PreviewOrganizationOperationRequest

try {
    $result = $apiInstance->previewOrganizationOperation($preview_organization_operation_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrganizationOperationsApi->previewOrganizationOperation: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **preview_organization_operation_request** | [**\Mencoro\Api\Model\PreviewOrganizationOperationRequest**](../Model/PreviewOrganizationOperationRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\PreviewOrganizationOperation200Response**](../Model/PreviewOrganizationOperation200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
