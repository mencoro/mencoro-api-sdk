# BulkAddClustersToTrackedQueries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**List[BatchPauseTrackedQueries200ResponseSuccessfulInner]**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries that were added to every named cluster. | [optional] 
**failed** | [**List[BatchPauseTrackedQueries200ResponseFailedInner]**](BatchPauseTrackedQueries200ResponseFailedInner.md) | Tracked queries left untouched, each with the domain error code a single-item call would have returned. | [optional] 

## Example

```python
from mencoro.models.bulk_add_clusters_to_tracked_queries200_response import BulkAddClustersToTrackedQueries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAddClustersToTrackedQueries200Response from a JSON string
bulk_add_clusters_to_tracked_queries200_response_instance = BulkAddClustersToTrackedQueries200Response.from_json(json)
# print the JSON string representation of the object
print(BulkAddClustersToTrackedQueries200Response.to_json())

# convert the object into a dict
bulk_add_clusters_to_tracked_queries200_response_dict = bulk_add_clusters_to_tracked_queries200_response_instance.to_dict()
# create an instance of BulkAddClustersToTrackedQueries200Response from a dict
bulk_add_clusters_to_tracked_queries200_response_from_dict = BulkAddClustersToTrackedQueries200Response.from_dict(bulk_add_clusters_to_tracked_queries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


