# Mencoro::ListShoppingSnapshots200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **items** | [**Array&lt;ShoppingSnapshotResource&gt;**](ShoppingSnapshotResource.md) |  | [optional] |
| **total** | **Integer** | Captures matching the filter, not the size of this page | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ListShoppingSnapshots200Response.new(
  items: null,
  total: null
)
```

