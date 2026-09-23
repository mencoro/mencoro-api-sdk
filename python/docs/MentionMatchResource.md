# MentionMatchResource

A stored mention match; no provider credentials or operational metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracked_query_id** | **UUID** |  | 
**project_id** | **UUID** |  | 
**engine** | **str** |  | 
**ai_response_id** | **UUID** |  | 
**competitor_id** | **UUID** |  | [optional] 
**mention_position** | **int** |  | 
**sentiment** | **str** |  | 
**mention_type** | **str** |  | 
**mention_type_condition** | **str** |  | [optional] 
**response_context** | **str** |  | 
**detected_at** | **datetime** |  | 
**mention_relation** | **str** |  | [optional] 
**brand_name** | **str** |  | [optional] 
**brand_name_as_mentioned** | **str** |  | [optional] 

## Example

```python
from mencoro.models.mention_match_resource import MentionMatchResource

# TODO update the JSON string below
json = "{}"
# create an instance of MentionMatchResource from a JSON string
mention_match_resource_instance = MentionMatchResource.from_json(json)
# print the JSON string representation of the object
print(MentionMatchResource.to_json())

# convert the object into a dict
mention_match_resource_dict = mention_match_resource_instance.to_dict()
# create an instance of MentionMatchResource from a dict
mention_match_resource_from_dict = MentionMatchResource.from_dict(mention_match_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


