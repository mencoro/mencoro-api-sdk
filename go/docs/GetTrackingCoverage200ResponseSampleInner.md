# GetTrackingCoverage200ResponseSampleInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackedQueryId** | Pointer to **string** |  | [optional] 
**QueryText** | Pointer to **string** |  | [optional] 
**Engine** | Pointer to **string** |  | [optional] 
**Country** | Pointer to **string** | ISO-3166 alpha-2 code | [optional] 
**CheckFrequency** | Pointer to **string** |  | [optional] 
**LastCheckedAt** | Pointer to **NullableTime** | RFC 3339 timestamp of the last check. Null means never checked, which this sample never contains. | [optional] 

## Methods

### NewGetTrackingCoverage200ResponseSampleInner

`func NewGetTrackingCoverage200ResponseSampleInner() *GetTrackingCoverage200ResponseSampleInner`

NewGetTrackingCoverage200ResponseSampleInner instantiates a new GetTrackingCoverage200ResponseSampleInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetTrackingCoverage200ResponseSampleInnerWithDefaults

`func NewGetTrackingCoverage200ResponseSampleInnerWithDefaults() *GetTrackingCoverage200ResponseSampleInner`

NewGetTrackingCoverage200ResponseSampleInnerWithDefaults instantiates a new GetTrackingCoverage200ResponseSampleInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTrackedQueryId

`func (o *GetTrackingCoverage200ResponseSampleInner) GetTrackedQueryId() string`

GetTrackedQueryId returns the TrackedQueryId field if non-nil, zero value otherwise.

### GetTrackedQueryIdOk

`func (o *GetTrackingCoverage200ResponseSampleInner) GetTrackedQueryIdOk() (*string, bool)`

GetTrackedQueryIdOk returns a tuple with the TrackedQueryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryId

`func (o *GetTrackingCoverage200ResponseSampleInner) SetTrackedQueryId(v string)`

SetTrackedQueryId sets TrackedQueryId field to given value.

### HasTrackedQueryId

`func (o *GetTrackingCoverage200ResponseSampleInner) HasTrackedQueryId() bool`

HasTrackedQueryId returns a boolean if a field has been set.

### GetQueryText

`func (o *GetTrackingCoverage200ResponseSampleInner) GetQueryText() string`

GetQueryText returns the QueryText field if non-nil, zero value otherwise.

### GetQueryTextOk

`func (o *GetTrackingCoverage200ResponseSampleInner) GetQueryTextOk() (*string, bool)`

GetQueryTextOk returns a tuple with the QueryText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryText

`func (o *GetTrackingCoverage200ResponseSampleInner) SetQueryText(v string)`

SetQueryText sets QueryText field to given value.

### HasQueryText

`func (o *GetTrackingCoverage200ResponseSampleInner) HasQueryText() bool`

HasQueryText returns a boolean if a field has been set.

### GetEngine

`func (o *GetTrackingCoverage200ResponseSampleInner) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *GetTrackingCoverage200ResponseSampleInner) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *GetTrackingCoverage200ResponseSampleInner) SetEngine(v string)`

SetEngine sets Engine field to given value.

### HasEngine

`func (o *GetTrackingCoverage200ResponseSampleInner) HasEngine() bool`

HasEngine returns a boolean if a field has been set.

### GetCountry

`func (o *GetTrackingCoverage200ResponseSampleInner) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *GetTrackingCoverage200ResponseSampleInner) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *GetTrackingCoverage200ResponseSampleInner) SetCountry(v string)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *GetTrackingCoverage200ResponseSampleInner) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### GetCheckFrequency

`func (o *GetTrackingCoverage200ResponseSampleInner) GetCheckFrequency() string`

GetCheckFrequency returns the CheckFrequency field if non-nil, zero value otherwise.

### GetCheckFrequencyOk

`func (o *GetTrackingCoverage200ResponseSampleInner) GetCheckFrequencyOk() (*string, bool)`

GetCheckFrequencyOk returns a tuple with the CheckFrequency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckFrequency

`func (o *GetTrackingCoverage200ResponseSampleInner) SetCheckFrequency(v string)`

SetCheckFrequency sets CheckFrequency field to given value.

### HasCheckFrequency

`func (o *GetTrackingCoverage200ResponseSampleInner) HasCheckFrequency() bool`

HasCheckFrequency returns a boolean if a field has been set.

### GetLastCheckedAt

`func (o *GetTrackingCoverage200ResponseSampleInner) GetLastCheckedAt() time.Time`

GetLastCheckedAt returns the LastCheckedAt field if non-nil, zero value otherwise.

### GetLastCheckedAtOk

`func (o *GetTrackingCoverage200ResponseSampleInner) GetLastCheckedAtOk() (*time.Time, bool)`

GetLastCheckedAtOk returns a tuple with the LastCheckedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastCheckedAt

`func (o *GetTrackingCoverage200ResponseSampleInner) SetLastCheckedAt(v time.Time)`

SetLastCheckedAt sets LastCheckedAt field to given value.

### HasLastCheckedAt

`func (o *GetTrackingCoverage200ResponseSampleInner) HasLastCheckedAt() bool`

HasLastCheckedAt returns a boolean if a field has been set.

### SetLastCheckedAtNil

`func (o *GetTrackingCoverage200ResponseSampleInner) SetLastCheckedAtNil(b bool)`

 SetLastCheckedAtNil sets the value for LastCheckedAt to be an explicit nil

### UnsetLastCheckedAt
`func (o *GetTrackingCoverage200ResponseSampleInner) UnsetLastCheckedAt()`

UnsetLastCheckedAt ensures that no value is present for LastCheckedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


