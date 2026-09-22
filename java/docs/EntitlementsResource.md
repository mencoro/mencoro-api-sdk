

# EntitlementsResource

What an organization's plan allows and what it has consumed

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | \&quot;none\&quot; when the organization has never had a subscription contract. |  |
|**isEntitled** | **Boolean** | Whether the organization may use paid features right now: an active contract, or a cancelled one still inside its paid grace window. |  |
|**checkBudget** | **Integer** | Checks the current cycle allows. Null when there is no plan on file, which is not the same as a budget of zero. |  [optional] |
|**checksConsumed** | **Integer** | Checks consumed so far in the current cycle. Null when there is no plan on file. |  [optional] |
|**checksAvailable** | **Integer** | Checks left in the current cycle. Null when there is no plan on file. |  [optional] |
|**billingCycleType** | [**BillingCycleTypeEnum**](#BillingCycleTypeEnum) | How often the allowance renews. Null when there is no plan on file. |  [optional] |
|**billingCycleAnchor** | **OffsetDateTime** | Start of the current cycle. Null when there is no plan on file. |  [optional] |
|**nextResetAt** | **OffsetDateTime** | When the check budget next resets. Null when there is no plan on file. |  [optional] |
|**cancelledAt** | **OffsetDateTime** | When the subscription was terminally cancelled. Null while it has not been. |  [optional] |
|**scheduledToCancelAt** | **OffsetDateTime** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. |  [optional] |
|**gracePeriodEndsAt** | **OffsetDateTime** | When paid access ends after a cancellation. Null when the subscription has not been cancelled. |  [optional] |



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



