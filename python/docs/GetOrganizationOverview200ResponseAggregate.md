# GetOrganizationOverview200ResponseAggregate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_count** | **int** | Active projects in the organization, the length of &#x60;projects&#x60;. | [optional] 
**projects_with_data** | **int** | How many of those have a share of voice; the averages below are means over the projects that report each metric, never over the ones still null. | [optional] 
**total_tracked_queries** | **int** |  | [optional] 
**avg_share_of_voice** | **float** | Null when no project reports a share of voice. | [optional] 
**avg_mention_rate** | **int** |  | [optional] 
**avg_mention_position** | **float** | 1-based rank; LOWER is better. | [optional] 
**avg_positivity_index** | **int** |  | [optional] 

## Example

```python
from mencoro.models.get_organization_overview200_response_aggregate import GetOrganizationOverview200ResponseAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationOverview200ResponseAggregate from a JSON string
get_organization_overview200_response_aggregate_instance = GetOrganizationOverview200ResponseAggregate.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationOverview200ResponseAggregate.to_json())

# convert the object into a dict
get_organization_overview200_response_aggregate_dict = get_organization_overview200_response_aggregate_instance.to_dict()
# create an instance of GetOrganizationOverview200ResponseAggregate from a dict
get_organization_overview200_response_aggregate_from_dict = GetOrganizationOverview200ResponseAggregate.from_dict(get_organization_overview200_response_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


