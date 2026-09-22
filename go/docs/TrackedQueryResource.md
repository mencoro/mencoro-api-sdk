# TrackedQueryResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**QueryText** | **string** | The keyword or prompt being tracked | 
**Engine** | **string** |  | 
**Country** | **string** | ISO-3166 alpha-2 country code the query is tracked in | 
**Status** | **string** |  | 
**QueryClusterIds** | **[]string** | Ids of the keyword clusters this query belongs to | 
**CheckFrequency** | **string** | How often the query is checked | 
**NPasses** | **int32** | How many times the query is asked per check | 
**LastSerpPosition** | Pointer to **NullableInt32** | Position in traditional search results at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**LastMentionPosition** | Pointer to **NullableInt32** | Position of the brand mention inside the AI answer at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**LastLinkPosition** | Pointer to **NullableInt32** | Position of a cited link to the brand at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**LastShoppingPosition** | Pointer to **NullableInt32** | Position in shopping results at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**LastShareOfVoice** | Pointer to **NullableFloat32** | 0-100 share of the weighted AI mentions against every tracked brand; HIGHER is better. Null when not known yet, which is not a share of zero. | [optional] 
**LastPositivityIndex** | Pointer to **NullableInt32** | 0-100 sentiment score of the brand mentions; HIGHER is better. Null when there were no mentions to score, which is not a score of zero. | [optional] 
**LastPositiveMentionCount** | Pointer to **NullableInt32** | Positive brand mentions at the last check. Null when not known yet. | [optional] 
**LastNeutralMentionCount** | Pointer to **NullableInt32** | Neutral brand mentions at the last check. Null when not known yet. | [optional] 
**LastNegativeMentionCount** | Pointer to **NullableInt32** | Negative brand mentions at the last check. Null when not known yet. | [optional] 
**LastCheckedAt** | Pointer to **NullableTime** | When the query was last checked. Null when it never has been. | [optional] 

## Methods

### NewTrackedQueryResource

`func NewTrackedQueryResource(id string, queryText string, engine string, country string, status string, queryClusterIds []string, checkFrequency string, nPasses int32, ) *TrackedQueryResource`

NewTrackedQueryResource instantiates a new TrackedQueryResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrackedQueryResourceWithDefaults

`func NewTrackedQueryResourceWithDefaults() *TrackedQueryResource`

NewTrackedQueryResourceWithDefaults instantiates a new TrackedQueryResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TrackedQueryResource) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TrackedQueryResource) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TrackedQueryResource) SetId(v string)`

SetId sets Id field to given value.


### GetQueryText

`func (o *TrackedQueryResource) GetQueryText() string`

GetQueryText returns the QueryText field if non-nil, zero value otherwise.

### GetQueryTextOk

`func (o *TrackedQueryResource) GetQueryTextOk() (*string, bool)`

GetQueryTextOk returns a tuple with the QueryText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryText

`func (o *TrackedQueryResource) SetQueryText(v string)`

SetQueryText sets QueryText field to given value.


### GetEngine

`func (o *TrackedQueryResource) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *TrackedQueryResource) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *TrackedQueryResource) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetCountry

`func (o *TrackedQueryResource) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *TrackedQueryResource) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *TrackedQueryResource) SetCountry(v string)`

SetCountry sets Country field to given value.


### GetStatus

