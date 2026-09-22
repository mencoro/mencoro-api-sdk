# Mencoro.Api.Model.BatchWriteOutcome
Per-item results of a batch write

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | [**List&lt;BatchPauseTrackedQueries200ResponseSuccessfulInner&gt;**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | The resources the operation was applied to. | [optional] 
**Failed** | [**List&lt;BatchWriteOutcomeFailedInner&gt;**](BatchWriteOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

