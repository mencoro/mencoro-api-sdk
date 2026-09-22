# GetShareOfVoiceFormula200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MentionTypeWeights** | Pointer to **map[string]float32** | Base weight per mention type; higher means a structurally stronger brand association. | [optional] 
**SentimentMultipliers** | Pointer to **map[string]float32** | Multiplier per tone, applied on top of the base weight. | [optional] 
**DirectMultiplier** | Pointer to **float32** | Applied when the mention carries no condition. | [optional] 
**ConditionalMultiplier** | Pointer to **float32** | Applied instead when the answer hedged the mention with a condition. | [optional] 

## Methods

### NewGetShareOfVoiceFormula200Response

`func NewGetShareOfVoiceFormula200Response() *GetShareOfVoiceFormula200Response`

NewGetShareOfVoiceFormula200Response instantiates a new GetShareOfVoiceFormula200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetShareOfVoiceFormula200ResponseWithDefaults

`func NewGetShareOfVoiceFormula200ResponseWithDefaults() *GetShareOfVoiceFormula200Response`

NewGetShareOfVoiceFormula200ResponseWithDefaults instantiates a new GetShareOfVoiceFormula200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMentionTypeWeights

`func (o *GetShareOfVoiceFormula200Response) GetMentionTypeWeights() map[string]float32`

GetMentionTypeWeights returns the MentionTypeWeights field if non-nil, zero value otherwise.

### GetMentionTypeWeightsOk

`func (o *GetShareOfVoiceFormula200Response) GetMentionTypeWeightsOk() (*map[string]float32, bool)`

GetMentionTypeWeightsOk returns a tuple with the MentionTypeWeights field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionTypeWeights

`func (o *GetShareOfVoiceFormula200Response) SetMentionTypeWeights(v map[string]float32)`

SetMentionTypeWeights sets MentionTypeWeights field to given value.

### HasMentionTypeWeights

`func (o *GetShareOfVoiceFormula200Response) HasMentionTypeWeights() bool`

HasMentionTypeWeights returns a boolean if a field has been set.

### GetSentimentMultipliers

`func (o *GetShareOfVoiceFormula200Response) GetSentimentMultipliers() map[string]float32`

GetSentimentMultipliers returns the SentimentMultipliers field if non-nil, zero value otherwise.

### GetSentimentMultipliersOk

`func (o *GetShareOfVoiceFormula200Response) GetSentimentMultipliersOk() (*map[string]float32, bool)`

GetSentimentMultipliersOk returns a tuple with the SentimentMultipliers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentMultipliers

`func (o *GetShareOfVoiceFormula200Response) SetSentimentMultipliers(v map[string]float32)`

SetSentimentMultipliers sets SentimentMultipliers field to given value.

### HasSentimentMultipliers

`func (o *GetShareOfVoiceFormula200Response) HasSentimentMultipliers() bool`

HasSentimentMultipliers returns a boolean if a field has been set.

### GetDirectMultiplier

`func (o *GetShareOfVoiceFormula200Response) GetDirectMultiplier() float32`

GetDirectMultiplier returns the DirectMultiplier field if non-nil, zero value otherwise.

### GetDirectMultiplierOk

`func (o *GetShareOfVoiceFormula200Response) GetDirectMultiplierOk() (*float32, bool)`

GetDirectMultiplierOk returns a tuple with the DirectMultiplier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDirectMultiplier

`func (o *GetShareOfVoiceFormula200Response) SetDirectMultiplier(v float32)`

SetDirectMultiplier sets DirectMultiplier field to given value.

### HasDirectMultiplier

`func (o *GetShareOfVoiceFormula200Response) HasDirectMultiplier() bool`

HasDirectMultiplier returns a boolean if a field has been set.

### GetConditionalMultiplier

`func (o *GetShareOfVoiceFormula200Response) GetConditionalMultiplier() float32`

GetConditionalMultiplier returns the ConditionalMultiplier field if non-nil, zero value otherwise.

### GetConditionalMultiplierOk

`func (o *GetShareOfVoiceFormula200Response) GetConditionalMultiplierOk() (*float32, bool)`

GetConditionalMultiplierOk returns a tuple with the ConditionalMultiplier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditionalMultiplier

`func (o *GetShareOfVoiceFormula200Response) SetConditionalMultiplier(v float32)`

SetConditionalMultiplier sets ConditionalMultiplier field to given value.

### HasConditionalMultiplier

`func (o *GetShareOfVoiceFormula200Response) HasConditionalMultiplier() bool`

HasConditionalMultiplier returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


