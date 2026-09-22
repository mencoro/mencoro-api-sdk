# GetOrganizationOverview200ResponseAggregate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_count** | **int** | Active projects in the organization, the length of &#x60;projects&#x60;. | [optional]
**projects_with_data** | **int** | How many of those have a share of voice; the averages below are means over the projects that report each metric, never over the ones still null. | [optional]
**total_tracked_queries** | **int** |  | [optional]
**avg_share_of_voice** | **float** | Null when no project reports a share of voice. | [optional]
**avg_mention_rate** | **int** |  | [optional]
**avg_mention_position** | **float** | 1-based rank; LOWER is better. | [optional]
**avg_positivity_index** | **int** |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
