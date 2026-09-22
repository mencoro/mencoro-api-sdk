# Mencoro.Api.Model.GetTrackingCoverage200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectId** | **Guid** |  | [optional] 
**Total** | **int** | Every tracked query on the project, whatever its status | [optional] 
**Active** | **int** | Tracked queries currently being checked | [optional] 
**Paused** | **int** | Tracked queries whose checks are suspended | [optional] 
**NeverChecked** | **int** | Active queries that have never run yet | [optional] 
**Overdue** | **int** | Active queries past their check-frequency interval, never-checked ones excluded | [optional] 
**Sample** | [**List&lt;GetTrackingCoverage200ResponseSampleInner&gt;**](GetTrackingCoverage200ResponseSampleInner.md) | Up to 20 overdue queries, oldest check first | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

