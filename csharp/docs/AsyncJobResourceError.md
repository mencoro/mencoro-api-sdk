# Mencoro.Api.Model.AsyncJobResourceError
Why the job failed, and what to do next. Null unless `status` is `failed`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | A stable code for the kind of failure: &#x60;timed_out&#x60;, &#x60;provider_failed&#x60;, &#x60;submission_failed&#x60; or &#x60;internal_error&#x60;. | 
**Message** | **string** | A fixed, readable explanation of the code. It is the same for every job that failed with that code. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

