# ApplyClusteringJobOutcomeFailedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracked_query_id** | **UUID** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from mencoro.models.apply_clustering_job_outcome_failed_inner import ApplyClusteringJobOutcomeFailedInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyClusteringJobOutcomeFailedInner from a JSON string
apply_clustering_job_outcome_failed_inner_instance = ApplyClusteringJobOutcomeFailedInner.from_json(json)
# print the JSON string representation of the object
print(ApplyClusteringJobOutcomeFailedInner.to_json())

# convert the object into a dict
apply_clustering_job_outcome_failed_inner_dict = apply_clustering_job_outcome_failed_inner_instance.to_dict()
# create an instance of ApplyClusteringJobOutcomeFailedInner from a dict
apply_clustering_job_outcome_failed_inner_from_dict = ApplyClusteringJobOutcomeFailedInner.from_dict(apply_clustering_job_outcome_failed_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


