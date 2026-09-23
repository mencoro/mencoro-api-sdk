# MentionMatchResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackedQueryId** | **string** |  | 
**ProjectId** | **string** |  | 
**Engine** | **string** |  | 
**AiResponseId** | **string** |  | 
**CompetitorId** | Pointer to **NullableString** |  | [optional] 
**MentionPosition** | **int32** |  | 
**Sentiment** | **string** |  | 
**MentionType** | **string** |  | 
**MentionTypeCondition** | Pointer to **NullableString** |  | [optional] 
**ResponseContext** | **string** |  | 
**DetectedAt** | **time.Time** |  | 
**MentionRelation** | Pointer to **NullableString** |  | [optional] 
**BrandName** | Pointer to **NullableString** |  | [optional] 
**BrandNameAsMentioned** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewMentionMatchResource

`func NewMentionMatchResource(trackedQueryId string, projectId string, engine string, aiResponseId string, mentionPosition int32, sentiment string, mentionType string, responseContext string, detectedAt time.Time, ) *MentionMatchResource`

NewMentionMatchResource instantiates a new MentionMatchResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMentionMatchResourceWithDefaults

`func NewMentionMatchResourceWithDefaults() *MentionMatchResource`

NewMentionMatchResourceWithDefaults instantiates a new MentionMatchResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTrackedQueryId

`func (o *MentionMatchResource) GetTrackedQueryId() string`

GetTrackedQueryId returns the TrackedQueryId field if non-nil, zero value otherwise.

### GetTrackedQueryIdOk

`func (o *MentionMatchResource) GetTrackedQueryIdOk() (*string, bool)`

GetTrackedQueryIdOk returns a tuple with the TrackedQueryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryId

`func (o *MentionMatchResource) SetTrackedQueryId(v string)`

SetTrackedQueryId sets TrackedQueryId field to given value.


### GetProjectId

`func (o *MentionMatchResource) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *MentionMatchResource) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *MentionMatchResource) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.


### GetEngine

`func (o *MentionMatchResource) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *MentionMatchResource) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *MentionMatchResource) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetAiResponseId

`func (o *MentionMatchResource) GetAiResponseId() string`

GetAiResponseId returns the AiResponseId field if non-nil, zero value otherwise.

### GetAiResponseIdOk

`func (o *MentionMatchResource) GetAiResponseIdOk() (*string, bool)`

GetAiResponseIdOk returns a tuple with the AiResponseId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAiResponseId

`func (o *MentionMatchResource) SetAiResponseId(v string)`

SetAiResponseId sets AiResponseId field to given value.


### GetCompetitorId

`func (o *MentionMatchResource) GetCompetitorId() string`

GetCompetitorId returns the CompetitorId field if non-nil, zero value otherwise.

### GetCompetitorIdOk

`func (o *MentionMatchResource) GetCompetitorIdOk() (*string, bool)`

GetCompetitorIdOk returns a tuple with the CompetitorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitorId

`func (o *MentionMatchResource) SetCompetitorId(v string)`

SetCompetitorId sets CompetitorId field to given value.

### HasCompetitorId

`func (o *MentionMatchResource) HasCompetitorId() bool`

HasCompetitorId returns a boolean if a field has been set.

### SetCompetitorIdNil

`func (o *MentionMatchResource) SetCompetitorIdNil(b bool)`

 SetCompetitorIdNil sets the value for CompetitorId to be an explicit nil

### UnsetCompetitorId
`func (o *MentionMatchResource) UnsetCompetitorId()`

UnsetCompetitorId ensures that no value is present for CompetitorId, not even an explicit nil
### GetMentionPosition

`func (o *MentionMatchResource) GetMentionPosition() int32`

GetMentionPosition returns the MentionPosition field if non-nil, zero value otherwise.

### GetMentionPositionOk

`func (o *MentionMatchResource) GetMentionPositionOk() (*int32, bool)`

GetMentionPositionOk returns a tuple with the MentionPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionPosition

`func (o *MentionMatchResource) SetMentionPosition(v int32)`

SetMentionPosition sets MentionPosition field to given value.


### GetSentiment

`func (o *MentionMatchResource) GetSentiment() string`

GetSentiment returns the Sentiment field if non-nil, zero value otherwise.

### GetSentimentOk

`func (o *MentionMatchResource) GetSentimentOk() (*string, bool)`

GetSentimentOk returns a tuple with the Sentiment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentiment

`func (o *MentionMatchResource) SetSentiment(v string)`

SetSentiment sets Sentiment field to given value.


### GetMentionType

`func (o *MentionMatchResource) GetMentionType() string`

GetMentionType returns the MentionType field if non-nil, zero value otherwise.

### GetMentionTypeOk

`func (o *MentionMatchResource) GetMentionTypeOk() (*string, bool)`

GetMentionTypeOk returns a tuple with the MentionType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionType

`func (o *MentionMatchResource) SetMentionType(v string)`

SetMentionType sets MentionType field to given value.


### GetMentionTypeCondition

`func (o *MentionMatchResource) GetMentionTypeCondition() string`

GetMentionTypeCondition returns the MentionTypeCondition field if non-nil, zero value otherwise.

