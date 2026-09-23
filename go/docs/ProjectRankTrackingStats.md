# ProjectRankTrackingStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**MentionCount** | **int32** |  | 
**AiTrackedQueryCount** | **int32** |  | 
**AiQueriesWithMention** | **int32** |  | 
**SerpTrackedQueryCount** | **int32** |  | 
**SerpQueriesWithResult** | **int32** |  | 
**ShoppingTrackedQueryCount** | **int32** |  | 
**ShoppingQueriesWithResult** | **int32** |  | 
**MentionTypeCounts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  | 
**DataDirtySince** | Pointer to **NullableString** |  | [optional] 
**MentionPositionDistribution** | Pointer to [**[]PositionDistributionBucket**](PositionDistributionBucket.md) |  | [optional] [default to {}]
**SerpPositionDistribution** | Pointer to [**[]PositionDistributionBucket**](PositionDistributionBucket.md) |  | [optional] [default to {}]
**ShoppingPositionDistribution** | Pointer to [**[]PositionDistributionBucket**](PositionDistributionBucket.md) |  | [optional] [default to {}]
**CompetitorShareOfVoice** | Pointer to [**[]CompetitorShareOfVoice**](CompetitorShareOfVoice.md) |  | [optional] [default to {}]

## Methods

### NewProjectRankTrackingStats

`func NewProjectRankTrackingStats(sentimentPositive int32, sentimentNeutral int32, sentimentNegative int32, mentionCount int32, aiTrackedQueryCount int32, aiQueriesWithMention int32, serpTrackedQueryCount int32, serpQueriesWithResult int32, shoppingTrackedQueryCount int32, shoppingQueriesWithResult int32, mentionTypeCounts MentionTypeCounts, ) *ProjectRankTrackingStats`

NewProjectRankTrackingStats instantiates a new ProjectRankTrackingStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectRankTrackingStatsWithDefaults

`func NewProjectRankTrackingStatsWithDefaults() *ProjectRankTrackingStats`

NewProjectRankTrackingStatsWithDefaults instantiates a new ProjectRankTrackingStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAvgSerpPosition

`func (o *ProjectRankTrackingStats) GetAvgSerpPosition() float32`

GetAvgSerpPosition returns the AvgSerpPosition field if non-nil, zero value otherwise.

### GetAvgSerpPositionOk

`func (o *ProjectRankTrackingStats) GetAvgSerpPositionOk() (*float32, bool)`

GetAvgSerpPositionOk returns a tuple with the AvgSerpPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgSerpPosition

`func (o *ProjectRankTrackingStats) SetAvgSerpPosition(v float32)`

SetAvgSerpPosition sets AvgSerpPosition field to given value.

### HasAvgSerpPosition

`func (o *ProjectRankTrackingStats) HasAvgSerpPosition() bool`

HasAvgSerpPosition returns a boolean if a field has been set.

### SetAvgSerpPositionNil

`func (o *ProjectRankTrackingStats) SetAvgSerpPositionNil(b bool)`

 SetAvgSerpPositionNil sets the value for AvgSerpPosition to be an explicit nil

### UnsetAvgSerpPosition
`func (o *ProjectRankTrackingStats) UnsetAvgSerpPosition()`

UnsetAvgSerpPosition ensures that no value is present for AvgSerpPosition, not even an explicit nil
### GetTrendSerp

`func (o *ProjectRankTrackingStats) GetTrendSerp() float32`

GetTrendSerp returns the TrendSerp field if non-nil, zero value otherwise.

### GetTrendSerpOk

`func (o *ProjectRankTrackingStats) GetTrendSerpOk() (*float32, bool)`

GetTrendSerpOk returns a tuple with the TrendSerp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendSerp

`func (o *ProjectRankTrackingStats) SetTrendSerp(v float32)`

SetTrendSerp sets TrendSerp field to given value.

### HasTrendSerp

`func (o *ProjectRankTrackingStats) HasTrendSerp() bool`

HasTrendSerp returns a boolean if a field has been set.

### SetTrendSerpNil

`func (o *ProjectRankTrackingStats) SetTrendSerpNil(b bool)`

 SetTrendSerpNil sets the value for TrendSerp to be an explicit nil

### UnsetTrendSerp
`func (o *ProjectRankTrackingStats) UnsetTrendSerp()`

UnsetTrendSerp ensures that no value is present for TrendSerp, not even an explicit nil
### GetAvgShoppingPosition

`func (o *ProjectRankTrackingStats) GetAvgShoppingPosition() float32`

GetAvgShoppingPosition returns the AvgShoppingPosition field if non-nil, zero value otherwise.

### GetAvgShoppingPositionOk

`func (o *ProjectRankTrackingStats) GetAvgShoppingPositionOk() (*float32, bool)`

GetAvgShoppingPositionOk returns a tuple with the AvgShoppingPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgShoppingPosition

`func (o *ProjectRankTrackingStats) SetAvgShoppingPosition(v float32)`

SetAvgShoppingPosition sets AvgShoppingPosition field to given value.

### HasAvgShoppingPosition

`func (o *ProjectRankTrackingStats) HasAvgShoppingPosition() bool`

HasAvgShoppingPosition returns a boolean if a field has been set.

### SetAvgShoppingPositionNil

