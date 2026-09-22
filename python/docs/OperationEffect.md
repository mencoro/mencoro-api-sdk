# OperationEffect

A single declared change, side effect, warning or condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Stable machine-readable identifier for this effect | 
**summary** | **str** | Human-readable description, safe to show to whoever must approve the operation | 
**targets** | **List[str]** |  | [optional] [default to []]

## Example

```python
from mencoro.models.operation_effect import OperationEffect

# TODO update the JSON string below
json = "{}"
# create an instance of OperationEffect from a JSON string
operation_effect_instance = OperationEffect.from_json(json)
# print the JSON string representation of the object
print(OperationEffect.to_json())

# convert the object into a dict
operation_effect_dict = operation_effect_instance.to_dict()
# create an instance of OperationEffect from a dict
operation_effect_from_dict = OperationEffect.from_dict(operation_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


