# Mencoro.Api.Model.ApplyClusteringJobOutcome
Per-tracked-query results of applying a clustering job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | [**List&lt;ApplyClusteringJobOutcomeSuccessfulInner&gt;**](ApplyClusteringJobOutcomeSuccessfulInner.md) | Tracked queries written, each with the cluster ids it ended up with - the resulting state, not the delta. | [optional] 
**Failed** | [**List&lt;ApplyClusteringJobOutcomeFailedInner&gt;**](ApplyClusteringJobOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 
**Clusters** | [**List&lt;ApplyClusteringJobOutcomeClustersInner&gt;**](ApplyClusteringJobOutcomeClustersInner.md) | Every cluster the assignments referred to, and whether this call created it. | [optional] 
**SkippedClusters** | [**List&lt;ApplyClusteringJobOutcomeSkippedClustersInner&gt;**](ApplyClusteringJobOutcomeSkippedClustersInner.md) | Proposed names the store cannot hold. A tracked query whose proposed cluster was skipped ends up with fewer clusters than the proposal showed. | [optional] 
**Unassigned** | **List&lt;Guid&gt;** | Tracked queries the job produced no assignment for. Nothing was written for them and they keep the clusters they already had, under every merge mode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

