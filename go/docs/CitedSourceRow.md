# CitedSourceRow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GroupKey** | **string** |  | 
**Domain** | Pointer to **NullableString** |  | [optional] 
**CitationCount** | **int32** |  | 
**DistinctQueryCount** | **int32** |  | 
**DistinctResponseCount** | **int32** |  | 
**AvgPosition** | Pointer to **NullableFloat32** |  | [optional] 
**SampleTitle** | Pointer to **NullableString** |  | [optional] 
**SampleUrl** | **string** |  | 

## Methods

### NewCitedSourceRow

`func NewCitedSourceRow(groupKey string, citationCount int32, distinctQueryCount int32, distinctResponseCount int32, sampleUrl string, ) *CitedSourceRow`

NewCitedSourceRow instantiates a new CitedSourceRow object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCitedSourceRowWithDefaults

`func NewCitedSourceRowWithDefaults() *CitedSourceRow`

NewCitedSourceRowWithDefaults instantiates a new CitedSourceRow object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGroupKey

`func (o *CitedSourceRow) GetGroupKey() string`

GetGroupKey returns the GroupKey field if non-nil, zero value otherwise.

### GetGroupKeyOk

`func (o *CitedSourceRow) GetGroupKeyOk() (*string, bool)`

GetGroupKeyOk returns a tuple with the GroupKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupKey

`func (o *CitedSourceRow) SetGroupKey(v string)`

SetGroupKey sets GroupKey field to given value.


### GetDomain

`func (o *CitedSourceRow) GetDomain() string`

GetDomain returns the Domain field if non-nil, zero value otherwise.

### GetDomainOk

`func (o *CitedSourceRow) GetDomainOk() (*string, bool)`

GetDomainOk returns a tuple with the Domain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomain

`func (o *CitedSourceRow) SetDomain(v string)`

SetDomain sets Domain field to given value.

### HasDomain

`func (o *CitedSourceRow) HasDomain() bool`

HasDomain returns a boolean if a field has been set.

### SetDomainNil

`func (o *CitedSourceRow) SetDomainNil(b bool)`

 SetDomainNil sets the value for Domain to be an explicit nil

### UnsetDomain
`func (o *CitedSourceRow) UnsetDomain()`

UnsetDomain ensures that no value is present for Domain, not even an explicit nil
### GetCitationCount

`func (o *CitedSourceRow) GetCitationCount() int32`

GetCitationCount returns the CitationCount field if non-nil, zero value otherwise.

### GetCitationCountOk

`func (o *CitedSourceRow) GetCitationCountOk() (*int32, bool)`

GetCitationCountOk returns a tuple with the CitationCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCitationCount

`func (o *CitedSourceRow) SetCitationCount(v int32)`

SetCitationCount sets CitationCount field to given value.


### GetDistinctQueryCount

`func (o *CitedSourceRow) GetDistinctQueryCount() int32`

GetDistinctQueryCount returns the DistinctQueryCount field if non-nil, zero value otherwise.

### GetDistinctQueryCountOk

`func (o *CitedSourceRow) GetDistinctQueryCountOk() (*int32, bool)`

GetDistinctQueryCountOk returns a tuple with the DistinctQueryCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDistinctQueryCount

`func (o *CitedSourceRow) SetDistinctQueryCount(v int32)`

SetDistinctQueryCount sets DistinctQueryCount field to given value.


### GetDistinctResponseCount

`func (o *CitedSourceRow) GetDistinctResponseCount() int32`

GetDistinctResponseCount returns the DistinctResponseCount field if non-nil, zero value otherwise.

### GetDistinctResponseCountOk

`func (o *CitedSourceRow) GetDistinctResponseCountOk() (*int32, bool)`

GetDistinctResponseCountOk returns a tuple with the DistinctResponseCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDistinctResponseCount

`func (o *CitedSourceRow) SetDistinctResponseCount(v int32)`

SetDistinctResponseCount sets DistinctResponseCount field to given value.


### GetAvgPosition

`func (o *CitedSourceRow) GetAvgPosition() float32`

GetAvgPosition returns the AvgPosition field if non-nil, zero value otherwise.

### GetAvgPositionOk

`func (o *CitedSourceRow) GetAvgPositionOk() (*float32, bool)`

GetAvgPositionOk returns a tuple with the AvgPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgPosition

`func (o *CitedSourceRow) SetAvgPosition(v float32)`

SetAvgPosition sets AvgPosition field to given value.

### HasAvgPosition

`func (o *CitedSourceRow) HasAvgPosition() bool`

HasAvgPosition returns a boolean if a field has been set.

### SetAvgPositionNil

`func (o *CitedSourceRow) SetAvgPositionNil(b bool)`

 SetAvgPositionNil sets the value for AvgPosition to be an explicit nil

### UnsetAvgPosition
`func (o *CitedSourceRow) UnsetAvgPosition()`

UnsetAvgPosition ensures that no value is present for AvgPosition, not even an explicit nil
### GetSampleTitle

`func (o *CitedSourceRow) GetSampleTitle() string`

GetSampleTitle returns the SampleTitle field if non-nil, zero value otherwise.

### GetSampleTitleOk

`func (o *CitedSourceRow) GetSampleTitleOk() (*string, bool)`

GetSampleTitleOk returns a tuple with the SampleTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSampleTitle

`func (o *CitedSourceRow) SetSampleTitle(v string)`

SetSampleTitle sets SampleTitle field to given value.

### HasSampleTitle

`func (o *CitedSourceRow) HasSampleTitle() bool`

HasSampleTitle returns a boolean if a field has been set.

### SetSampleTitleNil

`func (o *CitedSourceRow) SetSampleTitleNil(b bool)`

 SetSampleTitleNil sets the value for SampleTitle to be an explicit nil

### UnsetSampleTitle
`func (o *CitedSourceRow) UnsetSampleTitle()`

UnsetSampleTitle ensures that no value is present for SampleTitle, not even an explicit nil
### GetSampleUrl

`func (o *CitedSourceRow) GetSampleUrl() string`

GetSampleUrl returns the SampleUrl field if non-nil, zero value otherwise.

### GetSampleUrlOk

`func (o *CitedSourceRow) GetSampleUrlOk() (*string, bool)`

GetSampleUrlOk returns a tuple with the SampleUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSampleUrl

`func (o *CitedSourceRow) SetSampleUrl(v string)`

SetSampleUrl sets SampleUrl field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


