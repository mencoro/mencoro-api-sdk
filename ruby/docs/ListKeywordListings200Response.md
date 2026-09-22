# Mencoro::ListKeywordListings200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **items** | [**Array&lt;KeywordListingResource&gt;**](KeywordListingResource.md) |  | [optional] |
| **total** | **Integer** | Keywords matching the filters, not the size of this page. | [optional] |
| **total_variant_count** | **Integer** | Tracked queries behind the keywords matching every filter EXCEPT &#x60;search&#x60;. With a text search applied this still counts the whole project, so it is not a budget figure for a searched page. | [optional] |
| **data_dirty_since** | **Time** | When a pending recalculation was triggered. Null when the metrics are up to date. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ListKeywordListings200Response.new(
  items: null,
  total: null,
  total_variant_count: null,
  data_dirty_since: null
)
```

