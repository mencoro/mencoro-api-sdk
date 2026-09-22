# BatchCreateTrackedQueriesResultResourceFailedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_text** | **str** |  | [optional] 
**engine** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from mencoro.models.batch_create_tracked_queries_result_resource_failed_inner import BatchCreateTrackedQueriesResultResourceFailedInner

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCreateTrackedQueriesResultResourceFailedInner from a JSON string
batch_create_tracked_queries_result_resource_failed_inner_instance = BatchCreateTrackedQueriesResultResourceFailedInner.from_json(json)
# print the JSON string representation of the object
print(BatchCreateTrackedQueriesResultResourceFailedInner.to_json())

# convert the object into a dict
batch_create_tracked_queries_result_resource_failed_inner_dict = batch_create_tracked_queries_result_resource_failed_inner_instance.to_dict()
# create an instance of BatchCreateTrackedQueriesResultResourceFailedInner from a dict
batch_create_tracked_queries_result_resource_failed_inner_from_dict = BatchCreateTrackedQueriesResultResourceFailedInner.from_dict(batch_create_tracked_queries_result_resource_failed_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


