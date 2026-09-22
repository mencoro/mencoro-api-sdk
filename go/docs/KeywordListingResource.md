# KeywordListingResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Keyword** | **string** | The keyword as a human types it, picked from the variants for display. | 
**KeywordNormalized** | **string** | The grouping key: the keyword lower-cased and unaccented. Unique within the project, and the stable way to match a row across pages. | 
**VariantCount** | **int32** | Tracked queries behind this row that the current filters selected. | 
**VariantIds** | **[]string** | Ids of those tracked queries. Accepted by the single tracked-query operation. | 
**Engines** | **[]string** | Distinct engines across the variants, not a single engine. | 
**Countries** | **[]string** | Distinct ISO-3166 alpha-2 countries across the variants. | 
**QueryClusterIds** | **[]string** | Distinct keyword clusters the variants belong to. Empty when none of them is clustered. | 
**HasUnclusteredVariant** | **bool** | Whether at least one variant belongs to no cluster. | 
**StatusSummary** | **string** | \&quot;mixed\&quot; when the variants disagree; otherwise the one status they share. | 
**Statuses** | **[]string** | Distinct statuses across the variants. | 
**CheckFrequencies** | **[]string** | Distinct check frequencies across the variants. | 
**NPassesValues** | **[]int32** | Distinct pass counts across the variants. A pass is one budget unit per check. | 
**LastCheckedAt** | Pointer to **NullableTime** | The most recent completed check across the variants. Null when none has ever completed — not a check that found nothing. | [optional] 
**AvgSerpPosition** | Pointer to **NullableFloat32** | Average position in traditional search over the window. 1-based, LOWER is better. | [optional] 
**TrendSerp** | Pointer to **NullableFloat32** | Signed improvement in avgSerpPosition against the previous window. Positive is better. | [optional] 
**AvgShoppingPosition** | Pointer to **NullableFloat32** | Average position in shopping results over the window. 1-based, LOWER is better. | [optional] 
**TrendShopping** | Pointer to **NullableFloat32** | Signed improvement in avgShoppingPosition. Positive is better. | [optional] 
**AvgMentionPosition** | Pointer to **NullableFloat32** | Average position of the brand mention inside the AI answer. 1-based, LOWER is better. | [optional] 
**TrendMention** | Pointer to **NullableFloat32** | Signed improvement in avgMentionPosition. Positive is better. | [optional] 
**AvgLinkPosition** | Pointer to **NullableFloat32** | Average position of a cited link to the brand. 1-based, LOWER is better. | [optional] 
**TrendLink** | Pointer to **NullableFloat32** | Signed improvement in avgLinkPosition. Positive is better. | [optional] 
**MentionPositionStability** | Pointer to **NullableFloat32** | Day-to-day spread of the mention position (a standard deviation): LOWER means steadier. | [optional] 
**TrendStability** | Pointer to **NullableFloat32** | Signed improvement in mentionPositionStability. Positive means steadier than the previous window. | [optional] 
**PositivityIndex** | Pointer to **NullableInt32** | 0-100 weighted sentiment score of the mentions; HIGHER is better. Null when there were no mentions to score. | [optional] 
**TrendPositivity** | Pointer to **NullableInt32** | Signed improvement in positivityIndex. Positive is better. | [optional] 
**MentionRate** | Pointer to **NullableInt32** | 0-100 share of AI captures in the window that mentioned the brand; HIGHER is better. | [optional] 
**TrendMentionRate** | Pointer to **NullableInt32** | Signed improvement in mentionRate. Positive is better. | [optional] 
**SerpRate** | Pointer to **NullableInt32** | 0-100 share of traditional-search captures in the window that ranked the brand; HIGHER is better. | [optional] 
**TrendSerpRate** | Pointer to **NullableInt32** | Signed improvement in serpRate. Positive is better. | [optional] 
**ShareOfVoice** | Pointer to **NullableFloat32** | 0-100 share of the weighted AI mentions against every tracked brand; HIGHER is better. | [optional] 
**TrendShareOfVoice** | Pointer to **NullableFloat32** | Signed improvement in shareOfVoice. Positive is better. | [optional] 
**SentimentPositive** | **int32** | Positive brand mentions counted in the window. Zero here really is zero. | 
**SentimentNeutral** | **int32** | Neutral brand mentions counted in the window. | 
**SentimentNegative** | **int32** | Negative brand mentions counted in the window. | 
**AvgMentionCount** | Pointer to **NullableFloat32** | Mentions per AI engine per day with a capture, over the window. Not a total: the window total is not part of this contract. | [optional] 
**MentionTypeCounts** | [**KeywordListingResourceMentionTypeCounts**](KeywordListingResourceMentionTypeCounts.md) |  | 

