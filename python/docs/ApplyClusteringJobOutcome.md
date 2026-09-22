# ApplyClusteringJobOutcome

Per-tracked-query results of applying a clustering job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**List[ApplyClusteringJobOutcomeSuccessfulInner]**](ApplyClusteringJobOutcomeSuccessfulInner.md) | Tracked queries written, each with the cluster ids it ended up with - the resulting state, not the delta. | [optional] 
**failed** | [**List[ApplyClusteringJobOutcomeFailedInner]**](ApplyClusteringJobOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 
**clusters** | [**List[ApplyClusteringJobOutcomeClustersInner]**](ApplyClusteringJobOutcomeClustersInner.md) | Every cluster the assignments referred to, and whether this call created it. | [optional] 
**skipped_clusters** | [**List[ApplyClusteringJobOutcomeSkippedClustersInner]**](ApplyClusteringJobOutcomeSkippedClustersInner.md) | Proposed names the store cannot hold. A tracked query whose proposed cluster was skipped ends up with fewer clusters than the proposal showed. | [optional] 
**unassigned** | **List[UUID]** | Tracked queries the job produced no assignment for. Nothing was written for them and they keep the clusters they already had, under every merge mode. | [optional] 

## Example

```python
from mencoro.models.apply_clustering_job_outcome import ApplyClusteringJobOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyClusteringJobOutcome from a JSON string
apply_clustering_job_outcome_instance = ApplyClusteringJobOutcome.from_json(json)
# print the JSON string representation of the object
print(ApplyClusteringJobOutcome.to_json())

# convert the object into a dict
apply_clustering_job_outcome_dict = apply_clustering_job_outcome_instance.to_dict()
# create an instance of ApplyClusteringJobOutcome from a dict
apply_clustering_job_outcome_from_dict = ApplyClusteringJobOutcome.from_dict(apply_clustering_job_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


