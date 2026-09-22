# KeywordListingResource

One keyword of a project, its variants and its metrics over the requested window

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | The keyword as a human types it, picked from the variants for display. | 
**keyword_normalized** | **str** | The grouping key: the keyword lower-cased and unaccented. Unique within the project, and the stable way to match a row across pages. | 
**variant_count** | **int** | Tracked queries behind this row that the current filters selected. | 
**variant_ids** | **List[UUID]** | Ids of those tracked queries. Accepted by the single tracked-query operation. | 
**engines** | **List[str]** | Distinct engines across the variants, not a single engine. | 
**countries** | **List[str]** | Distinct ISO-3166 alpha-2 countries across the variants. | 
**query_cluster_ids** | **List[UUID]** | Distinct keyword clusters the variants belong to. Empty when none of them is clustered. | 
**has_unclustered_variant** | **bool** | Whether at least one variant belongs to no cluster. | 
**status_summary** | **str** | \&quot;mixed\&quot; when the variants disagree; otherwise the one status they share. | 
**statuses** | **List[str]** | Distinct statuses across the variants. | 
**check_frequencies** | **List[str]** | Distinct check frequencies across the variants. | 
**n_passes_values** | **List[int]** | Distinct pass counts across the variants. A pass is one budget unit per check. | 
**last_checked_at** | **datetime** | The most recent completed check across the variants. Null when none has ever completed — not a check that found nothing. | [optional] 
**avg_serp_position** | **float** | Average position in traditional search over the window. 1-based, LOWER is better. | [optional] 
**trend_serp** | **float** | Signed improvement in avgSerpPosition against the previous window. Positive is better. | [optional] 
**avg_shopping_position** | **float** | Average position in shopping results over the window. 1-based, LOWER is better. | [optional] 
**trend_shopping** | **float** | Signed improvement in avgShoppingPosition. Positive is better. | [optional] 
**avg_mention_position** | **float** | Average position of the brand mention inside the AI answer. 1-based, LOWER is better. | [optional] 
**trend_mention** | **float** | Signed improvement in avgMentionPosition. Positive is better. | [optional] 
**avg_link_position** | **float** | Average position of a cited link to the brand. 1-based, LOWER is better. | [optional] 
**trend_link** | **float** | Signed improvement in avgLinkPosition. Positive is better. | [optional] 
**mention_position_stability** | **float** | Day-to-day spread of the mention position (a standard deviation): LOWER means steadier. | [optional] 
**trend_stability** | **float** | Signed improvement in mentionPositionStability. Positive means steadier than the previous window. | [optional] 
**positivity_index** | **int** | 0-100 weighted sentiment score of the mentions; HIGHER is better. Null when there were no mentions to score. | [optional] 
**trend_positivity** | **int** | Signed improvement in positivityIndex. Positive is better. | [optional] 
**mention_rate** | **int** | 0-100 share of AI captures in the window that mentioned the brand; HIGHER is better. | [optional] 
**trend_mention_rate** | **int** | Signed improvement in mentionRate. Positive is better. | [optional] 
**serp_rate** | **int** | 0-100 share of traditional-search captures in the window that ranked the brand; HIGHER is better. | [optional] 
**trend_serp_rate** | **int** | Signed improvement in serpRate. Positive is better. | [optional] 
**share_of_voice** | **float** | 0-100 share of the weighted AI mentions against every tracked brand; HIGHER is better. | [optional] 
**trend_share_of_voice** | **float** | Signed improvement in shareOfVoice. Positive is better. | [optional] 
**sentiment_positive** | **int** | Positive brand mentions counted in the window. Zero here really is zero. | 
**sentiment_neutral** | **int** | Neutral brand mentions counted in the window. | 
**sentiment_negative** | **int** | Negative brand mentions counted in the window. | 
**avg_mention_count** | **float** | Mentions per AI engine per day with a capture, over the window. Not a total: the window total is not part of this contract. | [optional] 
**mention_type_counts** | [**KeywordListingResourceMentionTypeCounts**](KeywordListingResourceMentionTypeCounts.md) |  | 

## Example

```python
from mencoro.models.keyword_listing_resource import KeywordListingResource

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordListingResource from a JSON string
keyword_listing_resource_instance = KeywordListingResource.from_json(json)
# print the JSON string representation of the object
print(KeywordListingResource.to_json())

# convert the object into a dict
keyword_listing_resource_dict = keyword_listing_resource_instance.to_dict()
# create an instance of KeywordListingResource from a dict
keyword_listing_resource_from_dict = KeywordListingResource.from_dict(keyword_listing_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


