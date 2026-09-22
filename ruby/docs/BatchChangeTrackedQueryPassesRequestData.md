# Mencoro::BatchChangeTrackedQueryPassesRequestData

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | **Array&lt;String&gt;** | Ids of the tracked queries to change. Duplicates are collapsed. |  |
| **n_passes** | **Integer** | Passes run per check. Only an AI engine accepts more than one; a non-AI target is reported under \&quot;failed\&quot;. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BatchChangeTrackedQueryPassesRequestData.new(
  ids: null,
  n_passes: null
)
```

