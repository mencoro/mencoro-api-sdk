# GetAvailableFilters200ResponseClustersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Pass this in queryClusterIds, never the name | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from mencoro.models.get_available_filters200_response_clusters_inner import GetAvailableFilters200ResponseClustersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableFilters200ResponseClustersInner from a JSON string
get_available_filters200_response_clusters_inner_instance = GetAvailableFilters200ResponseClustersInner.from_json(json)
# print the JSON string representation of the object
print(GetAvailableFilters200ResponseClustersInner.to_json())

# convert the object into a dict
get_available_filters200_response_clusters_inner_dict = get_available_filters200_response_clusters_inner_instance.to_dict()
# create an instance of GetAvailableFilters200ResponseClustersInner from a dict
get_available_filters200_response_clusters_inner_from_dict = GetAvailableFilters200ResponseClustersInner.from_dict(get_available_filters200_response_clusters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


