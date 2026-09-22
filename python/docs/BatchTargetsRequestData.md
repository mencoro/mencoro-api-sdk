# BatchTargetsRequestData

The resources a batch operation acts on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** | Ids of the resources to act on. Duplicates are collapsed. | 

## Example

```python
from mencoro.models.batch_targets_request_data import BatchTargetsRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTargetsRequestData from a JSON string
batch_targets_request_data_instance = BatchTargetsRequestData.from_json(json)
# print the JSON string representation of the object
print(BatchTargetsRequestData.to_json())

# convert the object into a dict
batch_targets_request_data_dict = batch_targets_request_data_instance.to_dict()
# create an instance of BatchTargetsRequestData from a dict
batch_targets_request_data_from_dict = BatchTargetsRequestData.from_dict(batch_targets_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


