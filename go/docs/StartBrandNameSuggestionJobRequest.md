# StartBrandNameSuggestionJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | The display name of the entity to find aliases for. | 
**WebsiteDomains** | **[]string** | The entity website domains. At least one is required: the web search is grounded on them, and without one the name alone is ambiguous. Duplicates are collapsed, after the entry count has been checked against maxItems. | 
**EnteredBrandNames** | Pointer to **[]string** | Names already known, excluded from the suggestions. Duplicates are collapsed, after the entry count has been checked against maxItems. | [optional] 
**Country** | Pointer to **NullableString** | ISO 3166-1 alpha-2 country used to localize the web search. | [optional] 

## Methods

### NewStartBrandNameSuggestionJobRequest

`func NewStartBrandNameSuggestionJobRequest(name string, websiteDomains []string, ) *StartBrandNameSuggestionJobRequest`

NewStartBrandNameSuggestionJobRequest instantiates a new StartBrandNameSuggestionJobRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStartBrandNameSuggestionJobRequestWithDefaults

`func NewStartBrandNameSuggestionJobRequestWithDefaults() *StartBrandNameSuggestionJobRequest`

NewStartBrandNameSuggestionJobRequestWithDefaults instantiates a new StartBrandNameSuggestionJobRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *StartBrandNameSuggestionJobRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *StartBrandNameSuggestionJobRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *StartBrandNameSuggestionJobRequest) SetName(v string)`

SetName sets Name field to given value.


### GetWebsiteDomains

`func (o *StartBrandNameSuggestionJobRequest) GetWebsiteDomains() []string`

GetWebsiteDomains returns the WebsiteDomains field if non-nil, zero value otherwise.

### GetWebsiteDomainsOk

`func (o *StartBrandNameSuggestionJobRequest) GetWebsiteDomainsOk() (*[]string, bool)`

GetWebsiteDomainsOk returns a tuple with the WebsiteDomains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsiteDomains

`func (o *StartBrandNameSuggestionJobRequest) SetWebsiteDomains(v []string)`

SetWebsiteDomains sets WebsiteDomains field to given value.


### GetEnteredBrandNames

`func (o *StartBrandNameSuggestionJobRequest) GetEnteredBrandNames() []string`

GetEnteredBrandNames returns the EnteredBrandNames field if non-nil, zero value otherwise.

### GetEnteredBrandNamesOk

`func (o *StartBrandNameSuggestionJobRequest) GetEnteredBrandNamesOk() (*[]string, bool)`

GetEnteredBrandNamesOk returns a tuple with the EnteredBrandNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnteredBrandNames

`func (o *StartBrandNameSuggestionJobRequest) SetEnteredBrandNames(v []string)`

SetEnteredBrandNames sets EnteredBrandNames field to given value.

### HasEnteredBrandNames

`func (o *StartBrandNameSuggestionJobRequest) HasEnteredBrandNames() bool`

HasEnteredBrandNames returns a boolean if a field has been set.

### GetCountry

`func (o *StartBrandNameSuggestionJobRequest) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *StartBrandNameSuggestionJobRequest) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *StartBrandNameSuggestionJobRequest) SetCountry(v string)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *StartBrandNameSuggestionJobRequest) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### SetCountryNil

`func (o *StartBrandNameSuggestionJobRequest) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *StartBrandNameSuggestionJobRequest) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


