# BatchForceCheckTrackedQueries200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**\Mencoro\Api\Model\BatchPauseTrackedQueries200ResponseSuccessfulInner[]**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries whose check was accepted for submission. Accepted is not completed. | [optional]
**failed** | [**\Mencoro\Api\Model\BatchForceCheckTrackedQueries200ResponseFailedInner[]**](BatchForceCheckTrackedQueries200ResponseFailedInner.md) | Tracked queries no check was submitted for, each with the reason: check_budget_forecast_exhausted, subscription_not_found, tracked_query_already_paused or tracked_query_not_found. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
