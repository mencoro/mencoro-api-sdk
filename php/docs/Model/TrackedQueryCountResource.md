# TrackedQueryCountResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Tracked queries in the project matching the status filter. Every status when none was sent. |
**check_cost** | **int** | Budget cost of force-checking exactly those tracked queries, in checks: the sum of each one&#39;s configured passes multiplied by its engine weight. Five checks per Claude pass and one check per pass for every other engine, the same currency as the plan allowance. Reserves nothing and debits nothing. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
