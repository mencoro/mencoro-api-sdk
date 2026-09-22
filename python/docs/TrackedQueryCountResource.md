# TrackedQueryCountResource

How many tracked queries a project has, and what checking them would cost in budget units

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Tracked queries in the project matching the status filter. Every status when none was sent. | 
**check_cost** | **int** | Budget cost of force-checking exactly those tracked queries, in check budget units: the sum of each one&#39;s configured passes. One unit per pass, the same unit the plan allowance is counted in. Reserves nothing and debits nothing. | 

## Example

```python
from mencoro.models.tracked_query_count_resource import TrackedQueryCountResource

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedQueryCountResource from a JSON string
tracked_query_count_resource_instance = TrackedQueryCountResource.from_json(json)
# print the JSON string representation of the object
print(TrackedQueryCountResource.to_json())

# convert the object into a dict
tracked_query_count_resource_dict = tracked_query_count_resource_instance.to_dict()
# create an instance of TrackedQueryCountResource from a dict
tracked_query_count_resource_from_dict = TrackedQueryCountResource.from_dict(tracked_query_count_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


