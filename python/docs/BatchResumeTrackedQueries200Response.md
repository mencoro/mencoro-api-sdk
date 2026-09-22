# BatchResumeTrackedQueries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**List[BatchPauseTrackedQueries200ResponseSuccessfulInner]**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries that are now active, including ones that already were. | [optional] 
**failed** | [**List[BatchPauseTrackedQueries200ResponseFailedInner]**](BatchPauseTrackedQueries200ResponseFailedInner.md) | Tracked queries left untouched, each with the domain error code a single-item call would have returned. | [optional] 

## Example

```python
from mencoro.models.batch_resume_tracked_queries200_response import BatchResumeTrackedQueries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResumeTrackedQueries200Response from a JSON string
batch_resume_tracked_queries200_response_instance = BatchResumeTrackedQueries200Response.from_json(json)
# print the JSON string representation of the object
print(BatchResumeTrackedQueries200Response.to_json())

# convert the object into a dict
batch_resume_tracked_queries200_response_dict = batch_resume_tracked_queries200_response_instance.to_dict()
# create an instance of BatchResumeTrackedQueries200Response from a dict
batch_resume_tracked_queries200_response_from_dict = BatchResumeTrackedQueries200Response.from_dict(batch_resume_tracked_queries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


