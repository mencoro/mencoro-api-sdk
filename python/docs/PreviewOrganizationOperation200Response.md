# PreviewOrganizationOperation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**organization** | [**PreviewOrganizationOperation200ResponseOrganization**](PreviewOrganizationOperation200ResponseOrganization.md) |  | [optional] 
**resource_id** | **UUID** | The member or invitation the action acts on; null for the actions that name none. | [optional] 
**changes** | [**List[OperationEffect]**](OperationEffect.md) | What the operation itself will do. | [optional] 
**side_effects** | [**List[OperationEffect]**](OperationEffect.md) | What else it will cause, with the records it will touch in &#x60;targets&#x60;. | [optional] 
**warnings** | [**List[OperationEffect]**](OperationEffect.md) | How the system behaves around it. Not part of the effects digest: rewording one does not invalidate a confirmation. | [optional] 
**conditions** | [**List[OperationEffect]**](OperationEffect.md) | What must hold for the operation to be allowed. | [optional] 
**actor** | **object** | Who the confirmation is issued to: the user and the API key. It is valid for that pair only. | [optional] 
**confirmation** | **object** | The token to send back, the header to send it in, and how long it lives. | [optional] 

## Example

```python
from mencoro.models.preview_organization_operation200_response import PreviewOrganizationOperation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewOrganizationOperation200Response from a JSON string
preview_organization_operation200_response_instance = PreviewOrganizationOperation200Response.from_json(json)
# print the JSON string representation of the object
print(PreviewOrganizationOperation200Response.to_json())

# convert the object into a dict
preview_organization_operation200_response_dict = preview_organization_operation200_response_instance.to_dict()
# create an instance of PreviewOrganizationOperation200Response from a dict
preview_organization_operation200_response_from_dict = PreviewOrganizationOperation200Response.from_dict(preview_organization_operation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


