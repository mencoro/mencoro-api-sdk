# BulkRemoveClustersFromTrackedQueriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** | Tracked queries to remove. At most 100 distinct ids; duplicates are collapsed. | [optional] 
**query_cluster_ids** | **List[UUID]** | Clusters every named tracked query is removed from. All must belong to the project in the path. | [optional] 

## Example

```python
from mencoro.models.bulk_remove_clusters_from_tracked_queries_request import BulkRemoveClustersFromTrackedQueriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkRemoveClustersFromTrackedQueriesRequest from a JSON string
bulk_remove_clusters_from_tracked_queries_request_instance = BulkRemoveClustersFromTrackedQueriesRequest.from_json(json)
# print the JSON string representation of the object
print(BulkRemoveClustersFromTrackedQueriesRequest.to_json())

# convert the object into a dict
bulk_remove_clusters_from_tracked_queries_request_dict = bulk_remove_clusters_from_tracked_queries_request_instance.to_dict()
# create an instance of BulkRemoveClustersFromTrackedQueriesRequest from a dict
bulk_remove_clusters_from_tracked_queries_request_from_dict = BulkRemoveClustersFromTrackedQueriesRequest.from_dict(bulk_remove_clusters_from_tracked_queries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


