# BatchCreateTrackedQueriesRequestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**QueryTexts** | **[]string** | Prompts or keywords to track. Stored lower-cased with whitespace collapsed and leading list markers removed. | 
**Engines** | **[]string** | Engines each text is asked in. | 
**Countries** | **[]string** | ISO 3166-1 alpha-2 countries each text is asked from. | 
**Locale** | Pointer to **NullableString** | ISO 639-1 language the queries are asked in. Omit it to ask the engine without a language. | [optional] 
**CheckFrequency** | **string** | How often every created query is checked. | 
**NPasses** | **int32** | Passes run per check. Applied to AI-engine combinations only: a non-AI engine is always created with 1, whatever is sent here. | 
**QueryClusterIds** | **[]string** | Clusters every created query joins. Must already exist in the project. A combination that is already tracked has these clusters merged into it. | 

## Methods

### NewBatchCreateTrackedQueriesRequestData

`func NewBatchCreateTrackedQueriesRequestData(queryTexts []string, engines []string, countries []string, checkFrequency string, nPasses int32, queryClusterIds []string, ) *BatchCreateTrackedQueriesRequestData`

NewBatchCreateTrackedQueriesRequestData instantiates a new BatchCreateTrackedQueriesRequestData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchCreateTrackedQueriesRequestDataWithDefaults

`func NewBatchCreateTrackedQueriesRequestDataWithDefaults() *BatchCreateTrackedQueriesRequestData`

NewBatchCreateTrackedQueriesRequestDataWithDefaults instantiates a new BatchCreateTrackedQueriesRequestData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetQueryTexts

`func (o *BatchCreateTrackedQueriesRequestData) GetQueryTexts() []string`

GetQueryTexts returns the QueryTexts field if non-nil, zero value otherwise.

### GetQueryTextsOk

`func (o *BatchCreateTrackedQueriesRequestData) GetQueryTextsOk() (*[]string, bool)`

GetQueryTextsOk returns a tuple with the QueryTexts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryTexts

`func (o *BatchCreateTrackedQueriesRequestData) SetQueryTexts(v []string)`

SetQueryTexts sets QueryTexts field to given value.


### GetEngines

`func (o *BatchCreateTrackedQueriesRequestData) GetEngines() []string`

GetEngines returns the Engines field if non-nil, zero value otherwise.

### GetEnginesOk

`func (o *BatchCreateTrackedQueriesRequestData) GetEnginesOk() (*[]string, bool)`

GetEnginesOk returns a tuple with the Engines field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngines

`func (o *BatchCreateTrackedQueriesRequestData) SetEngines(v []string)`

SetEngines sets Engines field to given value.


### GetCountries

`func (o *BatchCreateTrackedQueriesRequestData) GetCountries() []string`

GetCountries returns the Countries field if non-nil, zero value otherwise.

### GetCountriesOk

`func (o *BatchCreateTrackedQueriesRequestData) GetCountriesOk() (*[]string, bool)`

GetCountriesOk returns a tuple with the Countries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountries

`func (o *BatchCreateTrackedQueriesRequestData) SetCountries(v []string)`

SetCountries sets Countries field to given value.


### GetLocale

`func (o *BatchCreateTrackedQueriesRequestData) GetLocale() string`

GetLocale returns the Locale field if non-nil, zero value otherwise.

### GetLocaleOk

`func (o *BatchCreateTrackedQueriesRequestData) GetLocaleOk() (*string, bool)`

GetLocaleOk returns a tuple with the Locale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocale

`func (o *BatchCreateTrackedQueriesRequestData) SetLocale(v string)`

SetLocale sets Locale field to given value.

### HasLocale

`func (o *BatchCreateTrackedQueriesRequestData) HasLocale() bool`

HasLocale returns a boolean if a field has been set.

### SetLocaleNil

`func (o *BatchCreateTrackedQueriesRequestData) SetLocaleNil(b bool)`

 SetLocaleNil sets the value for Locale to be an explicit nil

### UnsetLocale
`func (o *BatchCreateTrackedQueriesRequestData) UnsetLocale()`

UnsetLocale ensures that no value is present for Locale, not even an explicit nil
### GetCheckFrequency

`func (o *BatchCreateTrackedQueriesRequestData) GetCheckFrequency() string`

GetCheckFrequency returns the CheckFrequency field if non-nil, zero value otherwise.

### GetCheckFrequencyOk

`func (o *BatchCreateTrackedQueriesRequestData) GetCheckFrequencyOk() (*string, bool)`

GetCheckFrequencyOk returns a tuple with the CheckFrequency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckFrequency

`func (o *BatchCreateTrackedQueriesRequestData) SetCheckFrequency(v string)`

SetCheckFrequency sets CheckFrequency field to given value.


### GetNPasses

`func (o *BatchCreateTrackedQueriesRequestData) GetNPasses() int32`

GetNPasses returns the NPasses field if non-nil, zero value otherwise.

### GetNPassesOk

`func (o *BatchCreateTrackedQueriesRequestData) GetNPassesOk() (*int32, bool)`

GetNPassesOk returns a tuple with the NPasses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNPasses

`func (o *BatchCreateTrackedQueriesRequestData) SetNPasses(v int32)`

SetNPasses sets NPasses field to given value.


### GetQueryClusterIds

`func (o *BatchCreateTrackedQueriesRequestData) GetQueryClusterIds() []string`

GetQueryClusterIds returns the QueryClusterIds field if non-nil, zero value otherwise.

### GetQueryClusterIdsOk

`func (o *BatchCreateTrackedQueriesRequestData) GetQueryClusterIdsOk() (*[]string, bool)`

GetQueryClusterIdsOk returns a tuple with the QueryClusterIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryClusterIds

`func (o *BatchCreateTrackedQueriesRequestData) SetQueryClusterIds(v []string)`

SetQueryClusterIds sets QueryClusterIds field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


