# Mencoro.Api.Model.BatchCreateTrackedQueriesResultResource
Per-combination results of creating tracked queries in bulk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | [**List&lt;BatchCreateTrackedQueriesResultResourceSuccessfulInner&gt;**](BatchCreateTrackedQueriesResultResourceSuccessfulInner.md) | Tracked queries created by this call, one entry per query text, engine and country combination. | [optional] 
**Failed** | [**List&lt;BatchCreateTrackedQueriesResultResourceFailedInner&gt;**](BatchCreateTrackedQueriesResultResourceFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

