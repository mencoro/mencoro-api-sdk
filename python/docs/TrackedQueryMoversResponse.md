# TrackedQueryMoversResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[TrackedQueryMoverRow]**](TrackedQueryMoverRow.md) |  | 
**total** | **int** |  | 
**data_dirty_since** | **str** |  | [optional] 

## Example

```python
from mencoro.models.tracked_query_movers_response import TrackedQueryMoversResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedQueryMoversResponse from a JSON string
tracked_query_movers_response_instance = TrackedQueryMoversResponse.from_json(json)
# print the JSON string representation of the object
print(TrackedQueryMoversResponse.to_json())

# convert the object into a dict
tracked_query_movers_response_dict = tracked_query_movers_response_instance.to_dict()
# create an instance of TrackedQueryMoversResponse from a dict
tracked_query_movers_response_from_dict = TrackedQueryMoversResponse.from_dict(tracked_query_movers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


