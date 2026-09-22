# Mencoro::ShoppingSnapshotResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **project_id** | **String** | The project this capture belongs to |  |
| **tracked_query_id** | **String** | The tracked query that was searched |  |
| **engine** | **String** | The shopping surface that was captured |  |
| **offers** | [**Array&lt;ShoppingOfferResource&gt;**](ShoppingOfferResource.md) | Offers in rank order |  |
| **captured_at** | **Time** | When the page was captured, UTC |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ShoppingSnapshotResource.new(
  id: null,
  project_id: null,
  tracked_query_id: null,
  engine: null,
  offers: null,
  captured_at: null
)
```

