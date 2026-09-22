# BulkAddClustersToTrackedQueriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** | Tracked queries to add. At most 100 distinct ids; duplicates are collapsed. | [optional] 
**query_cluster_ids** | **List[UUID]** | Clusters every named tracked query is added to. All must belong to the project in the path. | [optional] 

## Example

```python
from mencoro.models.bulk_add_clusters_to_tracked_queries_request import BulkAddClustersToTrackedQueriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAddClustersToTrackedQueriesRequest from a JSON string
bulk_add_clusters_to_tracked_queries_request_instance = BulkAddClustersToTrackedQueriesRequest.from_json(json)
# print the JSON string representation of the object
print(BulkAddClustersToTrackedQueriesRequest.to_json())

# convert the object into a dict
bulk_add_clusters_to_tracked_queries_request_dict = bulk_add_clusters_to_tracked_queries_request_instance.to_dict()
# create an instance of BulkAddClustersToTrackedQueriesRequest from a dict
bulk_add_clusters_to_tracked_queries_request_from_dict = BulkAddClustersToTrackedQueriesRequest.from_dict(bulk_add_clusters_to_tracked_queries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


