# BatchCreateQueryClustersRequestData

The cluster names a batch create asks for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | Cluster names to create, already trimmed and lower-cased on the server. Duplicates are collapsed. | 

## Example

```python
from mencoro.models.batch_create_query_clusters_request_data import BatchCreateQueryClustersRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCreateQueryClustersRequestData from a JSON string
batch_create_query_clusters_request_data_instance = BatchCreateQueryClustersRequestData.from_json(json)
# print the JSON string representation of the object
print(BatchCreateQueryClustersRequestData.to_json())

# convert the object into a dict
batch_create_query_clusters_request_data_dict = batch_create_query_clusters_request_data_instance.to_dict()
# create an instance of BatchCreateQueryClustersRequestData from a dict
batch_create_query_clusters_request_data_from_dict = BatchCreateQueryClustersRequestData.from_dict(batch_create_query_clusters_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


