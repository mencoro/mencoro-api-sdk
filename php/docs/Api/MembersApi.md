# Mencoro\Api\MembersApi

Members

All URIs are relative to https://api.mencoro.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**changeMemberRole()**](MembersApi.md#changeMemberRole) | **PATCH** /api/v1/organizations/{organizationId}/members/{memberId} | Change a member role |
| [**getMember()**](MembersApi.md#getMember) | **GET** /api/v1/organizations/{organizationId}/members/{memberId} | Get one organization membership |
| [**listMembers()**](MembersApi.md#listMembers) | **GET** /api/v1/organizations/{organizationId}/members | List an organization&#39;s members |
| [**reactivateMember()**](MembersApi.md#reactivateMember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/reactivate | Reactivate a suspended member |
| [**suspendMember()**](MembersApi.md#suspendMember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/suspend | Suspend a member |


## `changeMemberRole()`

```php
changeMemberRole($organization_id, $member_id, $x_mencoro_confirmation, $idempotency_key, $change_member_role_request): \Mencoro\Api\Model\MemberResource
```

Change a member role

Minimum role: owner. The role of a suspended member cannot be changed, and the last active owner cannot be demoted. Preview it first: the confirmation is bound to the number of active owners, so another owner being suspended in between invalidates it rather than stranding the organization.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\MembersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$member_id = 'member_id_example'; // string
$x_mencoro_confirmation = 'x_mencoro_confirmation_example'; // string
$idempotency_key = 'idempotency_key_example'; // string
$change_member_role_request = new \Mencoro\Api\Model\ChangeMemberRoleRequest(); // \Mencoro\Api\Model\ChangeMemberRoleRequest

try {
    $result = $apiInstance->changeMemberRole($organization_id, $member_id, $x_mencoro_confirmation, $idempotency_key, $change_member_role_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MembersApi->changeMemberRole: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **member_id** | **string**|  | |
| **x_mencoro_confirmation** | **string**|  | |
| **idempotency_key** | **string**|  | |
| **change_member_role_request** | [**\Mencoro\Api\Model\ChangeMemberRoleRequest**](../Model/ChangeMemberRoleRequest.md)|  | |

### Return type

[**\Mencoro\Api\Model\MemberResource**](../Model/MemberResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMember()`

```php
getMember($organization_id, $member_id): \Mencoro\Api\Model\MemberResource
```

Get one organization membership

Minimum role: owner — the same floor the members listing enforces, because a caller who can page the roster has already seen this record. Returns the facts of one membership: its role, whether it is active or suspended, and when it was joined. It does NOT describe the person behind it: no name, no email address, no phone number and no profile image, so a membership id can never be turned into a contact lookup. The membership is read from PostgreSQL, the same row at the same freshness the listing publishes. A membership belonging to another organization answers 404, exactly as an unknown or malformed id does, so the API never confirms that an inaccessible membership exists; the one 403 is a key without the read capability. The response carries no organizationId — it is the one in the path — and no creation timestamp; joinedAt is the membership fact. No query parameters are accepted.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\MembersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$member_id = 'member_id_example'; // string | The membership id, not the user id. Must belong to the organization in the path.

try {
    $result = $apiInstance->getMember($organization_id, $member_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MembersApi->getMember: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **member_id** | **string**| The membership id, not the user id. Must belong to the organization in the path. | |

### Return type

[**\Mencoro\Api\Model\MemberResource**](../Model/MemberResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listMembers()`

```php
listMembers($organization_id, $limit, $offset, $status, $sort_by, $sort_order): \Mencoro\Api\Model\ListMembers200Response
```

List an organization's members

Minimum role: owner. The application exposes this roster twice and the two disagree — its member screen shows it to any viewer, while its non-BFF endpoint requires an owner — so the published API takes the stricter of the two and requires an owner. A membership describes the membership, not the person: names and email addresses are never returned here, and there is no search parameter, because both would turn the roster into a contact export. Omitting \"status\" returns active and suspended memberships alike. Sorting by \"role\" is alphabetical on the role name, not by seniority.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\MembersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$limit = 20; // int
$offset = 0; // int
$status = 'status_example'; // string | Absent means both states.
$sort_by = 'joinedAt'; // string
$sort_order = 'desc'; // string

try {
    $result = $apiInstance->listMembers($organization_id, $limit, $offset, $status, $sort_by, $sort_order);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MembersApi->listMembers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **limit** | **int**|  | [optional] [default to 20] |
| **offset** | **int**|  | [optional] [default to 0] |
| **status** | **string**| Absent means both states. | [optional] |
| **sort_by** | **string**|  | [optional] [default to &#39;joinedAt&#39;] |
| **sort_order** | **string**|  | [optional] [default to &#39;desc&#39;] |

### Return type

[**\Mencoro\Api\Model\ListMembers200Response**](../Model/ListMembers200Response.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/csv`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `reactivateMember()`

```php
reactivateMember($organization_id, $member_id, $x_mencoro_confirmation, $idempotency_key): \Mencoro\Api\Model\MemberResource
```

Reactivate a suspended member

Minimum role: owner. The member keeps the role they had and regains access on their very next request. A member who is already active cannot be reactivated.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\MembersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$member_id = 'member_id_example'; // string
$x_mencoro_confirmation = 'x_mencoro_confirmation_example'; // string
$idempotency_key = 'idempotency_key_example'; // string

try {
    $result = $apiInstance->reactivateMember($organization_id, $member_id, $x_mencoro_confirmation, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MembersApi->reactivateMember: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **member_id** | **string**|  | |
| **x_mencoro_confirmation** | **string**|  | |
| **idempotency_key** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\MemberResource**](../Model/MemberResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `suspendMember()`

```php
suspendMember($organization_id, $member_id, $x_mencoro_confirmation, $idempotency_key): \Mencoro\Api\Model\MemberResource
```

Suspend a member

Minimum role: owner. The member loses access on their very next request, including through any API key they own that is scoped to this organization. The last active owner cannot be suspended.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\MembersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$organization_id = 'organization_id_example'; // string
$member_id = 'member_id_example'; // string
$x_mencoro_confirmation = 'x_mencoro_confirmation_example'; // string
$idempotency_key = 'idempotency_key_example'; // string

try {
    $result = $apiInstance->suspendMember($organization_id, $member_id, $x_mencoro_confirmation, $idempotency_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MembersApi->suspendMember: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **member_id** | **string**|  | |
| **x_mencoro_confirmation** | **string**|  | |
| **idempotency_key** | **string**|  | |

### Return type

[**\Mencoro\Api\Model\MemberResource**](../Model/MemberResource.md)

### Authorization

[ApiKey](../../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
