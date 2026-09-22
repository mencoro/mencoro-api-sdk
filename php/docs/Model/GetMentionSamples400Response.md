# GetMentionSamples400Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **string** | Machine-readable reason. &#x60;validation_error&#x60; when the request was rejected; otherwise the domain error code. |
**message** | **string** | Human-readable reason. A 4xx carries the real message; a 5xx carries a fixed sentence and the detail goes to the logs only. |
**request_id** | **string** | Correlation id, also returned in the X-Request-Id header. |
**details** | **array<string,\Mencoro\Api\Model\GetMentionSamples400ResponseDetailsValueInner[]>** | Present only on a validation failure: one entry per rejected field, each an array of errors. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
