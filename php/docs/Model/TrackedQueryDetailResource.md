# TrackedQueryDetailResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**project_id** | **string** | The project this tracked query belongs to |
**query_text** | **string** | The prompt or keyword sent to the engine |
**engine** | **string** |  |
**locale** | **string** | Language tag the query is asked in. Null when the engine is asked without one. | [optional]
**country** | **string** | ISO-3166 alpha-2 country the query is asked from |
**query_cluster_ids** | **string[]** | Clusters (groups) this query belongs to. Empty when it is ungrouped. |
**status** | **string** |  |
**check_frequency** | **string** | How often the query is checked while active |
**n_passes** | **int** | Passes run per check. Greater than 1 only for AI engines. |
**last_checked_at** | **\DateTime** | When a check last completed. Null means no check has completed yet, which is not the same as a check that found nothing. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
