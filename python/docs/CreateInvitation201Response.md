# CreateInvitation201Response


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
**created** | **bool** | Always true on a 201. | [optional] 

## Example

```python
from mencoro.models.create_invitation201_response import CreateInvitation201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvitation201Response from a JSON string
create_invitation201_response_instance = CreateInvitation201Response.from_json(json)
# print the JSON string representation of the object
print(CreateInvitation201Response.to_json())

# convert the object into a dict
create_invitation201_response_dict = create_invitation201_response_instance.to_dict()
# create an instance of CreateInvitation201Response from a dict
create_invitation201_response_from_dict = CreateInvitation201Response.from_dict(create_invitation201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


