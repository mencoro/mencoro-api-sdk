# GetOrganizationOverview200ResponseProjectsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectId** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Status** | Pointer to **string** |  | [optional] 
**TrackedQueryCount** | Pointer to **int32** |  | [optional] 
**ShareOfVoice** | Pointer to **NullableFloat32** | 0-100 percentage share of weighted AI mentions against all tracked brands; higher is better. Null when the project has no rank data yet. | [optional] 
**MentionRate** | Pointer to **NullableInt32** | 0-100 percentage of tracked queries with a result; higher is better. Null when the project has no rank data yet. | [optional] 
**AvgMentionPosition** | Pointer to **NullableFloat32** | 1-based average rank of the brand within the answer; LOWER is better. Null when the project has no rank data yet. | [optional] 
**PositivityIndex** | Pointer to **NullableInt32** | 0-100 sentiment score; higher is better. Null when the project has no rank data yet. | [optional] 

## Methods

### NewGetOrganizationOverview200ResponseProjectsInner

`func NewGetOrganizationOverview200ResponseProjectsInner() *GetOrganizationOverview200ResponseProjectsInner`

NewGetOrganizationOverview200ResponseProjectsInner instantiates a new GetOrganizationOverview200ResponseProjectsInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetOrganizationOverview200ResponseProjectsInnerWithDefaults

`func NewGetOrganizationOverview200ResponseProjectsInnerWithDefaults() *GetOrganizationOverview200ResponseProjectsInner`

NewGetOrganizationOverview200ResponseProjectsInnerWithDefaults instantiates a new GetOrganizationOverview200ResponseProjectsInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjectId

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *GetOrganizationOverview200ResponseProjectsInner) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### GetName

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *GetOrganizationOverview200ResponseProjectsInner) HasName() bool`

HasName returns a boolean if a field has been set.

### GetStatus

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *GetOrganizationOverview200ResponseProjectsInner) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetTrackedQueryCount

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetTrackedQueryCount() int32`

GetTrackedQueryCount returns the TrackedQueryCount field if non-nil, zero value otherwise.

### GetTrackedQueryCountOk

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetTrackedQueryCountOk() (*int32, bool)`

GetTrackedQueryCountOk returns a tuple with the TrackedQueryCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryCount

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetTrackedQueryCount(v int32)`

SetTrackedQueryCount sets TrackedQueryCount field to given value.

### HasTrackedQueryCount

`func (o *GetOrganizationOverview200ResponseProjectsInner) HasTrackedQueryCount() bool`

HasTrackedQueryCount returns a boolean if a field has been set.

### GetShareOfVoice

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetShareOfVoice() float32`

GetShareOfVoice returns the ShareOfVoice field if non-nil, zero value otherwise.

### GetShareOfVoiceOk

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetShareOfVoiceOk() (*float32, bool)`

GetShareOfVoiceOk returns a tuple with the ShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShareOfVoice

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetShareOfVoice(v float32)`

SetShareOfVoice sets ShareOfVoice field to given value.

### HasShareOfVoice

`func (o *GetOrganizationOverview200ResponseProjectsInner) HasShareOfVoice() bool`

HasShareOfVoice returns a boolean if a field has been set.

### SetShareOfVoiceNil

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetShareOfVoiceNil(b bool)`

 SetShareOfVoiceNil sets the value for ShareOfVoice to be an explicit nil

### UnsetShareOfVoice
`func (o *GetOrganizationOverview200ResponseProjectsInner) UnsetShareOfVoice()`

UnsetShareOfVoice ensures that no value is present for ShareOfVoice, not even an explicit nil
### GetMentionRate

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetMentionRate() int32`

GetMentionRate returns the MentionRate field if non-nil, zero value otherwise.

### GetMentionRateOk

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetMentionRateOk() (*int32, bool)`

GetMentionRateOk returns a tuple with the MentionRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionRate

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetMentionRate(v int32)`

SetMentionRate sets MentionRate field to given value.

### HasMentionRate

`func (o *GetOrganizationOverview200ResponseProjectsInner) HasMentionRate() bool`

HasMentionRate returns a boolean if a field has been set.

### SetMentionRateNil

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetMentionRateNil(b bool)`

 SetMentionRateNil sets the value for MentionRate to be an explicit nil

### UnsetMentionRate
`func (o *GetOrganizationOverview200ResponseProjectsInner) UnsetMentionRate()`

UnsetMentionRate ensures that no value is present for MentionRate, not even an explicit nil
### GetAvgMentionPosition

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetAvgMentionPosition() float32`

GetAvgMentionPosition returns the AvgMentionPosition field if non-nil, zero value otherwise.

### GetAvgMentionPositionOk

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetAvgMentionPositionOk() (*float32, bool)`

GetAvgMentionPositionOk returns a tuple with the AvgMentionPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgMentionPosition

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetAvgMentionPosition(v float32)`

SetAvgMentionPosition sets AvgMentionPosition field to given value.

### HasAvgMentionPosition

`func (o *GetOrganizationOverview200ResponseProjectsInner) HasAvgMentionPosition() bool`

HasAvgMentionPosition returns a boolean if a field has been set.

### SetAvgMentionPositionNil

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetAvgMentionPositionNil(b bool)`

 SetAvgMentionPositionNil sets the value for AvgMentionPosition to be an explicit nil

### UnsetAvgMentionPosition
`func (o *GetOrganizationOverview200ResponseProjectsInner) UnsetAvgMentionPosition()`

UnsetAvgMentionPosition ensures that no value is present for AvgMentionPosition, not even an explicit nil
### GetPositivityIndex

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetPositivityIndex() int32`

GetPositivityIndex returns the PositivityIndex field if non-nil, zero value otherwise.

### GetPositivityIndexOk

`func (o *GetOrganizationOverview200ResponseProjectsInner) GetPositivityIndexOk() (*int32, bool)`

GetPositivityIndexOk returns a tuple with the PositivityIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositivityIndex

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetPositivityIndex(v int32)`

SetPositivityIndex sets PositivityIndex field to given value.

### HasPositivityIndex

`func (o *GetOrganizationOverview200ResponseProjectsInner) HasPositivityIndex() bool`

HasPositivityIndex returns a boolean if a field has been set.

### SetPositivityIndexNil

`func (o *GetOrganizationOverview200ResponseProjectsInner) SetPositivityIndexNil(b bool)`

 SetPositivityIndexNil sets the value for PositivityIndex to be an explicit nil

### UnsetPositivityIndex
`func (o *GetOrganizationOverview200ResponseProjectsInner) UnsetPositivityIndex()`

UnsetPositivityIndex ensures that no value is present for PositivityIndex, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


