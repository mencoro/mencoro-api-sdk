# BatchCreateQueryClustersOutcome

Per-name results of creating clusters in bulk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**List[BatchCreateQueryClustersOutcomeSuccessfulInner]**](BatchCreateQueryClustersOutcomeSuccessfulInner.md) | Clusters created by this call. | [optional] 
**failed** | [**List[BatchCreateQueryClustersOutcomeFailedInner]**](BatchCreateQueryClustersOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 

## Example

```python
from mencoro.models.batch_create_query_clusters_outcome import BatchCreateQueryClustersOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCreateQueryClustersOutcome from a JSON string
batch_create_query_clusters_outcome_instance = BatchCreateQueryClustersOutcome.from_json(json)
# print the JSON string representation of the object
print(BatchCreateQueryClustersOutcome.to_json())

# convert the object into a dict
batch_create_query_clusters_outcome_dict = batch_create_query_clusters_outcome_instance.to_dict()
# create an instance of BatchCreateQueryClustersOutcome from a dict
batch_create_query_clusters_outcome_from_dict = BatchCreateQueryClustersOutcome.from_dict(batch_create_query_clusters_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


