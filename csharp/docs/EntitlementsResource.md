# Mencoro.Api.Model.EntitlementsResource
What an organization's plan allows and what it has consumed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **string** | \&quot;none\&quot; when the organization has never had a subscription contract. | 
**IsEntitled** | **bool** | Whether the organization may use paid features right now: an active contract, or a cancelled one still inside its paid grace window. | 
**CheckBudget** | **int?** | Checks the current cycle allows. Null when there is no plan on file, which is not the same as a budget of zero. | [optional] 
**ChecksConsumed** | **int?** | Checks consumed so far in the current cycle. Null when there is no plan on file. | [optional] 
**ChecksAvailable** | **int?** | Checks left in the current cycle. Null when there is no plan on file. | [optional] 
**BillingCycleType** | **string** | How often the allowance renews. Null when there is no plan on file. | [optional] 
**BillingCycleAnchor** | **DateTime?** | Start of the current cycle. Null when there is no plan on file. | [optional] 
**NextResetAt** | **DateTime?** | When the check budget next resets. Null when there is no plan on file. | [optional] 
**CancelledAt** | **DateTime?** | When the subscription was terminally cancelled. Null while it has not been. | [optional] 
**ScheduledToCancelAt** | **DateTime?** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. | [optional] 
**GracePeriodEndsAt** | **DateTime?** | When paid access ends after a cancellation. Null when the subscription has not been cancelled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

