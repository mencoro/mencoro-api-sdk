# ProjectDetailResource

A project and the brand monitoring configuration its checks run against

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**organization_id** | **UUID** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**website_domains** | **List[str]** | Domains the project is monitored for. Empty when the project has no brand monitoring profile yet. | 
**brand_names** | **List[str]** | Brand names matched in AI answers and search results. Empty when the project has no brand monitoring profile yet. | 
**competitors** | [**List[ProjectDetailResourceCompetitorsInner]**](ProjectDetailResourceCompetitorsInner.md) | Competitors this project is measured against. Empty when none are configured. | 

## Example

```python
from mencoro.models.project_detail_resource import ProjectDetailResource

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDetailResource from a JSON string
project_detail_resource_instance = ProjectDetailResource.from_json(json)
# print the JSON string representation of the object
print(ProjectDetailResource.to_json())

# convert the object into a dict
project_detail_resource_dict = project_detail_resource_instance.to_dict()
# create an instance of ProjectDetailResource from a dict
project_detail_resource_from_dict = ProjectDetailResource.from_dict(project_detail_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


