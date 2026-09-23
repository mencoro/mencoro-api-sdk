# TrackedQueryMoverRow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackedQueryId** | **string** |  | 
**QueryText** | **string** |  | 
**Engine** | **string** |  | 
**Country** | **string** |  | 
**AvgSerpPosition** | Pointer to **NullableFloat32** |  | [optional] 
**TrendSerp** | Pointer to **NullableFloat32** |  | [optional] 
**AvgShoppingPosition** | Pointer to **NullableFloat32** |  | [optional] 
**TrendShopping** | Pointer to **NullableFloat32** |  | [optional] 
**AvgMentionPosition** | Pointer to **NullableFloat32** |  | [optional] 
**TrendMention** | Pointer to **NullableFloat32** |  | [optional] 
**AvgLinkPosition** | Pointer to **NullableFloat32** |  | [optional] 
**TrendLink** | Pointer to **NullableFloat32** |  | [optional] 
**ShareOfVoice** | Pointer to **NullableFloat32** |  | [optional] 
**TrendShareOfVoice** | Pointer to **NullableFloat32** |  | [optional] 
**PositivityIndex** | Pointer to **NullableInt32** |  | [optional] 
**TrendPositivity** | Pointer to **NullableInt32** |  | [optional] 
**SentimentPositive** | **int32** |  | 
**SentimentNeutral** | **int32** |  | 
**SentimentNegative** | **int32** |  | 
**MentionCount** | **int32** |  | 
**MentionTypeCounts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  | 

## Methods

### NewTrackedQueryMoverRow

`func NewTrackedQueryMoverRow(trackedQueryId string, queryText string, engine string, country string, sentimentPositive int32, sentimentNeutral int32, sentimentNegative int32, mentionCount int32, mentionTypeCounts MentionTypeCounts, ) *TrackedQueryMoverRow`

NewTrackedQueryMoverRow instantiates a new TrackedQueryMoverRow object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrackedQueryMoverRowWithDefaults

`func NewTrackedQueryMoverRowWithDefaults() *TrackedQueryMoverRow`

NewTrackedQueryMoverRowWithDefaults instantiates a new TrackedQueryMoverRow object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTrackedQueryId

`func (o *TrackedQueryMoverRow) GetTrackedQueryId() string`

GetTrackedQueryId returns the TrackedQueryId field if non-nil, zero value otherwise.

### GetTrackedQueryIdOk

`func (o *TrackedQueryMoverRow) GetTrackedQueryIdOk() (*string, bool)`

GetTrackedQueryIdOk returns a tuple with the TrackedQueryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryId

`func (o *TrackedQueryMoverRow) SetTrackedQueryId(v string)`

SetTrackedQueryId sets TrackedQueryId field to given value.


### GetQueryText

`func (o *TrackedQueryMoverRow) GetQueryText() string`

GetQueryText returns the QueryText field if non-nil, zero value otherwise.

### GetQueryTextOk

`func (o *TrackedQueryMoverRow) GetQueryTextOk() (*string, bool)`

GetQueryTextOk returns a tuple with the QueryText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryText

`func (o *TrackedQueryMoverRow) SetQueryText(v string)`

SetQueryText sets QueryText field to given value.


### GetEngine

