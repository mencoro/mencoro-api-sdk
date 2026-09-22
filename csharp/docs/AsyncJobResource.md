# Mencoro.Api.Model.AsyncJobResource
An asynchronous job and, once it has completed, its result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobId** | **Guid** |  | 
**Type** | **string** | What the job produces, and therefore the shape of &#x60;result&#x60; | 
**Status** | **string** | A job in &#x60;pending&#x60;, &#x60;running&#x60; or &#x60;awaiting_retry&#x60; is still in flight; &#x60;completed&#x60; and &#x60;failed&#x60; are terminal. | 
**Result** | **Object** | The job output, shaped by &#x60;type&#x60;. Null while the job is still in flight and for a job that failed: it means the result is not known, never that the job produced nothing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

