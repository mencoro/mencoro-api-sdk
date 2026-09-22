# BatchCreateTrackedQueriesResultResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**\Mencoro\Api\Model\BatchCreateTrackedQueriesResultResourceSuccessfulInner[]**](BatchCreateTrackedQueriesResultResourceSuccessfulInner.md) | Tracked queries created by this call, one entry per query text, engine and country combination. | [optional]
**failed** | [**\Mencoro\Api\Model\BatchCreateTrackedQueriesResultResourceFailedInner[]**](BatchCreateTrackedQueriesResultResourceFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
