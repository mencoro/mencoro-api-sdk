# StartKeywordDiscoveryJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** | Free text describing the keywords or topics to expand. | 
**language** | **str** | Language code. Omit to let the provider detect it from the input. | [optional] 
**country** | **str** | ISO 3166-1 alpha-2 country. Omit to let the provider infer it. | [optional] 
**exclude_queries** | **List[str]** | Extra queries to keep out of the suggestions for this run. Duplicates are collapsed, after the entry count has been checked against maxItems. The project tracked queries are excluded whether or not this is sent. | [optional] 

## Example

```python
from mencoro.models.start_keyword_discovery_job_request import StartKeywordDiscoveryJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartKeywordDiscoveryJobRequest from a JSON string
start_keyword_discovery_job_request_instance = StartKeywordDiscoveryJobRequest.from_json(json)
# print the JSON string representation of the object
print(StartKeywordDiscoveryJobRequest.to_json())

# convert the object into a dict
start_keyword_discovery_job_request_dict = start_keyword_discovery_job_request_instance.to_dict()
# create an instance of StartKeywordDiscoveryJobRequest from a dict
start_keyword_discovery_job_request_from_dict = StartKeywordDiscoveryJobRequest.from_dict(start_keyword_discovery_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