`func (o *ProjectRankTrackingStats) SetAvgShoppingPositionNil(b bool)`

 SetAvgShoppingPositionNil sets the value for AvgShoppingPosition to be an explicit nil

### UnsetAvgShoppingPosition
`func (o *ProjectRankTrackingStats) UnsetAvgShoppingPosition()`

UnsetAvgShoppingPosition ensures that no value is present for AvgShoppingPosition, not even an explicit nil
### GetTrendShopping

`func (o *ProjectRankTrackingStats) GetTrendShopping() float32`

GetTrendShopping returns the TrendShopping field if non-nil, zero value otherwise.

### GetTrendShoppingOk

`func (o *ProjectRankTrackingStats) GetTrendShoppingOk() (*float32, bool)`

GetTrendShoppingOk returns a tuple with the TrendShopping field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShopping

`func (o *ProjectRankTrackingStats) SetTrendShopping(v float32)`

SetTrendShopping sets TrendShopping field to given value.

### HasTrendShopping

`func (o *ProjectRankTrackingStats) HasTrendShopping() bool`

HasTrendShopping returns a boolean if a field has been set.

### SetTrendShoppingNil

`func (o *ProjectRankTrackingStats) SetTrendShoppingNil(b bool)`

 SetTrendShoppingNil sets the value for TrendShopping to be an explicit nil

### UnsetTrendShopping
`func (o *ProjectRankTrackingStats) UnsetTrendShopping()`

UnsetTrendShopping ensures that no value is present for TrendShopping, not even an explicit nil
### GetAvgMentionPosition

`func (o *ProjectRankTrackingStats) GetAvgMentionPosition() float32`

GetAvgMentionPosition returns the AvgMentionPosition field if non-nil, zero value otherwise.

### GetAvgMentionPositionOk

`func (o *ProjectRankTrackingStats) GetAvgMentionPositionOk() (*float32, bool)`

GetAvgMentionPositionOk returns a tuple with the AvgMentionPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgMentionPosition

`func (o *ProjectRankTrackingStats) SetAvgMentionPosition(v float32)`

SetAvgMentionPosition sets AvgMentionPosition field to given value.

### HasAvgMentionPosition

`func (o *ProjectRankTrackingStats) HasAvgMentionPosition() bool`

HasAvgMentionPosition returns a boolean if a field has been set.

### SetAvgMentionPositionNil

`func (o *ProjectRankTrackingStats) SetAvgMentionPositionNil(b bool)`

 SetAvgMentionPositionNil sets the value for AvgMentionPosition to be an explicit nil

### UnsetAvgMentionPosition
`func (o *ProjectRankTrackingStats) UnsetAvgMentionPosition()`

UnsetAvgMentionPosition ensures that no value is present for AvgMentionPosition, not even an explicit nil
### GetTrendMention

`func (o *ProjectRankTrackingStats) GetTrendMention() float32`

GetTrendMention returns the TrendMention field if non-nil, zero value otherwise.

### GetTrendMentionOk

`func (o *ProjectRankTrackingStats) GetTrendMentionOk() (*float32, bool)`

GetTrendMentionOk returns a tuple with the TrendMention field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendMention

`func (o *ProjectRankTrackingStats) SetTrendMention(v float32)`

SetTrendMention sets TrendMention field to given value.

### HasTrendMention

`func (o *ProjectRankTrackingStats) HasTrendMention() bool`

HasTrendMention returns a boolean if a field has been set.

### SetTrendMentionNil

`func (o *ProjectRankTrackingStats) SetTrendMentionNil(b bool)`

 SetTrendMentionNil sets the value for TrendMention to be an explicit nil

### UnsetTrendMention
`func (o *ProjectRankTrackingStats) UnsetTrendMention()`

UnsetTrendMention ensures that no value is present for TrendMention, not even an explicit nil
### GetAvgLinkPosition

`func (o *ProjectRankTrackingStats) GetAvgLinkPosition() float32`

GetAvgLinkPosition returns the AvgLinkPosition field if non-nil, zero value otherwise.

### GetAvgLinkPositionOk

`func (o *ProjectRankTrackingStats) GetAvgLinkPositionOk() (*float32, bool)`

GetAvgLinkPositionOk returns a tuple with the AvgLinkPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgLinkPosition

`func (o *ProjectRankTrackingStats) SetAvgLinkPosition(v float32)`

SetAvgLinkPosition sets AvgLinkPosition field to given value.

### HasAvgLinkPosition

`func (o *ProjectRankTrackingStats) HasAvgLinkPosition() bool`

HasAvgLinkPosition returns a boolean if a field has been set.

### SetAvgLinkPositionNil

`func (o *ProjectRankTrackingStats) SetAvgLinkPositionNil(b bool)`

 SetAvgLinkPositionNil sets the value for AvgLinkPosition to be an explicit nil

### UnsetAvgLinkPosition
`func (o *ProjectRankTrackingStats) UnsetAvgLinkPosition()`

UnsetAvgLinkPosition ensures that no value is present for AvgLinkPosition, not even an explicit nil
### GetTrendLink

`func (o *ProjectRankTrackingStats) GetTrendLink() float32`

GetTrendLink returns the TrendLink field if non-nil, zero value otherwise.

### GetTrendLinkOk