## Methods

### NewKeywordListingResource

`func NewKeywordListingResource(keyword string, keywordNormalized string, variantCount int32, variantIds []string, engines []string, countries []string, queryClusterIds []string, hasUnclusteredVariant bool, statusSummary string, statuses []string, checkFrequencies []string, nPassesValues []int32, sentimentPositive int32, sentimentNeutral int32, sentimentNegative int32, mentionTypeCounts KeywordListingResourceMentionTypeCounts, ) *KeywordListingResource`

NewKeywordListingResource instantiates a new KeywordListingResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewKeywordListingResourceWithDefaults

`func NewKeywordListingResourceWithDefaults() *KeywordListingResource`

NewKeywordListingResourceWithDefaults instantiates a new KeywordListingResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKeyword

`func (o *KeywordListingResource) GetKeyword() string`

GetKeyword returns the Keyword field if non-nil, zero value otherwise.

### GetKeywordOk

`func (o *KeywordListingResource) GetKeywordOk() (*string, bool)`

GetKeywordOk returns a tuple with the Keyword field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKeyword

`func (o *KeywordListingResource) SetKeyword(v string)`

SetKeyword sets Keyword field to given value.


### GetKeywordNormalized

`func (o *KeywordListingResource) GetKeywordNormalized() string`

GetKeywordNormalized returns the KeywordNormalized field if non-nil, zero value otherwise.

### GetKeywordNormalizedOk

`func (o *KeywordListingResource) GetKeywordNormalizedOk() (*string, bool)`

GetKeywordNormalizedOk returns a tuple with the KeywordNormalized field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKeywordNormalized

`func (o *KeywordListingResource) SetKeywordNormalized(v string)`

SetKeywordNormalized sets KeywordNormalized field to given value.


### GetVariantCount

`func (o *KeywordListingResource) GetVariantCount() int32`

GetVariantCount returns the VariantCount field if non-nil, zero value otherwise.

### GetVariantCountOk

`func (o *KeywordListingResource) GetVariantCountOk() (*int32, bool)`

GetVariantCountOk returns a tuple with the VariantCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariantCount

`func (o *KeywordListingResource) SetVariantCount(v int32)`

SetVariantCount sets VariantCount field to given value.


### GetVariantIds

`func (o *KeywordListingResource) GetVariantIds() []string`

GetVariantIds returns the VariantIds field if non-nil, zero value otherwise.

### GetVariantIdsOk

`func (o *KeywordListingResource) GetVariantIdsOk() (*[]string, bool)`

GetVariantIdsOk returns a tuple with the VariantIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariantIds

`func (o *KeywordListingResource) SetVariantIds(v []string)`

SetVariantIds sets VariantIds field to given value.


### GetEngines

`func (o *KeywordListingResource) GetEngines() []string`

GetEngines returns the Engines field if non-nil, zero value otherwise.

### GetEnginesOk

`func (o *KeywordListingResource) GetEnginesOk() (*[]string, bool)`

GetEnginesOk returns a tuple with the Engines field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngines

`func (o *KeywordListingResource) SetEngines(v []string)`

SetEngines sets Engines field to given value.


### GetCountries

`func (o *KeywordListingResource) GetCountries() []string`

GetCountries returns the Countries field if non-nil, zero value otherwise.

### GetCountriesOk

`func (o *KeywordListingResource) GetCountriesOk() (*[]string, bool)`

GetCountriesOk returns a tuple with the Countries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountries

`func (o *KeywordListingResource) SetCountries(v []string)`

SetCountries sets Countries field to given value.


### GetQueryClusterIds

`func (o *KeywordListingResource) GetQueryClusterIds() []string`

GetQueryClusterIds returns the QueryClusterIds field if non-nil, zero value otherwise.

### GetQueryClusterIdsOk

`func (o *KeywordListingResource) GetQueryClusterIdsOk() (*[]string, bool)`

GetQueryClusterIdsOk returns a tuple with the QueryClusterIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryClusterIds

`func (o *KeywordListingResource) SetQueryClusterIds(v []string)`

SetQueryClusterIds sets QueryClusterIds field to given value.


### GetHasUnclusteredVariant

`func (o *KeywordListingResource) GetHasUnclusteredVariant() bool`

