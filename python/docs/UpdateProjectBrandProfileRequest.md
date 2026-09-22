# UpdateProjectBrandProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website_domains** | **List[str]** | Domains a cited link or a search result is matched against. A full URL or a bare host. | [optional] 
**brand_names** | **List[str]** | Terms a mention in an AI answer is matched against. | [optional] 

## Example

```python
from mencoro.models.update_project_brand_profile_request import UpdateProjectBrandProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectBrandProfileRequest from a JSON string
update_project_brand_profile_request_instance = UpdateProjectBrandProfileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectBrandProfileRequest.to_json())

# convert the object into a dict
update_project_brand_profile_request_dict = update_project_brand_profile_request_instance.to_dict()
# create an instance of UpdateProjectBrandProfileRequest from a dict
update_project_brand_profile_request_from_dict = UpdateProjectBrandProfileRequest.from_dict(update_project_brand_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


