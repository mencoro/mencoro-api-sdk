# TrackedQueryDetailResource

A tracked query and how it is checked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**project_id** | **UUID** | The project this tracked query belongs to | 
**query_text** | **str** | The prompt or keyword sent to the engine | 
**engine** | **str** |  | 
**locale** | **str** | Language tag the query is asked in. Null when the engine is asked without one. | [optional] 
**country** | **str** | ISO-3166 alpha-2 country the query is asked from | 
**query_cluster_ids** | **List[UUID]** | Clusters (groups) this query belongs to. Empty when it is ungrouped. | 
**status** | **str** |  | 
**check_frequency** | **str** | How often the query is checked while active | 
**n_passes** | **int** | Passes run per check. Greater than 1 only for AI engines. | 
**last_checked_at** | **datetime** | When a check last completed. Null means no check has completed yet, which is not the same as a check that found nothing. | [optional] 

## Example

```python
from mencoro.models.tracked_query_detail_resource import TrackedQueryDetailResource

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedQueryDetailResource from a JSON string
tracked_query_detail_resource_instance = TrackedQueryDetailResource.from_json(json)
# print the JSON string representation of the object
print(TrackedQueryDetailResource.to_json())

# convert the object into a dict
tracked_query_detail_resource_dict = tracked_query_detail_resource_instance.to_dict()
# create an instance of TrackedQueryDetailResource from a dict
tracked_query_detail_resource_from_dict = TrackedQueryDetailResource.from_dict(tracked_query_detail_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


