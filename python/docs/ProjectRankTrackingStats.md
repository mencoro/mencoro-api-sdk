# ProjectRankTrackingStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**mention_count** | **int** |  | 
**ai_tracked_query_count** | **int** |  | 
**ai_queries_with_mention** | **int** |  | 
**serp_tracked_query_count** | **int** |  | 
**serp_queries_with_result** | **int** |  | 
**shopping_tracked_query_count** | **int** |  | 
**shopping_queries_with_result** | **int** |  | 
**mention_type_counts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  | 
**data_dirty_since** | **str** |  | [optional] 
**mention_position_distribution** | [**List[PositionDistributionBucket]**](PositionDistributionBucket.md) |  | [optional] [default to []]
**serp_position_distribution** | [**List[PositionDistributionBucket]**](PositionDistributionBucket.md) |  | [optional] [default to []]
**shopping_position_distribution** | [**List[PositionDistributionBucket]**](PositionDistributionBucket.md) |  | [optional] [default to []]
**competitor_share_of_voice** | [**List[CompetitorShareOfVoice]**](CompetitorShareOfVoice.md) |  | [optional] [default to []]

## Example

```python
from mencoro.models.project_rank_tracking_stats import ProjectRankTrackingStats

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRankTrackingStats from a JSON string
project_rank_tracking_stats_instance = ProjectRankTrackingStats.from_json(json)
# print the JSON string representation of the object
print(ProjectRankTrackingStats.to_json())

# convert the object into a dict
project_rank_tracking_stats_dict = project_rank_tracking_stats_instance.to_dict()
# create an instance of ProjectRankTrackingStats from a dict
project_rank_tracking_stats_from_dict = ProjectRankTrackingStats.from_dict(project_rank_tracking_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


