# ListQueryClusters200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[QueryClusterResource]**](QueryClusterResource.md) |  | [optional] 
**total** | **int** | Clusters in the project, not the size of this page | [optional] 

## Example

```python
from mencoro.models.list_query_clusters200_response import ListQueryClusters200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListQueryClusters200Response from a JSON string
list_query_clusters200_response_instance = ListQueryClusters200Response.from_json(json)
# print the JSON string representation of the object
print(ListQueryClusters200Response.to_json())

# convert the object into a dict
list_query_clusters200_response_dict = list_query_clusters200_response_instance.to_dict()
# create an instance of ListQueryClusters200Response from a dict
list_query_clusters200_response_from_dict = ListQueryClusters200Response.from_dict(list_query_clusters200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


