# Mencoro::BatchChangeTrackedQueryCheckFrequencyRequestData

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | **Array&lt;String&gt;** | Ids of the tracked queries to change. Duplicates are collapsed. |  |
| **check_frequency** | **String** | How often each query is checked while it is active. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BatchChangeTrackedQueryCheckFrequencyRequestData.new(
  ids: null,
  check_frequency: null
)
```

