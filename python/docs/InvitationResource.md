# InvitationResource

An invitation to join an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**email** | **str** |  | 
**role** | **str** |  | 
**state** | **str** |  | 
**created_at** | **datetime** |  | 
**expires_at** | **datetime** |  | 
**accepted_at** | **datetime** |  | [optional] 
**project_access_mode** | **str** | Which projects of the organization the invitee reaches on accepting: every project, or only projectIds | 
**project_ids** | **List[UUID]** | The projects a selected access reaches, limited to those still in the organization; empty when the mode is all. It may be empty on selected once its projects left the organization, which grants nothing | 

## Example

```python
from mencoro.models.invitation_resource import InvitationResource

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationResource from a JSON string
invitation_resource_instance = InvitationResource.from_json(json)
# print the JSON string representation of the object
print(InvitationResource.to_json())

# convert the object into a dict
invitation_resource_dict = invitation_resource_instance.to_dict()
# create an instance of InvitationResource from a dict
invitation_resource_from_dict = InvitationResource.from_dict(invitation_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


