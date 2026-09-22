

# BulkAddClustersToTrackedQueries200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**successful** | [**List&lt;BatchPauseTrackedQueries200ResponseSuccessfulInner&gt;**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries that were added to every named cluster. |  [optional] |
|**failed** | [**List&lt;BatchPauseTrackedQueries200ResponseFailedInner&gt;**](BatchPauseTrackedQueries200ResponseFailedInner.md) | Tracked queries left untouched, each with the domain error code a single-item call would have returned. |  [optional] |



