# OrganizationResource

An organization the caller is a member of

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**status** | **str** |  | 
**image_url** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**role** | **str** | The caller&#39;s current role in this organization | 
**created_at** | **datetime** |  | 

## Example

```python
from mencoro.models.organization_resource import OrganizationResource

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationResource from a JSON string
organization_resource_instance = OrganizationResource.from_json(json)
# print the JSON string representation of the object
print(OrganizationResource.to_json())

# convert the object into a dict
organization_resource_dict = organization_resource_instance.to_dict()
# create an instance of OrganizationResource from a dict
organization_resource_from_dict = OrganizationResource.from_dict(organization_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


