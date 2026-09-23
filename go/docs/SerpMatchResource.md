# SerpMatchResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackedQueryId** | **string** |  | 
**ProjectId** | **string** |  | 
**Engine** | **string** |  | 
**SearchPageId** | **string** |  | 
**CompetitorId** | Pointer to **NullableString** |  | [optional] 
**Position** | **int32** |  | 
**DetectedAt** | **time.Time** |  | 

## Methods

### NewSerpMatchResource

`func NewSerpMatchResource(trackedQueryId string, projectId string, engine string, searchPageId string, position int32, detectedAt time.Time, ) *SerpMatchResource`

NewSerpMatchResource instantiates a new SerpMatchResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSerpMatchResourceWithDefaults

`func NewSerpMatchResourceWithDefaults() *SerpMatchResource`

NewSerpMatchResourceWithDefaults instantiates a new SerpMatchResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTrackedQueryId

`func (o *SerpMatchResource) GetTrackedQueryId() string`

GetTrackedQueryId returns the TrackedQueryId field if non-nil, zero value otherwise.

### GetTrackedQueryIdOk

`func (o *SerpMatchResource) GetTrackedQueryIdOk() (*string, bool)`

GetTrackedQueryIdOk returns a tuple with the TrackedQueryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryId

`func (o *SerpMatchResource) SetTrackedQueryId(v string)`

SetTrackedQueryId sets TrackedQueryId field to given value.


### GetProjectId

`func (o *SerpMatchResource) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *SerpMatchResource) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *SerpMatchResource) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.


### GetEngine

`func (o *SerpMatchResource) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *SerpMatchResource) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *SerpMatchResource) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetSearchPageId

`func (o *SerpMatchResource) GetSearchPageId() string`

GetSearchPageId returns the SearchPageId field if non-nil, zero value otherwise.

### GetSearchPageIdOk

`func (o *SerpMatchResource) GetSearchPageIdOk() (*string, bool)`

GetSearchPageIdOk returns a tuple with the SearchPageId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSearchPageId

`func (o *SerpMatchResource) SetSearchPageId(v string)`

SetSearchPageId sets SearchPageId field to given value.


### GetCompetitorId

`func (o *SerpMatchResource) GetCompetitorId() string`

GetCompetitorId returns the CompetitorId field if non-nil, zero value otherwise.

### GetCompetitorIdOk

`func (o *SerpMatchResource) GetCompetitorIdOk() (*string, bool)`

GetCompetitorIdOk returns a tuple with the CompetitorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitorId

`func (o *SerpMatchResource) SetCompetitorId(v string)`

SetCompetitorId sets CompetitorId field to given value.

### HasCompetitorId

`func (o *SerpMatchResource) HasCompetitorId() bool`

HasCompetitorId returns a boolean if a field has been set.

### SetCompetitorIdNil

`func (o *SerpMatchResource) SetCompetitorIdNil(b bool)`

 SetCompetitorIdNil sets the value for CompetitorId to be an explicit nil

### UnsetCompetitorId
`func (o *SerpMatchResource) UnsetCompetitorId()`

UnsetCompetitorId ensures that no value is present for CompetitorId, not even an explicit nil
### GetPosition

`func (o *SerpMatchResource) GetPosition() int32`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *SerpMatchResource) GetPositionOk() (*int32, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *SerpMatchResource) SetPosition(v int32)`

SetPosition sets Position field to given value.


### GetDetectedAt

`func (o *SerpMatchResource) GetDetectedAt() time.Time`

GetDetectedAt returns the DetectedAt field if non-nil, zero value otherwise.

### GetDetectedAtOk

`func (o *SerpMatchResource) GetDetectedAtOk() (*time.Time, bool)`

GetDetectedAtOk returns a tuple with the DetectedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetectedAt

`func (o *SerpMatchResource) SetDetectedAt(v time.Time)`

SetDetectedAt sets DetectedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


