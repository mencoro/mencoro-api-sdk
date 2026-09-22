# ProjectedMonthlyChecksResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projected_monthly_checks** | **int** | Checks a month of the current configuration would consume: for each ACTIVE tracked query, its runs per month (daily 30, weekly 4, monthly 1) multiplied by its nPasses, summed. Never null. |
**active_tracked_query_count** | **int** | Active tracked queries the projection was summed over, across every project of the organization, archived projects included. Paused queries are excluded from both figures. Never null. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
