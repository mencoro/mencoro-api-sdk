# GetShareOfVoiceFormula200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mention_type_weights** | **Dict[str, float]** | Base weight per mention type; higher means a structurally stronger brand association. | [optional] 
**sentiment_multipliers** | **Dict[str, float]** | Multiplier per tone, applied on top of the base weight. | [optional] 
**direct_multiplier** | **float** | Applied when the mention carries no condition. | [optional] 
**conditional_multiplier** | **float** | Applied instead when the answer hedged the mention with a condition. | [optional] 

## Example

```python
from mencoro.models.get_share_of_voice_formula200_response import GetShareOfVoiceFormula200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetShareOfVoiceFormula200Response from a JSON string
get_share_of_voice_formula200_response_instance = GetShareOfVoiceFormula200Response.from_json(json)
# print the JSON string representation of the object
print(GetShareOfVoiceFormula200Response.to_json())

# convert the object into a dict
get_share_of_voice_formula200_response_dict = get_share_of_voice_formula200_response_instance.to_dict()
# create an instance of GetShareOfVoiceFormula200Response from a dict
get_share_of_voice_formula200_response_from_dict = GetShareOfVoiceFormula200Response.from_dict(get_share_of_voice_formula200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


