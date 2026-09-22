# BatchWriteOutcome

Per-item results of a batch write

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**List[BatchPauseTrackedQueries200ResponseSuccessfulInner]**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | The resources the operation was applied to. | [optional] 
**failed** | [**List[BatchWriteOutcomeFailedInner]**](BatchWriteOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 

## Example

```python
from mencoro.models.batch_write_outcome import BatchWriteOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of BatchWriteOutcome from a JSON string
batch_write_outcome_instance = BatchWriteOutcome.from_json(json)
# print the JSON string representation of the object
print(BatchWriteOutcome.to_json())

# convert the object into a dict
batch_write_outcome_dict = batch_write_outcome_instance.to_dict()
# create an instance of BatchWriteOutcome from a dict
batch_write_outcome_from_dict = BatchWriteOutcome.from_dict(batch_write_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


