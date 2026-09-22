# ShoppingOfferResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Rank** | **int32** | Rank on the captured page, starting at 1 | 
**Title** | **string** | Product title as the marketplace showed it | 
**ProductUrl** | **string** | Link to the offer | 
**SellerName** | **string** | Seller name as the marketplace showed it | 
**SellerDomain** | Pointer to **NullableString** | Seller host, when the marketplace reported one | [optional] 
**ProductId** | **string** | The marketplace&#39;s own identifier for this listing, not a Mencoro id | 
**ThumbnailUrl** | Pointer to **NullableString** | Product image the marketplace showed, when it showed one | [optional] 
**Price** | **float32** | Price as shown at capture time: no tax normalisation, no shipping, no conversion | 
**Currency** | **string** | ISO-4217 currency of price. May differ between offers in one snapshot | 
**Rating** | Pointer to **NullableFloat32** | Star rating shown for the offer, when there was one | [optional] 
**RatingVotes** | Pointer to **NullableInt32** | Number of votes behind rating, when the marketplace reported one | [optional] 

## Methods

### NewShoppingOfferResource

`func NewShoppingOfferResource(rank int32, title string, productUrl string, sellerName string, productId string, price float32, currency string, ) *ShoppingOfferResource`

NewShoppingOfferResource instantiates a new ShoppingOfferResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewShoppingOfferResourceWithDefaults

`func NewShoppingOfferResourceWithDefaults() *ShoppingOfferResource`

NewShoppingOfferResourceWithDefaults instantiates a new ShoppingOfferResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRank

`func (o *ShoppingOfferResource) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *ShoppingOfferResource) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *ShoppingOfferResource) SetRank(v int32)`

SetRank sets Rank field to given value.


### GetTitle

`func (o *ShoppingOfferResource) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *ShoppingOfferResource) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *ShoppingOfferResource) SetTitle(v string)`

SetTitle sets Title field to given value.


### GetProductUrl

`func (o *ShoppingOfferResource) GetProductUrl() string`

GetProductUrl returns the ProductUrl field if non-nil, zero value otherwise.

### GetProductUrlOk

`func (o *ShoppingOfferResource) GetProductUrlOk() (*string, bool)`

GetProductUrlOk returns a tuple with the ProductUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProductUrl

`func (o *ShoppingOfferResource) SetProductUrl(v string)`

SetProductUrl sets ProductUrl field to given value.


### GetSellerName

`func (o *ShoppingOfferResource) GetSellerName() string`

GetSellerName returns the SellerName field if non-nil, zero value otherwise.

### GetSellerNameOk

`func (o *ShoppingOfferResource) GetSellerNameOk() (*string, bool)`

GetSellerNameOk returns a tuple with the SellerName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSellerName

`func (o *ShoppingOfferResource) SetSellerName(v string)`

SetSellerName sets SellerName field to given value.


### GetSellerDomain

`func (o *ShoppingOfferResource) GetSellerDomain() string`

GetSellerDomain returns the SellerDomain field if non-nil, zero value otherwise.

### GetSellerDomainOk

`func (o *ShoppingOfferResource) GetSellerDomainOk() (*string, bool)`

GetSellerDomainOk returns a tuple with the SellerDomain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSellerDomain

`func (o *ShoppingOfferResource) SetSellerDomain(v string)`

SetSellerDomain sets SellerDomain field to given value.

### HasSellerDomain

`func (o *ShoppingOfferResource) HasSellerDomain() bool`

HasSellerDomain returns a boolean if a field has been set.

### SetSellerDomainNil

`func (o *ShoppingOfferResource) SetSellerDomainNil(b bool)`

 SetSellerDomainNil sets the value for SellerDomain to be an explicit nil

### UnsetSellerDomain
`func (o *ShoppingOfferResource) UnsetSellerDomain()`

UnsetSellerDomain ensures that no value is present for SellerDomain, not even an explicit nil
### GetProductId

`func (o *ShoppingOfferResource) GetProductId() string`

