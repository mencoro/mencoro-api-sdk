# ListAiResponses200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AiResponseResource]**](AiResponseResource.md) |  | [optional] 
**total** | **int** | Captures matching the filter, not the size of this page | [optional] 

## Example

```python
from mencoro.models.list_ai_responses200_response import ListAiResponses200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAiResponses200Response from a JSON string
list_ai_responses200_response_instance = ListAiResponses200Response.from_json(json)
# print the JSON string representation of the object
print(ListAiResponses200Response.to_json())

# convert the object into a dict
list_ai_responses200_response_dict = list_ai_responses200_response_instance.to_dict()
# create an instance of ListAiResponses200Response from a dict
list_ai_responses200_response_from_dict = ListAiResponses200Response.from_dict(list_ai_responses200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


