# Mencoro.Api.Model.BulkRemoveClustersFromTrackedQueriesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | **List&lt;Guid&gt;** | Tracked queries to remove. At most 100 distinct ids; duplicates are collapsed. | [optional] 
**QueryClusterIds** | **List&lt;Guid&gt;** | Clusters every named tracked query is removed from. All must belong to the project in the path. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

