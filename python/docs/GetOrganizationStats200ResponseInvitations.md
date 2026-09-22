# GetOrganizationStats200ResponseInvitations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | **int** | Invitations still awaiting an answer. Accepted, cancelled and expired ones are excluded. | [optional] 

## Example

```python
from mencoro.models.get_organization_stats200_response_invitations import GetOrganizationStats200ResponseInvitations

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationStats200ResponseInvitations from a JSON string
get_organization_stats200_response_invitations_instance = GetOrganizationStats200ResponseInvitations.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationStats200ResponseInvitations.to_json())

# convert the object into a dict
get_organization_stats200_response_invitations_dict = get_organization_stats200_response_invitations_instance.to_dict()
# create an instance of GetOrganizationStats200ResponseInvitations from a dict
get_organization_stats200_response_invitations_from_dict = GetOrganizationStats200ResponseInvitations.from_dict(get_organization_stats200_response_invitations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


