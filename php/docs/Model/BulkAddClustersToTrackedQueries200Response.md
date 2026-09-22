# BulkAddClustersToTrackedQueries200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**\Mencoro\Api\Model\BatchPauseTrackedQueries200ResponseSuccessfulInner[]**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries that were added to every named cluster. | [optional]
**failed** | [**\Mencoro\Api\Model\BatchPauseTrackedQueries200ResponseFailedInner[]**](BatchPauseTrackedQueries200ResponseFailedInner.md) | Tracked queries left untouched, each with the domain error code a single-item call would have returned. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
