# BrandProfileResource

The brand identity a project's checks are matched against

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** | The project this profile belongs to | 
**brand_names** | **List[str]** | The brand terms a mention in an AI answer is matched against. Empty when none has been configured yet. | 
**website_domains** | **List[str]** | The domains a cited link or a search result is matched against. Empty when none has been configured yet. | 
**description** | **str** | What the brand does, as generated from its names and domains. Null means it has not been generated yet, which is not the same as an empty description. | [optional] 

## Example

```python
from mencoro.models.brand_profile_resource import BrandProfileResource

# TODO update the JSON string below
json = "{}"
# create an instance of BrandProfileResource from a JSON string
brand_profile_resource_instance = BrandProfileResource.from_json(json)
# print the JSON string representation of the object
print(BrandProfileResource.to_json())

# convert the object into a dict
brand_profile_resource_dict = brand_profile_resource_instance.to_dict()
# create an instance of BrandProfileResource from a dict
brand_profile_resource_from_dict = BrandProfileResource.from_dict(brand_profile_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


