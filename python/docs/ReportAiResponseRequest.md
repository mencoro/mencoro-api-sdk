# ReportAiResponseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | What is wrong with the capture. | 
**comment** | **str** | Optional note for the reviewer, at most 1000 characters. An empty string is stored as no comment. | [optional] 
**missed_brand_names** | **List[str]** | Brands the engine mentioned that the pipeline did not record. Most useful with type \&quot;missed_mention\&quot;; accepted with either. At most 50 distinct names of 255 characters each. | [optional] 

## Example

```python
from mencoro.models.report_ai_response_request import ReportAiResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportAiResponseRequest from a JSON string
report_ai_response_request_instance = ReportAiResponseRequest.from_json(json)
# print the JSON string representation of the object
print(ReportAiResponseRequest.to_json())

# convert the object into a dict
report_ai_response_request_dict = report_ai_response_request_instance.to_dict()
# create an instance of ReportAiResponseRequest from a dict
report_ai_response_request_from_dict = ReportAiResponseRequest.from_dict(report_ai_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


