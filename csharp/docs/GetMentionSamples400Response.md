# Mencoro.Api.Model.GetMentionSamples400Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | Machine-readable reason. &#x60;validation_error&#x60; when the request was rejected; otherwise the domain error code. | 
**Message** | **string** | Human-readable reason. A 4xx carries the real message; a 5xx carries a fixed sentence and the detail goes to the logs only. | 
**RequestId** | **Guid** | Correlation id, also returned in the X-Request-Id header. | 
**Details** | **Dictionary&lt;string, List&lt;GetMentionSamples400ResponseDetailsValueInner&gt;&gt;** | Present only on a validation failure: one entry per rejected field, each an array of errors. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

