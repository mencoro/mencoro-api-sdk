# ClusterBreakdownRow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClusterId** | Pointer to **NullableString** |  | [optional] 
**ClusterName** | **string** |  | 
**QueryCount** | **int32** |  | 
**KeywordCount** | **int32** |  | 
**AvgSerpPosition** | Pointer to **NullableFloat32** |  | [optional] 
**TrendSerp** | Pointer to **NullableFloat32** |  | [optional] 
**AvgShoppingPosition** | Pointer to **NullableFloat32** |  | [optional] 
**TrendShopping** | Pointer to **NullableFloat32** |  | [optional] 
**AvgMentionPosition** | Pointer to **NullableFloat32** |  | [optional] 
**TrendMention** | Pointer to **NullableFloat32** |  | [optional] 
**AvgLinkPosition** | Pointer to **NullableFloat32** |  | [optional] 
**TrendLink** | Pointer to **NullableFloat32** |  | [optional] 
**MentionPositionStability** | Pointer to **NullableFloat32** |  | [optional] 
**TrendStability** | Pointer to **NullableFloat32** |  | [optional] 
**SerpPositionStability** | Pointer to **NullableFloat32** |  | [optional] 
**TrendSerpStability** | Pointer to **NullableFloat32** |  | [optional] 
**ShoppingPositionStability** | Pointer to **NullableFloat32** |  | [optional] 
**TrendShoppingStability** | Pointer to **NullableFloat32** |  | [optional] 
**PositivityIndex** | Pointer to **NullableInt32** |  | [optional] 
**TrendPositivity** | Pointer to **NullableInt32** |  | [optional] 
**MentionRate** | Pointer to **NullableInt32** |  | [optional] 
**TrendMentionRate** | Pointer to **NullableInt32** |  | [optional] 
**SerpRate** | Pointer to **NullableInt32** |  | [optional] 
**TrendSerpRate** | Pointer to **NullableInt32** |  | [optional] 
**ShoppingRate** | Pointer to **NullableInt32** |  | [optional] 
**TrendShoppingRate** | Pointer to **NullableInt32** |  | [optional] 
**ShareOfVoice** | Pointer to **NullableFloat32** |  | [optional] 
**TrendShareOfVoice** | Pointer to **NullableFloat32** |  | [optional] 
**SentimentPositive** | **int32** |  | 
**SentimentNeutral** | **int32** |  | 
**SentimentNegative** | **int32** |  | 
**AvgMentionCount** | Pointer to **NullableFloat32** |  | [optional] 
**MentionTypeCounts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  | 

## Methods

### NewClusterBreakdownRow

`func NewClusterBreakdownRow(clusterName string, queryCount int32, keywordCount int32, sentimentPositive int32, sentimentNeutral int32, sentimentNegative int32, mentionTypeCounts MentionTypeCounts, ) *ClusterBreakdownRow`

NewClusterBreakdownRow instantiates a new ClusterBreakdownRow object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClusterBreakdownRowWithDefaults

`func NewClusterBreakdownRowWithDefaults() *ClusterBreakdownRow`

NewClusterBreakdownRowWithDefaults instantiates a new ClusterBreakdownRow object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClusterId

`func (o *ClusterBreakdownRow) GetClusterId() string`

GetClusterId returns the ClusterId field if non-nil, zero value otherwise.

### GetClusterIdOk

`func (o *ClusterBreakdownRow) GetClusterIdOk() (*string, bool)`

GetClusterIdOk returns a tuple with the ClusterId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClusterId

`func (o *ClusterBreakdownRow) SetClusterId(v string)`

SetClusterId sets ClusterId field to given value.

### HasClusterId

`func (o *ClusterBreakdownRow) HasClusterId() bool`

HasClusterId returns a boolean if a field has been set.

### SetClusterIdNil

`func (o *ClusterBreakdownRow) SetClusterIdNil(b bool)`

 SetClusterIdNil sets the value for ClusterId to be an explicit nil

### UnsetClusterId
`func (o *ClusterBreakdownRow) UnsetClusterId()`

UnsetClusterId ensures that no value is present for ClusterId, not even an explicit nil
### GetClusterName

`func (o *ClusterBreakdownRow) GetClusterName() string`

GetClusterName returns the ClusterName field if non-nil, zero value otherwise.

### GetClusterNameOk

`func (o *ClusterBreakdownRow) GetClusterNameOk() (*string, bool)`

GetClusterNameOk returns a tuple with the ClusterName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClusterName

`func (o *ClusterBreakdownRow) SetClusterName(v string)`

SetClusterName sets ClusterName field to given value.


