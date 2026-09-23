# TrackedQueryRankTrackingTimeSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[TimeSeriesPoint]**](TimeSeriesPoint.md) |  | 
**data_dirty_since** | **str** |  | [optional] 

## Example

```python
from mencoro.models.tracked_query_rank_tracking_time_series import TrackedQueryRankTrackingTimeSeries

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedQueryRankTrackingTimeSeries from a JSON string
tracked_query_rank_tracking_time_series_instance = TrackedQueryRankTrackingTimeSeries.from_json(json)
# print the JSON string representation of the object
print(TrackedQueryRankTrackingTimeSeries.to_json())

# convert the object into a dict
tracked_query_rank_tracking_time_series_dict = tracked_query_rank_tracking_time_series_instance.to_dict()
# create an instance of TrackedQueryRankTrackingTimeSeries from a dict
tracked_query_rank_tracking_time_series_from_dict = TrackedQueryRankTrackingTimeSeries.from_dict(tracked_query_rank_tracking_time_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


