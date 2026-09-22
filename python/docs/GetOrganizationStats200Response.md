# GetOrganizationStats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**GetOrganizationStats200ResponseMembers**](GetOrganizationStats200ResponseMembers.md) |  | [optional] 
**projects** | [**GetOrganizationStats200ResponseProjects**](GetOrganizationStats200ResponseProjects.md) |  | [optional] 
**invitations** | [**GetOrganizationStats200ResponseInvitations**](GetOrganizationStats200ResponseInvitations.md) |  | [optional] 

## Example

```python
from mencoro.models.get_organization_stats200_response import GetOrganizationStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationStats200Response from a JSON string
get_organization_stats200_response_instance = GetOrganizationStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationStats200Response.to_json())

# convert the object into a dict
get_organization_stats200_response_dict = get_organization_stats200_response_instance.to_dict()
# create an instance of GetOrganizationStats200Response from a dict
get_organization_stats200_response_from_dict = GetOrganizationStats200Response.from_dict(get_organization_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


