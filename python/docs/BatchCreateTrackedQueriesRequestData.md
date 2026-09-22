# BatchCreateTrackedQueriesRequestData

Tracked queries to create, as a cross product of texts, engines and countries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_texts** | **List[str]** | Prompts or keywords to track. Stored lower-cased with whitespace collapsed and leading list markers removed. | 
**engines** | **List[str]** | Engines each text is asked in. | 
**countries** | **List[str]** | ISO 3166-1 alpha-2 countries each text is asked from. | 
**locale** | **str** | ISO 639-1 language the queries are asked in. Omit it to ask the engine without a language. | [optional] 
**check_frequency** | **str** | How often every created query is checked. | 
**n_passes** | **int** | Passes run per check. Applied to AI-engine combinations only: a non-AI engine is always created with 1, whatever is sent here. | 
**query_cluster_ids** | **List[UUID]** | Clusters every created query joins. Must already exist in the project. A combination that is already tracked has these clusters merged into it. | 

## Example

```python
from mencoro.models.batch_create_tracked_queries_request_data import BatchCreateTrackedQueriesRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCreateTrackedQueriesRequestData from a JSON string
batch_create_tracked_queries_request_data_instance = BatchCreateTrackedQueriesRequestData.from_json(json)
# print the JSON string representation of the object
print(BatchCreateTrackedQueriesRequestData.to_json())

# convert the object into a dict
batch_create_tracked_queries_request_data_dict = batch_create_tracked_queries_request_data_instance.to_dict()
# create an instance of BatchCreateTrackedQueriesRequestData from a dict
batch_create_tracked_queries_request_data_from_dict = BatchCreateTrackedQueriesRequestData.from_dict(batch_create_tracked_queries_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


