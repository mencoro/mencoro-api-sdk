# BatchWriteOutcomeFailedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**error_code** | **str** | The same code a single-item call returns for this problem. | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from mencoro.models.batch_write_outcome_failed_inner import BatchWriteOutcomeFailedInner

# TODO update the JSON string below
json = "{}"
# create an instance of BatchWriteOutcomeFailedInner from a JSON string
batch_write_outcome_failed_inner_instance = BatchWriteOutcomeFailedInner.from_json(json)
# print the JSON string representation of the object
print(BatchWriteOutcomeFailedInner.to_json())

# convert the object into a dict
batch_write_outcome_failed_inner_dict = batch_write_outcome_failed_inner_instance.to_dict()
# create an instance of BatchWriteOutcomeFailedInner from a dict
batch_write_outcome_failed_inner_from_dict = BatchWriteOutcomeFailedInner.from_dict(batch_write_outcome_failed_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


