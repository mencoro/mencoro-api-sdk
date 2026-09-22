# Mencoro\Api\InvitationsApi

Invitations

All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**cancelInvitation()**](InvitationsApi.md#cancelInvitation) | **POST** /api/v1/organizations/{organizationId}/invitations/{invitationId}/cancel | Cancel a pending invitation |
| [**createInvitation()**](InvitationsApi.md#createInvitation) | **POST** /api/v1/organizations/{organizationId}/invitations | Invite somebody to an organization |
| [**listInvitations()**](InvitationsApi.md#listInvitations) | **GET** /api/v1/organizations/{organizationId}/invitations | List an organization&#39;s invitations |


## `cancelInvitation()`

```php
cancelInvitation($organization_id, $invitation_id, $x_mencoro_confirmation, $idempotency_key): \Mencoro\Api\Model\InvitationResource
```

Cancel a pending invitation

Minimum role: owner. The link already emailed to the invitee stops working. Only a pending invitation can be cancelled; one that was accepted, rejected or has expired is refused.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\InvitationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$invitation_id = 'invitation_id_example'; // string
$x_mencoro_confirmation = 'x_mencoro_confirmation_example'; // string
$idempotency_key = 'idempotency_key_example'; // string

try {
    $result = $apiInstance->cancelInvitation($organization_id, $invitation_id, $x_mencoro_confirmation, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InvitationsApi->cancelInvitation: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **invitation_id** | **string**|  | |
| **x_mencoro_confirmation** | **string**|  | |
| **idempotency_key** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\InvitationResource**](../Model/InvitationResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createInvitation()`

```php
createInvitation($organization_id, $x_mencoro_confirmation, $idempotency_key, $create_invitation_request): \Mencoro\Api\Model\CreateInvitation200Response
```

Invite somebody to an organization

Minimum role: owner. Sends an invitation email that expires after 14 days. If the address already belongs to an active member the call succeeds and creates nothing - answered as 200 with created=false rather than 201, so a client can tell the two apart. Preview it first; the preview says which of the two will happen.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\InvitationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$x_mencoro_confirmation = 'x_mencoro_confirmation_example'; // string
$idempotency_key = 'idempotency_key_example'; // string
$create_invitation_request = new \Mencoro\Api\Model\CreateInvitationRequest(); // \Mencoro\Api\Model\CreateInvitationRequest

try {
    $result = $apiInstance->createInvitation($organization_id, $x_mencoro_confirmation, $idempotency_key, $create_invitation_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InvitationsApi->createInvitation: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **x_mencoro_confirmation** | **string**|  | |
| **idempotency_key** | **string**|  | |
| **create_invitation_request** | [**\Mencoro\Api\Model\CreateInvitationRequest**](../Model/CreateInvitationRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\CreateInvitation200Response**](../Model/CreateInvitation200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listInvitations()`

```php
listInvitations($organization_id, $limit, $offset, $search, $status, $sort_by, $sort_order): \Mencoro\Api\Model\ListInvitations200Response
```

List an organization's invitations

Minimum role: owner. Returns the invitations issued for this organization, in every state. The invitation token is never returned. `status` matches the stored state, so an invitation that has passed its `expiresAt` is still listed as pending until it is transitioned; compare `expiresAt` to decide. Rows are ordered by the chosen sort field, and invitations sharing the same value keep no guaranteed relative order across pages.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\InvitationsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$limit = 20; // int
$offset = 0; // int
$search = 'search_example'; // string | Matches part of the invited email address.
$status = 'status_example'; // string | Absent means every state.
$sort_by = 'createdAt'; // string
$sort_order = 'desc'; // string

try {
    $result = $apiInstance->listInvitations($organization_id, $limit, $offset, $search, $status, $sort_by, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling InvitationsApi->listInvitations: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **limit** | **int**|  | [optional] [default to 20] |
| **offset** | **int**|  | [optional] [default to 0] |
| **search** | **string**| Matches part of the invited email address. | [optional] |
| **status** | **string**| Absent means every state. | [optional] |
| **sort_by** | **string**|  | [optional] [default to &#39;createdAt&#39;] |
| **sort_order** | **string**|  | [optional] [default to &#39;desc&#39;] |

### Return type

[**\Mencoro\Api\Model\ListInvitations200Response**](../Model/ListInvitations200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
