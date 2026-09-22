# mencoro.OrganizationOperationsApi

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**preview_organization_operation**](OrganizationOperationsApi.md#preview_organization_operation) | **POST** /api/v1/organization-operation-previews | Preview an organization operation and obtain a confirmation


# **preview_organization_operation**
> PreviewOrganizationOperation200Response preview_organization_operation(preview_organization_operation_request)

Preview an organization operation and obtain a confirmation

Organization, member and invitation changes need two calls. This one reports the concrete changes, the side effects, the warnings and the conditions, and returns a confirmation valid for five minutes. Send it back in the X-Mencoro-Confirmation header, together with an Idempotency-Key, on the call that performs the operation. Previewing has no effects of any kind.

### Example

* Bearer Authentication (ApiKey):

```python
import mencoro
from mencoro.models.preview_organization_operation200_response import PreviewOrganizationOperation200Response
from mencoro.models.preview_organization_operation_request import PreviewOrganizationOperationRequest
from mencoro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mencoro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mencoro.Configuration(
    host = "https://api.mencoro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKey
configuration = mencoro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mencoro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mencoro.OrganizationOperationsApi(api_client)
    preview_organization_operation_request = {"action":"archiveOrganization","organizationId":"0193c4f0-11aa-7b22-9d33-4e5f60718293"} # PreviewOrganizationOperationRequest | 

    try:
        # Preview an organization operation and obtain a confirmation
        api_response = api_instance.preview_organization_operation(preview_organization_operation_request)
        print("The response of OrganizationOperationsApi->preview_organization_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationOperationsApi->preview_organization_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_organization_operation_request** | [**PreviewOrganizationOperationRequest**](PreviewOrganizationOperationRequest.md)|  | 

### Return type

[**PreviewOrganizationOperation200Response**](PreviewOrganizationOperation200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | What the operation would do, plus a confirmation |  -  |
**401** | Missing or invalid API key |  -  |
**400** | Unknown action, or a payload the operation does not accept |  -  |
**403** | The key lacks a required capability, or its scope is too narrow |  -  |
**404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

