# CreateQueryCluster409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**request_id** | **UUID** |  | [optional] 

## Example

```python
from mencoro.models.create_query_cluster409_response import CreateQueryCluster409Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQueryCluster409Response from a JSON string
create_query_cluster409_response_instance = CreateQueryCluster409Response.from_json(json)
# print the JSON string representation of the object
print(CreateQueryCluster409Response.to_json())

# convert the object into a dict
create_query_cluster409_response_dict = create_query_cluster409_response_instance.to_dict()
# create an instance of CreateQueryCluster409Response from a dict
create_query_cluster409_response_from_dict = CreateQueryCluster409Response.from_dict(create_query_cluster409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


