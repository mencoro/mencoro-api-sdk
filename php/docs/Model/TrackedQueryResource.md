# TrackedQueryResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**query_text** | **string** | The keyword or prompt being tracked |
**engine** | **string** |  |
**country** | **string** | ISO-3166 alpha-2 country code the query is tracked in |
**status** | **string** |  |
**query_cluster_ids** | **string[]** | Ids of the keyword clusters this query belongs to |
**check_frequency** | **string** | How often the query is checked |
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
**last_checked_at** | **\DateTime** | When the query was last checked. Null when it never has been. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
