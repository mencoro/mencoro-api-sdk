# GetMentionSamples400ResponseDetailsValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**parameters** | **List[str]** | Placeholder values behind the message. Always empty on this API: no rule it enforces carries any. | [optional] 

## Example

```python
from mencoro.models.get_mention_samples400_response_details_value_inner import GetMentionSamples400ResponseDetailsValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMentionSamples400ResponseDetailsValueInner from a JSON string
get_mention_samples400_response_details_value_inner_instance = GetMentionSamples400ResponseDetailsValueInner.from_json(json)
# print the JSON string representation of the object
print(GetMentionSamples400ResponseDetailsValueInner.to_json())

# convert the object into a dict
get_mention_samples400_response_details_value_inner_dict = get_mention_samples400_response_details_value_inner_instance.to_dict()
# create an instance of GetMentionSamples400ResponseDetailsValueInner from a dict
get_mention_samples400_response_details_value_inner_from_dict = GetMentionSamples400ResponseDetailsValueInner.from_dict(get_mention_samples400_response_details_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