### GetQueryCount

`func (o *ClusterBreakdownRow) GetQueryCount() int32`

GetQueryCount returns the QueryCount field if non-nil, zero value otherwise.

### GetQueryCountOk

`func (o *ClusterBreakdownRow) GetQueryCountOk() (*int32, bool)`

GetQueryCountOk returns a tuple with the QueryCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryCount

`func (o *ClusterBreakdownRow) SetQueryCount(v int32)`

SetQueryCount sets QueryCount field to given value.


### GetKeywordCount

`func (o *ClusterBreakdownRow) GetKeywordCount() int32`

GetKeywordCount returns the KeywordCount field if non-nil, zero value otherwise.

### GetKeywordCountOk

`func (o *ClusterBreakdownRow) GetKeywordCountOk() (*int32, bool)`

GetKeywordCountOk returns a tuple with the KeywordCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKeywordCount

`func (o *ClusterBreakdownRow) SetKeywordCount(v int32)`

SetKeywordCount sets KeywordCount field to given value.


### GetAvgSerpPosition

`func (o *ClusterBreakdownRow) GetAvgSerpPosition() float32`

GetAvgSerpPosition returns the AvgSerpPosition field if non-nil, zero value otherwise.

### GetAvgSerpPositionOk

`func (o *ClusterBreakdownRow) GetAvgSerpPositionOk() (*float32, bool)`

GetAvgSerpPositionOk returns a tuple with the AvgSerpPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgSerpPosition

`func (o *ClusterBreakdownRow) SetAvgSerpPosition(v float32)`

SetAvgSerpPosition sets AvgSerpPosition field to given value.

### HasAvgSerpPosition

`func (o *ClusterBreakdownRow) HasAvgSerpPosition() bool`

HasAvgSerpPosition returns a boolean if a field has been set.

### SetAvgSerpPositionNil

`func (o *ClusterBreakdownRow) SetAvgSerpPositionNil(b bool)`

 SetAvgSerpPositionNil sets the value for AvgSerpPosition to be an explicit nil

### UnsetAvgSerpPosition
`func (o *ClusterBreakdownRow) UnsetAvgSerpPosition()`

UnsetAvgSerpPosition ensures that no value is present for AvgSerpPosition, not even an explicit nil
### GetTrendSerp

`func (o *ClusterBreakdownRow) GetTrendSerp() float32`

GetTrendSerp returns the TrendSerp field if non-nil, zero value otherwise.

### GetTrendSerpOk

`func (o *ClusterBreakdownRow) GetTrendSerpOk() (*float32, bool)`

GetTrendSerpOk returns a tuple with the TrendSerp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendSerp

`func (o *ClusterBreakdownRow) SetTrendSerp(v float32)`

SetTrendSerp sets TrendSerp field to given value.

### HasTrendSerp

`func (o *ClusterBreakdownRow) HasTrendSerp() bool`

HasTrendSerp returns a boolean if a field has been set.

### SetTrendSerpNil

`func (o *ClusterBreakdownRow) SetTrendSerpNil(b bool)`

 SetTrendSerpNil sets the value for TrendSerp to be an explicit nil

### UnsetTrendSerp
`func (o *ClusterBreakdownRow) UnsetTrendSerp()`

UnsetTrendSerp ensures that no value is present for TrendSerp, not even an explicit nil
### GetAvgShoppingPosition

`func (o *ClusterBreakdownRow) GetAvgShoppingPosition() float32`

GetAvgShoppingPosition returns the AvgShoppingPosition field if non-nil, zero value otherwise.

### GetAvgShoppingPositionOk

`func (o *ClusterBreakdownRow) GetAvgShoppingPositionOk() (*float32, bool)`

GetAvgShoppingPositionOk returns a tuple with the AvgShoppingPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgShoppingPosition

`func (o *ClusterBreakdownRow) SetAvgShoppingPosition(v float32)`

SetAvgShoppingPosition sets AvgShoppingPosition field to given value.

### HasAvgShoppingPosition

`func (o *ClusterBreakdownRow) HasAvgShoppingPosition() bool`

HasAvgShoppingPosition returns a boolean if a field has been set.

### SetAvgShoppingPositionNil

`func (o *ClusterBreakdownRow) SetAvgShoppingPositionNil(b bool)`

 SetAvgShoppingPositionNil sets the value for AvgShoppingPosition to be an explicit nil

### UnsetAvgShoppingPosition
`func (o *ClusterBreakdownRow) UnsetAvgShoppingPosition()`

UnsetAvgShoppingPosition ensures that no value is present for AvgShoppingPosition, not even an explicit nil
### GetTrendShopping