GetHasUnclusteredVariant returns the HasUnclusteredVariant field if non-nil, zero value otherwise.

### GetHasUnclusteredVariantOk

`func (o *KeywordListingResource) GetHasUnclusteredVariantOk() (*bool, bool)`

GetHasUnclusteredVariantOk returns a tuple with the HasUnclusteredVariant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasUnclusteredVariant

`func (o *KeywordListingResource) SetHasUnclusteredVariant(v bool)`

SetHasUnclusteredVariant sets HasUnclusteredVariant field to given value.


### GetStatusSummary

`func (o *KeywordListingResource) GetStatusSummary() string`

GetStatusSummary returns the StatusSummary field if non-nil, zero value otherwise.

### GetStatusSummaryOk

`func (o *KeywordListingResource) GetStatusSummaryOk() (*string, bool)`

GetStatusSummaryOk returns a tuple with the StatusSummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusSummary

`func (o *KeywordListingResource) SetStatusSummary(v string)`

SetStatusSummary sets StatusSummary field to given value.


### GetStatuses

`func (o *KeywordListingResource) GetStatuses() []string`

GetStatuses returns the Statuses field if non-nil, zero value otherwise.

### GetStatusesOk

`func (o *KeywordListingResource) GetStatusesOk() (*[]string, bool)`

GetStatusesOk returns a tuple with the Statuses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatuses

`func (o *KeywordListingResource) SetStatuses(v []string)`

SetStatuses sets Statuses field to given value.


### GetCheckFrequencies

`func (o *KeywordListingResource) GetCheckFrequencies() []string`

GetCheckFrequencies returns the CheckFrequencies field if non-nil, zero value otherwise.

### GetCheckFrequenciesOk

`func (o *KeywordListingResource) GetCheckFrequenciesOk() (*[]string, bool)`

GetCheckFrequenciesOk returns a tuple with the CheckFrequencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckFrequencies

`func (o *KeywordListingResource) SetCheckFrequencies(v []string)`

SetCheckFrequencies sets CheckFrequencies field to given value.


### GetNPassesValues

`func (o *KeywordListingResource) GetNPassesValues() []int32`

GetNPassesValues returns the NPassesValues field if non-nil, zero value otherwise.

### GetNPassesValuesOk

`func (o *KeywordListingResource) GetNPassesValuesOk() (*[]int32, bool)`

GetNPassesValuesOk returns a tuple with the NPassesValues field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNPassesValues

`func (o *KeywordListingResource) SetNPassesValues(v []int32)`

SetNPassesValues sets NPassesValues field to given value.


### GetLastCheckedAt

`func (o *KeywordListingResource) GetLastCheckedAt() time.Time`

GetLastCheckedAt returns the LastCheckedAt field if non-nil, zero value otherwise.

### GetLastCheckedAtOk

`func (o *KeywordListingResource) GetLastCheckedAtOk() (*time.Time, bool)`

GetLastCheckedAtOk returns a tuple with the LastCheckedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastCheckedAt

`func (o *KeywordListingResource) SetLastCheckedAt(v time.Time)`

SetLastCheckedAt sets LastCheckedAt field to given value.

### HasLastCheckedAt

`func (o *KeywordListingResource) HasLastCheckedAt() bool`

HasLastCheckedAt returns a boolean if a field has been set.

### SetLastCheckedAtNil

`func (o *KeywordListingResource) SetLastCheckedAtNil(b bool)`

 SetLastCheckedAtNil sets the value for LastCheckedAt to be an explicit nil

### UnsetLastCheckedAt
`func (o *KeywordListingResource) UnsetLastCheckedAt()`

UnsetLastCheckedAt ensures that no value is present for LastCheckedAt, not even an explicit nil
### GetAvgSerpPosition

`func (o *KeywordListingResource) GetAvgSerpPosition() float32`

GetAvgSerpPosition returns the AvgSerpPosition field if non-nil, zero value otherwise.

### GetAvgSerpPositionOk

`func (o *KeywordListingResource) GetAvgSerpPositionOk() (*float32, bool)`

GetAvgSerpPositionOk returns a tuple with the AvgSerpPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgSerpPosition

`func (o *KeywordListingResource) SetAvgSerpPosition(v float32)`

SetAvgSerpPosition sets AvgSerpPosition field to given value.

### HasAvgSerpPosition

`func (o *KeywordListingResource) HasAvgSerpPosition() bool`

HasAvgSerpPosition returns a boolean if a field has been set.