`func (o *ProjectRankTrackingStats) GetTrendLinkOk() (*float32, bool)`

GetTrendLinkOk returns a tuple with the TrendLink field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendLink

`func (o *ProjectRankTrackingStats) SetTrendLink(v float32)`

SetTrendLink sets TrendLink field to given value.

### HasTrendLink

`func (o *ProjectRankTrackingStats) HasTrendLink() bool`

HasTrendLink returns a boolean if a field has been set.

### SetTrendLinkNil

`func (o *ProjectRankTrackingStats) SetTrendLinkNil(b bool)`

 SetTrendLinkNil sets the value for TrendLink to be an explicit nil

### UnsetTrendLink
`func (o *ProjectRankTrackingStats) UnsetTrendLink()`

UnsetTrendLink ensures that no value is present for TrendLink, not even an explicit nil
### GetMentionPositionStability

`func (o *ProjectRankTrackingStats) GetMentionPositionStability() float32`

GetMentionPositionStability returns the MentionPositionStability field if non-nil, zero value otherwise.

### GetMentionPositionStabilityOk

`func (o *ProjectRankTrackingStats) GetMentionPositionStabilityOk() (*float32, bool)`

GetMentionPositionStabilityOk returns a tuple with the MentionPositionStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionPositionStability

`func (o *ProjectRankTrackingStats) SetMentionPositionStability(v float32)`

SetMentionPositionStability sets MentionPositionStability field to given value.

### HasMentionPositionStability

`func (o *ProjectRankTrackingStats) HasMentionPositionStability() bool`

HasMentionPositionStability returns a boolean if a field has been set.

### SetMentionPositionStabilityNil

`func (o *ProjectRankTrackingStats) SetMentionPositionStabilityNil(b bool)`

 SetMentionPositionStabilityNil sets the value for MentionPositionStability to be an explicit nil

### UnsetMentionPositionStability
`func (o *ProjectRankTrackingStats) UnsetMentionPositionStability()`

UnsetMentionPositionStability ensures that no value is present for MentionPositionStability, not even an explicit nil
### GetTrendStability

`func (o *ProjectRankTrackingStats) GetTrendStability() float32`

GetTrendStability returns the TrendStability field if non-nil, zero value otherwise.

### GetTrendStabilityOk

`func (o *ProjectRankTrackingStats) GetTrendStabilityOk() (*float32, bool)`

GetTrendStabilityOk returns a tuple with the TrendStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendStability

`func (o *ProjectRankTrackingStats) SetTrendStability(v float32)`

SetTrendStability sets TrendStability field to given value.

### HasTrendStability

`func (o *ProjectRankTrackingStats) HasTrendStability() bool`

HasTrendStability returns a boolean if a field has been set.

### SetTrendStabilityNil

`func (o *ProjectRankTrackingStats) SetTrendStabilityNil(b bool)`

 SetTrendStabilityNil sets the value for TrendStability to be an explicit nil

### UnsetTrendStability
`func (o *ProjectRankTrackingStats) UnsetTrendStability()`

UnsetTrendStability ensures that no value is present for TrendStability, not even an explicit nil
### GetSerpPositionStability

`func (o *ProjectRankTrackingStats) GetSerpPositionStability() float32`

GetSerpPositionStability returns the SerpPositionStability field if non-nil, zero value otherwise.

### GetSerpPositionStabilityOk

`func (o *ProjectRankTrackingStats) GetSerpPositionStabilityOk() (*float32, bool)`

GetSerpPositionStabilityOk returns a tuple with the SerpPositionStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpPositionStability

`func (o *ProjectRankTrackingStats) SetSerpPositionStability(v float32)`

SetSerpPositionStability sets SerpPositionStability field to given value.

### HasSerpPositionStability

`func (o *ProjectRankTrackingStats) HasSerpPositionStability() bool`

HasSerpPositionStability returns a boolean if a field has been set.

### SetSerpPositionStabilityNil

`func (o *ProjectRankTrackingStats) SetSerpPositionStabilityNil(b bool)`

 SetSerpPositionStabilityNil sets the value for SerpPositionStability to be an explicit nil

### UnsetSerpPositionStability
`func (o *ProjectRankTrackingStats) UnsetSerpPositionStability()`

UnsetSerpPositionStability ensures that no value is present for SerpPositionStability, not even an explicit nil
### GetTrendSerpStability

`func (o *ProjectRankTrackingStats) GetTrendSerpStability() float32`

GetTrendSerpStability returns the TrendSerpStability field if non-nil, zero value otherwise.

### GetTrendSerpStabilityOk

`func (o *ProjectRankTrackingStats) GetTrendSerpStabilityOk() (*float32, bool)`

GetTrendSerpStabilityOk returns a tuple with the TrendSerpStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendSerpStability

`func (o *ProjectRankTrackingStats) SetTrendSerpStability(v float32)`

SetTrendSerpStability sets TrendSerpStability field to given value.

### HasTrendSerpStability

`func (o *ProjectRankTrackingStats) HasTrendSerpStability() bool`

HasTrendSerpStability returns a boolean if a field has been set.

### SetTrendSerpStabilityNil

`func (o *ProjectRankTrackingStats) SetTrendSerpStabilityNil(b bool)`

 SetTrendSerpStabilityNil sets the value for TrendSerpStability to be an explicit nil

