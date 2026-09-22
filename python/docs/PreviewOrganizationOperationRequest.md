# PreviewOrganizationOperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**organization_id** | **UUID** | Required for every action except createOrganization. | [optional] 
**resource_id** | **UUID** | The member or invitation the action acts on, for the actions that name one. | [optional] 
**payload** | **object** | The body you intend to send to the operation itself. | [optional] 

## Example

```python
from mencoro.models.preview_organization_operation_request import PreviewOrganizationOperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewOrganizationOperationRequest from a JSON string
preview_organization_operation_request_instance = PreviewOrganizationOperationRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewOrganizationOperationRequest.to_json())

# convert the object into a dict
preview_organization_operation_request_dict = preview_organization_operation_request_instance.to_dict()
# create an instance of PreviewOrganizationOperationRequest from a dict
preview_organization_operation_request_from_dict = PreviewOrganizationOperationRequest.from_dict(preview_organization_operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