### SetAvgSerpPositionNil

`func (o *KeywordListingResource) SetAvgSerpPositionNil(b bool)`

 SetAvgSerpPositionNil sets the value for AvgSerpPosition to be an explicit nil

### UnsetAvgSerpPosition
`func (o *KeywordListingResource) UnsetAvgSerpPosition()`

UnsetAvgSerpPosition ensures that no value is present for AvgSerpPosition, not even an explicit nil
### GetTrendSerp

`func (o *KeywordListingResource) GetTrendSerp() float32`

GetTrendSerp returns the TrendSerp field if non-nil, zero value otherwise.

### GetTrendSerpOk

`func (o *KeywordListingResource) GetTrendSerpOk() (*float32, bool)`

GetTrendSerpOk returns a tuple with the TrendSerp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendSerp

`func (o *KeywordListingResource) SetTrendSerp(v float32)`

SetTrendSerp sets TrendSerp field to given value.

### HasTrendSerp

`func (o *KeywordListingResource) HasTrendSerp() bool`

HasTrendSerp returns a boolean if a field has been set.

### SetTrendSerpNil

`func (o *KeywordListingResource) SetTrendSerpNil(b bool)`

 SetTrendSerpNil sets the value for TrendSerp to be an explicit nil

### UnsetTrendSerp
`func (o *KeywordListingResource) UnsetTrendSerp()`

UnsetTrendSerp ensures that no value is present for TrendSerp, not even an explicit nil
### GetAvgShoppingPosition

`func (o *KeywordListingResource) GetAvgShoppingPosition() float32`

GetAvgShoppingPosition returns the AvgShoppingPosition field if non-nil, zero value otherwise.

### GetAvgShoppingPositionOk

`func (o *KeywordListingResource) GetAvgShoppingPositionOk() (*float32, bool)`

GetAvgShoppingPositionOk returns a tuple with the AvgShoppingPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgShoppingPosition

`func (o *KeywordListingResource) SetAvgShoppingPosition(v float32)`

SetAvgShoppingPosition sets AvgShoppingPosition field to given value.

### HasAvgShoppingPosition

`func (o *KeywordListingResource) HasAvgShoppingPosition() bool`

HasAvgShoppingPosition returns a boolean if a field has been set.

### SetAvgShoppingPositionNil

`func (o *KeywordListingResource) SetAvgShoppingPositionNil(b bool)`

 SetAvgShoppingPositionNil sets the value for AvgShoppingPosition to be an explicit nil

### UnsetAvgShoppingPosition
`func (o *KeywordListingResource) UnsetAvgShoppingPosition()`

UnsetAvgShoppingPosition ensures that no value is present for AvgShoppingPosition, not even an explicit nil
### GetTrendShopping

`func (o *KeywordListingResource) GetTrendShopping() float32`

GetTrendShopping returns the TrendShopping field if non-nil, zero value otherwise.

### GetTrendShoppingOk

`func (o *KeywordListingResource) GetTrendShoppingOk() (*float32, bool)`

GetTrendShoppingOk returns a tuple with the TrendShopping field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShopping

`func (o *KeywordListingResource) SetTrendShopping(v float32)`

SetTrendShopping sets TrendShopping field to given value.

### HasTrendShopping

`func (o *KeywordListingResource) HasTrendShopping() bool`

HasTrendShopping returns a boolean if a field has been set.

### SetTrendShoppingNil

`func (o *KeywordListingResource) SetTrendShoppingNil(b bool)`

 SetTrendShoppingNil sets the value for TrendShopping to be an explicit nil

### UnsetTrendShopping
`func (o *KeywordListingResource) UnsetTrendShopping()`

UnsetTrendShopping ensures that no value is present for TrendShopping, not even an explicit nil
### GetAvgMentionPosition

`func (o *KeywordListingResource) GetAvgMentionPosition() float32`

GetAvgMentionPosition returns the AvgMentionPosition field if non-nil, zero value otherwise.

### GetAvgMentionPositionOk

`func (o *KeywordListingResource) GetAvgMentionPositionOk() (*float32, bool)`

GetAvgMentionPositionOk returns a tuple with the AvgMentionPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgMentionPosition

`func (o *KeywordListingResource) SetAvgMentionPosition(v float32)`

SetAvgMentionPosition sets AvgMentionPosition field to given value.

### HasAvgMentionPosition

`func (o *KeywordListingResource) HasAvgMentionPosition() bool`

HasAvgMentionPosition returns a boolean if a field has been set.

