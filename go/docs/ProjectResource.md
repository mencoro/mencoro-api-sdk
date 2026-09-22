# ProjectResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **string** |  | 
**Status** | **string** |  | 
**CreatedAt** | **time.Time** |  | 
**TrackedQueryCount** | **int32** | Number of tracked queries in the project | 
**AvgSerpPosition** | Pointer to **NullableFloat32** | Average position in traditional search results. Null when unknown. | [optional] 
**AvgShoppingPosition** | Pointer to **NullableFloat32** | Average position in shopping results. Null when unknown. | [optional] 
**AvgMentionPosition** | Pointer to **NullableFloat32** | Average position of the brand mention inside AI answers. Null when unknown. | [optional] 
**AvgLinkPosition** | Pointer to **NullableFloat32** | Average position of a cited link to the brand. Null when unknown. | [optional] 
**MentionRate** | Pointer to **NullableInt32** | Share of checks where the brand was mentioned. Null when unknown. | [optional] 
**SerpRate** | Pointer to **NullableInt32** |  | [optional] 
**ShoppingRate** | Pointer to **NullableInt32** |  | [optional] 
**PositivityIndex** | Pointer to **NullableInt32** | Sentiment balance of the brand&#39;s mentions. Null when unknown. | [optional] 
**ShareOfVoice** | Pointer to **NullableFloat32** | Share of voice against the tracked competitors. Null when unknown. | [optional] 
**SerpPositionStability** | Pointer to **NullableFloat32** |  | [optional] 
**ShoppingPositionStability** | Pointer to **NullableFloat32** |  | [optional] 
**LastRankDetectedAt** | Pointer to **NullableTime** | When a rank was last detected for this project. | [optional] 

## Methods

### NewProjectResource

`func NewProjectResource(id string, name string, status string, createdAt time.Time, trackedQueryCount int32, ) *ProjectResource`

NewProjectResource instantiates a new ProjectResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectResourceWithDefaults

`func NewProjectResourceWithDefaults() *ProjectResource`

NewProjectResourceWithDefaults instantiates a new ProjectResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ProjectResource) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ProjectResource) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ProjectResource) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *ProjectResource) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ProjectResource) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ProjectResource) SetName(v string)`

SetName sets Name field to given value.


### GetStatus

`func (o *ProjectResource) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ProjectResource) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ProjectResource) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetCreatedAt

