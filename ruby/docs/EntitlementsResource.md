# Mencoro::EntitlementsResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **status** | **String** | \&quot;none\&quot; when the organization has never had a subscription contract. |  |
| **is_entitled** | **Boolean** | Whether the organization may use paid features right now: an active contract, or a cancelled one still inside its paid grace window. |  |
| **check_budget** | **Integer** | Checks the current cycle allows. Null when there is no plan on file, which is not the same as a budget of zero. | [optional] |
| **checks_consumed** | **Integer** | Checks consumed so far in the current cycle. Null when there is no plan on file. | [optional] |
| **checks_available** | **Integer** | Checks left in the current cycle. Null when there is no plan on file. | [optional] |
| **billing_cycle_type** | **String** | How often the allowance renews. Null when there is no plan on file. | [optional] |
| **billing_cycle_anchor** | **Time** | Start of the current cycle. Null when there is no plan on file. | [optional] |
| **next_reset_at** | **Time** | When the check budget next resets. Null when there is no plan on file. | [optional] |
| **cancelled_at** | **Time** | When the subscription was terminally cancelled. Null while it has not been. | [optional] |
| **scheduled_to_cancel_at** | **Time** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. | [optional] |
| **grace_period_ends_at** | **Time** | When paid access ends after a cancellation. Null when the subscription has not been cancelled. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::EntitlementsResource.new(
  status: null,
  is_entitled: null,
  check_budget: null,
  checks_consumed: null,
  checks_available: null,
  billing_cycle_type: null,
  billing_cycle_anchor: null,
  next_reset_at: null,
  cancelled_at: null,
  scheduled_to_cancel_at: null,
  grace_period_ends_at: null
)
```

