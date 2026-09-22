# SearchSnapshotResource

One captured search-results page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**project_id** | **UUID** | The project this capture belongs to | 
**tracked_query_id** | **UUID** | The tracked query that was searched | 
**engine** | **str** | The search engine that was captured | 
**results** | [**List[SearchResultResource]**](SearchResultResource.md) | Organic results in rank order | 
**captured_at** | **datetime** | When the page was captured, UTC | 

## Example

```python
from mencoro.models.search_snapshot_resource import SearchSnapshotResource

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSnapshotResource from a JSON string
search_snapshot_resource_instance = SearchSnapshotResource.from_json(json)
# print the JSON string representation of the object
print(SearchSnapshotResource.to_json())

# convert the object into a dict
search_snapshot_resource_dict = search_snapshot_resource_instance.to_dict()
# create an instance of SearchSnapshotResource from a dict
search_snapshot_resource_from_dict = SearchSnapshotResource.from_dict(search_snapshot_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


