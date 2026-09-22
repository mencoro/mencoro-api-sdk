# DeleteQueryCluster200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The cluster that was deleted | [optional] 
**name** | **str** | Its name at the moment it was deleted | [optional] 
**deleted** | **bool** | Always true; present so the body is self-describing | [optional] 

## Example

```python
from mencoro.models.delete_query_cluster200_response import DeleteQueryCluster200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteQueryCluster200Response from a JSON string
delete_query_cluster200_response_instance = DeleteQueryCluster200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteQueryCluster200Response.to_json())

# convert the object into a dict
delete_query_cluster200_response_dict = delete_query_cluster200_response_instance.to_dict()
# create an instance of DeleteQueryCluster200Response from a dict
delete_query_cluster200_response_from_dict = DeleteQueryCluster200Response.from_dict(delete_query_cluster200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


