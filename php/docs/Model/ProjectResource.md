# ProjectResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**name** | **string** |  |
**status** | **string** |  |
**created_at** | **\DateTime** |  |
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
**last_rank_detected_at** | **\DateTime** | When a rank was last detected for this project. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