`func (o *TrackedQueryResource) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *TrackedQueryResource) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *TrackedQueryResource) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetQueryClusterIds

`func (o *TrackedQueryResource) GetQueryClusterIds() []string`

GetQueryClusterIds returns the QueryClusterIds field if non-nil, zero value otherwise.

### GetQueryClusterIdsOk

`func (o *TrackedQueryResource) GetQueryClusterIdsOk() (*[]string, bool)`

GetQueryClusterIdsOk returns a tuple with the QueryClusterIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryClusterIds

`func (o *TrackedQueryResource) SetQueryClusterIds(v []string)`

SetQueryClusterIds sets QueryClusterIds field to given value.


### GetCheckFrequency

`func (o *TrackedQueryResource) GetCheckFrequency() string`

GetCheckFrequency returns the CheckFrequency field if non-nil, zero value otherwise.

### GetCheckFrequencyOk

`func (o *TrackedQueryResource) GetCheckFrequencyOk() (*string, bool)`

GetCheckFrequencyOk returns a tuple with the CheckFrequency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckFrequency

`func (o *TrackedQueryResource) SetCheckFrequency(v string)`

SetCheckFrequency sets CheckFrequency field to given value.


### GetNPasses

`func (o *TrackedQueryResource) GetNPasses() int32`

GetNPasses returns the NPasses field if non-nil, zero value otherwise.

### GetNPassesOk

`func (o *TrackedQueryResource) GetNPassesOk() (*int32, bool)`

GetNPassesOk returns a tuple with the NPasses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNPasses

`func (o *TrackedQueryResource) SetNPasses(v int32)`

SetNPasses sets NPasses field to given value.


### GetLastSerpPosition

`func (o *TrackedQueryResource) GetLastSerpPosition() int32`

GetLastSerpPosition returns the LastSerpPosition field if non-nil, zero value otherwise.

### GetLastSerpPositionOk

`func (o *TrackedQueryResource) GetLastSerpPositionOk() (*int32, bool)`

GetLastSerpPositionOk returns a tuple with the LastSerpPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastSerpPosition

`func (o *TrackedQueryResource) SetLastSerpPosition(v int32)`

SetLastSerpPosition sets LastSerpPosition field to given value.

### HasLastSerpPosition

`func (o *TrackedQueryResource) HasLastSerpPosition() bool`

HasLastSerpPosition returns a boolean if a field has been set.

### SetLastSerpPositionNil

`func (o *TrackedQueryResource) SetLastSerpPositionNil(b bool)`

 SetLastSerpPositionNil sets the value for LastSerpPosition to be an explicit nil

### UnsetLastSerpPosition
`func (o *TrackedQueryResource) UnsetLastSerpPosition()`

UnsetLastSerpPosition ensures that no value is present for LastSerpPosition, not even an explicit nil
### GetLastMentionPosition

`func (o *TrackedQueryResource) GetLastMentionPosition() int32`

GetLastMentionPosition returns the LastMentionPosition field if non-nil, zero value otherwise.

### GetLastMentionPositionOk

`func (o *TrackedQueryResource) GetLastMentionPositionOk() (*int32, bool)`

GetLastMentionPositionOk returns a tuple with the LastMentionPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastMentionPosition

`func (o *TrackedQueryResource) SetLastMentionPosition(v int32)`

SetLastMentionPosition sets LastMentionPosition field to given value.

### HasLastMentionPosition

`func (o *TrackedQueryResource) HasLastMentionPosition() bool`

HasLastMentionPosition returns a boolean if a field has been set.

### SetLastMentionPositionNil

`func (o *TrackedQueryResource) SetLastMentionPositionNil(b bool)`

 SetLastMentionPositionNil sets the value for LastMentionPosition to be an explicit nil

### UnsetLastMentionPosition
`func (o *TrackedQueryResource) UnsetLastMentionPosition()`

UnsetLastMentionPosition ensures that no value is present for LastMentionPosition, not even an explicit nil
### GetLastLinkPosition

`func (o *TrackedQueryResource) GetLastLinkPosition() int32`

GetLastLinkPosition returns the LastLinkPosition field if non-nil, zero value otherwise.

### GetLastLinkPositionOk

`func (o *TrackedQueryResource) GetLastLinkPositionOk() (*int32, bool)`

GetLastLinkPositionOk returns a tuple with the LastLinkPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastLinkPosition

`func (o *TrackedQueryResource) SetLastLinkPosition(v int32)`

SetLastLinkPosition sets LastLinkPosition field to given value.

### HasLastLinkPosition

`func (o *TrackedQueryResource) HasLastLinkPosition() bool`

HasLastLinkPosition returns a boolean if a field has been set.

### SetLastLinkPositionNil

`func (o *TrackedQueryResource) SetLastLinkPositionNil(b bool)`

 SetLastLinkPositionNil sets the value for LastLinkPosition to be an explicit nil

### UnsetLastLinkPosition
`func (o *TrackedQueryResource) UnsetLastLinkPosition()`

UnsetLastLinkPosition ensures that no value is present for LastLinkPosition, not even an explicit nil
### GetLastShoppingPosition

`func (o *TrackedQueryResource) GetLastShoppingPosition() int32`

GetLastShoppingPosition returns the LastShoppingPosition field if non-nil, zero value otherwise.

### GetLastShoppingPositionOk

`func (o *TrackedQueryResource) GetLastShoppingPositionOk() (*int32, bool)`

GetLastShoppingPositionOk returns a tuple with the LastShoppingPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastShoppingPosition

`func (o *TrackedQueryResource) SetLastShoppingPosition(v int32)`

SetLastShoppingPosition sets LastShoppingPosition field to given value.

### HasLastShoppingPosition

`func (o *TrackedQueryResource) HasLastShoppingPosition() bool`

HasLastShoppingPosition returns a boolean if a field has been set.

### SetLastShoppingPositionNil

`func (o *TrackedQueryResource) SetLastShoppingPositionNil(b bool)`

 SetLastShoppingPositionNil sets the value for LastShoppingPosition to be an explicit nil

### UnsetLastShoppingPosition
`func (o *TrackedQueryResource) UnsetLastShoppingPosition()`

UnsetLastShoppingPosition ensures that no value is present for LastShoppingPosition, not even an explicit nil
### GetLastShareOfVoice

`func (o *TrackedQueryResource) GetLastShareOfVoice() float32`

GetLastShareOfVoice returns the LastShareOfVoice field if non-nil, zero value otherwise.

### GetLastShareOfVoiceOk

`func (o *TrackedQueryResource) GetLastShareOfVoiceOk() (*float32, bool)`

GetLastShareOfVoiceOk returns a tuple with the LastShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastShareOfVoice

`func (o *TrackedQueryResource) SetLastShareOfVoice(v float32)`

SetLastShareOfVoice sets LastShareOfVoice field to given value.

### HasLastShareOfVoice

`func (o *TrackedQueryResource) HasLastShareOfVoice() bool`

HasLastShareOfVoice returns a boolean if a field has been set.

### SetLastShareOfVoiceNil

`func (o *TrackedQueryResource) SetLastShareOfVoiceNil(b bool)`

 SetLastShareOfVoiceNil sets the value for LastShareOfVoice to be an explicit nil

### UnsetLastShareOfVoice
`func (o *TrackedQueryResource) UnsetLastShareOfVoice()`

UnsetLastShareOfVoice ensures that no value is present for LastShareOfVoice, not even an explicit nil
### GetLastPositivityIndex

`func (o *TrackedQueryResource) GetLastPositivityIndex() int32`

GetLastPositivityIndex returns the LastPositivityIndex field if non-nil, zero value otherwise.

### GetLastPositivityIndexOk

`func (o *TrackedQueryResource) GetLastPositivityIndexOk() (*int32, bool)`

GetLastPositivityIndexOk returns a tuple with the LastPositivityIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastPositivityIndex

`func (o *TrackedQueryResource) SetLastPositivityIndex(v int32)`

SetLastPositivityIndex sets LastPositivityIndex field to given value.

### HasLastPositivityIndex

`func (o *TrackedQueryResource) HasLastPositivityIndex() bool`

HasLastPositivityIndex returns a boolean if a field has been set.

### SetLastPositivityIndexNil

`func (o *TrackedQueryResource) SetLastPositivityIndexNil(b bool)`

 SetLastPositivityIndexNil sets the value for LastPositivityIndex to be an explicit nil

### UnsetLastPositivityIndex
`func (o *TrackedQueryResource) UnsetLastPositivityIndex()`

UnsetLastPositivityIndex ensures that no value is present for LastPositivityIndex, not even an explicit nil
### GetLastPositiveMentionCount

`func (o *TrackedQueryResource) GetLastPositiveMentionCount() int32`

GetLastPositiveMentionCount returns the LastPositiveMentionCount field if non-nil, zero value otherwise.

### GetLastPositiveMentionCountOk

`func (o *TrackedQueryResource) GetLastPositiveMentionCountOk() (*int32, bool)`

GetLastPositiveMentionCountOk returns a tuple with the LastPositiveMentionCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastPositiveMentionCount

`func (o *TrackedQueryResource) SetLastPositiveMentionCount(v int32)`

SetLastPositiveMentionCount sets LastPositiveMentionCount field to given value.

### HasLastPositiveMentionCount

`func (o *TrackedQueryResource) HasLastPositiveMentionCount() bool`

HasLastPositiveMentionCount returns a boolean if a field has been set.

### SetLastPositiveMentionCountNil

`func (o *TrackedQueryResource) SetLastPositiveMentionCountNil(b bool)`

 SetLastPositiveMentionCountNil sets the value for LastPositiveMentionCount to be an explicit nil

### UnsetLastPositiveMentionCount
`func (o *TrackedQueryResource) UnsetLastPositiveMentionCount()`

UnsetLastPositiveMentionCount ensures that no value is present for LastPositiveMentionCount, not even an explicit nil
### GetLastNeutralMentionCount

`func (o *TrackedQueryResource) GetLastNeutralMentionCount() int32`

GetLastNeutralMentionCount returns the LastNeutralMentionCount field if non-nil, zero value otherwise.

### GetLastNeutralMentionCountOk

`func (o *TrackedQueryResource) GetLastNeutralMentionCountOk() (*int32, bool)`

GetLastNeutralMentionCountOk returns a tuple with the LastNeutralMentionCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastNeutralMentionCount

`func (o *TrackedQueryResource) SetLastNeutralMentionCount(v int32)`

SetLastNeutralMentionCount sets LastNeutralMentionCount field to given value.

### HasLastNeutralMentionCount

`func (o *TrackedQueryResource) HasLastNeutralMentionCount() bool`

HasLastNeutralMentionCount returns a boolean if a field has been set.

### SetLastNeutralMentionCountNil

`func (o *TrackedQueryResource) SetLastNeutralMentionCountNil(b bool)`

 SetLastNeutralMentionCountNil sets the value for LastNeutralMentionCount to be an explicit nil

### UnsetLastNeutralMentionCount
`func (o *TrackedQueryResource) UnsetLastNeutralMentionCount()`

UnsetLastNeutralMentionCount ensures that no value is present for LastNeutralMentionCount, not even an explicit nil
### GetLastNegativeMentionCount

`func (o *TrackedQueryResource) GetLastNegativeMentionCount() int32`

GetLastNegativeMentionCount returns the LastNegativeMentionCount field if non-nil, zero value otherwise.

### GetLastNegativeMentionCountOk

`func (o *TrackedQueryResource) GetLastNegativeMentionCountOk() (*int32, bool)`

GetLastNegativeMentionCountOk returns a tuple with the LastNegativeMentionCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastNegativeMentionCount

`func (o *TrackedQueryResource) SetLastNegativeMentionCount(v int32)`

SetLastNegativeMentionCount sets LastNegativeMentionCount field to given value.

### HasLastNegativeMentionCount

`func (o *TrackedQueryResource) HasLastNegativeMentionCount() bool`

HasLastNegativeMentionCount returns a boolean if a field has been set.

### SetLastNegativeMentionCountNil

`func (o *TrackedQueryResource) SetLastNegativeMentionCountNil(b bool)`

 SetLastNegativeMentionCountNil sets the value for LastNegativeMentionCount to be an explicit nil

### UnsetLastNegativeMentionCount
`func (o *TrackedQueryResource) UnsetLastNegativeMentionCount()`

UnsetLastNegativeMentionCount ensures that no value is present for LastNegativeMentionCount, not even an explicit nil
### GetLastCheckedAt

`func (o *TrackedQueryResource) GetLastCheckedAt() time.Time`

GetLastCheckedAt returns the LastCheckedAt field if non-nil, zero value otherwise.

### GetLastCheckedAtOk

`func (o *TrackedQueryResource) GetLastCheckedAtOk() (*time.Time, bool)`

GetLastCheckedAtOk returns a tuple with the LastCheckedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastCheckedAt

`func (o *TrackedQueryResource) SetLastCheckedAt(v time.Time)`

SetLastCheckedAt sets LastCheckedAt field to given value.

### HasLastCheckedAt

`func (o *TrackedQueryResource) HasLastCheckedAt() bool`

HasLastCheckedAt returns a boolean if a field has been set.

### SetLastCheckedAtNil

`func (o *TrackedQueryResource) SetLastCheckedAtNil(b bool)`

 SetLastCheckedAtNil sets the value for LastCheckedAt to be an explicit nil

### UnsetLastCheckedAt
`func (o *TrackedQueryResource) UnsetLastCheckedAt()`

UnsetLastCheckedAt ensures that no value is present for LastCheckedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


