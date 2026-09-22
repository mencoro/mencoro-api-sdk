# GetOrganizationStats200ResponseProjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Every project in the organization, archived ones included. | [optional] 
**active** | **int** | Projects that are not archived; never greater than &#x60;total&#x60;. | [optional] 

## Example

```python
from mencoro.models.get_organization_stats200_response_projects import GetOrganizationStats200ResponseProjects

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationStats200ResponseProjects from a JSON string
get_organization_stats200_response_projects_instance = GetOrganizationStats200ResponseProjects.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationStats200ResponseProjects.to_json())

# convert the object into a dict
get_organization_stats200_response_projects_dict = get_organization_stats200_response_projects_instance.to_dict()
# create an instance of GetOrganizationStats200ResponseProjects from a dict
get_organization_stats200_response_projects_from_dict = GetOrganizationStats200ResponseProjects.from_dict(get_organization_stats200_response_projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


