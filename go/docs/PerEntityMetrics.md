# PerEntityMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Serp** | Pointer to **NullableFloat32** |  | [optional] 
**Shopping** | Pointer to **NullableFloat32** |  | [optional] 
**Mention** | Pointer to **NullableFloat32** |  | [optional] 
**Link** | Pointer to **NullableFloat32** |  | [optional] 
**Positivity** | Pointer to **NullableInt32** |  | [optional] 
**ShareOfVoice** | Pointer to **NullableFloat32** |  | [optional] 
**MentionRate** | Pointer to **NullableInt32** |  | [optional] 
**SerpRate** | Pointer to **NullableInt32** |  | [optional] 

## Methods

### NewPerEntityMetrics

`func NewPerEntityMetrics() *PerEntityMetrics`

NewPerEntityMetrics instantiates a new PerEntityMetrics object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPerEntityMetricsWithDefaults

`func NewPerEntityMetricsWithDefaults() *PerEntityMetrics`

NewPerEntityMetricsWithDefaults instantiates a new PerEntityMetrics object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSerp

`func (o *PerEntityMetrics) GetSerp() float32`

GetSerp returns the Serp field if non-nil, zero value otherwise.

### GetSerpOk

`func (o *PerEntityMetrics) GetSerpOk() (*float32, bool)`

GetSerpOk returns a tuple with the Serp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerp

`func (o *PerEntityMetrics) SetSerp(v float32)`

SetSerp sets Serp field to given value.

### HasSerp

`func (o *PerEntityMetrics) HasSerp() bool`

HasSerp returns a boolean if a field has been set.

### SetSerpNil

`func (o *PerEntityMetrics) SetSerpNil(b bool)`

 SetSerpNil sets the value for Serp to be an explicit nil

### UnsetSerp
`func (o *PerEntityMetrics) UnsetSerp()`

UnsetSerp ensures that no value is present for Serp, not even an explicit nil
### GetShopping

`func (o *PerEntityMetrics) GetShopping() float32`

GetShopping returns the Shopping field if non-nil, zero value otherwise.

### GetShoppingOk

`func (o *PerEntityMetrics) GetShoppingOk() (*float32, bool)`

GetShoppingOk returns a tuple with the Shopping field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopping

`func (o *PerEntityMetrics) SetShopping(v float32)`

SetShopping sets Shopping field to given value.

### HasShopping

`func (o *PerEntityMetrics) HasShopping() bool`

HasShopping returns a boolean if a field has been set.

### SetShoppingNil

`func (o *PerEntityMetrics) SetShoppingNil(b bool)`

 SetShoppingNil sets the value for Shopping to be an explicit nil

### UnsetShopping
`func (o *PerEntityMetrics) UnsetShopping()`

UnsetShopping ensures that no value is present for Shopping, not even an explicit nil
### GetMention

`func (o *PerEntityMetrics) GetMention() float32`

GetMention returns the Mention field if non-nil, zero value otherwise.

### GetMentionOk

`func (o *PerEntityMetrics) GetMentionOk() (*float32, bool)`

GetMentionOk returns a tuple with the Mention field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMention

`func (o *PerEntityMetrics) SetMention(v float32)`

SetMention sets Mention field to given value.

### HasMention

`func (o *PerEntityMetrics) HasMention() bool`

HasMention returns a boolean if a field has been set.

### SetMentionNil

`func (o *PerEntityMetrics) SetMentionNil(b bool)`

 SetMentionNil sets the value for Mention to be an explicit nil

### UnsetMention
`func (o *PerEntityMetrics) UnsetMention()`

UnsetMention ensures that no value is present for Mention, not even an explicit nil
### GetLink

