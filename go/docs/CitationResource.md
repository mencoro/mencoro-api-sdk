# CitationResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **string** | The URL exactly as the engine cited it, redirector included when unresolved is true | 
**Position** | **int32** | Place within this answer, starting at 1 | 
**AnchorText** | Pointer to **NullableString** | The visible link text, when the engine provided one | [optional] 
**Title** | Pointer to **NullableString** | Title of the cited page, when the engine provided one | [optional] 
**Snippet** | Pointer to **NullableString** | Excerpt the engine showed for this source, when it provided one | [optional] 
**PublicationDate** | Pointer to **NullableString** | Publication date the engine reported, when it provided one | [optional] 
**ThumbnailUrl** | Pointer to **NullableString** | Preview image the engine showed for this source, when it provided one | [optional] 
**Domain** | Pointer to **NullableString** | Host of url. Belongs to the redirector, not the publisher, when unresolved is true | [optional] 
**SourceName** | Pointer to **NullableString** | Publisher name the engine reported, when it provided one | [optional] 
**Unresolved** | **bool** | True when url still points at a redirector: count the citation, do not attribute the domain | 

## Methods

### NewCitationResource

`func NewCitationResource(url string, position int32, unresolved bool, ) *CitationResource`

NewCitationResource instantiates a new CitationResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCitationResourceWithDefaults

`func NewCitationResourceWithDefaults() *CitationResource`

NewCitationResourceWithDefaults instantiates a new CitationResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUrl

`func (o *CitationResource) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *CitationResource) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *CitationResource) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetPosition

`func (o *CitationResource) GetPosition() int32`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *CitationResource) GetPositionOk() (*int32, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *CitationResource) SetPosition(v int32)`

SetPosition sets Position field to given value.


### GetAnchorText

`func (o *CitationResource) GetAnchorText() string`

GetAnchorText returns the AnchorText field if non-nil, zero value otherwise.

### GetAnchorTextOk

`func (o *CitationResource) GetAnchorTextOk() (*string, bool)`

GetAnchorTextOk returns a tuple with the AnchorText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAnchorText

`func (o *CitationResource) SetAnchorText(v string)`

SetAnchorText sets AnchorText field to given value.

### HasAnchorText

`func (o *CitationResource) HasAnchorText() bool`

HasAnchorText returns a boolean if a field has been set.

### SetAnchorTextNil

`func (o *CitationResource) SetAnchorTextNil(b bool)`

 SetAnchorTextNil sets the value for AnchorText to be an explicit nil

### UnsetAnchorText
`func (o *CitationResource) UnsetAnchorText()`

UnsetAnchorText ensures that no value is present for AnchorText, not even an explicit nil
### GetTitle

`func (o *CitationResource) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *CitationResource) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *CitationResource) SetTitle(v string)`

SetTitle sets Title field to given value.

### HasTitle

`func (o *CitationResource) HasTitle() bool`

HasTitle returns a boolean if a field has been set.

### SetTitleNil

`func (o *CitationResource) SetTitleNil(b bool)`

 SetTitleNil sets the value for Title to be an explicit nil

### UnsetTitle
`func (o *CitationResource) UnsetTitle()`

UnsetTitle ensures that no value is present for Title, not even an explicit nil
### GetSnippet

`func (o *CitationResource) GetSnippet() string`

GetSnippet returns the Snippet field if non-nil, zero value otherwise.

### GetSnippetOk

`func (o *CitationResource) GetSnippetOk() (*string, bool)`

GetSnippetOk returns a tuple with the Snippet field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSnippet

`func (o *CitationResource) SetSnippet(v string)`

SetSnippet sets Snippet field to given value.

### HasSnippet

`func (o *CitationResource) HasSnippet() bool`

HasSnippet returns a boolean if a field has been set.

### SetSnippetNil

`func (o *CitationResource) SetSnippetNil(b bool)`

 SetSnippetNil sets the value for Snippet to be an explicit nil

### UnsetSnippet
`func (o *CitationResource) UnsetSnippet()`

UnsetSnippet ensures that no value is present for Snippet, not even an explicit nil
### GetPublicationDate

