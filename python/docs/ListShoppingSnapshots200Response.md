# ListShoppingSnapshots200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ShoppingSnapshotResource]**](ShoppingSnapshotResource.md) |  | [optional] 
**total** | **int** | Captures matching the filter, not the size of this page | [optional] 

## Example

```python
from mencoro.models.list_shopping_snapshots200_response import ListShoppingSnapshots200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListShoppingSnapshots200Response from a JSON string
list_shopping_snapshots200_response_instance = ListShoppingSnapshots200Response.from_json(json)
# print the JSON string representation of the object
print(ListShoppingSnapshots200Response.to_json())

# convert the object into a dict
list_shopping_snapshots200_response_dict = list_shopping_snapshots200_response_instance.to_dict()
# create an instance of ListShoppingSnapshots200Response from a dict
list_shopping_snapshots200_response_from_dict = ListShoppingSnapshots200Response.from_dict(list_shopping_snapshots200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


