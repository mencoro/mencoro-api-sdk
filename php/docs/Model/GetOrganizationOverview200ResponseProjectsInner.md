# GetOrganizationOverview200ResponseProjectsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **string** |  | [optional]
**name** | **string** |  | [optional]
**status** | **string** |  | [optional]
**tracked_query_count** | **int** | Configured tracked queries of the project, paused ones included. | [optional]
**ai_tracked_query_count** | **int** | How many of trackedQueryCount run on an AI answer engine (ChatGPT, Claude, Perplexity, Google AI Overview, Google AI Mode). | [optional]
**serp_tracked_query_count** | **int** | How many of trackedQueryCount run on classic Google SERP. | [optional]
**shopping_tracked_query_count** | **int** | How many of trackedQueryCount run on Google Shopping. | [optional]
**share_of_voice** | **float** | 0-100 percentage share of weighted AI mentions against all tracked brands; higher is better. Null when the project has no rank data yet. | [optional]
**mention_rate** | **int** | 0-100 percentage of AI checks (one per tracked query x engine x UTC day) across all retained data that mentioned the brand, each check counted as the share of its passes that did; higher is better. Null when the project has no rank data yet. | [optional]
**avg_mention_position** | **float** | 1-based average rank of the brand within the answer; LOWER is better. Null when the project has no rank data yet. | [optional]
**positivity_index** | **int** | 0-100 sentiment score; higher is better. Null when the project has no rank data yet. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
