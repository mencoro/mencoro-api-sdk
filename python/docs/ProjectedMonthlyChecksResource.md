# ProjectedMonthlyChecksResource

What an organization's current tracking configuration would consume in a month

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projected_monthly_checks** | **int** | Checks a month of the current configuration would consume: for each ACTIVE tracked query, its runs per month (daily 30, weekly 4, monthly 1) multiplied by its nPasses, summed. Never null. | 
**active_tracked_query_count** | **int** | Active tracked queries the projection was summed over, across every project of the organization, archived projects included. Paused queries are excluded from both figures. Never null. | 

## Example

```python
from mencoro.models.projected_monthly_checks_resource import ProjectedMonthlyChecksResource

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectedMonthlyChecksResource from a JSON string
projected_monthly_checks_resource_instance = ProjectedMonthlyChecksResource.from_json(json)
# print the JSON string representation of the object
print(ProjectedMonthlyChecksResource.to_json())

# convert the object into a dict
projected_monthly_checks_resource_dict = projected_monthly_checks_resource_instance.to_dict()
# create an instance of ProjectedMonthlyChecksResource from a dict
projected_monthly_checks_resource_from_dict = ProjectedMonthlyChecksResource.from_dict(projected_monthly_checks_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


