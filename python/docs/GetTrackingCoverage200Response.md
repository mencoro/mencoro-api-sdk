# GetTrackingCoverage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** |  | [optional] 
**total** | **int** | Every tracked query on the project, whatever its status | [optional] 
**active** | **int** | Tracked queries currently being checked | [optional] 
**paused** | **int** | Tracked queries whose checks are suspended | [optional] 
**never_checked** | **int** | Active queries that have never run yet | [optional] 
**overdue** | **int** | Active queries past their check-frequency interval, never-checked ones excluded | [optional] 
**sample** | [**List[GetTrackingCoverage200ResponseSampleInner]**](GetTrackingCoverage200ResponseSampleInner.md) | Up to 20 overdue queries, oldest check first | [optional] 

## Example

```python
from mencoro.models.get_tracking_coverage200_response import GetTrackingCoverage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTrackingCoverage200Response from a JSON string
get_tracking_coverage200_response_instance = GetTrackingCoverage200Response.from_json(json)
# print the JSON string representation of the object
print(GetTrackingCoverage200Response.to_json())

# convert the object into a dict
get_tracking_coverage200_response_dict = get_tracking_coverage200_response_instance.to_dict()
# create an instance of GetTrackingCoverage200Response from a dict
get_tracking_coverage200_response_from_dict = GetTrackingCoverage200Response.from_dict(get_tracking_coverage200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


