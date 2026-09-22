# Mencoro::TrackedQueryUsageResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tracked_query_count** | **Integer** | Tracked queries across every project of the organization, archived projects included, counting active and paused queries alike. Never null; 0 means none are configured. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::TrackedQueryUsageResource.new(
  tracked_query_count: 124
)
```

