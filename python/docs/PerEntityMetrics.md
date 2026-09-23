# PerEntityMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serp** | **float** |  | [optional] 
**shopping** | **float** |  | [optional] 
**mention** | **float** |  | [optional] 
**link** | **float** |  | [optional] 
**positivity** | **int** |  | [optional] 
**share_of_voice** | **float** |  | [optional] 
**mention_rate** | **int** |  | [optional] 
**serp_rate** | **int** |  | [optional] 

## Example

```python
from mencoro.models.per_entity_metrics import PerEntityMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of PerEntityMetrics from a JSON string
per_entity_metrics_instance = PerEntityMetrics.from_json(json)
# print the JSON string representation of the object
print(PerEntityMetrics.to_json())

# convert the object into a dict
per_entity_metrics_dict = per_entity_metrics_instance.to_dict()
# create an instance of PerEntityMetrics from a dict
per_entity_metrics_from_dict = PerEntityMetrics.from_dict(per_entity_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