### SetAvgMentionPositionNil

`func (o *KeywordListingResource) SetAvgMentionPositionNil(b bool)`

 SetAvgMentionPositionNil sets the value for AvgMentionPosition to be an explicit nil

### UnsetAvgMentionPosition
`func (o *KeywordListingResource) UnsetAvgMentionPosition()`

UnsetAvgMentionPosition ensures that no value is present for AvgMentionPosition, not even an explicit nil
### GetTrendMention

`func (o *KeywordListingResource) GetTrendMention() float32`

GetTrendMention returns the TrendMention field if non-nil, zero value otherwise.

### GetTrendMentionOk

`func (o *KeywordListingResource) GetTrendMentionOk() (*float32, bool)`

GetTrendMentionOk returns a tuple with the TrendMention field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendMention

`func (o *KeywordListingResource) SetTrendMention(v float32)`

SetTrendMention sets TrendMention field to given value.

### HasTrendMention

`func (o *KeywordListingResource) HasTrendMention() bool`

HasTrendMention returns a boolean if a field has been set.

### SetTrendMentionNil

`func (o *KeywordListingResource) SetTrendMentionNil(b bool)`

 SetTrendMentionNil sets the value for TrendMention to be an explicit nil

### UnsetTrendMention
`func (o *KeywordListingResource) UnsetTrendMention()`

UnsetTrendMention ensures that no value is present for TrendMention, not even an explicit nil
### GetAvgLinkPosition

`func (o *KeywordListingResource) GetAvgLinkPosition() float32`

GetAvgLinkPosition returns the AvgLinkPosition field if non-nil, zero value otherwise.

### GetAvgLinkPositionOk

`func (o *KeywordListingResource) GetAvgLinkPositionOk() (*float32, bool)`

GetAvgLinkPositionOk returns a tuple with the AvgLinkPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgLinkPosition

`func (o *KeywordListingResource) SetAvgLinkPosition(v float32)`

SetAvgLinkPosition sets AvgLinkPosition field to given value.

### HasAvgLinkPosition

`func (o *KeywordListingResource) HasAvgLinkPosition() bool`

HasAvgLinkPosition returns a boolean if a field has been set.

### SetAvgLinkPositionNil

`func (o *KeywordListingResource) SetAvgLinkPositionNil(b bool)`

 SetAvgLinkPositionNil sets the value for AvgLinkPosition to be an explicit nil

### UnsetAvgLinkPosition
`func (o *KeywordListingResource) UnsetAvgLinkPosition()`

UnsetAvgLinkPosition ensures that no value is present for AvgLinkPosition, not even an explicit nil
### GetTrendLink

`func (o *KeywordListingResource) GetTrendLink() float32`

GetTrendLink returns the TrendLink field if non-nil, zero value otherwise.

### GetTrendLinkOk

`func (o *KeywordListingResource) GetTrendLinkOk() (*float32, bool)`

GetTrendLinkOk returns a tuple with the TrendLink field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendLink

`func (o *KeywordListingResource) SetTrendLink(v float32)`

SetTrendLink sets TrendLink field to given value.

### HasTrendLink

`func (o *KeywordListingResource) HasTrendLink() bool`

HasTrendLink returns a boolean if a field has been set.

### SetTrendLinkNil

`func (o *KeywordListingResource) SetTrendLinkNil(b bool)`

 SetTrendLinkNil sets the value for TrendLink to be an explicit nil

### UnsetTrendLink
`func (o *KeywordListingResource) UnsetTrendLink()`

UnsetTrendLink ensures that no value is present for TrendLink, not even an explicit nil
### GetMentionPositionStability

`func (o *KeywordListingResource) GetMentionPositionStability() float32`

GetMentionPositionStability returns the MentionPositionStability field if non-nil, zero value otherwise.

### GetMentionPositionStabilityOk

`func (o *KeywordListingResource) GetMentionPositionStabilityOk() (*float32, bool)`

GetMentionPositionStabilityOk returns a tuple with the MentionPositionStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionPositionStability

`func (o *KeywordListingResource) SetMentionPositionStability(v float32)`

SetMentionPositionStability sets MentionPositionStability field to given value.

### HasMentionPositionStability

`func (o *KeywordListingResource) HasMentionPositionStability() bool`

HasMentionPositionStability returns a boolean if a field has been set.

### SetMentionPositionStabilityNil

`func (o *KeywordListingResource) SetMentionPositionStabilityNil(b bool)`

 SetMentionPositionStabilityNil sets the value for MentionPositionStability to be an explicit nil