`func (o *CitationResource) GetPublicationDate() string`

GetPublicationDate returns the PublicationDate field if non-nil, zero value otherwise.

### GetPublicationDateOk

`func (o *CitationResource) GetPublicationDateOk() (*string, bool)`

GetPublicationDateOk returns a tuple with the PublicationDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicationDate

`func (o *CitationResource) SetPublicationDate(v string)`

SetPublicationDate sets PublicationDate field to given value.

### HasPublicationDate

`func (o *CitationResource) HasPublicationDate() bool`

HasPublicationDate returns a boolean if a field has been set.

### SetPublicationDateNil

`func (o *CitationResource) SetPublicationDateNil(b bool)`

 SetPublicationDateNil sets the value for PublicationDate to be an explicit nil

### UnsetPublicationDate
`func (o *CitationResource) UnsetPublicationDate()`

UnsetPublicationDate ensures that no value is present for PublicationDate, not even an explicit nil
### GetThumbnailUrl

`func (o *CitationResource) GetThumbnailUrl() string`

GetThumbnailUrl returns the ThumbnailUrl field if non-nil, zero value otherwise.

### GetThumbnailUrlOk

`func (o *CitationResource) GetThumbnailUrlOk() (*string, bool)`

GetThumbnailUrlOk returns a tuple with the ThumbnailUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThumbnailUrl

`func (o *CitationResource) SetThumbnailUrl(v string)`

SetThumbnailUrl sets ThumbnailUrl field to given value.

### HasThumbnailUrl

`func (o *CitationResource) HasThumbnailUrl() bool`

HasThumbnailUrl returns a boolean if a field has been set.

### SetThumbnailUrlNil

`func (o *CitationResource) SetThumbnailUrlNil(b bool)`

 SetThumbnailUrlNil sets the value for ThumbnailUrl to be an explicit nil

### UnsetThumbnailUrl
`func (o *CitationResource) UnsetThumbnailUrl()`

UnsetThumbnailUrl ensures that no value is present for ThumbnailUrl, not even an explicit nil
### GetDomain

`func (o *CitationResource) GetDomain() string`

GetDomain returns the Domain field if non-nil, zero value otherwise.

### GetDomainOk

`func (o *CitationResource) GetDomainOk() (*string, bool)`

GetDomainOk returns a tuple with the Domain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomain

`func (o *CitationResource) SetDomain(v string)`

SetDomain sets Domain field to given value.

### HasDomain

`func (o *CitationResource) HasDomain() bool`

HasDomain returns a boolean if a field has been set.

### SetDomainNil

`func (o *CitationResource) SetDomainNil(b bool)`

 SetDomainNil sets the value for Domain to be an explicit nil

### UnsetDomain
`func (o *CitationResource) UnsetDomain()`

UnsetDomain ensures that no value is present for Domain, not even an explicit nil
### GetSourceName

`func (o *CitationResource) GetSourceName() string`

GetSourceName returns the SourceName field if non-nil, zero value otherwise.

### GetSourceNameOk

`func (o *CitationResource) GetSourceNameOk() (*string, bool)`

GetSourceNameOk returns a tuple with the SourceName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceName

`func (o *CitationResource) SetSourceName(v string)`

SetSourceName sets SourceName field to given value.

### HasSourceName

`func (o *CitationResource) HasSourceName() bool`

HasSourceName returns a boolean if a field has been set.

### SetSourceNameNil

`func (o *CitationResource) SetSourceNameNil(b bool)`

 SetSourceNameNil sets the value for SourceName to be an explicit nil

### UnsetSourceName
`func (o *CitationResource) UnsetSourceName()`

UnsetSourceName ensures that no value is present for SourceName, not even an explicit nil
### GetUnresolved

`func (o *CitationResource) GetUnresolved() bool`

GetUnresolved returns the Unresolved field if non-nil, zero value otherwise.

### GetUnresolvedOk

`func (o *CitationResource) GetUnresolvedOk() (*bool, bool)`

GetUnresolvedOk returns a tuple with the Unresolved field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnresolved

`func (o *CitationResource) SetUnresolved(v bool)`

SetUnresolved sets Unresolved field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


