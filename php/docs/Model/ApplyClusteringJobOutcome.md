# ApplyClusteringJobOutcome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**\Mencoro\Api\Model\ApplyClusteringJobOutcomeSuccessfulInner[]**](ApplyClusteringJobOutcomeSuccessfulInner.md) | Tracked queries written, each with the cluster ids it ended up with - the resulting state, not the delta. | [optional]
**failed** | [**\Mencoro\Api\Model\ApplyClusteringJobOutcomeFailedInner[]**](ApplyClusteringJobOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional]
**clusters** | [**\Mencoro\Api\Model\ApplyClusteringJobOutcomeClustersInner[]**](ApplyClusteringJobOutcomeClustersInner.md) | Every cluster the assignments referred to, and whether this call created it. | [optional]
**skipped_clusters** | [**\Mencoro\Api\Model\ApplyClusteringJobOutcomeSkippedClustersInner[]**](ApplyClusteringJobOutcomeSkippedClustersInner.md) | Proposed names the store cannot hold. A tracked query whose proposed cluster was skipped ends up with fewer clusters than the proposal showed. | [optional]
**unassigned** | **string[]** | Tracked queries the job produced no assignment for. Nothing was written for them and they keep the clusters they already had, under every merge mode. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