`func (o *ProjectResource) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ProjectResource) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ProjectResource) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetTrackedQueryCount

`func (o *ProjectResource) GetTrackedQueryCount() int32`

GetTrackedQueryCount returns the TrackedQueryCount field if non-nil, zero value otherwise.

### GetTrackedQueryCountOk

`func (o *ProjectResource) GetTrackedQueryCountOk() (*int32, bool)`

GetTrackedQueryCountOk returns a tuple with the TrackedQueryCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryCount

`func (o *ProjectResource) SetTrackedQueryCount(v int32)`

SetTrackedQueryCount sets TrackedQueryCount field to given value.


### GetAvgSerpPosition

`func (o *ProjectResource) GetAvgSerpPosition() float32`

GetAvgSerpPosition returns the AvgSerpPosition field if non-nil, zero value otherwise.

### GetAvgSerpPositionOk

`func (o *ProjectResource) GetAvgSerpPositionOk() (*float32, bool)`

GetAvgSerpPositionOk returns a tuple with the AvgSerpPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgSerpPosition

`func (o *ProjectResource) SetAvgSerpPosition(v float32)`

SetAvgSerpPosition sets AvgSerpPosition field to given value.

### HasAvgSerpPosition

`func (o *ProjectResource) HasAvgSerpPosition() bool`

HasAvgSerpPosition returns a boolean if a field has been set.

### SetAvgSerpPositionNil

`func (o *ProjectResource) SetAvgSerpPositionNil(b bool)`

 SetAvgSerpPositionNil sets the value for AvgSerpPosition to be an explicit nil

### UnsetAvgSerpPosition
`func (o *ProjectResource) UnsetAvgSerpPosition()`

UnsetAvgSerpPosition ensures that no value is present for AvgSerpPosition, not even an explicit nil
### GetAvgShoppingPosition

`func (o *ProjectResource) GetAvgShoppingPosition() float32`

GetAvgShoppingPosition returns the AvgShoppingPosition field if non-nil, zero value otherwise.

### GetAvgShoppingPositionOk

`func (o *ProjectResource) GetAvgShoppingPositionOk() (*float32, bool)`

GetAvgShoppingPositionOk returns a tuple with the AvgShoppingPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgShoppingPosition

`func (o *ProjectResource) SetAvgShoppingPosition(v float32)`

SetAvgShoppingPosition sets AvgShoppingPosition field to given value.

### HasAvgShoppingPosition

`func (o *ProjectResource) HasAvgShoppingPosition() bool`

HasAvgShoppingPosition returns a boolean if a field has been set.

### SetAvgShoppingPositionNil

`func (o *ProjectResource) SetAvgShoppingPositionNil(b bool)`

 SetAvgShoppingPositionNil sets the value for AvgShoppingPosition to be an explicit nil

### UnsetAvgShoppingPosition
`func (o *ProjectResource) UnsetAvgShoppingPosition()`

UnsetAvgShoppingPosition ensures that no value is present for AvgShoppingPosition, not even an explicit nil
### GetAvgMentionPosition

`func (o *ProjectResource) GetAvgMentionPosition() float32`

GetAvgMentionPosition returns the AvgMentionPosition field if non-nil, zero value otherwise.

### GetAvgMentionPositionOk

`func (o *ProjectResource) GetAvgMentionPositionOk() (*float32, bool)`

GetAvgMentionPositionOk returns a tuple with the AvgMentionPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgMentionPosition

`func (o *ProjectResource) SetAvgMentionPosition(v float32)`

SetAvgMentionPosition sets AvgMentionPosition field to given value.

### HasAvgMentionPosition

`func (o *ProjectResource) HasAvgMentionPosition() bool`

HasAvgMentionPosition returns a boolean if a field has been set.

### SetAvgMentionPositionNil

`func (o *ProjectResource) SetAvgMentionPositionNil(b bool)`

 SetAvgMentionPositionNil sets the value for AvgMentionPosition to be an explicit nil

### UnsetAvgMentionPosition
`func (o *ProjectResource) UnsetAvgMentionPosition()`

UnsetAvgMentionPosition ensures that no value is present for AvgMentionPosition, not even an explicit nil
### GetAvgLinkPosition

`func (o *ProjectResource) GetAvgLinkPosition() float32`

GetAvgLinkPosition returns the AvgLinkPosition field if non-nil, zero value otherwise.

### GetAvgLinkPositionOk

`func (o *ProjectResource) GetAvgLinkPositionOk() (*float32, bool)`

GetAvgLinkPositionOk returns a tuple with the AvgLinkPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgLinkPosition

`func (o *ProjectResource) SetAvgLinkPosition(v float32)`

SetAvgLinkPosition sets AvgLinkPosition field to given value.

### HasAvgLinkPosition

`func (o *ProjectResource) HasAvgLinkPosition() bool`

HasAvgLinkPosition returns a boolean if a field has been set.

### SetAvgLinkPositionNil

`func (o *ProjectResource) SetAvgLinkPositionNil(b bool)`

 SetAvgLinkPositionNil sets the value for AvgLinkPosition to be an explicit nil

### UnsetAvgLinkPosition
`func (o *ProjectResource) UnsetAvgLinkPosition()`

UnsetAvgLinkPosition ensures that no value is present for AvgLinkPosition, not even an explicit nil
### GetMentionRate

`func (o *ProjectResource) GetMentionRate() int32`

GetMentionRate returns the MentionRate field if non-nil, zero value otherwise.

### GetMentionRateOk

`func (o *ProjectResource) GetMentionRateOk() (*int32, bool)`

GetMentionRateOk returns a tuple with the MentionRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionRate

`func (o *ProjectResource) SetMentionRate(v int32)`

SetMentionRate sets MentionRate field to given value.

### HasMentionRate

`func (o *ProjectResource) HasMentionRate() bool`

HasMentionRate returns a boolean if a field has been set.

### SetMentionRateNil

`func (o *ProjectResource) SetMentionRateNil(b bool)`

 SetMentionRateNil sets the value for MentionRate to be an explicit nil

### UnsetMentionRate
`func (o *ProjectResource) UnsetMentionRate()`

UnsetMentionRate ensures that no value is present for MentionRate, not even an explicit nil
### GetSerpRate

`func (o *ProjectResource) GetSerpRate() int32`

GetSerpRate returns the SerpRate field if non-nil, zero value otherwise.

### GetSerpRateOk

`func (o *ProjectResource) GetSerpRateOk() (*int32, bool)`

GetSerpRateOk returns a tuple with the SerpRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpRate

`func (o *ProjectResource) SetSerpRate(v int32)`

SetSerpRate sets SerpRate field to given value.

### HasSerpRate

`func (o *ProjectResource) HasSerpRate() bool`

HasSerpRate returns a boolean if a field has been set.

### SetSerpRateNil

`func (o *ProjectResource) SetSerpRateNil(b bool)`

 SetSerpRateNil sets the value for SerpRate to be an explicit nil

### UnsetSerpRate
`func (o *ProjectResource) UnsetSerpRate()`

UnsetSerpRate ensures that no value is present for SerpRate, not even an explicit nil
### GetShoppingRate

`func (o *ProjectResource) GetShoppingRate() int32`

GetShoppingRate returns the ShoppingRate field if non-nil, zero value otherwise.

### GetShoppingRateOk

`func (o *ProjectResource) GetShoppingRateOk() (*int32, bool)`

GetShoppingRateOk returns a tuple with the ShoppingRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShoppingRate

`func (o *ProjectResource) SetShoppingRate(v int32)`

SetShoppingRate sets ShoppingRate field to given value.

### HasShoppingRate

`func (o *ProjectResource) HasShoppingRate() bool`

HasShoppingRate returns a boolean if a field has been set.

### SetShoppingRateNil

`func (o *ProjectResource) SetShoppingRateNil(b bool)`

 SetShoppingRateNil sets the value for ShoppingRate to be an explicit nil

### UnsetShoppingRate
`func (o *ProjectResource) UnsetShoppingRate()`

UnsetShoppingRate ensures that no value is present for ShoppingRate, not even an explicit nil
### GetPositivityIndex

`func (o *ProjectResource) GetPositivityIndex() int32`

GetPositivityIndex returns the PositivityIndex field if non-nil, zero value otherwise.

### GetPositivityIndexOk

`func (o *ProjectResource) GetPositivityIndexOk() (*int32, bool)`

GetPositivityIndexOk returns a tuple with the PositivityIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositivityIndex

`func (o *ProjectResource) SetPositivityIndex(v int32)`

SetPositivityIndex sets PositivityIndex field to given value.

### HasPositivityIndex

`func (o *ProjectResource) HasPositivityIndex() bool`

HasPositivityIndex returns a boolean if a field has been set.

### SetPositivityIndexNil

`func (o *ProjectResource) SetPositivityIndexNil(b bool)`

 SetPositivityIndexNil sets the value for PositivityIndex to be an explicit nil

### UnsetPositivityIndex
`func (o *ProjectResource) UnsetPositivityIndex()`

UnsetPositivityIndex ensures that no value is present for PositivityIndex, not even an explicit nil
### GetShareOfVoice

`func (o *ProjectResource) GetShareOfVoice() float32`

GetShareOfVoice returns the ShareOfVoice field if non-nil, zero value otherwise.

### GetShareOfVoiceOk

`func (o *ProjectResource) GetShareOfVoiceOk() (*float32, bool)`

GetShareOfVoiceOk returns a tuple with the ShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShareOfVoice

`func (o *ProjectResource) SetShareOfVoice(v float32)`

SetShareOfVoice sets ShareOfVoice field to given value.

### HasShareOfVoice

`func (o *ProjectResource) HasShareOfVoice() bool`

HasShareOfVoice returns a boolean if a field has been set.

### SetShareOfVoiceNil

`func (o *ProjectResource) SetShareOfVoiceNil(b bool)`

 SetShareOfVoiceNil sets the value for ShareOfVoice to be an explicit nil

### UnsetShareOfVoice
`func (o *ProjectResource) UnsetShareOfVoice()`

UnsetShareOfVoice ensures that no value is present for ShareOfVoice, not even an explicit nil
### GetSerpPositionStability

`func (o *ProjectResource) GetSerpPositionStability() float32`

GetSerpPositionStability returns the SerpPositionStability field if non-nil, zero value otherwise.

### GetSerpPositionStabilityOk

`func (o *ProjectResource) GetSerpPositionStabilityOk() (*float32, bool)`

GetSerpPositionStabilityOk returns a tuple with the SerpPositionStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpPositionStability

`func (o *ProjectResource) SetSerpPositionStability(v float32)`

SetSerpPositionStability sets SerpPositionStability field to given value.

### HasSerpPositionStability

`func (o *ProjectResource) HasSerpPositionStability() bool`

HasSerpPositionStability returns a boolean if a field has been set.

### SetSerpPositionStabilityNil

`func (o *ProjectResource) SetSerpPositionStabilityNil(b bool)`

 SetSerpPositionStabilityNil sets the value for SerpPositionStability to be an explicit nil

### UnsetSerpPositionStability
`func (o *ProjectResource) UnsetSerpPositionStability()`

UnsetSerpPositionStability ensures that no value is present for SerpPositionStability, not even an explicit nil
### GetShoppingPositionStability

`func (o *ProjectResource) GetShoppingPositionStability() float32`

GetShoppingPositionStability returns the ShoppingPositionStability field if non-nil, zero value otherwise.

### GetShoppingPositionStabilityOk

`func (o *ProjectResource) GetShoppingPositionStabilityOk() (*float32, bool)`

GetShoppingPositionStabilityOk returns a tuple with the ShoppingPositionStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShoppingPositionStability

`func (o *ProjectResource) SetShoppingPositionStability(v float32)`

SetShoppingPositionStability sets ShoppingPositionStability field to given value.

### HasShoppingPositionStability

`func (o *ProjectResource) HasShoppingPositionStability() bool`

HasShoppingPositionStability returns a boolean if a field has been set.

### SetShoppingPositionStabilityNil

`func (o *ProjectResource) SetShoppingPositionStabilityNil(b bool)`

 SetShoppingPositionStabilityNil sets the value for ShoppingPositionStability to be an explicit nil

### UnsetShoppingPositionStability
`func (o *ProjectResource) UnsetShoppingPositionStability()`

UnsetShoppingPositionStability ensures that no value is present for ShoppingPositionStability, not even an explicit nil
### GetLastRankDetectedAt

`func (o *ProjectResource) GetLastRankDetectedAt() time.Time`

GetLastRankDetectedAt returns the LastRankDetectedAt field if non-nil, zero value otherwise.

### GetLastRankDetectedAtOk

`func (o *ProjectResource) GetLastRankDetectedAtOk() (*time.Time, bool)`

GetLastRankDetectedAtOk returns a tuple with the LastRankDetectedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRankDetectedAt

`func (o *ProjectResource) SetLastRankDetectedAt(v time.Time)`

SetLastRankDetectedAt sets LastRankDetectedAt field to given value.

### HasLastRankDetectedAt

`func (o *ProjectResource) HasLastRankDetectedAt() bool`

HasLastRankDetectedAt returns a boolean if a field has been set.

### SetLastRankDetectedAtNil

`func (o *ProjectResource) SetLastRankDetectedAtNil(b bool)`

 SetLastRankDetectedAtNil sets the value for LastRankDetectedAt to be an explicit nil

### UnsetLastRankDetectedAt
`func (o *ProjectResource) UnsetLastRankDetectedAt()`

UnsetLastRankDetectedAt ensures that no value is present for LastRankDetectedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


