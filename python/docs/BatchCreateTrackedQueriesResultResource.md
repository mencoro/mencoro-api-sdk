# BatchCreateTrackedQueriesResultResource

Per-combination results of creating tracked queries in bulk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**List[BatchCreateTrackedQueriesResultResourceSuccessfulInner]**](BatchCreateTrackedQueriesResultResourceSuccessfulInner.md) | Tracked queries created by this call, one entry per query text, engine and country combination. | [optional] 
**failed** | [**List[BatchCreateTrackedQueriesResultResourceFailedInner]**](BatchCreateTrackedQueriesResultResourceFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 

## Example

```python
from mencoro.models.batch_create_tracked_queries_result_resource import BatchCreateTrackedQueriesResultResource

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCreateTrackedQueriesResultResource from a JSON string
batch_create_tracked_queries_result_resource_instance = BatchCreateTrackedQueriesResultResource.from_json(json)
# print the JSON string representation of the object
print(BatchCreateTrackedQueriesResultResource.to_json())

# convert the object into a dict
batch_create_tracked_queries_result_resource_dict = batch_create_tracked_queries_result_resource_instance.to_dict()
# create an instance of BatchCreateTrackedQueriesResultResource from a dict
batch_create_tracked_queries_result_resource_from_dict = BatchCreateTrackedQueriesResultResource.from_dict(batch_create_tracked_queries_result_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


