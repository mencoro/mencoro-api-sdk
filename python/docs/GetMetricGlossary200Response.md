# GetMetricGlossary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[GetMetricGlossary200ResponseMetricsInner]**](GetMetricGlossary200ResponseMetricsInner.md) |  | [optional] 

## Example

```python
from mencoro.models.get_metric_glossary200_response import GetMetricGlossary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricGlossary200Response from a JSON string
get_metric_glossary200_response_instance = GetMetricGlossary200Response.from_json(json)
# print the JSON string representation of the object
print(GetMetricGlossary200Response.to_json())

# convert the object into a dict
get_metric_glossary200_response_dict = get_metric_glossary200_response_instance.to_dict()
# create an instance of GetMetricGlossary200Response from a dict
get_metric_glossary200_response_from_dict = GetMetricGlossary200Response.from_dict(get_metric_glossary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


