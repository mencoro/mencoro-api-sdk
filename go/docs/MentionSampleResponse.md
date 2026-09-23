# MentionSampleResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**TrackedQueryId** | **string** |  | 
**AiResponseId** | **string** |  | 
**Engine** | **string** |  | 
**CompetitorId** | Pointer to **NullableString** |  | [optional] 
**Sentiment** | **string** |  | 
**MentionType** | **string** |  | 
**MentionPosition** | **int32** |  | 
**Text** | **string** |  | 
**DetectedAt** | **string** |  | 
**QueryText** | **string** |  | 
**Country** | Pointer to **NullableString** |  | [optional] 
**MentionRelation** | Pointer to **NullableString** | Published because &#x60;competitorId&#x60; alone cannot answer the question. Own-brand AND untracked-competitor mentions both carry a null competitor id - the confusion migration Version20260608130000 was written to end - so a reader that treats a null competitor id as \&quot;us\&quot; silently counts a rival as the brand. | [optional] 
**BrandName** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewMentionSampleResponse

`func NewMentionSampleResponse(id string, trackedQueryId string, aiResponseId string, engine string, sentiment string, mentionType string, mentionPosition int32, text string, detectedAt string, queryText string, ) *MentionSampleResponse`

NewMentionSampleResponse instantiates a new MentionSampleResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMentionSampleResponseWithDefaults

`func NewMentionSampleResponseWithDefaults() *MentionSampleResponse`

NewMentionSampleResponseWithDefaults instantiates a new MentionSampleResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *MentionSampleResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *MentionSampleResponse) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *MentionSampleResponse) SetId(v string)`

SetId sets Id field to given value.


### GetTrackedQueryId

`func (o *MentionSampleResponse) GetTrackedQueryId() string`

GetTrackedQueryId returns the TrackedQueryId field if non-nil, zero value otherwise.

### GetTrackedQueryIdOk

`func (o *MentionSampleResponse) GetTrackedQueryIdOk() (*string, bool)`

GetTrackedQueryIdOk returns a tuple with the TrackedQueryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryId

`func (o *MentionSampleResponse) SetTrackedQueryId(v string)`

SetTrackedQueryId sets TrackedQueryId field to given value.


### GetAiResponseId

`func (o *MentionSampleResponse) GetAiResponseId() string`

GetAiResponseId returns the AiResponseId field if non-nil, zero value otherwise.

### GetAiResponseIdOk

`func (o *MentionSampleResponse) GetAiResponseIdOk() (*string, bool)`

GetAiResponseIdOk returns a tuple with the AiResponseId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAiResponseId

`func (o *MentionSampleResponse) SetAiResponseId(v string)`

SetAiResponseId sets AiResponseId field to given value.


### GetEngine

`func (o *MentionSampleResponse) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *MentionSampleResponse) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *MentionSampleResponse) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetCompetitorId

`func (o *MentionSampleResponse) GetCompetitorId() string`

GetCompetitorId returns the CompetitorId field if non-nil, zero value otherwise.

### GetCompetitorIdOk

`func (o *MentionSampleResponse) GetCompetitorIdOk() (*string, bool)`

GetCompetitorIdOk returns a tuple with the CompetitorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitorId

`func (o *MentionSampleResponse) SetCompetitorId(v string)`

SetCompetitorId sets CompetitorId field to given value.

### HasCompetitorId

`func (o *MentionSampleResponse) HasCompetitorId() bool`

HasCompetitorId returns a boolean if a field has been set.

### SetCompetitorIdNil

`func (o *MentionSampleResponse) SetCompetitorIdNil(b bool)`

 SetCompetitorIdNil sets the value for CompetitorId to be an explicit nil

### UnsetCompetitorId
`func (o *MentionSampleResponse) UnsetCompetitorId()`

UnsetCompetitorId ensures that no value is present for CompetitorId, not even an explicit nil
### GetSentiment

`func (o *MentionSampleResponse) GetSentiment() string`

GetSentiment returns the Sentiment field if non-nil, zero value otherwise.

### GetSentimentOk

`func (o *MentionSampleResponse) GetSentimentOk() (*string, bool)`

GetSentimentOk returns a tuple with the Sentiment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentiment

`func (o *MentionSampleResponse) SetSentiment(v string)`

SetSentiment sets Sentiment field to given value.


### GetMentionType

`func (o *MentionSampleResponse) GetMentionType() string`