GetProductId returns the ProductId field if non-nil, zero value otherwise.

### GetProductIdOk

`func (o *ShoppingOfferResource) GetProductIdOk() (*string, bool)`

GetProductIdOk returns a tuple with the ProductId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProductId

`func (o *ShoppingOfferResource) SetProductId(v string)`

SetProductId sets ProductId field to given value.


### GetThumbnailUrl

`func (o *ShoppingOfferResource) GetThumbnailUrl() string`

GetThumbnailUrl returns the ThumbnailUrl field if non-nil, zero value otherwise.

### GetThumbnailUrlOk

`func (o *ShoppingOfferResource) GetThumbnailUrlOk() (*string, bool)`

GetThumbnailUrlOk returns a tuple with the ThumbnailUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThumbnailUrl

`func (o *ShoppingOfferResource) SetThumbnailUrl(v string)`

SetThumbnailUrl sets ThumbnailUrl field to given value.

### HasThumbnailUrl

`func (o *ShoppingOfferResource) HasThumbnailUrl() bool`

HasThumbnailUrl returns a boolean if a field has been set.

### SetThumbnailUrlNil

`func (o *ShoppingOfferResource) SetThumbnailUrlNil(b bool)`

 SetThumbnailUrlNil sets the value for ThumbnailUrl to be an explicit nil

### UnsetThumbnailUrl
`func (o *ShoppingOfferResource) UnsetThumbnailUrl()`

UnsetThumbnailUrl ensures that no value is present for ThumbnailUrl, not even an explicit nil
### GetPrice

`func (o *ShoppingOfferResource) GetPrice() float32`

GetPrice returns the Price field if non-nil, zero value otherwise.

### GetPriceOk

`func (o *ShoppingOfferResource) GetPriceOk() (*float32, bool)`

GetPriceOk returns a tuple with the Price field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrice

`func (o *ShoppingOfferResource) SetPrice(v float32)`

SetPrice sets Price field to given value.


### GetCurrency

`func (o *ShoppingOfferResource) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *ShoppingOfferResource) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *ShoppingOfferResource) SetCurrency(v string)`

SetCurrency sets Currency field to given value.


### GetRating

`func (o *ShoppingOfferResource) GetRating() float32`

GetRating returns the Rating field if non-nil, zero value otherwise.

### GetRatingOk

`func (o *ShoppingOfferResource) GetRatingOk() (*float32, bool)`

GetRatingOk returns a tuple with the Rating field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRating

`func (o *ShoppingOfferResource) SetRating(v float32)`

SetRating sets Rating field to given value.

### HasRating

`func (o *ShoppingOfferResource) HasRating() bool`

HasRating returns a boolean if a field has been set.

### SetRatingNil

`func (o *ShoppingOfferResource) SetRatingNil(b bool)`

 SetRatingNil sets the value for Rating to be an explicit nil

### UnsetRating
`func (o *ShoppingOfferResource) UnsetRating()`

UnsetRating ensures that no value is present for Rating, not even an explicit nil
### GetRatingVotes

`func (o *ShoppingOfferResource) GetRatingVotes() int32`

GetRatingVotes returns the RatingVotes field if non-nil, zero value otherwise.

### GetRatingVotesOk

`func (o *ShoppingOfferResource) GetRatingVotesOk() (*int32, bool)`

GetRatingVotesOk returns a tuple with the RatingVotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRatingVotes

`func (o *ShoppingOfferResource) SetRatingVotes(v int32)`

SetRatingVotes sets RatingVotes field to given value.

### HasRatingVotes

`func (o *ShoppingOfferResource) HasRatingVotes() bool`

HasRatingVotes returns a boolean if a field has been set.

### SetRatingVotesNil

`func (o *ShoppingOfferResource) SetRatingVotesNil(b bool)`

 SetRatingVotesNil sets the value for RatingVotes to be an explicit nil

### UnsetRatingVotes
`func (o *ShoppingOfferResource) UnsetRatingVotes()`

UnsetRatingVotes ensures that no value is present for RatingVotes, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


