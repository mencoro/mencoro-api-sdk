# CreateInvitationRequestProjectAccess

Which projects of the organization the invitee reaches once they accept. Omitted or null, they reach every project. An owner always reaches every project, so an owner invitation cannot carry a selection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**project_ids** | **List[UUID]** | For selected: at least one and at most 500 projects of the organization. | [optional] 

## Example

```python
from mencoro.models.create_invitation_request_project_access import CreateInvitationRequestProjectAccess

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvitationRequestProjectAccess from a JSON string
create_invitation_request_project_access_instance = CreateInvitationRequestProjectAccess.from_json(json)
# print the JSON string representation of the object
print(CreateInvitationRequestProjectAccess.to_json())

# convert the object into a dict
create_invitation_request_project_access_dict = create_invitation_request_project_access_instance.to_dict()
# create an instance of CreateInvitationRequestProjectAccess from a dict
create_invitation_request_project_access_from_dict = CreateInvitationRequestProjectAccess.from_dict(create_invitation_request_project_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


