# BatchChangeTrackedQueryCheckFrequencyRequestData

Tracked queries to retune, and the check frequency to set on them

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** | Ids of the tracked queries to change. Duplicates are collapsed. | 
**check_frequency** | **str** | How often each query is checked while it is active. | 

## Example

```python
from mencoro.models.batch_change_tracked_query_check_frequency_request_data import BatchChangeTrackedQueryCheckFrequencyRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BatchChangeTrackedQueryCheckFrequencyRequestData from a JSON string
batch_change_tracked_query_check_frequency_request_data_instance = BatchChangeTrackedQueryCheckFrequencyRequestData.from_json(json)
# print the JSON string representation of the object
print(BatchChangeTrackedQueryCheckFrequencyRequestData.to_json())

# convert the object into a dict
batch_change_tracked_query_check_frequency_request_data_dict = batch_change_tracked_query_check_frequency_request_data_instance.to_dict()
# create an instance of BatchChangeTrackedQueryCheckFrequencyRequestData from a dict
batch_change_tracked_query_check_frequency_request_data_from_dict = BatchChangeTrackedQueryCheckFrequencyRequestData.from_dict(batch_change_tracked_query_check_frequency_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


