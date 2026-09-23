# CompetitorShareOfVoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competitor_id** | **str** |  | 
**share_of_voice** | **float** |  | [optional] 

## Example

```python
from mencoro.models.competitor_share_of_voice import CompetitorShareOfVoice

# TODO update the JSON string below
json = "{}"
# create an instance of CompetitorShareOfVoice from a JSON string
competitor_share_of_voice_instance = CompetitorShareOfVoice.from_json(json)
# print the JSON string representation of the object
print(CompetitorShareOfVoice.to_json())

# convert the object into a dict
competitor_share_of_voice_dict = competitor_share_of_voice_instance.to_dict()
# create an instance of CompetitorShareOfVoice from a dict
competitor_share_of_voice_from_dict = CompetitorShareOfVoice.from_dict(competitor_share_of_voice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


