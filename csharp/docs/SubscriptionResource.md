# Mencoro.Api.Model.SubscriptionResource
The current subscription contract of an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **string** | Contract state. \&quot;none\&quot; when the organization has never held a subscription. | 
**TierCode** | **string** | Public tier identifier derived from the check budget. | [optional] 
**BillingCycleType** | **string** | Billing interval of the contract. | [optional] 
**BillingCycleAnchor** | **DateTime?** | Instant the billing cycle is anchored to. | [optional] 
**CheckBudget** | **int?** | Checks the current cycle grants. Null when there is no subscription, never a stand-in for zero. | [optional] 
**ChecksConsumed** | **int?** | Checks consumed so far in the current cycle. Null when there is no subscription; zero means none consumed yet. | [optional] 
**ChecksAvailable** | **int?** | Checks still available in the current cycle. Null when there is no subscription; zero means the budget is exhausted. | [optional] 
**NextResetAt** | **DateTime?** | When the check budget resets next. | [optional] 
**CancelledAt** | **DateTime?** | When the subscription was terminally cancelled. Null while it has not been. | [optional] 
**ScheduledToCancelAt** | **DateTime?** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. | [optional] 
**GracePeriodEndsAt** | **DateTime?** | When paid access ends after a cancellation. Null when the subscription is not cancelled. | [optional] 
**DeactivationReason** | **string** | Why the subscription is currently inactive. Null for an active subscription, and meaningless once \&quot;cancelledAt\&quot; is set - the cancellation supersedes it. | [optional] 
**IsEntitled** | **bool** | Whether the organization may use paid features right now: active, or cancelled but still inside its paid grace window. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

