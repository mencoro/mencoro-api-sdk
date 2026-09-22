# GetMeStats200ResponseProjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Projects across those organizations, archived ones included. | [optional] 
**active** | **int** | How many of those are active; the remainder are archived. | [optional] 

## Example

```python
from mencoro.models.get_me_stats200_response_projects import GetMeStats200ResponseProjects

# TODO update the JSON string below
json = "{}"
# create an instance of GetMeStats200ResponseProjects from a JSON string
get_me_stats200_response_projects_instance = GetMeStats200ResponseProjects.from_json(json)
# print the JSON string representation of the object
print(GetMeStats200ResponseProjects.to_json())

# convert the object into a dict
get_me_stats200_response_projects_dict = get_me_stats200_response_projects_instance.to_dict()
# create an instance of GetMeStats200ResponseProjects from a dict
get_me_stats200_response_projects_from_dict = GetMeStats200ResponseProjects.from_dict(get_me_stats200_response_projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


