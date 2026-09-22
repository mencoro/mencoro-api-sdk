

# ApplyClusteringJobOutcome

Per-tracked-query results of applying a clustering job

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**successful** | [**List&lt;ApplyClusteringJobOutcomeSuccessfulInner&gt;**](ApplyClusteringJobOutcomeSuccessfulInner.md) | Tracked queries written, each with the cluster ids it ended up with - the resulting state, not the delta. |  [optional] |
|**failed** | [**List&lt;ApplyClusteringJobOutcomeFailedInner&gt;**](ApplyClusteringJobOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. |  [optional] |
|**clusters** | [**List&lt;ApplyClusteringJobOutcomeClustersInner&gt;**](ApplyClusteringJobOutcomeClustersInner.md) | Every cluster the assignments referred to, and whether this call created it. |  [optional] |
|**skippedClusters** | [**List&lt;ApplyClusteringJobOutcomeSkippedClustersInner&gt;**](ApplyClusteringJobOutcomeSkippedClustersInner.md) | Proposed names the store cannot hold. A tracked query whose proposed cluster was skipped ends up with fewer clusters than the proposal showed. |  [optional] |
|**unassigned** | **List&lt;UUID&gt;** | Tracked queries the job produced no assignment for. Nothing was written for them and they keep the clusters they already had, under every merge mode. |  [optional] |



