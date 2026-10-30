# SetMemberProjectAccessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**project_ids** | **List[UUID]** | The projects of the organization a selected access reaches: at least one and at most 500. Omit it, or send an empty list, for all. | [optional] 

## Example

```python
from mencoro.models.set_member_project_access_request import SetMemberProjectAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetMemberProjectAccessRequest from a JSON string
set_member_project_access_request_instance = SetMemberProjectAccessRequest.from_json(json)
# print the JSON string representation of the object
print(SetMemberProjectAccessRequest.to_json())

# convert the object into a dict
set_member_project_access_request_dict = set_member_project_access_request_instance.to_dict()
# create an instance of SetMemberProjectAccessRequest from a dict
set_member_project_access_request_from_dict = SetMemberProjectAccessRequest.from_dict(set_member_project_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