### UnsetMentionPositionStability
`func (o *KeywordListingResource) UnsetMentionPositionStability()`

UnsetMentionPositionStability ensures that no value is present for MentionPositionStability, not even an explicit nil
### GetTrendStability

`func (o *KeywordListingResource) GetTrendStability() float32`

GetTrendStability returns the TrendStability field if non-nil, zero value otherwise.

### GetTrendStabilityOk

`func (o *KeywordListingResource) GetTrendStabilityOk() (*float32, bool)`

GetTrendStabilityOk returns a tuple with the TrendStability field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendStability

`func (o *KeywordListingResource) SetTrendStability(v float32)`

SetTrendStability sets TrendStability field to given value.

### HasTrendStability

`func (o *KeywordListingResource) HasTrendStability() bool`

HasTrendStability returns a boolean if a field has been set.

### SetTrendStabilityNil

`func (o *KeywordListingResource) SetTrendStabilityNil(b bool)`

 SetTrendStabilityNil sets the value for TrendStability to be an explicit nil

### UnsetTrendStability
`func (o *KeywordListingResource) UnsetTrendStability()`

UnsetTrendStability ensures that no value is present for TrendStability, not even an explicit nil
### GetPositivityIndex

`func (o *KeywordListingResource) GetPositivityIndex() int32`

GetPositivityIndex returns the PositivityIndex field if non-nil, zero value otherwise.

### GetPositivityIndexOk

`func (o *KeywordListingResource) GetPositivityIndexOk() (*int32, bool)`

GetPositivityIndexOk returns a tuple with the PositivityIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPositivityIndex

`func (o *KeywordListingResource) SetPositivityIndex(v int32)`

SetPositivityIndex sets PositivityIndex field to given value.

### HasPositivityIndex

`func (o *KeywordListingResource) HasPositivityIndex() bool`

HasPositivityIndex returns a boolean if a field has been set.

### SetPositivityIndexNil

`func (o *KeywordListingResource) SetPositivityIndexNil(b bool)`

 SetPositivityIndexNil sets the value for PositivityIndex to be an explicit nil

### UnsetPositivityIndex
`func (o *KeywordListingResource) UnsetPositivityIndex()`

UnsetPositivityIndex ensures that no value is present for PositivityIndex, not even an explicit nil
### GetTrendPositivity

`func (o *KeywordListingResource) GetTrendPositivity() int32`

GetTrendPositivity returns the TrendPositivity field if non-nil, zero value otherwise.

### GetTrendPositivityOk

`func (o *KeywordListingResource) GetTrendPositivityOk() (*int32, bool)`

GetTrendPositivityOk returns a tuple with the TrendPositivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendPositivity

`func (o *KeywordListingResource) SetTrendPositivity(v int32)`

SetTrendPositivity sets TrendPositivity field to given value.

### HasTrendPositivity

`func (o *KeywordListingResource) HasTrendPositivity() bool`

HasTrendPositivity returns a boolean if a field has been set.

### SetTrendPositivityNil

`func (o *KeywordListingResource) SetTrendPositivityNil(b bool)`

 SetTrendPositivityNil sets the value for TrendPositivity to be an explicit nil

### UnsetTrendPositivity
`func (o *KeywordListingResource) UnsetTrendPositivity()`

UnsetTrendPositivity ensures that no value is present for TrendPositivity, not even an explicit nil
### GetMentionRate

`func (o *KeywordListingResource) GetMentionRate() int32`

GetMentionRate returns the MentionRate field if non-nil, zero value otherwise.

### GetMentionRateOk

`func (o *KeywordListingResource) GetMentionRateOk() (*int32, bool)`

GetMentionRateOk returns a tuple with the MentionRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionRate

`func (o *KeywordListingResource) SetMentionRate(v int32)`

SetMentionRate sets MentionRate field to given value.

### HasMentionRate

`func (o *KeywordListingResource) HasMentionRate() bool`

HasMentionRate returns a boolean if a field has been set.

### SetMentionRateNil

`func (o *KeywordListingResource) SetMentionRateNil(b bool)`

 SetMentionRateNil sets the value for MentionRate to be an explicit nil

### UnsetMentionRate
`func (o *KeywordListingResource) UnsetMentionRate()`

UnsetMentionRate ensures that no value is present for MentionRate, not even an explicit nil
### GetTrendMentionRate

`func (o *KeywordListingResource) GetTrendMentionRate() int32`

