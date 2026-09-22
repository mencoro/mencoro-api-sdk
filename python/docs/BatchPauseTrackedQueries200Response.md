# BatchPauseTrackedQueries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**List[BatchPauseTrackedQueries200ResponseSuccessfulInner]**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries that are now paused, including ones that already were. | [optional] 
**failed** | [**List[BatchPauseTrackedQueries200ResponseFailedInner]**](BatchPauseTrackedQueries200ResponseFailedInner.md) | Tracked queries left untouched, each with the domain error code a single-item call would have returned. | [optional] 

## Example

```python
from mencoro.models.batch_pause_tracked_queries200_response import BatchPauseTrackedQueries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BatchPauseTrackedQueries200Response from a JSON string
batch_pause_tracked_queries200_response_instance = BatchPauseTrackedQueries200Response.from_json(json)
# print the JSON string representation of the object
print(BatchPauseTrackedQueries200Response.to_json())

# convert the object into a dict
batch_pause_tracked_queries200_response_dict = batch_pause_tracked_queries200_response_instance.to_dict()
# create an instance of BatchPauseTrackedQueries200Response from a dict
batch_pause_tracked_queries200_response_from_dict = BatchPauseTrackedQueries200Response.from_dict(batch_pause_tracked_queries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