`func (o *ClusterBreakdownRow) GetTrendShopping() float32`

GetTrendShopping returns the TrendShopping field if non-nil, zero value otherwise.

### GetTrendShoppingOk

`func (o *ClusterBreakdownRow) GetTrendShoppingOk() (*float32, bool)`

GetTrendShoppingOk returns a tuple with the TrendShopping field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShopping

`func (o *ClusterBreakdownRow) SetTrendShopping(v float32)`

SetTrendShopping sets TrendShopping field to given value.

### HasTrendShopping

`func (o *ClusterBreakdownRow) HasTrendShopping() bool`

HasTrendShopping returns a boolean if a field has been set.

### SetTrendShoppingNil

`func (o *ClusterBreakdownRow) SetTrendShoppingNil(b bool)`

 SetTrendShoppingNil sets the value for TrendShopping to be an explicit nil

### UnsetTrendShopping
`func (o *ClusterBreakdownRow) UnsetTrendShopping()`

UnsetTrendShopping ensures that no value is present for TrendShopping, not even an explicit nil
### GetAvgMentionPosition

`func (o *ClusterBreakdownRow) GetAvgMentionPosition() float32`

GetAvgMentionPosition returns the AvgMentionPosition field if non-nil, zero value otherwise.

### GetAvgMentionPositionOk

`func (o *ClusterBreakdownRow) GetAvgMentionPositionOk() (*float32, bool)`

GetAvgMentionPositionOk returns a tuple with the AvgMentionPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgMentionPosition

`func (o *ClusterBreakdownRow) SetAvgMentionPosition(v float32)`

SetAvgMentionPosition sets AvgMentionPosition field to given value.

### HasAvgMentionPosition

`func (o *ClusterBreakdownRow) HasAvgMentionPosition() bool`

HasAvgMentionPosition returns a boolean if a field has been set.

### SetAvgMentionPositionNil

`func (o *ClusterBreakdownRow) SetAvgMentionPositionNil(b bool)`

 SetAvgMentionPositionNil sets the value for AvgMentionPosition to be an explicit nil

### UnsetAvgMentionPosition
`func (o *ClusterBreakdownRow) UnsetAvgMentionPosition()`

UnsetAvgMentionPosition ensures that no value is present for AvgMentionPosition, not even an explicit nil
### GetTrendMention

`func (o *ClusterBreakdownRow) GetTrendMention() float32`

GetTrendMention returns the TrendMention field if non-nil, zero value otherwise.

### GetTrendMentionOk

`func (o *ClusterBreakdownRow) GetTrendMentionOk() (*float32, bool)`

GetTrendMentionOk returns a tuple with the TrendMention field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendMention

`func (o *ClusterBreakdownRow) SetTrendMention(v float32)`

SetTrendMention sets TrendMention field to given value.

### HasTrendMention

`func (o *ClusterBreakdownRow) HasTrendMention() bool`

HasTrendMention returns a boolean if a field has been set.

### SetTrendMentionNil

`func (o *ClusterBreakdownRow) SetTrendMentionNil(b bool)`

 SetTrendMentionNil sets the value for TrendMention to be an explicit nil

### UnsetTrendMention
`func (o *ClusterBreakdownRow) UnsetTrendMention()`

UnsetTrendMention ensures that no value is present for TrendMention, not even an explicit nil
### GetAvgLinkPosition

`func (o *ClusterBreakdownRow) GetAvgLinkPosition() float32`

GetAvgLinkPosition returns the AvgLinkPosition field if non-nil, zero value otherwise.

### GetAvgLinkPositionOk

`func (o *ClusterBreakdownRow) GetAvgLinkPositionOk() (*float32, bool)`

GetAvgLinkPositionOk returns a tuple with the AvgLinkPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgLinkPosition

`func (o *ClusterBreakdownRow) SetAvgLinkPosition(v float32)`

SetAvgLinkPosition sets AvgLinkPosition field to given value.

### HasAvgLinkPosition

`func (o *ClusterBreakdownRow) HasAvgLinkPosition() bool`

HasAvgLinkPosition returns a boolean if a field has been set.

### SetAvgLinkPositionNil

`func (o *ClusterBreakdownRow) SetAvgLinkPositionNil(b bool)`

 SetAvgLinkPositionNil sets the value for AvgLinkPosition to be an explicit nil

### UnsetAvgLinkPosition
`func (o *ClusterBreakdownRow) UnsetAvgLinkPosition()`

UnsetAvgLinkPosition ensures that no value is present for AvgLinkPosition, not even an explicit nil
### GetTrendLink

`func (o *ClusterBreakdownRow) GetTrendLink() float32`

