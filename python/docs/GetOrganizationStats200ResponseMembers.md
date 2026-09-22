# GetOrganizationStats200ResponseMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Active memberships. Suspended members are excluded. | [optional] 

## Example

```python
from mencoro.models.get_organization_stats200_response_members import GetOrganizationStats200ResponseMembers

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationStats200ResponseMembers from a JSON string
get_organization_stats200_response_members_instance = GetOrganizationStats200ResponseMembers.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationStats200ResponseMembers.to_json())

# convert the object into a dict
get_organization_stats200_response_members_dict = get_organization_stats200_response_members_instance.to_dict()
# create an instance of GetOrganizationStats200ResponseMembers from a dict
get_organization_stats200_response_members_from_dict = GetOrganizationStats200ResponseMembers.from_dict(get_organization_stats200_response_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


