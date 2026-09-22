# AiResponseResource

One captured AI answer with its citations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**project_id** | **UUID** | The project this capture belongs to | 
**tracked_query_id** | **UUID** | The tracked query that was asked | 
**engine** | **str** | The AI engine that answered | 
**response_text** | **str** | The full answer text as the engine produced it | 
**citations** | [**List[CitationResource]**](CitationResource.md) | Sources the engine cited, in the order it cited them | 
**captured_at** | **datetime** | When the answer was captured, UTC | 
**model_name** | **str** | Engine-reported model, when it reported one. Absent on captures taken before engines exposed it | [optional] 
**pass_index** | **int** | Which sampling pass of the run this answer is, starting at 0 | 
**pass_count** | **int** | How many passes that run took. Rows of one run share trackedQueryId and capturedAt | 

## Example

```python
from mencoro.models.ai_response_resource import AiResponseResource

# TODO update the JSON string below
json = "{}"
# create an instance of AiResponseResource from a JSON string
ai_response_resource_instance = AiResponseResource.from_json(json)
# print the JSON string representation of the object
print(AiResponseResource.to_json())

# convert the object into a dict
ai_response_resource_dict = ai_response_resource_instance.to_dict()
# create an instance of AiResponseResource from a dict
ai_response_resource_from_dict = AiResponseResource.from_dict(ai_response_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


