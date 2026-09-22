# CreateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**website_domains** | **List[str]** | At least one website URL or domain to monitor. | 
**brand_names** | **List[str]** | At least one brand name to match in AI answers and search results. | 
**competitors** | [**List[CreateProjectRequestCompetitorsInner]**](CreateProjectRequestCompetitorsInner.md) | Competitors to create with the project. Optional; they can also be added later through the competitor endpoints. | [optional] 

## Example

```python
from mencoro.models.create_project_request import CreateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectRequest from a JSON string
create_project_request_instance = CreateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectRequest.to_json())

# convert the object into a dict
create_project_request_dict = create_project_request_instance.to_dict()
# create an instance of CreateProjectRequest from a dict
create_project_request_from_dict = CreateProjectRequest.from_dict(create_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


