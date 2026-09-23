# SerpMatchResource

A stored serp match; no provider credentials or operational metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracked_query_id** | **UUID** |  | 
**project_id** | **UUID** |  | 
**engine** | **str** |  | 
**search_page_id** | **UUID** |  | 
**competitor_id** | **UUID** |  | [optional] 
**position** | **int** |  | 
**detected_at** | **datetime** |  | 

## Example

```python
from mencoro.models.serp_match_resource import SerpMatchResource

# TODO update the JSON string below
json = "{}"
# create an instance of SerpMatchResource from a JSON string
serp_match_resource_instance = SerpMatchResource.from_json(json)
# print the JSON string representation of the object
print(SerpMatchResource.to_json())

# convert the object into a dict
serp_match_resource_dict = serp_match_resource_instance.to_dict()
# create an instance of SerpMatchResource from a dict
serp_match_resource_from_dict = SerpMatchResource.from_dict(serp_match_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


