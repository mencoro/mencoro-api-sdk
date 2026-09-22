# BatchChangeTrackedQueryPassesRequestData

Tracked queries to retune, and the passes per check to set on them

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** | Ids of the tracked queries to change. Duplicates are collapsed. | 
**n_passes** | **int** | Passes run per check. Only an AI engine accepts more than one; a non-AI target is reported under \&quot;failed\&quot;. | 

## Example

```python
from mencoro.models.batch_change_tracked_query_passes_request_data import BatchChangeTrackedQueryPassesRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BatchChangeTrackedQueryPassesRequestData from a JSON string
batch_change_tracked_query_passes_request_data_instance = BatchChangeTrackedQueryPassesRequestData.from_json(json)
# print the JSON string representation of the object
print(BatchChangeTrackedQueryPassesRequestData.to_json())

# convert the object into a dict
batch_change_tracked_query_passes_request_data_dict = batch_change_tracked_query_passes_request_data_instance.to_dict()
# create an instance of BatchChangeTrackedQueryPassesRequestData from a dict
batch_change_tracked_query_passes_request_data_from_dict = BatchChangeTrackedQueryPassesRequestData.from_dict(batch_change_tracked_query_passes_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


