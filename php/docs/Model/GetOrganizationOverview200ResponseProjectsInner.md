# GetOrganizationOverview200ResponseProjectsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **string** |  | [optional]
**name** | **string** |  | [optional]
**status** | **string** |  | [optional]
**tracked_query_count** | **int** |  | [optional]
**share_of_voice** | **float** | 0-100 percentage share of weighted AI mentions against all tracked brands; higher is better. Null when the project has no rank data yet. | [optional]
**mention_rate** | **int** | 0-100 percentage of tracked queries with a result; higher is better. Null when the project has no rank data yet. | [optional]
**avg_mention_position** | **float** | 1-based average rank of the brand within the answer; LOWER is better. Null when the project has no rank data yet. | [optional]
**positivity_index** | **int** | 0-100 sentiment score; higher is better. Null when the project has no rank data yet. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
