# PreviewOrganizationOperation200ResponseOrganization

The organization the operation acts on. For createOrganization there is none yet, so `id` is null and `name` carries the name you proposed — the preview shows what you are about to create rather than hiding it. Branch on `organization.id`, never on `organization` itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from mencoro.models.preview_organization_operation200_response_organization import PreviewOrganizationOperation200ResponseOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewOrganizationOperation200ResponseOrganization from a JSON string
preview_organization_operation200_response_organization_instance = PreviewOrganizationOperation200ResponseOrganization.from_json(json)
# print the JSON string representation of the object
print(PreviewOrganizationOperation200ResponseOrganization.to_json())

# convert the object into a dict
preview_organization_operation200_response_organization_dict = preview_organization_operation200_response_organization_instance.to_dict()
# create an instance of PreviewOrganizationOperation200ResponseOrganization from a dict
preview_organization_operation200_response_organization_from_dict = PreviewOrganizationOperation200ResponseOrganization.from_dict(preview_organization_operation200_response_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


