# TrackedQueryUsageResource

How many tracked queries an organization has configured

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracked_query_count** | **int** | Tracked queries across every project of the organization, archived projects included, counting active and paused queries alike. Never null; 0 means none are configured. | 

## Example

```python
from mencoro.models.tracked_query_usage_resource import TrackedQueryUsageResource

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedQueryUsageResource from a JSON string
tracked_query_usage_resource_instance = TrackedQueryUsageResource.from_json(json)
# print the JSON string representation of the object
print(TrackedQueryUsageResource.to_json())

# convert the object into a dict
tracked_query_usage_resource_dict = tracked_query_usage_resource_instance.to_dict()
# create an instance of TrackedQueryUsageResource from a dict
tracked_query_usage_resource_from_dict = TrackedQueryUsageResource.from_dict(tracked_query_usage_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


