# MemberResource

A membership of an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**user_id** | **UUID** | The user this membership belongs to | 
**role** | **str** |  | 
**state** | **str** |  | 
**is_active** | **bool** |  | 
**joined_at** | **datetime** |  | 

## Example

```python
from mencoro.models.member_resource import MemberResource

# TODO update the JSON string below
json = "{}"
# create an instance of MemberResource from a JSON string
member_resource_instance = MemberResource.from_json(json)
# print the JSON string representation of the object
print(MemberResource.to_json())

# convert the object into a dict
member_resource_dict = member_resource_instance.to_dict()
# create an instance of MemberResource from a dict
member_resource_from_dict = MemberResource.from_dict(member_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


