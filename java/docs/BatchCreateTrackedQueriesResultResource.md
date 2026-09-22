

# BatchCreateTrackedQueriesResultResource

Per-combination results of creating tracked queries in bulk

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**successful** | [**List&lt;BatchCreateTrackedQueriesResultResourceSuccessfulInner&gt;**](BatchCreateTrackedQueriesResultResourceSuccessfulInner.md) | Tracked queries created by this call, one entry per query text, engine and country combination. |  [optional] |
|**failed** | [**List&lt;BatchCreateTrackedQueriesResultResourceFailedInner&gt;**](BatchCreateTrackedQueriesResultResourceFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. |  [optional] |