GetTrendLink returns the TrendLink field if non-nil, zero value otherwise.

### GetTrendLinkOk

`func (o *ClusterBreakdownRow) GetTrendLinkOk() (*float32, bool)`

GetTrendLinkOk returns a tuple with the TrendLink field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendLink

`func (o *ClusterBreakdownRow) SetTrendLink(v float32)`

SetTrendLink sets TrendLink field to given value.

### HasTrendLink

`func (o *ClusterBreakdownRow) HasTrendLink() bool`

HasTrendLink returns a boolean if a field has been set.

### SetTrendLinkNil

`func (o *ClusterBreakdownRow) SetTrendLinkNil(b bool)`

 SetTrendLinkNil sets the value for TrendLink to be an explicit nil

### UnsetTrendLink
`func (o *ClusterBreakdownRow) UnsetTrendLink()`

UnsetTrendLink ensures that no value is present for TrendLink, not even an explicit nil
### GetMentionPositionStability

`func (o *ClusterBreakdownRow) GetMentionPositionStability() float32`

GetMentionPositionStability returns the MentionPositionStability field if non-nil, zero value otherwise.

### GetMentionPositionStabilityOk

`func (o *ClusterBreakdownRow) GetMentionPositionStabilityOk() (*float32, bool)`

GetMentionPositionStabilityOk returns a tuple with the MentionPositionStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionPositionStability

`func (o *ClusterBreakdownRow) SetMentionPositionStability(v float32)`

SetMentionPositionStability sets MentionPositionStability field to given value.

### HasMentionPositionStability

`func (o *ClusterBreakdownRow) HasMentionPositionStability() bool`

HasMentionPositionStability returns a boolean if a field has been set.

### SetMentionPositionStabilityNil

`func (o *ClusterBreakdownRow) SetMentionPositionStabilityNil(b bool)`

 SetMentionPositionStabilityNil sets the value for MentionPositionStability to be an explicit nil

### UnsetMentionPositionStability
`func (o *ClusterBreakdownRow) UnsetMentionPositionStability()`

UnsetMentionPositionStability ensures that no value is present for MentionPositionStability, not even an explicit nil
### GetTrendStability

`func (o *ClusterBreakdownRow) GetTrendStability() float32`

GetTrendStability returns the TrendStability field if non-nil, zero value otherwise.

### GetTrendStabilityOk

`func (o *ClusterBreakdownRow) GetTrendStabilityOk() (*float32, bool)`

GetTrendStabilityOk returns a tuple with the TrendStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendStability

`func (o *ClusterBreakdownRow) SetTrendStability(v float32)`

SetTrendStability sets TrendStability field to given value.

### HasTrendStability

`func (o *ClusterBreakdownRow) HasTrendStability() bool`

HasTrendStability returns a boolean if a field has been set.

### SetTrendStabilityNil

`func (o *ClusterBreakdownRow) SetTrendStabilityNil(b bool)`

 SetTrendStabilityNil sets the value for TrendStability to be an explicit nil

### UnsetTrendStability
`func (o *ClusterBreakdownRow) UnsetTrendStability()`

UnsetTrendStability ensures that no value is present for TrendStability, not even an explicit nil
### GetSerpPositionStability

`func (o *ClusterBreakdownRow) GetSerpPositionStability() float32`

GetSerpPositionStability returns the SerpPositionStability field if non-nil, zero value otherwise.

### GetSerpPositionStabilityOk

`func (o *ClusterBreakdownRow) GetSerpPositionStabilityOk() (*float32, bool)`

GetSerpPositionStabilityOk returns a tuple with the SerpPositionStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpPositionStability

`func (o *ClusterBreakdownRow) SetSerpPositionStability(v float32)`

SetSerpPositionStability sets SerpPositionStability field to given value.

### HasSerpPositionStability

`func (o *ClusterBreakdownRow) HasSerpPositionStability() bool`

HasSerpPositionStability returns a boolean if a field has been set.

### SetSerpPositionStabilityNil

`func (o *ClusterBreakdownRow) SetSerpPositionStabilityNil(b bool)`

 SetSerpPositionStabilityNil sets the value for SerpPositionStability to be an explicit nil

### UnsetSerpPositionStability
`func (o *ClusterBreakdownRow) UnsetSerpPositionStability()`

UnsetSerpPositionStability ensures that no value is present for SerpPositionStability, not even an explicit nil
### GetTrendSerpStability

`func (o *ClusterBreakdownRow) GetTrendSerpStability() float32`

GetTrendSerpStability returns the TrendSerpStability field if non-nil, zero value otherwise.

