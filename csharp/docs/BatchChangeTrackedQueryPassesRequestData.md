# Mencoro.Api.Model.BatchChangeTrackedQueryPassesRequestData
Tracked queries to retune, and the passes per check to set on them

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | **List&lt;Guid&gt;** | Ids of the tracked queries to change. Duplicates are collapsed. | 
**NPasses** | **int** | Passes run per check. Only an AI engine accepts more than one; a non-AI target is reported under \&quot;failed\&quot;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

