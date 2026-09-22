# ListSearchSnapshots200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SearchSnapshotResource]**](SearchSnapshotResource.md) |  | [optional] 
**total** | **int** | Captures matching the filter, not the size of this page | [optional] 

## Example

```python
from mencoro.models.list_search_snapshots200_response import ListSearchSnapshots200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSearchSnapshots200Response from a JSON string
list_search_snapshots200_response_instance = ListSearchSnapshots200Response.from_json(json)
# print the JSON string representation of the object
print(ListSearchSnapshots200Response.to_json())

# convert the object into a dict
list_search_snapshots200_response_dict = list_search_snapshots200_response_instance.to_dict()
# create an instance of ListSearchSnapshots200Response from a dict
list_search_snapshots200_response_from_dict = ListSearchSnapshots200Response.from_dict(list_search_snapshots200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


