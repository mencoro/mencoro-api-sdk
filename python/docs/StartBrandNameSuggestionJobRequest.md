# StartBrandNameSuggestionJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name of the entity to find aliases for. | 
**website_domains** | **List[str]** | The entity website domains. At least one is required: the web search is grounded on them, and without one the name alone is ambiguous. Duplicates are collapsed, after the entry count has been checked against maxItems. | 
**entered_brand_names** | **List[str]** | Names already known, excluded from the suggestions. Duplicates are collapsed, after the entry count has been checked against maxItems. | [optional] 
**country** | **str** | ISO 3166-1 alpha-2 country used to localize the web search. | [optional] 

## Example

```python
from mencoro.models.start_brand_name_suggestion_job_request import StartBrandNameSuggestionJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartBrandNameSuggestionJobRequest from a JSON string
start_brand_name_suggestion_job_request_instance = StartBrandNameSuggestionJobRequest.from_json(json)
# print the JSON string representation of the object
print(StartBrandNameSuggestionJobRequest.to_json())

# convert the object into a dict
start_brand_name_suggestion_job_request_dict = start_brand_name_suggestion_job_request_instance.to_dict()
# create an instance of StartBrandNameSuggestionJobRequest from a dict
start_brand_name_suggestion_job_request_from_dict = StartBrandNameSuggestionJobRequest.from_dict(start_brand_name_suggestion_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


