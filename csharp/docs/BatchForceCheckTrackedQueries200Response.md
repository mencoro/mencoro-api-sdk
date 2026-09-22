# Mencoro.Api.Model.BatchForceCheckTrackedQueries200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | [**List&lt;BatchPauseTrackedQueries200ResponseSuccessfulInner&gt;**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries whose check was accepted for submission. Accepted is not completed. | [optional] 
**Failed** | [**List&lt;BatchForceCheckTrackedQueries200ResponseFailedInner&gt;**](BatchForceCheckTrackedQueries200ResponseFailedInner.md) | Tracked queries no check was submitted for, each with the reason: check_budget_forecast_exhausted, subscription_not_found, tracked_query_already_paused or tracked_query_not_found. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

