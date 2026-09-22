# MeResource

The authenticated user and the API key the request was made with

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** |  | 
**full_name** | **str** |  | 
**email** | **str** |  | 
**language** | **str** | IETF language tag the user reads the product in | 
**created_at** | **datetime** |  | 
**api_key_id** | **UUID** | The API key this request authenticated with | 
**capabilities** | **List[str]** |  | 
**scope_mode** | **str** |  | 
**organization_ids** | **List[UUID]** | Organizations the key names. Empty for a key scoped to all organizations, which instead follows the owner&#39;s membership. | 

## Example

```python
from mencoro.models.me_resource import MeResource

# TODO update the JSON string below
json = "{}"
# create an instance of MeResource from a JSON string
me_resource_instance = MeResource.from_json(json)
# print the JSON string representation of the object
print(MeResource.to_json())

# convert the object into a dict
me_resource_dict = me_resource_instance.to_dict()
# create an instance of MeResource from a dict
me_resource_from_dict = MeResource.from_dict(me_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


