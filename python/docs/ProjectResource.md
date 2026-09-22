# ProjectResource

A project and its headline metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**tracked_query_count** | **int** | Number of tracked queries in the project | 
**avg_serp_position** | **float** | Average position in traditional search results. Null when unknown. | [optional] 
**avg_shopping_position** | **float** | Average position in shopping results. Null when unknown. | [optional] 
**avg_mention_position** | **float** | Average position of the brand mention inside AI answers. Null when unknown. | [optional] 
**avg_link_position** | **float** | Average position of a cited link to the brand. Null when unknown. | [optional] 
**mention_rate** | **int** | Share of checks where the brand was mentioned. Null when unknown. | [optional] 
**serp_rate** | **int** |  | [optional] 
**shopping_rate** | **int** |  | [optional] 
**positivity_index** | **int** | Sentiment balance of the brand&#39;s mentions. Null when unknown. | [optional] 
**share_of_voice** | **float** | Share of voice against the tracked competitors. Null when unknown. | [optional] 
**serp_position_stability** | **float** |  | [optional] 
**shopping_position_stability** | **float** |  | [optional] 
**last_rank_detected_at** | **datetime** | When a rank was last detected for this project. | [optional] 

## Example

```python
from mencoro.models.project_resource import ProjectResource

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResource from a JSON string
project_resource_instance = ProjectResource.from_json(json)
# print the JSON string representation of the object
print(ProjectResource.to_json())

# convert the object into a dict
project_resource_dict = project_resource_instance.to_dict()
# create an instance of ProjectResource from a dict
project_resource_from_dict = ProjectResource.from_dict(project_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


