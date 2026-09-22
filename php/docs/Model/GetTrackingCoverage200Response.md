# GetTrackingCoverage200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **string** |  | [optional]
**total** | **int** | Every tracked query on the project, whatever its status | [optional]
**active** | **int** | Tracked queries currently being checked | [optional]
**paused** | **int** | Tracked queries whose checks are suspended | [optional]
**never_checked** | **int** | Active queries that have never run yet | [optional]
**overdue** | **int** | Active queries past their check-frequency interval, never-checked ones excluded | [optional]
**sample** | [**\Mencoro\Api\Model\GetTrackingCoverage200ResponseSampleInner[]**](GetTrackingCoverage200ResponseSampleInner.md) | Up to 20 overdue queries, oldest check first | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
