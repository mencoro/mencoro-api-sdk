# ProjectMentionMixResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by_type** | **Dict[str, int]** |  | 
**by_tone** | **Dict[str, int]** |  | 
**by_qualifier** | **Dict[str, int]** |  | 

## Example

```python
from mencoro.models.project_mention_mix_response import ProjectMentionMixResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMentionMixResponse from a JSON string
project_mention_mix_response_instance = ProjectMentionMixResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectMentionMixResponse.to_json())

# convert the object into a dict
project_mention_mix_response_dict = project_mention_mix_response_instance.to_dict()
# create an instance of ProjectMentionMixResponse from a dict
project_mention_mix_response_from_dict = ProjectMentionMixResponse.from_dict(project_mention_mix_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


