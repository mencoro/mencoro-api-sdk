# Mencoro::TrackedQueryCountResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **count** | **Integer** | Tracked queries in the project matching the status filter. Every status when none was sent. |  |
| **check_cost** | **Integer** | Budget cost of force-checking exactly those tracked queries, in check budget units: the sum of each one&#39;s configured passes. One unit per pass, the same unit the plan allowance is counted in. Reserves nothing and debits nothing. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::TrackedQueryCountResource.new(
  count: 42,
  check_cost: 96
)
```

