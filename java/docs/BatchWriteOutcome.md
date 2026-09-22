

# BatchWriteOutcome

Per-item results of a batch write

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**successful** | [**List&lt;BatchPauseTrackedQueries200ResponseSuccessfulInner&gt;**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | The resources the operation was applied to. |  [optional] |
|**failed** | [**List&lt;BatchWriteOutcomeFailedInner&gt;**](BatchWriteOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. |  [optional] |