### GetTrendSerpStabilityOk

`func (o *ClusterBreakdownRow) GetTrendSerpStabilityOk() (*float32, bool)`

GetTrendSerpStabilityOk returns a tuple with the TrendSerpStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendSerpStability

`func (o *ClusterBreakdownRow) SetTrendSerpStability(v float32)`

SetTrendSerpStability sets TrendSerpStability field to given value.

### HasTrendSerpStability

`func (o *ClusterBreakdownRow) HasTrendSerpStability() bool`

HasTrendSerpStability returns a boolean if a field has been set.

### SetTrendSerpStabilityNil

`func (o *ClusterBreakdownRow) SetTrendSerpStabilityNil(b bool)`

 SetTrendSerpStabilityNil sets the value for TrendSerpStability to be an explicit nil

### UnsetTrendSerpStability
`func (o *ClusterBreakdownRow) UnsetTrendSerpStability()`

UnsetTrendSerpStability ensures that no value is present for TrendSerpStability, not even an explicit nil
### GetShoppingPositionStability

`func (o *ClusterBreakdownRow) GetShoppingPositionStability() float32`

GetShoppingPositionStability returns the ShoppingPositionStability field if non-nil, zero value otherwise.

### GetShoppingPositionStabilityOk

`func (o *ClusterBreakdownRow) GetShoppingPositionStabilityOk() (*float32, bool)`

GetShoppingPositionStabilityOk returns a tuple with the ShoppingPositionStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShoppingPositionStability

`func (o *ClusterBreakdownRow) SetShoppingPositionStability(v float32)`

SetShoppingPositionStability sets ShoppingPositionStability field to given value.

### HasShoppingPositionStability

`func (o *ClusterBreakdownRow) HasShoppingPositionStability() bool`

HasShoppingPositionStability returns a boolean if a field has been set.

### SetShoppingPositionStabilityNil

`func (o *ClusterBreakdownRow) SetShoppingPositionStabilityNil(b bool)`

 SetShoppingPositionStabilityNil sets the value for ShoppingPositionStability to be an explicit nil

### UnsetShoppingPositionStability
`func (o *ClusterBreakdownRow) UnsetShoppingPositionStability()`

UnsetShoppingPositionStability ensures that no value is present for ShoppingPositionStability, not even an explicit nil
### GetTrendShoppingStability

`func (o *ClusterBreakdownRow) GetTrendShoppingStability() float32`

GetTrendShoppingStability returns the TrendShoppingStability field if non-nil, zero value otherwise.

### GetTrendShoppingStabilityOk

`func (o *ClusterBreakdownRow) GetTrendShoppingStabilityOk() (*float32, bool)`

GetTrendShoppingStabilityOk returns a tuple with the TrendShoppingStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShoppingStability

`func (o *ClusterBreakdownRow) SetTrendShoppingStability(v float32)`

SetTrendShoppingStability sets TrendShoppingStability field to given value.

### HasTrendShoppingStability

`func (o *ClusterBreakdownRow) HasTrendShoppingStability() bool`

HasTrendShoppingStability returns a boolean if a field has been set.

### SetTrendShoppingStabilityNil

`func (o *ClusterBreakdownRow) SetTrendShoppingStabilityNil(b bool)`

 SetTrendShoppingStabilityNil sets the value for TrendShoppingStability to be an explicit nil

### UnsetTrendShoppingStability
`func (o *ClusterBreakdownRow) UnsetTrendShoppingStability()`

UnsetTrendShoppingStability ensures that no value is present for TrendShoppingStability, not even an explicit nil
### GetPositivityIndex

`func (o *ClusterBreakdownRow) GetPositivityIndex() int32`

GetPositivityIndex returns the PositivityIndex field if non-nil, zero value otherwise.

### GetPositivityIndexOk

`func (o *ClusterBreakdownRow) GetPositivityIndexOk() (*int32, bool)`

GetPositivityIndexOk returns a tuple with the PositivityIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositivityIndex

`func (o *ClusterBreakdownRow) SetPositivityIndex(v int32)`

SetPositivityIndex sets PositivityIndex field to given value.

### HasPositivityIndex

`func (o *ClusterBreakdownRow) HasPositivityIndex() bool`

HasPositivityIndex returns a boolean if a field has been set.

### SetPositivityIndexNil

`func (o *ClusterBreakdownRow) SetPositivityIndexNil(b bool)`

 SetPositivityIndexNil sets the value for PositivityIndex to be an explicit nil

### UnsetPositivityIndex
`func (o *ClusterBreakdownRow) UnsetPositivityIndex()`

