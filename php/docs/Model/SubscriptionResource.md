# SubscriptionResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **string** | Contract state. \&quot;none\&quot; when the organization has never held a subscription. |
**tier_code** | **string** | Public tier identifier derived from the check budget. | [optional]
**billing_cycle_type** | **string** | Billing interval of the contract. | [optional]
**billing_cycle_anchor** | **\DateTime** | Instant the billing cycle is anchored to. | [optional]
**check_budget** | **int** | Checks the current cycle grants. Null when there is no subscription, never a stand-in for zero. | [optional]
**checks_consumed** | **int** | Checks consumed so far in the current cycle. Null when there is no subscription; zero means none consumed yet. | [optional]
**checks_available** | **int** | Checks still available in the current cycle. Null when there is no subscription; zero means the budget is exhausted. | [optional]
**next_reset_at** | **\DateTime** | When the check budget resets next. | [optional]
**cancelled_at** | **\DateTime** | When the subscription was terminally cancelled. Null while it has not been. | [optional]
**scheduled_to_cancel_at** | **\DateTime** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. | [optional]
**grace_period_ends_at** | **\DateTime** | When paid access ends after a cancellation. Null when the subscription is not cancelled. | [optional]
**deactivation_reason** | **string** | Why the subscription is currently inactive. Null for an active subscription, and meaningless once \&quot;cancelledAt\&quot; is set - the cancellation supersedes it. | [optional]
**is_entitled** | **bool** | Whether the organization may use paid features right now: active, or cancelled but still inside its paid grace window. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
