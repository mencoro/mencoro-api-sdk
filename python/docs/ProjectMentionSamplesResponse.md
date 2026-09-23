# ProjectMentionSamplesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**samples** | [**List[MentionSampleResponse]**](MentionSampleResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from mencoro.models.project_mention_samples_response import ProjectMentionSamplesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMentionSamplesResponse from a JSON string
project_mention_samples_response_instance = ProjectMentionSamplesResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectMentionSamplesResponse.to_json())

# convert the object into a dict
project_mention_samples_response_dict = project_mention_samples_response_instance.to_dict()
# create an instance of ProjectMentionSamplesResponse from a dict
project_mention_samples_response_from_dict = ProjectMentionSamplesResponse.from_dict(project_mention_samples_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