`func (o *TrackedQueryMoverRow) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *TrackedQueryMoverRow) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *TrackedQueryMoverRow) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetCountry

`func (o *TrackedQueryMoverRow) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *TrackedQueryMoverRow) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *TrackedQueryMoverRow) SetCountry(v string)`

SetCountry sets Country field to given value.


### GetAvgSerpPosition

`func (o *TrackedQueryMoverRow) GetAvgSerpPosition() float32`

GetAvgSerpPosition returns the AvgSerpPosition field if non-nil, zero value otherwise.

### GetAvgSerpPositionOk

`func (o *TrackedQueryMoverRow) GetAvgSerpPositionOk() (*float32, bool)`

GetAvgSerpPositionOk returns a tuple with the AvgSerpPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgSerpPosition

`func (o *TrackedQueryMoverRow) SetAvgSerpPosition(v float32)`

SetAvgSerpPosition sets AvgSerpPosition field to given value.

### HasAvgSerpPosition

`func (o *TrackedQueryMoverRow) HasAvgSerpPosition() bool`

HasAvgSerpPosition returns a boolean if a field has been set.

### SetAvgSerpPositionNil

`func (o *TrackedQueryMoverRow) SetAvgSerpPositionNil(b bool)`

 SetAvgSerpPositionNil sets the value for AvgSerpPosition to be an explicit nil

### UnsetAvgSerpPosition
`func (o *TrackedQueryMoverRow) UnsetAvgSerpPosition()`

UnsetAvgSerpPosition ensures that no value is present for AvgSerpPosition, not even an explicit nil
### GetTrendSerp

`func (o *TrackedQueryMoverRow) GetTrendSerp() float32`

GetTrendSerp returns the TrendSerp field if non-nil, zero value otherwise.

### GetTrendSerpOk

`func (o *TrackedQueryMoverRow) GetTrendSerpOk() (*float32, bool)`

GetTrendSerpOk returns a tuple with the TrendSerp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendSerp

`func (o *TrackedQueryMoverRow) SetTrendSerp(v float32)`

SetTrendSerp sets TrendSerp field to given value.

### HasTrendSerp

`func (o *TrackedQueryMoverRow) HasTrendSerp() bool`

HasTrendSerp returns a boolean if a field has been set.

### SetTrendSerpNil

`func (o *TrackedQueryMoverRow) SetTrendSerpNil(b bool)`

 SetTrendSerpNil sets the value for TrendSerp to be an explicit nil

### UnsetTrendSerp
`func (o *TrackedQueryMoverRow) UnsetTrendSerp()`

UnsetTrendSerp ensures that no value is present for TrendSerp, not even an explicit nil
### GetAvgShoppingPosition

`func (o *TrackedQueryMoverRow) GetAvgShoppingPosition() float32`

GetAvgShoppingPosition returns the AvgShoppingPosition field if non-nil, zero value otherwise.

### GetAvgShoppingPositionOk

`func (o *TrackedQueryMoverRow) GetAvgShoppingPositionOk() (*float32, bool)`

GetAvgShoppingPositionOk returns a tuple with the AvgShoppingPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgShoppingPosition

`func (o *TrackedQueryMoverRow) SetAvgShoppingPosition(v float32)`

SetAvgShoppingPosition sets AvgShoppingPosition field to given value.

### HasAvgShoppingPosition

`func (o *TrackedQueryMoverRow) HasAvgShoppingPosition() bool`

HasAvgShoppingPosition returns a boolean if a field has been set.

### SetAvgShoppingPositionNil

`func (o *TrackedQueryMoverRow) SetAvgShoppingPositionNil(b bool)`

 SetAvgShoppingPositionNil sets the value for AvgShoppingPosition to be an explicit nil

### UnsetAvgShoppingPosition
`func (o *TrackedQueryMoverRow) UnsetAvgShoppingPosition()`

UnsetAvgShoppingPosition ensures that no value is present for AvgShoppingPosition, not even an explicit nil
### GetTrendShopping

`func (o *TrackedQueryMoverRow) GetTrendShopping() float32`

GetTrendShopping returns the TrendShopping field if non-nil, zero value otherwise.

### GetTrendShoppingOk

`func (o *TrackedQueryMoverRow) GetTrendShoppingOk() (*float32, bool)`

GetTrendShoppingOk returns a tuple with the TrendShopping field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShopping

`func (o *TrackedQueryMoverRow) SetTrendShopping(v float32)`

SetTrendShopping sets TrendShopping field to given value.

### HasTrendShopping

`func (o *TrackedQueryMoverRow) HasTrendShopping() bool`

HasTrendShopping returns a boolean if a field has been set.

### SetTrendShoppingNil

`func (o *TrackedQueryMoverRow) SetTrendShoppingNil(b bool)`

 SetTrendShoppingNil sets the value for TrendShopping to be an explicit nil

### UnsetTrendShopping
`func (o *TrackedQueryMoverRow) UnsetTrendShopping()`

UnsetTrendShopping ensures that no value is present for TrendShopping, not even an explicit nil
### GetAvgMentionPosition

`func (o *TrackedQueryMoverRow) GetAvgMentionPosition() float32`

GetAvgMentionPosition returns the AvgMentionPosition field if non-nil, zero value otherwise.

### GetAvgMentionPositionOk

`func (o *TrackedQueryMoverRow) GetAvgMentionPositionOk() (*float32, bool)`

GetAvgMentionPositionOk returns a tuple with the AvgMentionPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgMentionPosition

`func (o *TrackedQueryMoverRow) SetAvgMentionPosition(v float32)`

SetAvgMentionPosition sets AvgMentionPosition field to given value.

### HasAvgMentionPosition

`func (o *TrackedQueryMoverRow) HasAvgMentionPosition() bool`

HasAvgMentionPosition returns a boolean if a field has been set.

### SetAvgMentionPositionNil

`func (o *TrackedQueryMoverRow) SetAvgMentionPositionNil(b bool)`

 SetAvgMentionPositionNil sets the value for AvgMentionPosition to be an explicit nil

### UnsetAvgMentionPosition
`func (o *TrackedQueryMoverRow) UnsetAvgMentionPosition()`

UnsetAvgMentionPosition ensures that no value is present for AvgMentionPosition, not even an explicit nil
### GetTrendMention

`func (o *TrackedQueryMoverRow) GetTrendMention() float32`

GetTrendMention returns the TrendMention field if non-nil, zero value otherwise.

### GetTrendMentionOk

`func (o *TrackedQueryMoverRow) GetTrendMentionOk() (*float32, bool)`

GetTrendMentionOk returns a tuple with the TrendMention field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendMention

`func (o *TrackedQueryMoverRow) SetTrendMention(v float32)`

SetTrendMention sets TrendMention field to given value.

### HasTrendMention

`func (o *TrackedQueryMoverRow) HasTrendMention() bool`

HasTrendMention returns a boolean if a field has been set.

### SetTrendMentionNil

`func (o *TrackedQueryMoverRow) SetTrendMentionNil(b bool)`

 SetTrendMentionNil sets the value for TrendMention to be an explicit nil

### UnsetTrendMention
`func (o *TrackedQueryMoverRow) UnsetTrendMention()`

UnsetTrendMention ensures that no value is present for TrendMention, not even an explicit nil
### GetAvgLinkPosition

`func (o *TrackedQueryMoverRow) GetAvgLinkPosition() float32`

GetAvgLinkPosition returns the AvgLinkPosition field if non-nil, zero value otherwise.

### GetAvgLinkPositionOk

`func (o *TrackedQueryMoverRow) GetAvgLinkPositionOk() (*float32, bool)`

GetAvgLinkPositionOk returns a tuple with the AvgLinkPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgLinkPosition

`func (o *TrackedQueryMoverRow) SetAvgLinkPosition(v float32)`

SetAvgLinkPosition sets AvgLinkPosition field to given value.

### HasAvgLinkPosition

`func (o *TrackedQueryMoverRow) HasAvgLinkPosition() bool`

HasAvgLinkPosition returns a boolean if a field has been set.

### SetAvgLinkPositionNil

`func (o *TrackedQueryMoverRow) SetAvgLinkPositionNil(b bool)`

 SetAvgLinkPositionNil sets the value for AvgLinkPosition to be an explicit nil

### UnsetAvgLinkPosition
`func (o *TrackedQueryMoverRow) UnsetAvgLinkPosition()`

UnsetAvgLinkPosition ensures that no value is present for AvgLinkPosition, not even an explicit nil
### GetTrendLink

`func (o *TrackedQueryMoverRow) GetTrendLink() float32`

GetTrendLink returns the TrendLink field if non-nil, zero value otherwise.

### GetTrendLinkOk

`func (o *TrackedQueryMoverRow) GetTrendLinkOk() (*float32, bool)`

GetTrendLinkOk returns a tuple with the TrendLink field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendLink

`func (o *TrackedQueryMoverRow) SetTrendLink(v float32)`

SetTrendLink sets TrendLink field to given value.

### HasTrendLink

`func (o *TrackedQueryMoverRow) HasTrendLink() bool`

HasTrendLink returns a boolean if a field has been set.

### SetTrendLinkNil

`func (o *TrackedQueryMoverRow) SetTrendLinkNil(b bool)`

 SetTrendLinkNil sets the value for TrendLink to be an explicit nil

### UnsetTrendLink
`func (o *TrackedQueryMoverRow) UnsetTrendLink()`

UnsetTrendLink ensures that no value is present for TrendLink, not even an explicit nil
### GetShareOfVoice

`func (o *TrackedQueryMoverRow) GetShareOfVoice() float32`

GetShareOfVoice returns the ShareOfVoice field if non-nil, zero value otherwise.

### GetShareOfVoiceOk

`func (o *TrackedQueryMoverRow) GetShareOfVoiceOk() (*float32, bool)`

GetShareOfVoiceOk returns a tuple with the ShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShareOfVoice

`func (o *TrackedQueryMoverRow) SetShareOfVoice(v float32)`

SetShareOfVoice sets ShareOfVoice field to given value.

### HasShareOfVoice

`func (o *TrackedQueryMoverRow) HasShareOfVoice() bool`

HasShareOfVoice returns a boolean if a field has been set.

### SetShareOfVoiceNil

`func (o *TrackedQueryMoverRow) SetShareOfVoiceNil(b bool)`

 SetShareOfVoiceNil sets the value for ShareOfVoice to be an explicit nil

### UnsetShareOfVoice
`func (o *TrackedQueryMoverRow) UnsetShareOfVoice()`

UnsetShareOfVoice ensures that no value is present for ShareOfVoice, not even an explicit nil
### GetTrendShareOfVoice

`func (o *TrackedQueryMoverRow) GetTrendShareOfVoice() float32`

GetTrendShareOfVoice returns the TrendShareOfVoice field if non-nil, zero value otherwise.

### GetTrendShareOfVoiceOk

`func (o *TrackedQueryMoverRow) GetTrendShareOfVoiceOk() (*float32, bool)`

GetTrendShareOfVoiceOk returns a tuple with the TrendShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShareOfVoice

`func (o *TrackedQueryMoverRow) SetTrendShareOfVoice(v float32)`

SetTrendShareOfVoice sets TrendShareOfVoice field to given value.

### HasTrendShareOfVoice

`func (o *TrackedQueryMoverRow) HasTrendShareOfVoice() bool`

HasTrendShareOfVoice returns a boolean if a field has been set.

### SetTrendShareOfVoiceNil

`func (o *TrackedQueryMoverRow) SetTrendShareOfVoiceNil(b bool)`

 SetTrendShareOfVoiceNil sets the value for TrendShareOfVoice to be an explicit nil

### UnsetTrendShareOfVoice
`func (o *TrackedQueryMoverRow) UnsetTrendShareOfVoice()`

UnsetTrendShareOfVoice ensures that no value is present for TrendShareOfVoice, not even an explicit nil
### GetPositivityIndex

`func (o *TrackedQueryMoverRow) GetPositivityIndex() int32`

GetPositivityIndex returns the PositivityIndex field if non-nil, zero value otherwise.

### GetPositivityIndexOk

`func (o *TrackedQueryMoverRow) GetPositivityIndexOk() (*int32, bool)`

GetPositivityIndexOk returns a tuple with the PositivityIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositivityIndex

`func (o *TrackedQueryMoverRow) SetPositivityIndex(v int32)`

SetPositivityIndex sets PositivityIndex field to given value.

### HasPositivityIndex

`func (o *TrackedQueryMoverRow) HasPositivityIndex() bool`

HasPositivityIndex returns a boolean if a field has been set.

### SetPositivityIndexNil

`func (o *TrackedQueryMoverRow) SetPositivityIndexNil(b bool)`

 SetPositivityIndexNil sets the value for PositivityIndex to be an explicit nil

### UnsetPositivityIndex
`func (o *TrackedQueryMoverRow) UnsetPositivityIndex()`

UnsetPositivityIndex ensures that no value is present for PositivityIndex, not even an explicit nil
### GetTrendPositivity

`func (o *TrackedQueryMoverRow) GetTrendPositivity() int32`

GetTrendPositivity returns the TrendPositivity field if non-nil, zero value otherwise.

### GetTrendPositivityOk

`func (o *TrackedQueryMoverRow) GetTrendPositivityOk() (*int32, bool)`

GetTrendPositivityOk returns a tuple with the TrendPositivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendPositivity

`func (o *TrackedQueryMoverRow) SetTrendPositivity(v int32)`

SetTrendPositivity sets TrendPositivity field to given value.

### HasTrendPositivity

`func (o *TrackedQueryMoverRow) HasTrendPositivity() bool`

HasTrendPositivity returns a boolean if a field has been set.

### SetTrendPositivityNil

`func (o *TrackedQueryMoverRow) SetTrendPositivityNil(b bool)`

 SetTrendPositivityNil sets the value for TrendPositivity to be an explicit nil

### UnsetTrendPositivity
`func (o *TrackedQueryMoverRow) UnsetTrendPositivity()`

UnsetTrendPositivity ensures that no value is present for TrendPositivity, not even an explicit nil
### GetSentimentPositive

`func (o *TrackedQueryMoverRow) GetSentimentPositive() int32`

GetSentimentPositive returns the SentimentPositive field if non-nil, zero value otherwise.

### GetSentimentPositiveOk

`func (o *TrackedQueryMoverRow) GetSentimentPositiveOk() (*int32, bool)`

GetSentimentPositiveOk returns a tuple with the SentimentPositive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentPositive

`func (o *TrackedQueryMoverRow) SetSentimentPositive(v int32)`

SetSentimentPositive sets SentimentPositive field to given value.


### GetSentimentNeutral

`func (o *TrackedQueryMoverRow) GetSentimentNeutral() int32`

GetSentimentNeutral returns the SentimentNeutral field if non-nil, zero value otherwise.

### GetSentimentNeutralOk

`func (o *TrackedQueryMoverRow) GetSentimentNeutralOk() (*int32, bool)`

GetSentimentNeutralOk returns a tuple with the SentimentNeutral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentNeutral

`func (o *TrackedQueryMoverRow) SetSentimentNeutral(v int32)`

SetSentimentNeutral sets SentimentNeutral field to given value.


### GetSentimentNegative

`func (o *TrackedQueryMoverRow) GetSentimentNegative() int32`

GetSentimentNegative returns the SentimentNegative field if non-nil, zero value otherwise.

### GetSentimentNegativeOk

`func (o *TrackedQueryMoverRow) GetSentimentNegativeOk() (*int32, bool)`

GetSentimentNegativeOk returns a tuple with the SentimentNegative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentNegative

`func (o *TrackedQueryMoverRow) SetSentimentNegative(v int32)`

SetSentimentNegative sets SentimentNegative field to given value.


### GetMentionCount

`func (o *TrackedQueryMoverRow) GetMentionCount() int32`

GetMentionCount returns the MentionCount field if non-nil, zero value otherwise.

### GetMentionCountOk

`func (o *TrackedQueryMoverRow) GetMentionCountOk() (*int32, bool)`

GetMentionCountOk returns a tuple with the MentionCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionCount

`func (o *TrackedQueryMoverRow) SetMentionCount(v int32)`

SetMentionCount sets MentionCount field to given value.


### GetMentionTypeCounts

`func (o *TrackedQueryMoverRow) GetMentionTypeCounts() MentionTypeCounts`

GetMentionTypeCounts returns the MentionTypeCounts field if non-nil, zero value otherwise.

### GetMentionTypeCountsOk

`func (o *TrackedQueryMoverRow) GetMentionTypeCountsOk() (*MentionTypeCounts, bool)`

GetMentionTypeCountsOk returns a tuple with the MentionTypeCounts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionTypeCounts

`func (o *TrackedQueryMoverRow) SetMentionTypeCounts(v MentionTypeCounts)`

SetMentionTypeCounts sets MentionTypeCounts field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


