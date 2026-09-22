# BatchForceCheckTrackedQueries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**List[BatchPauseTrackedQueries200ResponseSuccessfulInner]**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries whose check was accepted for submission. Accepted is not completed. | [optional] 
**failed** | [**List[BatchForceCheckTrackedQueries200ResponseFailedInner]**](BatchForceCheckTrackedQueries200ResponseFailedInner.md) | Tracked queries no check was submitted for, each with the reason: check_budget_forecast_exhausted, subscription_not_found, tracked_query_already_paused or tracked_query_not_found. | [optional] 

## Example

```python
from mencoro.models.batch_force_check_tracked_queries200_response import BatchForceCheckTrackedQueries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BatchForceCheckTrackedQueries200Response from a JSON string
batch_force_check_tracked_queries200_response_instance = BatchForceCheckTrackedQueries200Response.from_json(json)
# print the JSON string representation of the object
print(BatchForceCheckTrackedQueries200Response.to_json())

# convert the object into a dict
batch_force_check_tracked_queries200_response_dict = batch_force_check_tracked_queries200_response_instance.to_dict()
# create an instance of BatchForceCheckTrackedQueries200Response from a dict
batch_force_check_tracked_queries200_response_from_dict = BatchForceCheckTrackedQueries200Response.from_dict(batch_force_check_tracked_queries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


