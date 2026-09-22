# GetMetricGlossary200ResponseMetricsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**unit** | **str** |  | [optional] 
**range** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**operation** | **str** | The operationId that returns this metric | [optional] 
**example_questions** | **List[str]** |  | [optional] 

## Example

```python
from mencoro.models.get_metric_glossary200_response_metrics_inner import GetMetricGlossary200ResponseMetricsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricGlossary200ResponseMetricsInner from a JSON string
get_metric_glossary200_response_metrics_inner_instance = GetMetricGlossary200ResponseMetricsInner.from_json(json)
# print the JSON string representation of the object
print(GetMetricGlossary200ResponseMetricsInner.to_json())

# convert the object into a dict
get_metric_glossary200_response_metrics_inner_dict = get_metric_glossary200_response_metrics_inner_instance.to_dict()
# create an instance of GetMetricGlossary200ResponseMetricsInner from a dict
get_metric_glossary200_response_metrics_inner_from_dict = GetMetricGlossary200ResponseMetricsInner.from_dict(get_metric_glossary200_response_metrics_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


