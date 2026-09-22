# ProjectDetailResourceCompetitorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**website_domains** | **List[str]** |  | [optional] 
**brand_names** | **List[str]** |  | [optional] 

## Example

```python
from mencoro.models.project_detail_resource_competitors_inner import ProjectDetailResourceCompetitorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDetailResourceCompetitorsInner from a JSON string
project_detail_resource_competitors_inner_instance = ProjectDetailResourceCompetitorsInner.from_json(json)
# print the JSON string representation of the object
print(ProjectDetailResourceCompetitorsInner.to_json())

# convert the object into a dict
project_detail_resource_competitors_inner_dict = project_detail_resource_competitors_inner_instance.to_dict()
# create an instance of ProjectDetailResourceCompetitorsInner from a dict
project_detail_resource_competitors_inner_from_dict = ProjectDetailResourceCompetitorsInner.from_dict(project_detail_resource_competitors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


