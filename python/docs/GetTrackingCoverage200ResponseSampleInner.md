# GetTrackingCoverage200ResponseSampleInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracked_query_id** | **UUID** |  | [optional] 
**query_text** | **str** |  | [optional] 
**engine** | **str** |  | [optional] 
**country** | **str** | ISO-3166 alpha-2 code | [optional] 
**check_frequency** | **str** |  | [optional] 
**last_checked_at** | **datetime** | RFC 3339 timestamp of the last check. Null means never checked, which this sample never contains. | [optional] 

## Example

```python
from mencoro.models.get_tracking_coverage200_response_sample_inner import GetTrackingCoverage200ResponseSampleInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTrackingCoverage200ResponseSampleInner from a JSON string
get_tracking_coverage200_response_sample_inner_instance = GetTrackingCoverage200ResponseSampleInner.from_json(json)
# print the JSON string representation of the object
print(GetTrackingCoverage200ResponseSampleInner.to_json())

# convert the object into a dict
get_tracking_coverage200_response_sample_inner_dict = get_tracking_coverage200_response_sample_inner_instance.to_dict()
# create an instance of GetTrackingCoverage200ResponseSampleInner from a dict
get_tracking_coverage200_response_sample_inner_from_dict = GetTrackingCoverage200ResponseSampleInner.from_dict(get_tracking_coverage200_response_sample_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


