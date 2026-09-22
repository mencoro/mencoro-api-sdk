# ChangeTrackedQueryCheckFrequencyRequestData

How often a tracked query is checked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_frequency** | **str** | How often the query is checked while it is active. | 

## Example

```python
from mencoro.models.change_tracked_query_check_frequency_request_data import ChangeTrackedQueryCheckFrequencyRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeTrackedQueryCheckFrequencyRequestData from a JSON string
change_tracked_query_check_frequency_request_data_instance = ChangeTrackedQueryCheckFrequencyRequestData.from_json(json)
# print the JSON string representation of the object
print(ChangeTrackedQueryCheckFrequencyRequestData.to_json())

# convert the object into a dict
change_tracked_query_check_frequency_request_data_dict = change_tracked_query_check_frequency_request_data_instance.to_dict()
# create an instance of ChangeTrackedQueryCheckFrequencyRequestData from a dict
change_tracked_query_check_frequency_request_data_from_dict = ChangeTrackedQueryCheckFrequencyRequestData.from_dict(change_tracked_query_check_frequency_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