### UnsetTrendSerpStability
`func (o *ProjectRankTrackingStats) UnsetTrendSerpStability()`

UnsetTrendSerpStability ensures that no value is present for TrendSerpStability, not even an explicit nil
### GetShoppingPositionStability

`func (o *ProjectRankTrackingStats) GetShoppingPositionStability() float32`

GetShoppingPositionStability returns the ShoppingPositionStability field if non-nil, zero value otherwise.

### GetShoppingPositionStabilityOk

`func (o *ProjectRankTrackingStats) GetShoppingPositionStabilityOk() (*float32, bool)`

GetShoppingPositionStabilityOk returns a tuple with the ShoppingPositionStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShoppingPositionStability

`func (o *ProjectRankTrackingStats) SetShoppingPositionStability(v float32)`

SetShoppingPositionStability sets ShoppingPositionStability field to given value.

### HasShoppingPositionStability

`func (o *ProjectRankTrackingStats) HasShoppingPositionStability() bool`

HasShoppingPositionStability returns a boolean if a field has been set.

### SetShoppingPositionStabilityNil

`func (o *ProjectRankTrackingStats) SetShoppingPositionStabilityNil(b bool)`

 SetShoppingPositionStabilityNil sets the value for ShoppingPositionStability to be an explicit nil

### UnsetShoppingPositionStability
`func (o *ProjectRankTrackingStats) UnsetShoppingPositionStability()`

UnsetShoppingPositionStability ensures that no value is present for ShoppingPositionStability, not even an explicit nil
### GetTrendShoppingStability

`func (o *ProjectRankTrackingStats) GetTrendShoppingStability() float32`

GetTrendShoppingStability returns the TrendShoppingStability field if non-nil, zero value otherwise.

### GetTrendShoppingStabilityOk

`func (o *ProjectRankTrackingStats) GetTrendShoppingStabilityOk() (*float32, bool)`

GetTrendShoppingStabilityOk returns a tuple with the TrendShoppingStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShoppingStability

`func (o *ProjectRankTrackingStats) SetTrendShoppingStability(v float32)`

SetTrendShoppingStability sets TrendShoppingStability field to given value.

### HasTrendShoppingStability

`func (o *ProjectRankTrackingStats) HasTrendShoppingStability() bool`

HasTrendShoppingStability returns a boolean if a field has been set.

### SetTrendShoppingStabilityNil

`func (o *ProjectRankTrackingStats) SetTrendShoppingStabilityNil(b bool)`

 SetTrendShoppingStabilityNil sets the value for TrendShoppingStability to be an explicit nil

### UnsetTrendShoppingStability
`func (o *ProjectRankTrackingStats) UnsetTrendShoppingStability()`

UnsetTrendShoppingStability ensures that no value is present for TrendShoppingStability, not even an explicit nil
### GetPositivityIndex

`func (o *ProjectRankTrackingStats) GetPositivityIndex() int32`

GetPositivityIndex returns the PositivityIndex field if non-nil, zero value otherwise.

### GetPositivityIndexOk

`func (o *ProjectRankTrackingStats) GetPositivityIndexOk() (*int32, bool)`

GetPositivityIndexOk returns a tuple with the PositivityIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositivityIndex

`func (o *ProjectRankTrackingStats) SetPositivityIndex(v int32)`

SetPositivityIndex sets PositivityIndex field to given value.

### HasPositivityIndex

`func (o *ProjectRankTrackingStats) HasPositivityIndex() bool`

HasPositivityIndex returns a boolean if a field has been set.

### SetPositivityIndexNil

`func (o *ProjectRankTrackingStats) SetPositivityIndexNil(b bool)`

 SetPositivityIndexNil sets the value for PositivityIndex to be an explicit nil

### UnsetPositivityIndex
`func (o *ProjectRankTrackingStats) UnsetPositivityIndex()`

UnsetPositivityIndex ensures that no value is present for PositivityIndex, not even an explicit nil
### GetTrendPositivity

`func (o *ProjectRankTrackingStats) GetTrendPositivity() int32`

GetTrendPositivity returns the TrendPositivity field if non-nil, zero value otherwise.

### GetTrendPositivityOk

`func (o *ProjectRankTrackingStats) GetTrendPositivityOk() (*int32, bool)`

GetTrendPositivityOk returns a tuple with the TrendPositivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendPositivity

`func (o *ProjectRankTrackingStats) SetTrendPositivity(v int32)`

SetTrendPositivity sets TrendPositivity field to given value.

### HasTrendPositivity

`func (o *ProjectRankTrackingStats) HasTrendPositivity() bool`

HasTrendPositivity returns a boolean if a field has been set.

### SetTrendPositivityNil

`func (o *ProjectRankTrackingStats) SetTrendPositivityNil(b bool)`

 SetTrendPositivityNil sets the value for TrendPositivity to be an explicit nil

### UnsetTrendPositivity
`func (o *ProjectRankTrackingStats) UnsetTrendPositivity()`

UnsetTrendPositivity ensures that no value is present for TrendPositivity, not even an explicit nil
### GetMentionRate

`func (o *ProjectRankTrackingStats) GetMentionRate() int32`

GetMentionRate returns the MentionRate field if non-nil, zero value otherwise.

