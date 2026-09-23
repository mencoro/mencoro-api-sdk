# MentionSampleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tracked_query_id** | **str** |  | 
**ai_response_id** | **str** |  | 
**engine** | **str** |  | 
**competitor_id** | **str** |  | [optional] 
**sentiment** | **str** |  | 
**mention_type** | **str** |  | 
**mention_position** | **int** |  | 
**text** | **str** |  | 
**detected_at** | **str** |  | 
**query_text** | **str** |  | 
**country** | **str** |  | [optional] 
**mention_relation** | **str** | Published because &#x60;competitorId&#x60; alone cannot answer the question. Own-brand AND untracked-competitor mentions both carry a null competitor id - the confusion migration Version20260608130000 was written to end - so a reader that treats a null competitor id as \&quot;us\&quot; silently counts a rival as the brand. | [optional] 
**brand_name** | **str** |  | [optional] 

## Example

```python
from mencoro.models.mention_sample_response import MentionSampleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MentionSampleResponse from a JSON string
mention_sample_response_instance = MentionSampleResponse.from_json(json)
# print the JSON string representation of the object
print(MentionSampleResponse.to_json())

# convert the object into a dict
mention_sample_response_dict = mention_sample_response_instance.to_dict()
# create an instance of MentionSampleResponse from a dict
mention_sample_response_from_dict = MentionSampleResponse.from_dict(mention_sample_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