`func (o *PerEntityMetrics) GetLink() float32`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *PerEntityMetrics) GetLinkOk() (*float32, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *PerEntityMetrics) SetLink(v float32)`

SetLink sets Link field to given value.

### HasLink

`func (o *PerEntityMetrics) HasLink() bool`

HasLink returns a boolean if a field has been set.

### SetLinkNil

`func (o *PerEntityMetrics) SetLinkNil(b bool)`

 SetLinkNil sets the value for Link to be an explicit nil

### UnsetLink
`func (o *PerEntityMetrics) UnsetLink()`

UnsetLink ensures that no value is present for Link, not even an explicit nil
### GetPositivity

`func (o *PerEntityMetrics) GetPositivity() int32`

GetPositivity returns the Positivity field if non-nil, zero value otherwise.

### GetPositivityOk

`func (o *PerEntityMetrics) GetPositivityOk() (*int32, bool)`

GetPositivityOk returns a tuple with the Positivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositivity

`func (o *PerEntityMetrics) SetPositivity(v int32)`

SetPositivity sets Positivity field to given value.

### HasPositivity

`func (o *PerEntityMetrics) HasPositivity() bool`

HasPositivity returns a boolean if a field has been set.

### SetPositivityNil

`func (o *PerEntityMetrics) SetPositivityNil(b bool)`

 SetPositivityNil sets the value for Positivity to be an explicit nil

### UnsetPositivity
`func (o *PerEntityMetrics) UnsetPositivity()`

UnsetPositivity ensures that no value is present for Positivity, not even an explicit nil
### GetShareOfVoice

`func (o *PerEntityMetrics) GetShareOfVoice() float32`

GetShareOfVoice returns the ShareOfVoice field if non-nil, zero value otherwise.

### GetShareOfVoiceOk

`func (o *PerEntityMetrics) GetShareOfVoiceOk() (*float32, bool)`

GetShareOfVoiceOk returns a tuple with the ShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShareOfVoice

`func (o *PerEntityMetrics) SetShareOfVoice(v float32)`

SetShareOfVoice sets ShareOfVoice field to given value.

### HasShareOfVoice

`func (o *PerEntityMetrics) HasShareOfVoice() bool`

HasShareOfVoice returns a boolean if a field has been set.

### SetShareOfVoiceNil

`func (o *PerEntityMetrics) SetShareOfVoiceNil(b bool)`

 SetShareOfVoiceNil sets the value for ShareOfVoice to be an explicit nil

### UnsetShareOfVoice
`func (o *PerEntityMetrics) UnsetShareOfVoice()`

UnsetShareOfVoice ensures that no value is present for ShareOfVoice, not even an explicit nil
### GetMentionRate

`func (o *PerEntityMetrics) GetMentionRate() int32`

GetMentionRate returns the MentionRate field if non-nil, zero value otherwise.

### GetMentionRateOk

`func (o *PerEntityMetrics) GetMentionRateOk() (*int32, bool)`

GetMentionRateOk returns a tuple with the MentionRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionRate

`func (o *PerEntityMetrics) SetMentionRate(v int32)`

SetMentionRate sets MentionRate field to given value.

### HasMentionRate

`func (o *PerEntityMetrics) HasMentionRate() bool`

HasMentionRate returns a boolean if a field has been set.

### SetMentionRateNil

`func (o *PerEntityMetrics) SetMentionRateNil(b bool)`

 SetMentionRateNil sets the value for MentionRate to be an explicit nil

### UnsetMentionRate
`func (o *PerEntityMetrics) UnsetMentionRate()`

UnsetMentionRate ensures that no value is present for MentionRate, not even an explicit nil
### GetSerpRate

`func (o *PerEntityMetrics) GetSerpRate() int32`

GetSerpRate returns the SerpRate field if non-nil, zero value otherwise.

### GetSerpRateOk

`func (o *PerEntityMetrics) GetSerpRateOk() (*int32, bool)`

GetSerpRateOk returns a tuple with the SerpRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpRate

`func (o *PerEntityMetrics) SetSerpRate(v int32)`

SetSerpRate sets SerpRate field to given value.

### HasSerpRate

`func (o *PerEntityMetrics) HasSerpRate() bool`

HasSerpRate returns a boolean if a field has been set.

### SetSerpRateNil

`func (o *PerEntityMetrics) SetSerpRateNil(b bool)`

 SetSerpRateNil sets the value for SerpRate to be an explicit nil

### UnsetSerpRate
`func (o *PerEntityMetrics) UnsetSerpRate()`

UnsetSerpRate ensures that no value is present for SerpRate, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


