# PerCompetitorSentiment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competitor_id** | **str** |  | 
**positive** | **int** |  | 
**neutral** | **int** |  | 
**negative** | **int** |  | 
**mention_count** | **int** |  | 
**positivity_index** | **int** |  | [optional] 
**mention_type_counts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  | 

## Example

```python
from mencoro.models.per_competitor_sentiment import PerCompetitorSentiment

# TODO update the JSON string below
json = "{}"
# create an instance of PerCompetitorSentiment from a JSON string
per_competitor_sentiment_instance = PerCompetitorSentiment.from_json(json)
# print the JSON string representation of the object
print(PerCompetitorSentiment.to_json())

# convert the object into a dict
per_competitor_sentiment_dict = per_competitor_sentiment_instance.to_dict()
# create an instance of PerCompetitorSentiment from a dict
per_competitor_sentiment_from_dict = PerCompetitorSentiment.from_dict(per_competitor_sentiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


