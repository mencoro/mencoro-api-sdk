# AiResponseReportResource

Acknowledgement of a report about a captured AI answer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_response_id** | **UUID** | The captured AI answer the report is about | 
**tracked_query_id** | **UUID** | The tracked query that answer was captured for | 
**type** | **str** | The kind of problem reported | 
**comment** | **str** | The note as stored. An empty or whitespace-only comment is stored as null. | [optional] 
**missed_brand_names** | **List[str]** | Brand names reported as missed, de-duplicated and trimmed. | 
**accepted** | **bool** | True once the report has been accepted for review. It is never false: a report that could not be delivered answers with an error instead. | 

## Example

```python
from mencoro.models.ai_response_report_resource import AiResponseReportResource

# TODO update the JSON string below
json = "{}"
# create an instance of AiResponseReportResource from a JSON string
ai_response_report_resource_instance = AiResponseReportResource.from_json(json)
# print the JSON string representation of the object
print(AiResponseReportResource.to_json())

# convert the object into a dict
ai_response_report_resource_dict = ai_response_report_resource_instance.to_dict()
# create an instance of AiResponseReportResource from a dict
ai_response_report_resource_from_dict = AiResponseReportResource.from_dict(ai_response_report_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


