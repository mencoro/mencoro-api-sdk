# ClusterBreakdownRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | [optional] 
**cluster_name** | **str** |  | 
**query_count** | **int** |  | 
**keyword_count** | **int** |  | 
**avg_serp_position** | **float** |  | [optional] 
**trend_serp** | **float** |  | [optional] 
**avg_shopping_position** | **float** |  | [optional] 
**trend_shopping** | **float** |  | [optional] 
**avg_mention_position** | **float** |  | [optional] 
**trend_mention** | **float** |  | [optional] 
**avg_link_position** | **float** |  | [optional] 
**trend_link** | **float** |  | [optional] 
**mention_position_stability** | **float** |  | [optional] 
**trend_stability** | **float** |  | [optional] 
**serp_position_stability** | **float** |  | [optional] 
**trend_serp_stability** | **float** |  | [optional] 
**shopping_position_stability** | **float** |  | [optional] 
**trend_shopping_stability** | **float** |  | [optional] 
**positivity_index** | **int** |  | [optional] 
**trend_positivity** | **int** |  | [optional] 
**mention_rate** | **int** |  | [optional] 
**trend_mention_rate** | **int** |  | [optional] 
**serp_rate** | **int** |  | [optional] 
**trend_serp_rate** | **int** |  | [optional] 
**shopping_rate** | **int** |  | [optional] 
**trend_shopping_rate** | **int** |  | [optional] 
**share_of_voice** | **float** |  | [optional] 
**trend_share_of_voice** | **float** |  | [optional] 
**sentiment_positive** | **int** |  | 
**sentiment_neutral** | **int** |  | 
**sentiment_negative** | **int** |  | 
**avg_mention_count** | **float** |  | [optional] 
**mention_type_counts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  | 

## Example

```python
from mencoro.models.cluster_breakdown_row import ClusterBreakdownRow

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterBreakdownRow from a JSON string
cluster_breakdown_row_instance = ClusterBreakdownRow.from_json(json)
# print the JSON string representation of the object
print(ClusterBreakdownRow.to_json())

# convert the object into a dict
cluster_breakdown_row_dict = cluster_breakdown_row_instance.to_dict()
# create an instance of ClusterBreakdownRow from a dict
cluster_breakdown_row_from_dict = ClusterBreakdownRow.from_dict(cluster_breakdown_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


