# ChangeMemberRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 

## Example

```python
from mencoro.models.change_member_role_request import ChangeMemberRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeMemberRoleRequest from a JSON string
change_member_role_request_instance = ChangeMemberRoleRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeMemberRoleRequest.to_json())

# convert the object into a dict
change_member_role_request_dict = change_member_role_request_instance.to_dict()
# create an instance of ChangeMemberRoleRequest from a dict
change_member_role_request_from_dict = ChangeMemberRoleRequest.from_dict(change_member_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


