# TrackedQueryMoverRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracked_query_id** | **str** |  | 
**query_text** | **str** |  | 
**engine** | **str** |  | 
**country** | **str** |  | 
**avg_serp_position** | **float** |  | [optional] 
**trend_serp** | **float** |  | [optional] 
**avg_shopping_position** | **float** |  | [optional] 
**trend_shopping** | **float** |  | [optional] 
**avg_mention_position** | **float** |  | [optional] 
**trend_mention** | **float** |  | [optional] 
**avg_link_position** | **float** |  | [optional] 
**trend_link** | **float** |  | [optional] 
**share_of_voice** | **float** |  | [optional] 
**trend_share_of_voice** | **float** |  | [optional] 
**positivity_index** | **int** |  | [optional] 
**trend_positivity** | **int** |  | [optional] 
**sentiment_positive** | **int** |  | 
**sentiment_neutral** | **int** |  | 
**sentiment_negative** | **int** |  | 
**mention_count** | **int** |  | 
**mention_type_counts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  | 

## Example

```python
from mencoro.models.tracked_query_mover_row import TrackedQueryMoverRow

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedQueryMoverRow from a JSON string
tracked_query_mover_row_instance = TrackedQueryMoverRow.from_json(json)
# print the JSON string representation of the object
print(TrackedQueryMoverRow.to_json())

# convert the object into a dict
tracked_query_mover_row_dict = tracked_query_mover_row_instance.to_dict()
# create an instance of TrackedQueryMoverRow from a dict
tracked_query_mover_row_from_dict = TrackedQueryMoverRow.from_dict(tracked_query_mover_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