UnsetPositivityIndex ensures that no value is present for PositivityIndex, not even an explicit nil
### GetTrendPositivity

`func (o *ClusterBreakdownRow) GetTrendPositivity() int32`

GetTrendPositivity returns the TrendPositivity field if non-nil, zero value otherwise.

### GetTrendPositivityOk

`func (o *ClusterBreakdownRow) GetTrendPositivityOk() (*int32, bool)`

GetTrendPositivityOk returns a tuple with the TrendPositivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendPositivity

`func (o *ClusterBreakdownRow) SetTrendPositivity(v int32)`

SetTrendPositivity sets TrendPositivity field to given value.

### HasTrendPositivity

`func (o *ClusterBreakdownRow) HasTrendPositivity() bool`

HasTrendPositivity returns a boolean if a field has been set.

### SetTrendPositivityNil

`func (o *ClusterBreakdownRow) SetTrendPositivityNil(b bool)`

 SetTrendPositivityNil sets the value for TrendPositivity to be an explicit nil

### UnsetTrendPositivity
`func (o *ClusterBreakdownRow) UnsetTrendPositivity()`

UnsetTrendPositivity ensures that no value is present for TrendPositivity, not even an explicit nil
### GetMentionRate

`func (o *ClusterBreakdownRow) GetMentionRate() int32`

GetMentionRate returns the MentionRate field if non-nil, zero value otherwise.

### GetMentionRateOk

`func (o *ClusterBreakdownRow) GetMentionRateOk() (*int32, bool)`

GetMentionRateOk returns a tuple with the MentionRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionRate

`func (o *ClusterBreakdownRow) SetMentionRate(v int32)`

SetMentionRate sets MentionRate field to given value.

### HasMentionRate

`func (o *ClusterBreakdownRow) HasMentionRate() bool`

HasMentionRate returns a boolean if a field has been set.

### SetMentionRateNil

`func (o *ClusterBreakdownRow) SetMentionRateNil(b bool)`

 SetMentionRateNil sets the value for MentionRate to be an explicit nil

### UnsetMentionRate
`func (o *ClusterBreakdownRow) UnsetMentionRate()`

UnsetMentionRate ensures that no value is present for MentionRate, not even an explicit nil
### GetTrendMentionRate

`func (o *ClusterBreakdownRow) GetTrendMentionRate() int32`

GetTrendMentionRate returns the TrendMentionRate field if non-nil, zero value otherwise.

### GetTrendMentionRateOk

`func (o *ClusterBreakdownRow) GetTrendMentionRateOk() (*int32, bool)`

GetTrendMentionRateOk returns a tuple with the TrendMentionRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendMentionRate

`func (o *ClusterBreakdownRow) SetTrendMentionRate(v int32)`

SetTrendMentionRate sets TrendMentionRate field to given value.

### HasTrendMentionRate

`func (o *ClusterBreakdownRow) HasTrendMentionRate() bool`

HasTrendMentionRate returns a boolean if a field has been set.

### SetTrendMentionRateNil

`func (o *ClusterBreakdownRow) SetTrendMentionRateNil(b bool)`

 SetTrendMentionRateNil sets the value for TrendMentionRate to be an explicit nil

### UnsetTrendMentionRate
`func (o *ClusterBreakdownRow) UnsetTrendMentionRate()`

UnsetTrendMentionRate ensures that no value is present for TrendMentionRate, not even an explicit nil
### GetSerpRate

`func (o *ClusterBreakdownRow) GetSerpRate() int32`

GetSerpRate returns the SerpRate field if non-nil, zero value otherwise.

### GetSerpRateOk

`func (o *ClusterBreakdownRow) GetSerpRateOk() (*int32, bool)`

GetSerpRateOk returns a tuple with the SerpRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpRate

`func (o *ClusterBreakdownRow) SetSerpRate(v int32)`

SetSerpRate sets SerpRate field to given value.

### HasSerpRate

`func (o *ClusterBreakdownRow) HasSerpRate() bool`

HasSerpRate returns a boolean if a field has been set.

### SetSerpRateNil

`func (o *ClusterBreakdownRow) SetSerpRateNil(b bool)`

 SetSerpRateNil sets the value for SerpRate to be an explicit nil

### UnsetSerpRate
`func (o *ClusterBreakdownRow) UnsetSerpRate()`

UnsetSerpRate ensures that no value is present for SerpRate, not even an explicit nil
### GetTrendSerpRate

`func (o *ClusterBreakdownRow) GetTrendSerpRate() int32`

GetTrendSerpRate returns the TrendSerpRate field if non-nil, zero value otherwise.

### GetTrendSerpRateOk

