# AiResponseResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**ProjectId** | **string** | The project this capture belongs to | 
**TrackedQueryId** | **string** | The tracked query that was asked | 
**Engine** | **string** | The AI engine that answered | 
**ResponseText** | **string** | The full answer text as the engine produced it | 
**Citations** | [**[]CitationResource**](CitationResource.md) | Sources the engine cited, in the order it cited them | 
**CapturedAt** | **time.Time** | When the answer was captured, UTC | 
**ModelName** | Pointer to **NullableString** | Engine-reported model, when it reported one. Absent on captures taken before engines exposed it | [optional] 
**PassIndex** | **int32** | Which sampling pass of the run this answer is, starting at 0 | 
**PassCount** | **int32** | How many passes that run took. Rows of one run share trackedQueryId and capturedAt | 

## Methods

### NewAiResponseResource

`func NewAiResponseResource(id string, projectId string, trackedQueryId string, engine string, responseText string, citations []CitationResource, capturedAt time.Time, passIndex int32, passCount int32, ) *AiResponseResource`

NewAiResponseResource instantiates a new AiResponseResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAiResponseResourceWithDefaults

`func NewAiResponseResourceWithDefaults() *AiResponseResource`

NewAiResponseResourceWithDefaults instantiates a new AiResponseResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *AiResponseResource) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AiResponseResource) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AiResponseResource) SetId(v string)`

SetId sets Id field to given value.


### GetProjectId

`func (o *AiResponseResource) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *AiResponseResource) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *AiResponseResource) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.


### GetTrackedQueryId

`func (o *AiResponseResource) GetTrackedQueryId() string`

GetTrackedQueryId returns the TrackedQueryId field if non-nil, zero value otherwise.

### GetTrackedQueryIdOk

`func (o *AiResponseResource) GetTrackedQueryIdOk() (*string, bool)`

GetTrackedQueryIdOk returns a tuple with the TrackedQueryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryId

`func (o *AiResponseResource) SetTrackedQueryId(v string)`

SetTrackedQueryId sets TrackedQueryId field to given value.


### GetEngine

`func (o *AiResponseResource) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *AiResponseResource) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *AiResponseResource) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetResponseText

`func (o *AiResponseResource) GetResponseText() string`

GetResponseText returns the ResponseText field if non-nil, zero value otherwise.

### GetResponseTextOk

`func (o *AiResponseResource) GetResponseTextOk() (*string, bool)`

GetResponseTextOk returns a tuple with the ResponseText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseText

`func (o *AiResponseResource) SetResponseText(v string)`

SetResponseText sets ResponseText field to given value.


### GetCitations

`func (o *AiResponseResource) GetCitations() []CitationResource`

GetCitations returns the Citations field if non-nil, zero value otherwise.

### GetCitationsOk

`func (o *AiResponseResource) GetCitationsOk() (*[]CitationResource, bool)`

GetCitationsOk returns a tuple with the Citations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCitations

`func (o *AiResponseResource) SetCitations(v []CitationResource)`

SetCitations sets Citations field to given value.


### GetCapturedAt

`func (o *AiResponseResource) GetCapturedAt() time.Time`

GetCapturedAt returns the CapturedAt field if non-nil, zero value otherwise.

### GetCapturedAtOk

`func (o *AiResponseResource) GetCapturedAtOk() (*time.Time, bool)`

GetCapturedAtOk returns a tuple with the CapturedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCapturedAt

`func (o *AiResponseResource) SetCapturedAt(v time.Time)`

SetCapturedAt sets CapturedAt field to given value.


### GetModelName

`func (o *AiResponseResource) GetModelName() string`

GetModelName returns the ModelName field if non-nil, zero value otherwise.

### GetModelNameOk

`func (o *AiResponseResource) GetModelNameOk() (*string, bool)`

GetModelNameOk returns a tuple with the ModelName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelName

`func (o *AiResponseResource) SetModelName(v string)`

SetModelName sets ModelName field to given value.

### HasModelName

`func (o *AiResponseResource) HasModelName() bool`

HasModelName returns a boolean if a field has been set.

### SetModelNameNil

`func (o *AiResponseResource) SetModelNameNil(b bool)`

 SetModelNameNil sets the value for ModelName to be an explicit nil

### UnsetModelName
`func (o *AiResponseResource) UnsetModelName()`

UnsetModelName ensures that no value is present for ModelName, not even an explicit nil
### GetPassIndex

`func (o *AiResponseResource) GetPassIndex() int32`

GetPassIndex returns the PassIndex field if non-nil, zero value otherwise.

### GetPassIndexOk

`func (o *AiResponseResource) GetPassIndexOk() (*int32, bool)`

GetPassIndexOk returns a tuple with the PassIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPassIndex

`func (o *AiResponseResource) SetPassIndex(v int32)`

SetPassIndex sets PassIndex field to given value.


### GetPassCount

`func (o *AiResponseResource) GetPassCount() int32`

GetPassCount returns the PassCount field if non-nil, zero value otherwise.

### GetPassCountOk

`func (o *AiResponseResource) GetPassCountOk() (*int32, bool)`

GetPassCountOk returns a tuple with the PassCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPassCount

`func (o *AiResponseResource) SetPassCount(v int32)`

SetPassCount sets PassCount field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


