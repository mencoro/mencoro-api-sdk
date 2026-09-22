# Mencoro.Api.Model.ShoppingOfferResource
One offer of a captured shopping page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Rank** | **int** | Rank on the captured page, starting at 1 | 
**Title** | **string** | Product title as the marketplace showed it | 
**ProductUrl** | **string** | Link to the offer | 
**SellerName** | **string** | Seller name as the marketplace showed it | 
**SellerDomain** | **string** | Seller host, when the marketplace reported one | [optional] 
**ProductId** | **string** | The marketplace&#39;s own identifier for this listing, not a Mencoro id | 
**ThumbnailUrl** | **string** | Product image the marketplace showed, when it showed one | [optional] 
**Price** | **float** | Price as shown at capture time: no tax normalisation, no shipping, no conversion | 
**Currency** | **string** | ISO-4217 currency of price. May differ between offers in one snapshot | 
**Rating** | **float?** | Star rating shown for the offer, when there was one | [optional] 
**RatingVotes** | **int?** | Number of votes behind rating, when the marketplace reported one | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

