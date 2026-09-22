# Mencoro::SubscriptionResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **status** | **String** | Contract state. \&quot;none\&quot; when the organization has never held a subscription. |  |
| **tier_code** | **String** | Public tier identifier derived from the check budget. | [optional] |
| **billing_cycle_type** | **String** | Billing interval of the contract. | [optional] |
| **billing_cycle_anchor** | **Time** | Instant the billing cycle is anchored to. | [optional] |
| **check_budget** | **Integer** | Checks the current cycle grants. Null when there is no subscription, never a stand-in for zero. | [optional] |
| **checks_consumed** | **Integer** | Checks consumed so far in the current cycle. Null when there is no subscription; zero means none consumed yet. | [optional] |
| **checks_available** | **Integer** | Checks still available in the current cycle. Null when there is no subscription; zero means the budget is exhausted. | [optional] |
| **next_reset_at** | **Time** | When the check budget resets next. | [optional] |
| **cancelled_at** | **Time** | When the subscription was terminally cancelled. Null while it has not been. | [optional] |
| **scheduled_to_cancel_at** | **Time** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. | [optional] |
| **grace_period_ends_at** | **Time** | When paid access ends after a cancellation. Null when the subscription is not cancelled. | [optional] |
| **deactivation_reason** | **String** | Why the subscription is currently inactive. Null for an active subscription, and meaningless once \&quot;cancelledAt\&quot; is set - the cancellation supersedes it. | [optional] |
| **is_entitled** | **Boolean** | Whether the organization may use paid features right now: active, or cancelled but still inside its paid grace window. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::SubscriptionResource.new(
  status: null,
  tier_code: tier_2000,
  billing_cycle_type: null,
  billing_cycle_anchor: null,
  check_budget: null,
  checks_consumed: null,
  checks_available: null,
  next_reset_at: null,
  cancelled_at: null,
  scheduled_to_cancel_at: null,
  grace_period_ends_at: null,
  deactivation_reason: null,
  is_entitled: null
)
```

