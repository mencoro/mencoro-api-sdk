# ShoppingOfferResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** | Rank on the captured page, starting at 1 |
**title** | **string** | Product title as the marketplace showed it |
**product_url** | **string** | Link to the offer |
**seller_name** | **string** | Seller name as the marketplace showed it |
**seller_domain** | **string** | Seller host, when the marketplace reported one | [optional]
**product_id** | **string** | The marketplace&#39;s own identifier for this listing, not a Mencoro id |
**thumbnail_url** | **string** | Product image the marketplace showed, when it showed one | [optional]
**price** | **float** | Price as shown at capture time: no tax normalisation, no shipping, no conversion |
**currency** | **string** | ISO-4217 currency of price. May differ between offers in one snapshot |
**rating** | **float** | Star rating shown for the offer, when there was one | [optional]
**rating_votes** | **int** | Number of votes behind rating, when the marketplace reported one | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
