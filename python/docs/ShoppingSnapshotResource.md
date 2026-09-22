# ShoppingSnapshotResource

One captured shopping-results page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**project_id** | **UUID** | The project this capture belongs to | 
**tracked_query_id** | **UUID** | The tracked query that was searched | 
**engine** | **str** | The shopping surface that was captured | 
**offers** | [**List[ShoppingOfferResource]**](ShoppingOfferResource.md) | Offers in rank order | 
**captured_at** | **datetime** | When the page was captured, UTC | 

## Example

```python
from mencoro.models.shopping_snapshot_resource import ShoppingSnapshotResource

# TODO update the JSON string below
json = "{}"
# create an instance of ShoppingSnapshotResource from a JSON string
shopping_snapshot_resource_instance = ShoppingSnapshotResource.from_json(json)
# print the JSON string representation of the object
print(ShoppingSnapshotResource.to_json())

# convert the object into a dict
shopping_snapshot_resource_dict = shopping_snapshot_resource_instance.to_dict()
# create an instance of ShoppingSnapshotResource from a dict
shopping_snapshot_resource_from_dict = ShoppingSnapshotResource.from_dict(shopping_snapshot_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


