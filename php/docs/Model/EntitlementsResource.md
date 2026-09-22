# EntitlementsResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **string** | \&quot;none\&quot; when the organization has never had a subscription contract. |
**is_entitled** | **bool** | Whether the organization may use paid features right now: an active contract, or a cancelled one still inside its paid grace window. |
**check_budget** | **int** | Checks the current cycle allows. Null when there is no plan on file, which is not the same as a budget of zero. | [optional]
**checks_consumed** | **int** | Checks consumed so far in the current cycle. Null when there is no plan on file. | [optional]
**checks_available** | **int** | Checks left in the current cycle. Null when there is no plan on file. | [optional]
**billing_cycle_type** | **string** | How often the allowance renews. Null when there is no plan on file. | [optional]
**billing_cycle_anchor** | **\DateTime** | Start of the current cycle. Null when there is no plan on file. | [optional]
**next_reset_at** | **\DateTime** | When the check budget next resets. Null when there is no plan on file. | [optional]
**cancelled_at** | **\DateTime** | When the subscription was terminally cancelled. Null while it has not been. | [optional]
**scheduled_to_cancel_at** | **\DateTime** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. | [optional]
**grace_period_ends_at** | **\DateTime** | When paid access ends after a cancellation. Null when the subscription has not been cancelled. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