### GetMentionRateOk

`func (o *ProjectRankTrackingStats) GetMentionRateOk() (*int32, bool)`

GetMentionRateOk returns a tuple with the MentionRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionRate

`func (o *ProjectRankTrackingStats) SetMentionRate(v int32)`

SetMentionRate sets MentionRate field to given value.

### HasMentionRate

`func (o *ProjectRankTrackingStats) HasMentionRate() bool`

HasMentionRate returns a boolean if a field has been set.

### SetMentionRateNil

`func (o *ProjectRankTrackingStats) SetMentionRateNil(b bool)`

 SetMentionRateNil sets the value for MentionRate to be an explicit nil

### UnsetMentionRate
`func (o *ProjectRankTrackingStats) UnsetMentionRate()`

UnsetMentionRate ensures that no value is present for MentionRate, not even an explicit nil
### GetTrendMentionRate

`func (o *ProjectRankTrackingStats) GetTrendMentionRate() int32`

GetTrendMentionRate returns the TrendMentionRate field if non-nil, zero value otherwise.

### GetTrendMentionRateOk

`func (o *ProjectRankTrackingStats) GetTrendMentionRateOk() (*int32, bool)`

GetTrendMentionRateOk returns a tuple with the TrendMentionRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendMentionRate

`func (o *ProjectRankTrackingStats) SetTrendMentionRate(v int32)`

SetTrendMentionRate sets TrendMentionRate field to given value.

### HasTrendMentionRate

`func (o *ProjectRankTrackingStats) HasTrendMentionRate() bool`

HasTrendMentionRate returns a boolean if a field has been set.

### SetTrendMentionRateNil

`func (o *ProjectRankTrackingStats) SetTrendMentionRateNil(b bool)`

 SetTrendMentionRateNil sets the value for TrendMentionRate to be an explicit nil

### UnsetTrendMentionRate
`func (o *ProjectRankTrackingStats) UnsetTrendMentionRate()`

UnsetTrendMentionRate ensures that no value is present for TrendMentionRate, not even an explicit nil
### GetSerpRate

`func (o *ProjectRankTrackingStats) GetSerpRate() int32`

GetSerpRate returns the SerpRate field if non-nil, zero value otherwise.

### GetSerpRateOk

`func (o *ProjectRankTrackingStats) GetSerpRateOk() (*int32, bool)`

GetSerpRateOk returns a tuple with the SerpRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpRate

`func (o *ProjectRankTrackingStats) SetSerpRate(v int32)`

SetSerpRate sets SerpRate field to given value.

### HasSerpRate

`func (o *ProjectRankTrackingStats) HasSerpRate() bool`

HasSerpRate returns a boolean if a field has been set.

### SetSerpRateNil

`func (o *ProjectRankTrackingStats) SetSerpRateNil(b bool)`

 SetSerpRateNil sets the value for SerpRate to be an explicit nil

### UnsetSerpRate
`func (o *ProjectRankTrackingStats) UnsetSerpRate()`

UnsetSerpRate ensures that no value is present for SerpRate, not even an explicit nil
### GetTrendSerpRate

`func (o *ProjectRankTrackingStats) GetTrendSerpRate() int32`

GetTrendSerpRate returns the TrendSerpRate field if non-nil, zero value otherwise.

### GetTrendSerpRateOk

`func (o *ProjectRankTrackingStats) GetTrendSerpRateOk() (*int32, bool)`

GetTrendSerpRateOk returns a tuple with the TrendSerpRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendSerpRate

`func (o *ProjectRankTrackingStats) SetTrendSerpRate(v int32)`

SetTrendSerpRate sets TrendSerpRate field to given value.

### HasTrendSerpRate

`func (o *ProjectRankTrackingStats) HasTrendSerpRate() bool`

HasTrendSerpRate returns a boolean if a field has been set.

### SetTrendSerpRateNil

`func (o *ProjectRankTrackingStats) SetTrendSerpRateNil(b bool)`

 SetTrendSerpRateNil sets the value for TrendSerpRate to be an explicit nil

### UnsetTrendSerpRate
`func (o *ProjectRankTrackingStats) UnsetTrendSerpRate()`

UnsetTrendSerpRate ensures that no value is present for TrendSerpRate, not even an explicit nil
### GetShoppingRate

`func (o *ProjectRankTrackingStats) GetShoppingRate() int32`

GetShoppingRate returns the ShoppingRate field if non-nil, zero value otherwise.

### GetShoppingRateOk

`func (o *ProjectRankTrackingStats) GetShoppingRateOk() (*int32, bool)`

GetShoppingRateOk returns a tuple with the ShoppingRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShoppingRate

`func (o *ProjectRankTrackingStats) SetShoppingRate(v int32)`

SetShoppingRate sets ShoppingRate field to given value.

### HasShoppingRate

`func (o *ProjectRankTrackingStats) HasShoppingRate() bool`

HasShoppingRate returns a boolean if a field has been set.

### SetShoppingRateNil

`func (o *ProjectRankTrackingStats) SetShoppingRateNil(b bool)`

 SetShoppingRateNil sets the value for ShoppingRate to be an explicit nil

### UnsetShoppingRate
`func (o *ProjectRankTrackingStats) UnsetShoppingRate()`

