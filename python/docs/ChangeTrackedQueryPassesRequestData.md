# ChangeTrackedQueryPassesRequestData

How many passes a tracked query runs per check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n_passes** | **int** | Passes run per check. Only an AI engine accepts more than one. | 

## Example

```python
from mencoro.models.change_tracked_query_passes_request_data import ChangeTrackedQueryPassesRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeTrackedQueryPassesRequestData from a JSON string
change_tracked_query_passes_request_data_instance = ChangeTrackedQueryPassesRequestData.from_json(json)
# print the JSON string representation of the object
print(ChangeTrackedQueryPassesRequestData.to_json())

# convert the object into a dict
change_tracked_query_passes_request_data_dict = change_tracked_query_passes_request_data_instance.to_dict()
# create an instance of ChangeTrackedQueryPassesRequestData from a dict
change_tracked_query_passes_request_data_from_dict = ChangeTrackedQueryPassesRequestData.from_dict(change_tracked_query_passes_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


