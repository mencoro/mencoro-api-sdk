# CreateQueryClusterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Stored trimmed and lower-cased. Unique within the project. | [optional] 

## Example

```python
from mencoro.models.create_query_cluster_request import CreateQueryClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQueryClusterRequest from a JSON string
create_query_cluster_request_instance = CreateQueryClusterRequest.from_json(json)
# print the JSON string representation of the object
print(CreateQueryClusterRequest.to_json())

# convert the object into a dict
create_query_cluster_request_dict = create_query_cluster_request_instance.to_dict()
# create an instance of CreateQueryClusterRequest from a dict
create_query_cluster_request_from_dict = CreateQueryClusterRequest.from_dict(create_query_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