UnsetShoppingRate ensures that no value is present for ShoppingRate, not even an explicit nil
### GetTrendShoppingRate

`func (o *ProjectRankTrackingStats) GetTrendShoppingRate() int32`

GetTrendShoppingRate returns the TrendShoppingRate field if non-nil, zero value otherwise.

### GetTrendShoppingRateOk

`func (o *ProjectRankTrackingStats) GetTrendShoppingRateOk() (*int32, bool)`

GetTrendShoppingRateOk returns a tuple with the TrendShoppingRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShoppingRate

`func (o *ProjectRankTrackingStats) SetTrendShoppingRate(v int32)`

SetTrendShoppingRate sets TrendShoppingRate field to given value.

### HasTrendShoppingRate

`func (o *ProjectRankTrackingStats) HasTrendShoppingRate() bool`

HasTrendShoppingRate returns a boolean if a field has been set.

### SetTrendShoppingRateNil

`func (o *ProjectRankTrackingStats) SetTrendShoppingRateNil(b bool)`

 SetTrendShoppingRateNil sets the value for TrendShoppingRate to be an explicit nil

### UnsetTrendShoppingRate
`func (o *ProjectRankTrackingStats) UnsetTrendShoppingRate()`

UnsetTrendShoppingRate ensures that no value is present for TrendShoppingRate, not even an explicit nil
### GetShareOfVoice

`func (o *ProjectRankTrackingStats) GetShareOfVoice() float32`

GetShareOfVoice returns the ShareOfVoice field if non-nil, zero value otherwise.

### GetShareOfVoiceOk

`func (o *ProjectRankTrackingStats) GetShareOfVoiceOk() (*float32, bool)`

GetShareOfVoiceOk returns a tuple with the ShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShareOfVoice

`func (o *ProjectRankTrackingStats) SetShareOfVoice(v float32)`

SetShareOfVoice sets ShareOfVoice field to given value.

### HasShareOfVoice

`func (o *ProjectRankTrackingStats) HasShareOfVoice() bool`

HasShareOfVoice returns a boolean if a field has been set.

### SetShareOfVoiceNil

`func (o *ProjectRankTrackingStats) SetShareOfVoiceNil(b bool)`

 SetShareOfVoiceNil sets the value for ShareOfVoice to be an explicit nil

### UnsetShareOfVoice
`func (o *ProjectRankTrackingStats) UnsetShareOfVoice()`

UnsetShareOfVoice ensures that no value is present for ShareOfVoice, not even an explicit nil
### GetTrendShareOfVoice

`func (o *ProjectRankTrackingStats) GetTrendShareOfVoice() float32`

GetTrendShareOfVoice returns the TrendShareOfVoice field if non-nil, zero value otherwise.

### GetTrendShareOfVoiceOk

`func (o *ProjectRankTrackingStats) GetTrendShareOfVoiceOk() (*float32, bool)`

GetTrendShareOfVoiceOk returns a tuple with the TrendShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShareOfVoice

`func (o *ProjectRankTrackingStats) SetTrendShareOfVoice(v float32)`

SetTrendShareOfVoice sets TrendShareOfVoice field to given value.

### HasTrendShareOfVoice

`func (o *ProjectRankTrackingStats) HasTrendShareOfVoice() bool`

HasTrendShareOfVoice returns a boolean if a field has been set.

### SetTrendShareOfVoiceNil

`func (o *ProjectRankTrackingStats) SetTrendShareOfVoiceNil(b bool)`

 SetTrendShareOfVoiceNil sets the value for TrendShareOfVoice to be an explicit nil

### UnsetTrendShareOfVoice
`func (o *ProjectRankTrackingStats) UnsetTrendShareOfVoice()`

UnsetTrendShareOfVoice ensures that no value is present for TrendShareOfVoice, not even an explicit nil
### GetSentimentPositive

`func (o *ProjectRankTrackingStats) GetSentimentPositive() int32`

GetSentimentPositive returns the SentimentPositive field if non-nil, zero value otherwise.

### GetSentimentPositiveOk

`func (o *ProjectRankTrackingStats) GetSentimentPositiveOk() (*int32, bool)`

GetSentimentPositiveOk returns a tuple with the SentimentPositive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentPositive

`func (o *ProjectRankTrackingStats) SetSentimentPositive(v int32)`

SetSentimentPositive sets SentimentPositive field to given value.


### GetSentimentNeutral

`func (o *ProjectRankTrackingStats) GetSentimentNeutral() int32`

GetSentimentNeutral returns the SentimentNeutral field if non-nil, zero value otherwise.

### GetSentimentNeutralOk

`func (o *ProjectRankTrackingStats) GetSentimentNeutralOk() (*int32, bool)`

GetSentimentNeutralOk returns a tuple with the SentimentNeutral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentNeutral

`func (o *ProjectRankTrackingStats) SetSentimentNeutral(v int32)`

SetSentimentNeutral sets SentimentNeutral field to given value.


### GetSentimentNegative

`func (o *ProjectRankTrackingStats) GetSentimentNegative() int32`

GetSentimentNegative returns the SentimentNegative field if non-nil, zero value otherwise.

### GetSentimentNegativeOk

`func (o *ProjectRankTrackingStats) GetSentimentNegativeOk() (*int32, bool)`