GetTrendMentionRate returns the TrendMentionRate field if non-nil, zero value otherwise.

### GetTrendMentionRateOk

`func (o *KeywordListingResource) GetTrendMentionRateOk() (*int32, bool)`

GetTrendMentionRateOk returns a tuple with the TrendMentionRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendMentionRate

`func (o *KeywordListingResource) SetTrendMentionRate(v int32)`

SetTrendMentionRate sets TrendMentionRate field to given value.

### HasTrendMentionRate

`func (o *KeywordListingResource) HasTrendMentionRate() bool`

HasTrendMentionRate returns a boolean if a field has been set.

### SetTrendMentionRateNil

`func (o *KeywordListingResource) SetTrendMentionRateNil(b bool)`

 SetTrendMentionRateNil sets the value for TrendMentionRate to be an explicit nil

### UnsetTrendMentionRate
`func (o *KeywordListingResource) UnsetTrendMentionRate()`

UnsetTrendMentionRate ensures that no value is present for TrendMentionRate, not even an explicit nil
### GetSerpRate

`func (o *KeywordListingResource) GetSerpRate() int32`

GetSerpRate returns the SerpRate field if non-nil, zero value otherwise.

### GetSerpRateOk

`func (o *KeywordListingResource) GetSerpRateOk() (*int32, bool)`

GetSerpRateOk returns a tuple with the SerpRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSerpRate

`func (o *KeywordListingResource) SetSerpRate(v int32)`

SetSerpRate sets SerpRate field to given value.

### HasSerpRate

`func (o *KeywordListingResource) HasSerpRate() bool`

HasSerpRate returns a boolean if a field has been set.

### SetSerpRateNil

`func (o *KeywordListingResource) SetSerpRateNil(b bool)`

 SetSerpRateNil sets the value for SerpRate to be an explicit nil

### UnsetSerpRate
`func (o *KeywordListingResource) UnsetSerpRate()`

UnsetSerpRate ensures that no value is present for SerpRate, not even an explicit nil
### GetTrendSerpRate

`func (o *KeywordListingResource) GetTrendSerpRate() int32`

GetTrendSerpRate returns the TrendSerpRate field if non-nil, zero value otherwise.

### GetTrendSerpRateOk

`func (o *KeywordListingResource) GetTrendSerpRateOk() (*int32, bool)`

GetTrendSerpRateOk returns a tuple with the TrendSerpRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendSerpRate

`func (o *KeywordListingResource) SetTrendSerpRate(v int32)`

SetTrendSerpRate sets TrendSerpRate field to given value.

### HasTrendSerpRate

`func (o *KeywordListingResource) HasTrendSerpRate() bool`

HasTrendSerpRate returns a boolean if a field has been set.

### SetTrendSerpRateNil

`func (o *KeywordListingResource) SetTrendSerpRateNil(b bool)`

 SetTrendSerpRateNil sets the value for TrendSerpRate to be an explicit nil

### UnsetTrendSerpRate
`func (o *KeywordListingResource) UnsetTrendSerpRate()`

UnsetTrendSerpRate ensures that no value is present for TrendSerpRate, not even an explicit nil
### GetShareOfVoice

`func (o *KeywordListingResource) GetShareOfVoice() float32`

GetShareOfVoice returns the ShareOfVoice field if non-nil, zero value otherwise.

### GetShareOfVoiceOk

`func (o *KeywordListingResource) GetShareOfVoiceOk() (*float32, bool)`

GetShareOfVoiceOk returns a tuple with the ShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShareOfVoice

`func (o *KeywordListingResource) SetShareOfVoice(v float32)`

SetShareOfVoice sets ShareOfVoice field to given value.

### HasShareOfVoice

`func (o *KeywordListingResource) HasShareOfVoice() bool`

HasShareOfVoice returns a boolean if a field has been set.

### SetShareOfVoiceNil

`func (o *KeywordListingResource) SetShareOfVoiceNil(b bool)`

 SetShareOfVoiceNil sets the value for ShareOfVoice to be an explicit nil

### UnsetShareOfVoice
`func (o *KeywordListingResource) UnsetShareOfVoice()`

UnsetShareOfVoice ensures that no value is present for ShareOfVoice, not even an explicit nil
### GetTrendShareOfVoice

`func (o *KeywordListingResource) GetTrendShareOfVoice() float32`

GetTrendShareOfVoice returns the TrendShareOfVoice field if non-nil, zero value otherwise.

### GetTrendShareOfVoiceOk

