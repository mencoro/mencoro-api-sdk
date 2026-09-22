# Mencoro.Api.Model.StartClusteringJobRequestData
What a clustering job should group, and how

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackedQueryIds** | **List&lt;Guid&gt;** | The tracked queries to cluster. Duplicates are collapsed. | 
**Mode** | **string** | fill_gaps groups only tracked queries that belong to no cluster; add_on_top adds the new clusters to whatever each query already has; full_regroup replaces the current clusters with the job&#39;s. | 
**RestrictToExistingClusters** | **bool** | When true the job may only use clusters the project already has, and leaves a query ungrouped rather than inventing a name for it. | [optional] [default to false]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