`func (o *ClusterBreakdownRow) GetTrendSerpRateOk() (*int32, bool)`

GetTrendSerpRateOk returns a tuple with the TrendSerpRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendSerpRate

`func (o *ClusterBreakdownRow) SetTrendSerpRate(v int32)`

SetTrendSerpRate sets TrendSerpRate field to given value.

### HasTrendSerpRate

`func (o *ClusterBreakdownRow) HasTrendSerpRate() bool`

HasTrendSerpRate returns a boolean if a field has been set.

### SetTrendSerpRateNil

`func (o *ClusterBreakdownRow) SetTrendSerpRateNil(b bool)`

 SetTrendSerpRateNil sets the value for TrendSerpRate to be an explicit nil

### UnsetTrendSerpRate
`func (o *ClusterBreakdownRow) UnsetTrendSerpRate()`

UnsetTrendSerpRate ensures that no value is present for TrendSerpRate, not even an explicit nil
### GetShoppingRate

`func (o *ClusterBreakdownRow) GetShoppingRate() int32`

GetShoppingRate returns the ShoppingRate field if non-nil, zero value otherwise.

### GetShoppingRateOk

`func (o *ClusterBreakdownRow) GetShoppingRateOk() (*int32, bool)`

GetShoppingRateOk returns a tuple with the ShoppingRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShoppingRate

`func (o *ClusterBreakdownRow) SetShoppingRate(v int32)`

SetShoppingRate sets ShoppingRate field to given value.

### HasShoppingRate

`func (o *ClusterBreakdownRow) HasShoppingRate() bool`

HasShoppingRate returns a boolean if a field has been set.

### SetShoppingRateNil

`func (o *ClusterBreakdownRow) SetShoppingRateNil(b bool)`

 SetShoppingRateNil sets the value for ShoppingRate to be an explicit nil

### UnsetShoppingRate
`func (o *ClusterBreakdownRow) UnsetShoppingRate()`

UnsetShoppingRate ensures that no value is present for ShoppingRate, not even an explicit nil
### GetTrendShoppingRate

`func (o *ClusterBreakdownRow) GetTrendShoppingRate() int32`

GetTrendShoppingRate returns the TrendShoppingRate field if non-nil, zero value otherwise.

### GetTrendShoppingRateOk

`func (o *ClusterBreakdownRow) GetTrendShoppingRateOk() (*int32, bool)`

GetTrendShoppingRateOk returns a tuple with the TrendShoppingRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShoppingRate

`func (o *ClusterBreakdownRow) SetTrendShoppingRate(v int32)`

SetTrendShoppingRate sets TrendShoppingRate field to given value.

### HasTrendShoppingRate

`func (o *ClusterBreakdownRow) HasTrendShoppingRate() bool`

HasTrendShoppingRate returns a boolean if a field has been set.

### SetTrendShoppingRateNil

`func (o *ClusterBreakdownRow) SetTrendShoppingRateNil(b bool)`

 SetTrendShoppingRateNil sets the value for TrendShoppingRate to be an explicit nil

### UnsetTrendShoppingRate
`func (o *ClusterBreakdownRow) UnsetTrendShoppingRate()`

UnsetTrendShoppingRate ensures that no value is present for TrendShoppingRate, not even an explicit nil
### GetShareOfVoice

`func (o *ClusterBreakdownRow) GetShareOfVoice() float32`

GetShareOfVoice returns the ShareOfVoice field if non-nil, zero value otherwise.

### GetShareOfVoiceOk

`func (o *ClusterBreakdownRow) GetShareOfVoiceOk() (*float32, bool)`

GetShareOfVoiceOk returns a tuple with the ShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShareOfVoice

`func (o *ClusterBreakdownRow) SetShareOfVoice(v float32)`

SetShareOfVoice sets ShareOfVoice field to given value.

### HasShareOfVoice

`func (o *ClusterBreakdownRow) HasShareOfVoice() bool`

HasShareOfVoice returns a boolean if a field has been set.

### SetShareOfVoiceNil

`func (o *ClusterBreakdownRow) SetShareOfVoiceNil(b bool)`

 SetShareOfVoiceNil sets the value for ShareOfVoice to be an explicit nil

### UnsetShareOfVoice
`func (o *ClusterBreakdownRow) UnsetShareOfVoice()`

UnsetShareOfVoice ensures that no value is present for ShareOfVoice, not even an explicit nil
### GetTrendShareOfVoice

`func (o *ClusterBreakdownRow) GetTrendShareOfVoice() float32`

GetTrendShareOfVoice returns the TrendShareOfVoice field if non-nil, zero value otherwise.

