# GetMembershipStats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_members_count** | **int** | Members in the active state. | [optional] 
**suspended_members_count** | **int** | Members in the suspended state. | [optional] 
**total_members_count** | **int** | Every membership record, suspended ones included. | [optional] 
**active_projects_count** | **int** | Projects in the active state. | [optional] 
**total_projects_count** | **int** | Every project, archived ones included. | [optional] 
**pending_invitations_count** | **int** | Invitations still pending and not yet expired. | [optional] 
**computed_at** | **str** | When the snapshot was computed. A database timestamp, not an ISO-8601 instant. | [optional] 

## Example

```python
from mencoro.models.get_membership_stats200_response import GetMembershipStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMembershipStats200Response from a JSON string
get_membership_stats200_response_instance = GetMembershipStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetMembershipStats200Response.to_json())

# convert the object into a dict
get_membership_stats200_response_dict = get_membership_stats200_response_instance.to_dict()
# create an instance of GetMembershipStats200Response from a dict
get_membership_stats200_response_from_dict = GetMembershipStats200Response.from_dict(get_membership_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


