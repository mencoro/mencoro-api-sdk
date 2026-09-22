

# SubscriptionResource

The current subscription contract of an organization

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | Contract state. \&quot;none\&quot; when the organization has never held a subscription. |  |
|**tierCode** | **String** | Public tier identifier derived from the check budget. |  [optional] |
|**billingCycleType** | [**BillingCycleTypeEnum**](#BillingCycleTypeEnum) | Billing interval of the contract. |  [optional] |
|**billingCycleAnchor** | **OffsetDateTime** | Instant the billing cycle is anchored to. |  [optional] |
|**checkBudget** | **Integer** | Checks the current cycle grants. Null when there is no subscription, never a stand-in for zero. |  [optional] |
|**checksConsumed** | **Integer** | Checks consumed so far in the current cycle. Null when there is no subscription; zero means none consumed yet. |  [optional] |
|**checksAvailable** | **Integer** | Checks still available in the current cycle. Null when there is no subscription; zero means the budget is exhausted. |  [optional] |
|**nextResetAt** | **OffsetDateTime** | When the check budget resets next. |  [optional] |
|**cancelledAt** | **OffsetDateTime** | When the subscription was terminally cancelled. Null while it has not been. |  [optional] |
|**scheduledToCancelAt** | **OffsetDateTime** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. |  [optional] |
|**gracePeriodEndsAt** | **OffsetDateTime** | When paid access ends after a cancellation. Null when the subscription is not cancelled. |  [optional] |
|**deactivationReason** | [**DeactivationReasonEnum**](#DeactivationReasonEnum) | Why the subscription is currently inactive. Null for an active subscription, and meaningless once \&quot;cancelledAt\&quot; is set - the cancellation supersedes it. |  [optional] |
|**isEntitled** | **Boolean** | Whether the organization may use paid features right now: active, or cancelled but still inside its paid grace window. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| NONE | &quot;none&quot; |



## Enum: BillingCycleTypeEnum

| Name | Value |
|---- | -----|
| MONTHLY | &quot;monthly&quot; |
| YEARLY | &quot;yearly&quot; |



## Enum: DeactivationReasonEnum

| Name | Value |
|---- | -----|
| PAYMENT_FAILED | &quot;payment_failed&quot; |
| PAUSED | &quot;paused&quot; |
| INCOMPLETE | &quot;incomplete&quot; |
| OTHER | &quot;other&quot; |



