# CreateProjectRequestCompetitorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**website_domains** | **List[str]** |  | 
**brand_names** | **List[str]** |  | 

## Example

```python
from mencoro.models.create_project_request_competitors_inner import CreateProjectRequestCompetitorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectRequestCompetitorsInner from a JSON string
create_project_request_competitors_inner_instance = CreateProjectRequestCompetitorsInner.from_json(json)
# print the JSON string representation of the object
print(CreateProjectRequestCompetitorsInner.to_json())

# convert the object into a dict
create_project_request_competitors_inner_dict = create_project_request_competitors_inner_instance.to_dict()
# create an instance of CreateProjectRequestCompetitorsInner from a dict
create_project_request_competitors_inner_from_dict = CreateProjectRequestCompetitorsInner.from_dict(create_project_request_competitors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


