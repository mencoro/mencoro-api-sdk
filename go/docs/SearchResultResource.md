# SearchResultResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Position** | **int32** | Rank on the captured page, starting at 1 | 
**Url** | **string** | The result URL as captured, redirector included when unresolved is true | 
**Title** | Pointer to **NullableString** | Result title, when the page showed one | [optional] 
**Snippet** | Pointer to **NullableString** | Result snippet, when the page showed one | [optional] 
**Domain** | Pointer to **NullableString** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true | [optional] 
**Rating** | Pointer to **NullableFloat32** | Star rating shown in the rich result, when there was one | [optional] 
**RatingVotes** | Pointer to **NullableInt32** | Number of votes behind rating, when the rich result reported one | [optional] 
**Unresolved** | **bool** | True when url still points at a redirector: count the result, do not attribute the domain | 

## Methods

### NewSearchResultResource

`func NewSearchResultResource(position int32, url string, unresolved bool, ) *SearchResultResource`

NewSearchResultResource instantiates a new SearchResultResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSearchResultResourceWithDefaults

`func NewSearchResultResourceWithDefaults() *SearchResultResource`

NewSearchResultResourceWithDefaults instantiates a new SearchResultResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPosition

`func (o *SearchResultResource) GetPosition() int32`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *SearchResultResource) GetPositionOk() (*int32, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *SearchResultResource) SetPosition(v int32)`

SetPosition sets Position field to given value.


### GetUrl

`func (o *SearchResultResource) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SearchResultResource) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SearchResultResource) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetTitle

`func (o *SearchResultResource) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *SearchResultResource) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *SearchResultResource) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *SearchResultResource) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### SetTitleNil

`func (o *SearchResultResource) SetTitleNil(b bool)`

 SetTitleNil sets the value for Title to be an explicit nil

### UnsetTitle
`func (o *SearchResultResource) UnsetTitle()`

UnsetTitle ensures that no value is present for Title, not even an explicit nil
### GetSnippet

`func (o *SearchResultResource) GetSnippet() string`

GetSnippet returns the Snippet field if non-nil, zero value otherwise.

### GetSnippetOk

`func (o *SearchResultResource) GetSnippetOk() (*string, bool)`

GetSnippetOk returns a tuple with the Snippet field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSnippet

`func (o *SearchResultResource) SetSnippet(v string)`

SetSnippet sets Snippet field to given value.

### HasSnippet

`func (o *SearchResultResource) HasSnippet() bool`

HasSnippet returns a boolean if a field has been set.

### SetSnippetNil

`func (o *SearchResultResource) SetSnippetNil(b bool)`

 SetSnippetNil sets the value for Snippet to be an explicit nil

### UnsetSnippet
`func (o *SearchResultResource) UnsetSnippet()`

UnsetSnippet ensures that no value is present for Snippet, not even an explicit nil
### GetDomain

`func (o *SearchResultResource) GetDomain() string`

GetDomain returns the Domain field if non-nil, zero value otherwise.

### GetDomainOk

`func (o *SearchResultResource) GetDomainOk() (*string, bool)`

GetDomainOk returns a tuple with the Domain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomain

`func (o *SearchResultResource) SetDomain(v string)`

SetDomain sets Domain field to given value.

### HasDomain

`func (o *SearchResultResource) HasDomain() bool`

HasDomain returns a boolean if a field has been set.

### SetDomainNil

`func (o *SearchResultResource) SetDomainNil(b bool)`

 SetDomainNil sets the value for Domain to be an explicit nil

### UnsetDomain
`func (o *SearchResultResource) UnsetDomain()`

UnsetDomain ensures that no value is present for Domain, not even an explicit nil
### GetRating

`func (o *SearchResultResource) GetRating() float32`

GetRating returns the Rating field if non-nil, zero value otherwise.

### GetRatingOk

`func (o *SearchResultResource) GetRatingOk() (*float32, bool)`

GetRatingOk returns a tuple with the Rating field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRating

`func (o *SearchResultResource) SetRating(v float32)`

SetRating sets Rating field to given value.

### HasRating

`func (o *SearchResultResource) HasRating() bool`

HasRating returns a boolean if a field has been set.

### SetRatingNil

`func (o *SearchResultResource) SetRatingNil(b bool)`

 SetRatingNil sets the value for Rating to be an explicit nil

### UnsetRating
`func (o *SearchResultResource) UnsetRating()`

UnsetRating ensures that no value is present for Rating, not even an explicit nil
### GetRatingVotes

`func (o *SearchResultResource) GetRatingVotes() int32`

GetRatingVotes returns the RatingVotes field if non-nil, zero value otherwise.

### GetRatingVotesOk

`func (o *SearchResultResource) GetRatingVotesOk() (*int32, bool)`

GetRatingVotesOk returns a tuple with the RatingVotes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRatingVotes

`func (o *SearchResultResource) SetRatingVotes(v int32)`

SetRatingVotes sets RatingVotes field to given value.

### HasRatingVotes

`func (o *SearchResultResource) HasRatingVotes() bool`

HasRatingVotes returns a boolean if a field has been set.

### SetRatingVotesNil

`func (o *SearchResultResource) SetRatingVotesNil(b bool)`

 SetRatingVotesNil sets the value for RatingVotes to be an explicit nil

### UnsetRatingVotes
`func (o *SearchResultResource) UnsetRatingVotes()`

UnsetRatingVotes ensures that no value is present for RatingVotes, not even an explicit nil
### GetUnresolved

`func (o *SearchResultResource) GetUnresolved() bool`

GetUnresolved returns the Unresolved field if non-nil, zero value otherwise.

### GetUnresolvedOk

`func (o *SearchResultResource) GetUnresolvedOk() (*bool, bool)`

GetUnresolvedOk returns a tuple with the Unresolved field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnresolved

`func (o *SearchResultResource) SetUnresolved(v bool)`

SetUnresolved sets Unresolved field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


