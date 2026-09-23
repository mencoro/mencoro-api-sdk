# PerEngineSentiment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Engine** | **string** |  | 
**Positive** | **int32** |  | 
**Neutral** | **int32** |  | 
**Negative** | **int32** |  | 
**MentionCount** | **int32** |  | 
**PositivityIndex** | Pointer to **NullableInt32** |  | [optional] 

## Methods

### NewPerEngineSentiment

`func NewPerEngineSentiment(engine string, positive int32, neutral int32, negative int32, mentionCount int32, ) *PerEngineSentiment`

NewPerEngineSentiment instantiates a new PerEngineSentiment object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPerEngineSentimentWithDefaults

`func NewPerEngineSentimentWithDefaults() *PerEngineSentiment`

NewPerEngineSentimentWithDefaults instantiates a new PerEngineSentiment object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEngine

`func (o *PerEngineSentiment) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *PerEngineSentiment) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *PerEngineSentiment) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetPositive

`func (o *PerEngineSentiment) GetPositive() int32`

GetPositive returns the Positive field if non-nil, zero value otherwise.

### GetPositiveOk

`func (o *PerEngineSentiment) GetPositiveOk() (*int32, bool)`

GetPositiveOk returns a tuple with the Positive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositive

`func (o *PerEngineSentiment) SetPositive(v int32)`

SetPositive sets Positive field to given value.


### GetNeutral

`func (o *PerEngineSentiment) GetNeutral() int32`

GetNeutral returns the Neutral field if non-nil, zero value otherwise.

### GetNeutralOk

`func (o *PerEngineSentiment) GetNeutralOk() (*int32, bool)`

GetNeutralOk returns a tuple with the Neutral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeutral

`func (o *PerEngineSentiment) SetNeutral(v int32)`

SetNeutral sets Neutral field to given value.


### GetNegative

`func (o *PerEngineSentiment) GetNegative() int32`

GetNegative returns the Negative field if non-nil, zero value otherwise.

### GetNegativeOk

`func (o *PerEngineSentiment) GetNegativeOk() (*int32, bool)`

GetNegativeOk returns a tuple with the Negative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNegative

`func (o *PerEngineSentiment) SetNegative(v int32)`

SetNegative sets Negative field to given value.


### GetMentionCount

`func (o *PerEngineSentiment) GetMentionCount() int32`

GetMentionCount returns the MentionCount field if non-nil, zero value otherwise.

### GetMentionCountOk

`func (o *PerEngineSentiment) GetMentionCountOk() (*int32, bool)`

GetMentionCountOk returns a tuple with the MentionCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionCount

`func (o *PerEngineSentiment) SetMentionCount(v int32)`

SetMentionCount sets MentionCount field to given value.


### GetPositivityIndex

`func (o *PerEngineSentiment) GetPositivityIndex() int32`

GetPositivityIndex returns the PositivityIndex field if non-nil, zero value otherwise.

### GetPositivityIndexOk

`func (o *PerEngineSentiment) GetPositivityIndexOk() (*int32, bool)`

GetPositivityIndexOk returns a tuple with the PositivityIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositivityIndex

`func (o *PerEngineSentiment) SetPositivityIndex(v int32)`

SetPositivityIndex sets PositivityIndex field to given value.

### HasPositivityIndex

`func (o *PerEngineSentiment) HasPositivityIndex() bool`

HasPositivityIndex returns a boolean if a field has been set.

### SetPositivityIndexNil

`func (o *PerEngineSentiment) SetPositivityIndexNil(b bool)`

 SetPositivityIndexNil sets the value for PositivityIndex to be an explicit nil

### UnsetPositivityIndex
`func (o *PerEngineSentiment) UnsetPositivityIndex()`

UnsetPositivityIndex ensures that no value is present for PositivityIndex, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