GetMentionType returns the MentionType field if non-nil, zero value otherwise.

### GetMentionTypeOk

`func (o *MentionSampleResponse) GetMentionTypeOk() (*string, bool)`

GetMentionTypeOk returns a tuple with the MentionType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionType

`func (o *MentionSampleResponse) SetMentionType(v string)`

SetMentionType sets MentionType field to given value.


### GetMentionPosition

`func (o *MentionSampleResponse) GetMentionPosition() int32`

GetMentionPosition returns the MentionPosition field if non-nil, zero value otherwise.

### GetMentionPositionOk

`func (o *MentionSampleResponse) GetMentionPositionOk() (*int32, bool)`

GetMentionPositionOk returns a tuple with the MentionPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionPosition

`func (o *MentionSampleResponse) SetMentionPosition(v int32)`

SetMentionPosition sets MentionPosition field to given value.


### GetText

`func (o *MentionSampleResponse) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *MentionSampleResponse) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *MentionSampleResponse) SetText(v string)`

SetText sets Text field to given value.


### GetDetectedAt

`func (o *MentionSampleResponse) GetDetectedAt() string`

GetDetectedAt returns the DetectedAt field if non-nil, zero value otherwise.

### GetDetectedAtOk

`func (o *MentionSampleResponse) GetDetectedAtOk() (*string, bool)`

GetDetectedAtOk returns a tuple with the DetectedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetectedAt

`func (o *MentionSampleResponse) SetDetectedAt(v string)`

SetDetectedAt sets DetectedAt field to given value.


### GetQueryText

`func (o *MentionSampleResponse) GetQueryText() string`

GetQueryText returns the QueryText field if non-nil, zero value otherwise.

### GetQueryTextOk

`func (o *MentionSampleResponse) GetQueryTextOk() (*string, bool)`

GetQueryTextOk returns a tuple with the QueryText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryText

`func (o *MentionSampleResponse) SetQueryText(v string)`

SetQueryText sets QueryText field to given value.


### GetCountry

`func (o *MentionSampleResponse) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *MentionSampleResponse) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *MentionSampleResponse) SetCountry(v string)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *MentionSampleResponse) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### SetCountryNil

`func (o *MentionSampleResponse) SetCountryNil(b bool)`

 SetCountryNil sets the value for Country to be an explicit nil

### UnsetCountry
`func (o *MentionSampleResponse) UnsetCountry()`

UnsetCountry ensures that no value is present for Country, not even an explicit nil
### GetMentionRelation

`func (o *MentionSampleResponse) GetMentionRelation() string`

GetMentionRelation returns the MentionRelation field if non-nil, zero value otherwise.

### GetMentionRelationOk

`func (o *MentionSampleResponse) GetMentionRelationOk() (*string, bool)`

GetMentionRelationOk returns a tuple with the MentionRelation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionRelation

`func (o *MentionSampleResponse) SetMentionRelation(v string)`

SetMentionRelation sets MentionRelation field to given value.

### HasMentionRelation

`func (o *MentionSampleResponse) HasMentionRelation() bool`

HasMentionRelation returns a boolean if a field has been set.

### SetMentionRelationNil

`func (o *MentionSampleResponse) SetMentionRelationNil(b bool)`

 SetMentionRelationNil sets the value for MentionRelation to be an explicit nil

### UnsetMentionRelation
`func (o *MentionSampleResponse) UnsetMentionRelation()`

UnsetMentionRelation ensures that no value is present for MentionRelation, not even an explicit nil
### GetBrandName

`func (o *MentionSampleResponse) GetBrandName() string`

GetBrandName returns the BrandName field if non-nil, zero value otherwise.

### GetBrandNameOk

`func (o *MentionSampleResponse) GetBrandNameOk() (*string, bool)`

GetBrandNameOk returns a tuple with the BrandName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrandName

`func (o *MentionSampleResponse) SetBrandName(v string)`

SetBrandName sets BrandName field to given value.

### HasBrandName

`func (o *MentionSampleResponse) HasBrandName() bool`

HasBrandName returns a boolean if a field has been set.

### SetBrandNameNil

`func (o *MentionSampleResponse) SetBrandNameNil(b bool)`

 SetBrandNameNil sets the value for BrandName to be an explicit nil

### UnsetBrandName
`func (o *MentionSampleResponse) UnsetBrandName()`

UnsetBrandName ensures that no value is present for BrandName, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