### GetMentionTypeConditionOk

`func (o *MentionMatchResource) GetMentionTypeConditionOk() (*string, bool)`

GetMentionTypeConditionOk returns a tuple with the MentionTypeCondition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionTypeCondition

`func (o *MentionMatchResource) SetMentionTypeCondition(v string)`

SetMentionTypeCondition sets MentionTypeCondition field to given value.

### HasMentionTypeCondition

`func (o *MentionMatchResource) HasMentionTypeCondition() bool`

HasMentionTypeCondition returns a boolean if a field has been set.

### SetMentionTypeConditionNil

`func (o *MentionMatchResource) SetMentionTypeConditionNil(b bool)`

 SetMentionTypeConditionNil sets the value for MentionTypeCondition to be an explicit nil

### UnsetMentionTypeCondition
`func (o *MentionMatchResource) UnsetMentionTypeCondition()`

UnsetMentionTypeCondition ensures that no value is present for MentionTypeCondition, not even an explicit nil
### GetResponseContext

`func (o *MentionMatchResource) GetResponseContext() string`

GetResponseContext returns the ResponseContext field if non-nil, zero value otherwise.

### GetResponseContextOk

`func (o *MentionMatchResource) GetResponseContextOk() (*string, bool)`

GetResponseContextOk returns a tuple with the ResponseContext field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseContext

`func (o *MentionMatchResource) SetResponseContext(v string)`

SetResponseContext sets ResponseContext field to given value.


### GetDetectedAt

`func (o *MentionMatchResource) GetDetectedAt() time.Time`

GetDetectedAt returns the DetectedAt field if non-nil, zero value otherwise.

### GetDetectedAtOk

`func (o *MentionMatchResource) GetDetectedAtOk() (*time.Time, bool)`

GetDetectedAtOk returns a tuple with the DetectedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetectedAt

`func (o *MentionMatchResource) SetDetectedAt(v time.Time)`

SetDetectedAt sets DetectedAt field to given value.


### GetMentionRelation

`func (o *MentionMatchResource) GetMentionRelation() string`

GetMentionRelation returns the MentionRelation field if non-nil, zero value otherwise.

### GetMentionRelationOk

`func (o *MentionMatchResource) GetMentionRelationOk() (*string, bool)`

GetMentionRelationOk returns a tuple with the MentionRelation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMentionRelation

`func (o *MentionMatchResource) SetMentionRelation(v string)`

SetMentionRelation sets MentionRelation field to given value.

### HasMentionRelation

`func (o *MentionMatchResource) HasMentionRelation() bool`

HasMentionRelation returns a boolean if a field has been set.

### SetMentionRelationNil

`func (o *MentionMatchResource) SetMentionRelationNil(b bool)`

 SetMentionRelationNil sets the value for MentionRelation to be an explicit nil

### UnsetMentionRelation
`func (o *MentionMatchResource) UnsetMentionRelation()`

UnsetMentionRelation ensures that no value is present for MentionRelation, not even an explicit nil
### GetBrandName

`func (o *MentionMatchResource) GetBrandName() string`

GetBrandName returns the BrandName field if non-nil, zero value otherwise.

### GetBrandNameOk

`func (o *MentionMatchResource) GetBrandNameOk() (*string, bool)`

GetBrandNameOk returns a tuple with the BrandName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrandName

`func (o *MentionMatchResource) SetBrandName(v string)`

SetBrandName sets BrandName field to given value.

### HasBrandName

`func (o *MentionMatchResource) HasBrandName() bool`

HasBrandName returns a boolean if a field has been set.

### SetBrandNameNil

`func (o *MentionMatchResource) SetBrandNameNil(b bool)`

 SetBrandNameNil sets the value for BrandName to be an explicit nil

### UnsetBrandName
`func (o *MentionMatchResource) UnsetBrandName()`

UnsetBrandName ensures that no value is present for BrandName, not even an explicit nil
### GetBrandNameAsMentioned

`func (o *MentionMatchResource) GetBrandNameAsMentioned() string`

GetBrandNameAsMentioned returns the BrandNameAsMentioned field if non-nil, zero value otherwise.

### GetBrandNameAsMentionedOk

`func (o *MentionMatchResource) GetBrandNameAsMentionedOk() (*string, bool)`

GetBrandNameAsMentionedOk returns a tuple with the BrandNameAsMentioned field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrandNameAsMentioned

`func (o *MentionMatchResource) SetBrandNameAsMentioned(v string)`

SetBrandNameAsMentioned sets BrandNameAsMentioned field to given value.

### HasBrandNameAsMentioned

`func (o *MentionMatchResource) HasBrandNameAsMentioned() bool`

HasBrandNameAsMentioned returns a boolean if a field has been set.

### SetBrandNameAsMentionedNil

`func (o *MentionMatchResource) SetBrandNameAsMentionedNil(b bool)`

 SetBrandNameAsMentionedNil sets the value for BrandNameAsMentioned to be an explicit nil

### UnsetBrandNameAsMentioned
`func (o *MentionMatchResource) UnsetBrandNameAsMentioned()`

UnsetBrandNameAsMentioned ensures that no value is present for BrandNameAsMentioned, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


