# TrackedQueryResource

A tracked query and the metrics of its most recent check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**query_text** | **str** | The keyword or prompt being tracked | 
**engine** | **str** |  | 
**country** | **str** | ISO-3166 alpha-2 country code the query is tracked in | 
**status** | **str** |  | 
**query_cluster_ids** | **List[UUID]** | Ids of the keyword clusters this query belongs to | 
**check_frequency** | **str** | How often the query is checked | 
**n_passes** | **int** | How many times the query is asked per check | 
**last_serp_position** | **int** | Position in traditional search results at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**last_mention_position** | **int** | Position of the brand mention inside the AI answer at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**last_link_position** | **int** | Position of a cited link to the brand at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**last_shopping_position** | **int** | Position in shopping results at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**last_share_of_voice** | **float** | 0-100 share of the weighted AI mentions against every tracked brand; HIGHER is better. Null when not known yet, which is not a share of zero. | [optional] 
**last_positivity_index** | **int** | 0-100 sentiment score of the brand mentions; HIGHER is better. Null when there were no mentions to score, which is not a score of zero. | [optional] 
**last_positive_mention_count** | **int** | Positive brand mentions at the last check. Null when not known yet. | [optional] 
**last_neutral_mention_count** | **int** | Neutral brand mentions at the last check. Null when not known yet. | [optional] 
**last_negative_mention_count** | **int** | Negative brand mentions at the last check. Null when not known yet. | [optional] 
**last_checked_at** | **datetime** | When the query was last checked. Null when it never has been. | [optional] 

## Example

```python
from mencoro.models.tracked_query_resource import TrackedQueryResource

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedQueryResource from a JSON string
tracked_query_resource_instance = TrackedQueryResource.from_json(json)
# print the JSON string representation of the object
print(TrackedQueryResource.to_json())

# convert the object into a dict
tracked_query_resource_dict = tracked_query_resource_instance.to_dict()
# create an instance of TrackedQueryResource from a dict
tracked_query_resource_from_dict = TrackedQueryResource.from_dict(tracked_query_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


