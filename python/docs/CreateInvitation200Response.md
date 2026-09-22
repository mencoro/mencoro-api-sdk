# CreateInvitation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **bool** | Always false on a 200. | [optional] 
**reason** | **str** | Why nothing was created. | [optional] 
**email** | **str** | The address as it was normalised. | [optional] 

## Example

```python
from mencoro.models.create_invitation200_response import CreateInvitation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvitation200Response from a JSON string
create_invitation200_response_instance = CreateInvitation200Response.from_json(json)
# print the JSON string representation of the object
print(CreateInvitation200Response.to_json())

# convert the object into a dict
create_invitation200_response_dict = create_invitation200_response_instance.to_dict()
# create an instance of CreateInvitation200Response from a dict
create_invitation200_response_from_dict = CreateInvitation200Response.from_dict(create_invitation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