`func (o *KeywordListingResource) GetTrendShareOfVoiceOk() (*float32, bool)`

GetTrendShareOfVoiceOk returns a tuple with the TrendShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrendShareOfVoice

`func (o *KeywordListingResource) SetTrendShareOfVoice(v float32)`

SetTrendShareOfVoice sets TrendShareOfVoice field to given value.

### HasTrendShareOfVoice

`func (o *KeywordListingResource) HasTrendShareOfVoice() bool`

HasTrendShareOfVoice returns a boolean if a field has been set.

### SetTrendShareOfVoiceNil

`func (o *KeywordListingResource) SetTrendShareOfVoiceNil(b bool)`

 SetTrendShareOfVoiceNil sets the value for TrendShareOfVoice to be an explicit nil

### UnsetTrendShareOfVoice
`func (o *KeywordListingResource) UnsetTrendShareOfVoice()`

UnsetTrendShareOfVoice ensures that no value is present for TrendShareOfVoice, not even an explicit nil
### GetSentimentPositive

`func (o *KeywordListingResource) GetSentimentPositive() int32`

GetSentimentPositive returns the SentimentPositive field if non-nil, zero value otherwise.

### GetSentimentPositiveOk

`func (o *KeywordListingResource) GetSentimentPositiveOk() (*int32, bool)`

GetSentimentPositiveOk returns a tuple with the SentimentPositive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentPositive

`func (o *KeywordListingResource) SetSentimentPositive(v int32)`

SetSentimentPositive sets SentimentPositive field to given value.


### GetSentimentNeutral

`func (o *KeywordListingResource) GetSentimentNeutral() int32`

GetSentimentNeutral returns the SentimentNeutral field if non-nil, zero value otherwise.

### GetSentimentNeutralOk

`func (o *KeywordListingResource) GetSentimentNeutralOk() (*int32, bool)`

GetSentimentNeutralOk returns a tuple with the SentimentNeutral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentNeutral

`func (o *KeywordListingResource) SetSentimentNeutral(v int32)`

SetSentimentNeutral sets SentimentNeutral field to given value.


### GetSentimentNegative

`func (o *KeywordListingResource) GetSentimentNegative() int32`

GetSentimentNegative returns the SentimentNegative field if non-nil, zero value otherwise.

### GetSentimentNegativeOk

`func (o *KeywordListingResource) GetSentimentNegativeOk() (*int32, bool)`

GetSentimentNegativeOk returns a tuple with the SentimentNegative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentimentNegative

`func (o *KeywordListingResource) SetSentimentNegative(v int32)`

SetSentimentNegative sets SentimentNegative field to given value.


### GetAvgMentionCount

`func (o *KeywordListingResource) GetAvgMentionCount() float32`

GetAvgMentionCount returns the AvgMentionCount field if non-nil, zero value otherwise.

### GetAvgMentionCountOk

`func (o *KeywordListingResource) GetAvgMentionCountOk() (*float32, bool)`

GetAvgMentionCountOk returns a tuple with the AvgMentionCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgMentionCount

`func (o *KeywordListingResource) SetAvgMentionCount(v float32)`

SetAvgMentionCount sets AvgMentionCount field to given value.

### HasAvgMentionCount

`func (o *KeywordListingResource) HasAvgMentionCount() bool`

HasAvgMentionCount returns a boolean if a field has been set.

### SetAvgMentionCountNil

`func (o *KeywordListingResource) SetAvgMentionCountNil(b bool)`

 SetAvgMentionCountNil sets the value for AvgMentionCount to be an explicit nil

### UnsetAvgMentionCount
`func (o *KeywordListingResource) UnsetAvgMentionCount()`

UnsetAvgMentionCount ensures that no value is present for AvgMentionCount, not even an explicit nil
### GetMentionTypeCounts

`func (o *KeywordListingResource) GetMentionTypeCounts() KeywordListingResourceMentionTypeCounts`

GetMentionTypeCounts returns the MentionTypeCounts field if non-nil, zero value otherwise.

### GetMentionTypeCountsOk

`func (o *KeywordListingResource) GetMentionTypeCountsOk() (*KeywordListingResourceMentionTypeCounts, bool)`

GetMentionTypeCountsOk returns a tuple with the MentionTypeCounts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionTypeCounts

`func (o *KeywordListingResource) SetMentionTypeCounts(v KeywordListingResourceMentionTypeCounts)`

SetMentionTypeCounts sets MentionTypeCounts field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