### GetTrendShareOfVoiceOk

`func (o *ClusterBreakdownRow) GetTrendShareOfVoiceOk() (*float32, bool)`

GetTrendShareOfVoiceOk returns a tuple with the TrendShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShareOfVoice

`func (o *ClusterBreakdownRow) SetTrendShareOfVoice(v float32)`

SetTrendShareOfVoice sets TrendShareOfVoice field to given value.

### HasTrendShareOfVoice

`func (o *ClusterBreakdownRow) HasTrendShareOfVoice() bool`

HasTrendShareOfVoice returns a boolean if a field has been set.

### SetTrendShareOfVoiceNil

`func (o *ClusterBreakdownRow) SetTrendShareOfVoiceNil(b bool)`

 SetTrendShareOfVoiceNil sets the value for TrendShareOfVoice to be an explicit nil

### UnsetTrendShareOfVoice
`func (o *ClusterBreakdownRow) UnsetTrendShareOfVoice()`

UnsetTrendShareOfVoice ensures that no value is present for TrendShareOfVoice, not even an explicit nil
### GetSentimentPositive

`func (o *ClusterBreakdownRow) GetSentimentPositive() int32`

GetSentimentPositive returns the SentimentPositive field if non-nil, zero value otherwise.

### GetSentimentPositiveOk

`func (o *ClusterBreakdownRow) GetSentimentPositiveOk() (*int32, bool)`

GetSentimentPositiveOk returns a tuple with the SentimentPositive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentPositive

`func (o *ClusterBreakdownRow) SetSentimentPositive(v int32)`

SetSentimentPositive sets SentimentPositive field to given value.


### GetSentimentNeutral

`func (o *ClusterBreakdownRow) GetSentimentNeutral() int32`

GetSentimentNeutral returns the SentimentNeutral field if non-nil, zero value otherwise.

### GetSentimentNeutralOk

`func (o *ClusterBreakdownRow) GetSentimentNeutralOk() (*int32, bool)`

GetSentimentNeutralOk returns a tuple with the SentimentNeutral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentNeutral

`func (o *ClusterBreakdownRow) SetSentimentNeutral(v int32)`

SetSentimentNeutral sets SentimentNeutral field to given value.


### GetSentimentNegative

`func (o *ClusterBreakdownRow) GetSentimentNegative() int32`

GetSentimentNegative returns the SentimentNegative field if non-nil, zero value otherwise.

### GetSentimentNegativeOk

`func (o *ClusterBreakdownRow) GetSentimentNegativeOk() (*int32, bool)`

GetSentimentNegativeOk returns a tuple with the SentimentNegative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentNegative

`func (o *ClusterBreakdownRow) SetSentimentNegative(v int32)`

SetSentimentNegative sets SentimentNegative field to given value.


### GetAvgMentionCount

`func (o *ClusterBreakdownRow) GetAvgMentionCount() float32`

GetAvgMentionCount returns the AvgMentionCount field if non-nil, zero value otherwise.

### GetAvgMentionCountOk

`func (o *ClusterBreakdownRow) GetAvgMentionCountOk() (*float32, bool)`

GetAvgMentionCountOk returns a tuple with the AvgMentionCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgMentionCount

`func (o *ClusterBreakdownRow) SetAvgMentionCount(v float32)`

SetAvgMentionCount sets AvgMentionCount field to given value.

### HasAvgMentionCount

`func (o *ClusterBreakdownRow) HasAvgMentionCount() bool`

HasAvgMentionCount returns a boolean if a field has been set.

### SetAvgMentionCountNil

`func (o *ClusterBreakdownRow) SetAvgMentionCountNil(b bool)`

 SetAvgMentionCountNil sets the value for AvgMentionCount to be an explicit nil

### UnsetAvgMentionCount
`func (o *ClusterBreakdownRow) UnsetAvgMentionCount()`

UnsetAvgMentionCount ensures that no value is present for AvgMentionCount, not even an explicit nil
### GetMentionTypeCounts

`func (o *ClusterBreakdownRow) GetMentionTypeCounts() MentionTypeCounts`

GetMentionTypeCounts returns the MentionTypeCounts field if non-nil, zero value otherwise.

### GetMentionTypeCountsOk

`func (o *ClusterBreakdownRow) GetMentionTypeCountsOk() (*MentionTypeCounts, bool)`

GetMentionTypeCountsOk returns a tuple with the MentionTypeCounts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionTypeCounts

`func (o *ClusterBreakdownRow) SetMentionTypeCounts(v MentionTypeCounts)`

SetMentionTypeCounts sets MentionTypeCounts field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


