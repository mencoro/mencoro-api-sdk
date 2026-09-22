# GetOrganizationOverview200ResponseProjectsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**tracked_query_count** | **int** |  | [optional] 
**share_of_voice** | **float** | 0-100 percentage share of weighted AI mentions against all tracked brands; higher is better. Null when the project has no rank data yet. | [optional] 
**mention_rate** | **int** | 0-100 percentage of tracked queries with a result; higher is better. Null when the project has no rank data yet. | [optional] 
**avg_mention_position** | **float** | 1-based average rank of the brand within the answer; LOWER is better. Null when the project has no rank data yet. | [optional] 
**positivity_index** | **int** | 0-100 sentiment score; higher is better. Null when the project has no rank data yet. | [optional] 

## Example

```python
from mencoro.models.get_organization_overview200_response_projects_inner import GetOrganizationOverview200ResponseProjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationOverview200ResponseProjectsInner from a JSON string
get_organization_overview200_response_projects_inner_instance = GetOrganizationOverview200ResponseProjectsInner.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationOverview200ResponseProjectsInner.to_json())

# convert the object into a dict
get_organization_overview200_response_projects_inner_dict = get_organization_overview200_response_projects_inner_instance.to_dict()
# create an instance of GetOrganizationOverview200ResponseProjectsInner from a dict
get_organization_overview200_response_projects_inner_from_dict = GetOrganizationOverview200ResponseProjectsInner.from_dict(get_organization_overview200_response_projects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


