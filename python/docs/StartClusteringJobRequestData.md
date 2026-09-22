# StartClusteringJobRequestData

What a clustering job should group, and how

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracked_query_ids** | **List[UUID]** | The tracked queries to cluster. Duplicates are collapsed. | 
**mode** | **str** | fill_gaps groups only tracked queries that belong to no cluster; add_on_top adds the new clusters to whatever each query already has; full_regroup replaces the current clusters with the job&#39;s. | 
**restrict_to_existing_clusters** | **bool** | When true the job may only use clusters the project already has, and leaves a query ungrouped rather than inventing a name for it. | [optional] [default to False]

## Example

```python
from mencoro.models.start_clustering_job_request_data import StartClusteringJobRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of StartClusteringJobRequestData from a JSON string
start_clustering_job_request_data_instance = StartClusteringJobRequestData.from_json(json)
# print the JSON string representation of the object
print(StartClusteringJobRequestData.to_json())

# convert the object into a dict
start_clustering_job_request_data_dict = start_clustering_job_request_data_instance.to_dict()
# create an instance of StartClusteringJobRequestData from a dict
start_clustering_job_request_data_from_dict = StartClusteringJobRequestData.from_dict(start_clustering_job_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


