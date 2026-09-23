# ProjectRankTrackingTimeSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[TimeSeriesPoint]**](TimeSeriesPoint.md) |  | 
**data_dirty_since** | **str** |  | [optional] 

## Example

```python
from mencoro.models.project_rank_tracking_time_series import ProjectRankTrackingTimeSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRankTrackingTimeSeries from a JSON string
project_rank_tracking_time_series_instance = ProjectRankTrackingTimeSeries.from_json(json)
# print the JSON string representation of the object
print(ProjectRankTrackingTimeSeries.to_json())

# convert the object into a dict
project_rank_tracking_time_series_dict = project_rank_tracking_time_series_instance.to_dict()
# create an instance of ProjectRankTrackingTimeSeries from a dict
project_rank_tracking_time_series_from_dict = ProjectRankTrackingTimeSeries.from_dict(project_rank_tracking_time_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