GetSentimentNegativeOk returns a tuple with the SentimentNegative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentNegative

`func (o *ProjectRankTrackingStats) SetSentimentNegative(v int32)`

SetSentimentNegative sets SentimentNegative field to given value.


### GetMentionCount

`func (o *ProjectRankTrackingStats) GetMentionCount() int32`

GetMentionCount returns the MentionCount field if non-nil, zero value otherwise.

### GetMentionCountOk

`func (o *ProjectRankTrackingStats) GetMentionCountOk() (*int32, bool)`

GetMentionCountOk returns a tuple with the MentionCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionCount

`func (o *ProjectRankTrackingStats) SetMentionCount(v int32)`

SetMentionCount sets MentionCount field to given value.


### GetAiTrackedQueryCount

`func (o *ProjectRankTrackingStats) GetAiTrackedQueryCount() int32`

GetAiTrackedQueryCount returns the AiTrackedQueryCount field if non-nil, zero value otherwise.

### GetAiTrackedQueryCountOk

`func (o *ProjectRankTrackingStats) GetAiTrackedQueryCountOk() (*int32, bool)`

GetAiTrackedQueryCountOk returns a tuple with the AiTrackedQueryCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAiTrackedQueryCount

`func (o *ProjectRankTrackingStats) SetAiTrackedQueryCount(v int32)`

SetAiTrackedQueryCount sets AiTrackedQueryCount field to given value.


### GetAiQueriesWithMention

`func (o *ProjectRankTrackingStats) GetAiQueriesWithMention() int32`

GetAiQueriesWithMention returns the AiQueriesWithMention field if non-nil, zero value otherwise.

### GetAiQueriesWithMentionOk

`func (o *ProjectRankTrackingStats) GetAiQueriesWithMentionOk() (*int32, bool)`

GetAiQueriesWithMentionOk returns a tuple with the AiQueriesWithMention field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAiQueriesWithMention

`func (o *ProjectRankTrackingStats) SetAiQueriesWithMention(v int32)`

SetAiQueriesWithMention sets AiQueriesWithMention field to given value.


### GetSerpTrackedQueryCount

`func (o *ProjectRankTrackingStats) GetSerpTrackedQueryCount() int32`

GetSerpTrackedQueryCount returns the SerpTrackedQueryCount field if non-nil, zero value otherwise.

### GetSerpTrackedQueryCountOk

`func (o *ProjectRankTrackingStats) GetSerpTrackedQueryCountOk() (*int32, bool)`

GetSerpTrackedQueryCountOk returns a tuple with the SerpTrackedQueryCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpTrackedQueryCount

`func (o *ProjectRankTrackingStats) SetSerpTrackedQueryCount(v int32)`

SetSerpTrackedQueryCount sets SerpTrackedQueryCount field to given value.


### GetSerpQueriesWithResult

`func (o *ProjectRankTrackingStats) GetSerpQueriesWithResult() int32`

GetSerpQueriesWithResult returns the SerpQueriesWithResult field if non-nil, zero value otherwise.

### GetSerpQueriesWithResultOk

`func (o *ProjectRankTrackingStats) GetSerpQueriesWithResultOk() (*int32, bool)`

GetSerpQueriesWithResultOk returns a tuple with the SerpQueriesWithResult field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpQueriesWithResult

`func (o *ProjectRankTrackingStats) SetSerpQueriesWithResult(v int32)`

SetSerpQueriesWithResult sets SerpQueriesWithResult field to given value.


### GetShoppingTrackedQueryCount

`func (o *ProjectRankTrackingStats) GetShoppingTrackedQueryCount() int32`

GetShoppingTrackedQueryCount returns the ShoppingTrackedQueryCount field if non-nil, zero value otherwise.

### GetShoppingTrackedQueryCountOk

`func (o *ProjectRankTrackingStats) GetShoppingTrackedQueryCountOk() (*int32, bool)`

GetShoppingTrackedQueryCountOk returns a tuple with the ShoppingTrackedQueryCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShoppingTrackedQueryCount

`func (o *ProjectRankTrackingStats) SetShoppingTrackedQueryCount(v int32)`

SetShoppingTrackedQueryCount sets ShoppingTrackedQueryCount field to given value.


### GetShoppingQueriesWithResult

`func (o *ProjectRankTrackingStats) GetShoppingQueriesWithResult() int32`

GetShoppingQueriesWithResult returns the ShoppingQueriesWithResult field if non-nil, zero value otherwise.

### GetShoppingQueriesWithResultOk

`func (o *ProjectRankTrackingStats) GetShoppingQueriesWithResultOk() (*int32, bool)`

GetShoppingQueriesWithResultOk returns a tuple with the ShoppingQueriesWithResult field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShoppingQueriesWithResult

`func (o *ProjectRankTrackingStats) SetShoppingQueriesWithResult(v int32)`

SetShoppingQueriesWithResult sets ShoppingQueriesWithResult field to given value.


### GetMentionTypeCounts

`func (o *ProjectRankTrackingStats) GetMentionTypeCounts() MentionTypeCounts`

GetMentionTypeCounts returns the MentionTypeCounts field if non-nil, zero value otherwise.

### GetMentionTypeCountsOk

