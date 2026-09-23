# PerCompetitorSentiment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CompetitorId** | **string** |  | 
**Positive** | **int32** |  | 
**Neutral** | **int32** |  | 
**Negative** | **int32** |  | 
**MentionCount** | **int32** |  | 
**PositivityIndex** | Pointer to **NullableInt32** |  | [optional] 
**MentionTypeCounts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  | 

## Methods

### NewPerCompetitorSentiment

`func NewPerCompetitorSentiment(competitorId string, positive int32, neutral int32, negative int32, mentionCount int32, mentionTypeCounts MentionTypeCounts, ) *PerCompetitorSentiment`

NewPerCompetitorSentiment instantiates a new PerCompetitorSentiment object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPerCompetitorSentimentWithDefaults

`func NewPerCompetitorSentimentWithDefaults() *PerCompetitorSentiment`

NewPerCompetitorSentimentWithDefaults instantiates a new PerCompetitorSentiment object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCompetitorId

`func (o *PerCompetitorSentiment) GetCompetitorId() string`

GetCompetitorId returns the CompetitorId field if non-nil, zero value otherwise.

### GetCompetitorIdOk

`func (o *PerCompetitorSentiment) GetCompetitorIdOk() (*string, bool)`

GetCompetitorIdOk returns a tuple with the CompetitorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitorId

`func (o *PerCompetitorSentiment) SetCompetitorId(v string)`

SetCompetitorId sets CompetitorId field to given value.


### GetPositive

`func (o *PerCompetitorSentiment) GetPositive() int32`

GetPositive returns the Positive field if non-nil, zero value otherwise.

### GetPositiveOk

`func (o *PerCompetitorSentiment) GetPositiveOk() (*int32, bool)`

GetPositiveOk returns a tuple with the Positive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositive

`func (o *PerCompetitorSentiment) SetPositive(v int32)`

SetPositive sets Positive field to given value.


### GetNeutral

`func (o *PerCompetitorSentiment) GetNeutral() int32`

GetNeutral returns the Neutral field if non-nil, zero value otherwise.

### GetNeutralOk

`func (o *PerCompetitorSentiment) GetNeutralOk() (*int32, bool)`

GetNeutralOk returns a tuple with the Neutral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeutral

`func (o *PerCompetitorSentiment) SetNeutral(v int32)`

SetNeutral sets Neutral field to given value.


### GetNegative

`func (o *PerCompetitorSentiment) GetNegative() int32`

GetNegative returns the Negative field if non-nil, zero value otherwise.

### GetNegativeOk

`func (o *PerCompetitorSentiment) GetNegativeOk() (*int32, bool)`

GetNegativeOk returns a tuple with the Negative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNegative

`func (o *PerCompetitorSentiment) SetNegative(v int32)`

SetNegative sets Negative field to given value.


### GetMentionCount

`func (o *PerCompetitorSentiment) GetMentionCount() int32`

GetMentionCount returns the MentionCount field if non-nil, zero value otherwise.

### GetMentionCountOk

`func (o *PerCompetitorSentiment) GetMentionCountOk() (*int32, bool)`

GetMentionCountOk returns a tuple with the MentionCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionCount

`func (o *PerCompetitorSentiment) SetMentionCount(v int32)`

SetMentionCount sets MentionCount field to given value.


### GetPositivityIndex

`func (o *PerCompetitorSentiment) GetPositivityIndex() int32`

GetPositivityIndex returns the PositivityIndex field if non-nil, zero value otherwise.

### GetPositivityIndexOk

`func (o *PerCompetitorSentiment) GetPositivityIndexOk() (*int32, bool)`

GetPositivityIndexOk returns a tuple with the PositivityIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositivityIndex

`func (o *PerCompetitorSentiment) SetPositivityIndex(v int32)`

SetPositivityIndex sets PositivityIndex field to given value.

### HasPositivityIndex

`func (o *PerCompetitorSentiment) HasPositivityIndex() bool`

HasPositivityIndex returns a boolean if a field has been set.

### SetPositivityIndexNil

`func (o *PerCompetitorSentiment) SetPositivityIndexNil(b bool)`

 SetPositivityIndexNil sets the value for PositivityIndex to be an explicit nil

### UnsetPositivityIndex
`func (o *PerCompetitorSentiment) UnsetPositivityIndex()`

UnsetPositivityIndex ensures that no value is present for PositivityIndex, not even an explicit nil
### GetMentionTypeCounts

`func (o *PerCompetitorSentiment) GetMentionTypeCounts() MentionTypeCounts`

GetMentionTypeCounts returns the MentionTypeCounts field if non-nil, zero value otherwise.

### GetMentionTypeCountsOk

`func (o *PerCompetitorSentiment) GetMentionTypeCountsOk() (*MentionTypeCounts, bool)`

GetMentionTypeCountsOk returns a tuple with the MentionTypeCounts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionTypeCounts

`func (o *PerCompetitorSentiment) SetMentionTypeCounts(v MentionTypeCounts)`

SetMentionTypeCounts sets MentionTypeCounts field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


