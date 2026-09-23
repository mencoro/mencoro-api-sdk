# Mencoro::TrackedQueryMoversResponse

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **rows** | [**Array&lt;TrackedQueryMoverRow&gt;**](TrackedQueryMoverRow.md) |  |  |
| **total** | **Integer** |  |  |
| **data_dirty_since** | **String** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::TrackedQueryMoversResponse.new(
  rows: null,
  total: null,
  data_dirty_since: null
)
```

