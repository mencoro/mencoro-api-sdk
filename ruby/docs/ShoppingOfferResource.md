# Mencoro::ShoppingOfferResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **rank** | **Integer** | Rank on the captured page, starting at 1 |  |
| **title** | **String** | Product title as the marketplace showed it |  |
| **product_url** | **String** | Link to the offer |  |
| **seller_name** | **String** | Seller name as the marketplace showed it |  |
| **seller_domain** | **String** | Seller host, when the marketplace reported one | [optional] |
| **product_id** | **String** | The marketplace&#39;s own identifier for this listing, not a Mencoro id |  |
| **thumbnail_url** | **String** | Product image the marketplace showed, when it showed one | [optional] |
| **price** | **Float** | Price as shown at capture time: no tax normalisation, no shipping, no conversion |  |
| **currency** | **String** | ISO-4217 currency of price. May differ between offers in one snapshot |  |
| **rating** | **Float** | Star rating shown for the offer, when there was one | [optional] |
| **rating_votes** | **Integer** | Number of votes behind rating, when the marketplace reported one | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ShoppingOfferResource.new(
  rank: null,
  title: null,
  product_url: null,
  seller_name: null,
  seller_domain: null,
  product_id: null,
  thumbnail_url: null,
  price: null,
  currency: null,
  rating: null,
  rating_votes: null
)
```