`func (o *ProjectRankTrackingStats) GetMentionTypeCountsOk() (*MentionTypeCounts, bool)`

GetMentionTypeCountsOk returns a tuple with the MentionTypeCounts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionTypeCounts

`func (o *ProjectRankTrackingStats) SetMentionTypeCounts(v MentionTypeCounts)`

SetMentionTypeCounts sets MentionTypeCounts field to given value.


### GetDataDirtySince

`func (o *ProjectRankTrackingStats) GetDataDirtySince() string`

GetDataDirtySince returns the DataDirtySince field if non-nil, zero value otherwise.

### GetDataDirtySinceOk

`func (o *ProjectRankTrackingStats) GetDataDirtySinceOk() (*string, bool)`

GetDataDirtySinceOk returns a tuple with the DataDirtySince field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataDirtySince

`func (o *ProjectRankTrackingStats) SetDataDirtySince(v string)`

SetDataDirtySince sets DataDirtySince field to given value.

### HasDataDirtySince

`func (o *ProjectRankTrackingStats) HasDataDirtySince() bool`

HasDataDirtySince returns a boolean if a field has been set.

### SetDataDirtySinceNil

`func (o *ProjectRankTrackingStats) SetDataDirtySinceNil(b bool)`

 SetDataDirtySinceNil sets the value for DataDirtySince to be an explicit nil

### UnsetDataDirtySince
`func (o *ProjectRankTrackingStats) UnsetDataDirtySince()`

UnsetDataDirtySince ensures that no value is present for DataDirtySince, not even an explicit nil
### GetMentionPositionDistribution

`func (o *ProjectRankTrackingStats) GetMentionPositionDistribution() []PositionDistributionBucket`

GetMentionPositionDistribution returns the MentionPositionDistribution field if non-nil, zero value otherwise.

### GetMentionPositionDistributionOk

`func (o *ProjectRankTrackingStats) GetMentionPositionDistributionOk() (*[]PositionDistributionBucket, bool)`

GetMentionPositionDistributionOk returns a tuple with the MentionPositionDistribution field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionPositionDistribution

`func (o *ProjectRankTrackingStats) SetMentionPositionDistribution(v []PositionDistributionBucket)`

SetMentionPositionDistribution sets MentionPositionDistribution field to given value.

### HasMentionPositionDistribution

`func (o *ProjectRankTrackingStats) HasMentionPositionDistribution() bool`

HasMentionPositionDistribution returns a boolean if a field has been set.

### GetSerpPositionDistribution

`func (o *ProjectRankTrackingStats) GetSerpPositionDistribution() []PositionDistributionBucket`

GetSerpPositionDistribution returns the SerpPositionDistribution field if non-nil, zero value otherwise.

### GetSerpPositionDistributionOk

`func (o *ProjectRankTrackingStats) GetSerpPositionDistributionOk() (*[]PositionDistributionBucket, bool)`

GetSerpPositionDistributionOk returns a tuple with the SerpPositionDistribution field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpPositionDistribution

`func (o *ProjectRankTrackingStats) SetSerpPositionDistribution(v []PositionDistributionBucket)`

SetSerpPositionDistribution sets SerpPositionDistribution field to given value.

### HasSerpPositionDistribution

`func (o *ProjectRankTrackingStats) HasSerpPositionDistribution() bool`

HasSerpPositionDistribution returns a boolean if a field has been set.

### GetShoppingPositionDistribution

`func (o *ProjectRankTrackingStats) GetShoppingPositionDistribution() []PositionDistributionBucket`

GetShoppingPositionDistribution returns the ShoppingPositionDistribution field if non-nil, zero value otherwise.

### GetShoppingPositionDistributionOk

`func (o *ProjectRankTrackingStats) GetShoppingPositionDistributionOk() (*[]PositionDistributionBucket, bool)`

GetShoppingPositionDistributionOk returns a tuple with the ShoppingPositionDistribution field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShoppingPositionDistribution

`func (o *ProjectRankTrackingStats) SetShoppingPositionDistribution(v []PositionDistributionBucket)`

SetShoppingPositionDistribution sets ShoppingPositionDistribution field to given value.

### HasShoppingPositionDistribution

`func (o *ProjectRankTrackingStats) HasShoppingPositionDistribution() bool`

HasShoppingPositionDistribution returns a boolean if a field has been set.

### GetCompetitorShareOfVoice

`func (o *ProjectRankTrackingStats) GetCompetitorShareOfVoice() []CompetitorShareOfVoice`

GetCompetitorShareOfVoice returns the CompetitorShareOfVoice field if non-nil, zero value otherwise.

### GetCompetitorShareOfVoiceOk

`func (o *ProjectRankTrackingStats) GetCompetitorShareOfVoiceOk() (*[]CompetitorShareOfVoice, bool)`

GetCompetitorShareOfVoiceOk returns a tuple with the CompetitorShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitorShareOfVoice

`func (o *ProjectRankTrackingStats) SetCompetitorShareOfVoice(v []CompetitorShareOfVoice)`

SetCompetitorShareOfVoice sets CompetitorShareOfVoice field to given value.

### HasCompetitorShareOfVoice

`func (o *ProjectRankTrackingStats) HasCompetitorShareOfVoice() bool`

HasCompetitorShareOfVoice returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


