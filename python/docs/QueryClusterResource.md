# QueryClusterResource

A keyword cluster of a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Pass this value in the queryClusterIds filter of the analytics operations | 
**project_id** | **UUID** | The project this cluster belongs to | 
**name** | **str** | Unique within the project, stored lower-cased | 

## Example

```python
from mencoro.models.query_cluster_resource import QueryClusterResource

# TODO update the JSON string below
json = "{}"
# create an instance of QueryClusterResource from a JSON string
query_cluster_resource_instance = QueryClusterResource.from_json(json)
# print the JSON string representation of the object
print(QueryClusterResource.to_json())

# convert the object into a dict
query_cluster_resource_dict = query_cluster_resource_instance.to_dict()
# create an instance of QueryClusterResource from a dict
query_cluster_resource_from_dict = QueryClusterResource.from_dict(query_cluster_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


