# ListInvitations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[InvitationResource]**](InvitationResource.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mencoro.models.list_invitations200_response import ListInvitations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvitations200Response from a JSON string
list_invitations200_response_instance = ListInvitations200Response.from_json(json)
# print the JSON string representation of the object
print(ListInvitations200Response.to_json())

# convert the object into a dict
list_invitations200_response_dict = list_invitations200_response_instance.to_dict()
# create an instance of ListInvitations200Response from a dict
list_invitations200_response_from_dict = ListInvitations200Response.from_dict(list_invitations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


