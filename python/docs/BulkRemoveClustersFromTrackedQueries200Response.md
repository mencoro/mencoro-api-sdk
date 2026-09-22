# BulkRemoveClustersFromTrackedQueries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**List[BatchPauseTrackedQueries200ResponseSuccessfulInner]**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries that were removed from every named cluster. | [optional] 
**failed** | [**List[BatchPauseTrackedQueries200ResponseFailedInner]**](BatchPauseTrackedQueries200ResponseFailedInner.md) | Tracked queries left untouched, each with the domain error code a single-item call would have returned. | [optional] 

## Example

```python
from mencoro.models.bulk_remove_clusters_from_tracked_queries200_response import BulkRemoveClustersFromTrackedQueries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkRemoveClustersFromTrackedQueries200Response from a JSON string
bulk_remove_clusters_from_tracked_queries200_response_instance = BulkRemoveClustersFromTrackedQueries200Response.from_json(json)
# print the JSON string representation of the object
print(BulkRemoveClustersFromTrackedQueries200Response.to_json())

# convert the object into a dict
bulk_remove_clusters_from_tracked_queries200_response_dict = bulk_remove_clusters_from_tracked_queries200_response_instance.to_dict()
# create an instance of BulkRemoveClustersFromTrackedQueries200Response from a dict
bulk_remove_clusters_from_tracked_queries200_response_from_dict = BulkRemoveClustersFromTrackedQueries200Response.from_dict(bulk_remove_clusters_from_tracked_queries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


