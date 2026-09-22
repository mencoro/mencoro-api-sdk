# Mencoro.Api.Model.TrackedQueryDetailResource
A tracked query and how it is checked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**ProjectId** | **Guid** | The project this tracked query belongs to | 
**QueryText** | **string** | The prompt or keyword sent to the engine | 
**Engine** | **string** |  | 
**Locale** | **string** | Language tag the query is asked in. Null when the engine is asked without one. | [optional] 
**Country** | **string** | ISO-3166 alpha-2 country the query is asked from | 
**QueryClusterIds** | **List&lt;Guid&gt;** | Clusters (groups) this query belongs to. Empty when it is ungrouped. | 
**Status** | **string** |  | 
**CheckFrequency** | **string** | How often the query is checked while active | 
**NPasses** | **int** | Passes run per check. Greater than 1 only for AI engines. | 
**LastCheckedAt** | **DateTime?** | When a check last completed. Null means no check has completed yet, which is not the same as a check that found nothing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

