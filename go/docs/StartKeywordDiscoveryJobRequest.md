# StartKeywordDiscoveryJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Input** | **string** | Free text describing the keywords or topics to expand. | 
**Language** | Pointer to **NullableString** | Language code. Omit to let the provider detect it from the input. | [optional] 
**Country** | Pointer to **NullableString** | ISO 3166-1 alpha-2 country. Omit to let the provider infer it. | [optional] 
**ExcludeQueries** | Pointer to **[]string** | Extra queries to keep out of the suggestions for this run. Duplicates are collapsed, after the entry count has been checked against maxItems. The project tracked queries are excluded whether or not this is sent. | [optional] 

## Methods

### NewStartKeywordDiscoveryJobRequest

`func NewStartKeywordDiscoveryJobRequest(input string, ) *StartKeywordDiscoveryJobRequest`

NewStartKeywordDiscoveryJobRequest instantiates a new StartKeywordDiscoveryJobRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStartKeywordDiscoveryJobRequestWithDefaults

`func NewStartKeywordDiscoveryJobRequestWithDefaults() *StartKeywordDiscoveryJobRequest`

NewStartKeywordDiscoveryJobRequestWithDefaults instantiates a new StartKeywordDiscoveryJobRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInput

`func (o *StartKeywordDiscoveryJobRequest) GetInput() string`

GetInput returns the Input field if non-nil, zero value otherwise.

### GetInputOk

`func (o *StartKeywordDiscoveryJobRequest) GetInputOk() (*string, bool)`

GetInputOk returns a tuple with the Input field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInput

`func (o *StartKeywordDiscoveryJobRequest) SetInput(v string)`

SetInput sets Input field to given value.


### GetLanguage

`func (o *StartKeywordDiscoveryJobRequest) GetLanguage() string`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *StartKeywordDiscoveryJobRequest) GetLanguageOk() (*string, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *StartKeywordDiscoveryJobRequest) SetLanguage(v string)`

SetLanguage sets Language field to given value.

### HasLanguage

`func (o *StartKeywordDiscoveryJobRequest) HasLanguage() bool`

HasLanguage returns a boolean if a field has been set.

### SetLanguageNil

`func (o *StartKeywordDiscoveryJobRequest) SetLanguageNil(b bool)`

 SetLanguageNil sets the value for Language to be an explicit nil

### UnsetLanguage
`func (o *StartKeywordDiscoveryJobRequest) UnsetLanguage()`

UnsetLanguage ensures that no value is present for Language, not even an explicit nil
### GetCountry

`func (o *StartKeywordDiscoveryJobRequest) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *StartKeywordDiscoveryJobRequest) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *StartKeywordDiscoveryJobRequest) SetCountry(v string)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *StartKeywordDiscoveryJobRequest) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### SetCountryNil

`func (o *StartKeywordDiscoveryJobRequest) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *StartKeywordDiscoveryJobRequest) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetExcludeQueries

`func (o *StartKeywordDiscoveryJobRequest) GetExcludeQueries() []string`

GetExcludeQueries returns the ExcludeQueries field if non-nil, zero value otherwise.

### GetExcludeQueriesOk

`func (o *StartKeywordDiscoveryJobRequest) GetExcludeQueriesOk() (*[]string, bool)`

GetExcludeQueriesOk returns a tuple with the ExcludeQueries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeQueries

`func (o *StartKeywordDiscoveryJobRequest) SetExcludeQueries(v []string)`

SetExcludeQueries sets ExcludeQueries field to given value.

### HasExcludeQueries

`func (o *StartKeywordDiscoveryJobRequest) HasExcludeQueries() bool`

HasExcludeQueries returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


