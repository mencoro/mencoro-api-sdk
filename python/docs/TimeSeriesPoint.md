# TimeSeriesPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_date** | **str** |  | 
**brand** | [**PerEntityMetrics**](PerEntityMetrics.md) |  | 
**competitors** | [**Dict[str, PerEntityMetrics]**](PerEntityMetrics.md) |  | 

## Example

```python
from mencoro.models.time_series_point import TimeSeriesPoint

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeriesPoint from a JSON string
time_series_point_instance = TimeSeriesPoint.from_json(json)
# print the JSON string representation of the object
print(TimeSeriesPoint.to_json())

# convert the object into a dict
time_series_point_dict = time_series_point_instance.to_dict()
# create an instance of TimeSeriesPoint from a dict
time_series_point_from_dict = TimeSeriesPoint.from_dict(time_series_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


