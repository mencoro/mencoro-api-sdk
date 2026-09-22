# AiResponseReportResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AiResponseId** | **string** | The captured AI answer the report is about | 
**TrackedQueryId** | **string** | The tracked query that answer was captured for | 
**Type** | **string** | The kind of problem reported | 
**Comment** | Pointer to **NullableString** | The note as stored. An empty or whitespace-only comment is stored as null. | [optional] 
**MissedBrandNames** | **[]string** | Brand names reported as missed, de-duplicated and trimmed. | 
**Accepted** | **bool** | True once the report has been accepted for review. It is never false: a report that could not be delivered answers with an error instead. | 

## Methods

### NewAiResponseReportResource

`func NewAiResponseReportResource(aiResponseId string, trackedQueryId string, type_ string, missedBrandNames []string, accepted bool, ) *AiResponseReportResource`

NewAiResponseReportResource instantiates a new AiResponseReportResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAiResponseReportResourceWithDefaults

`func NewAiResponseReportResourceWithDefaults() *AiResponseReportResource`

NewAiResponseReportResourceWithDefaults instantiates a new AiResponseReportResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAiResponseId

`func (o *AiResponseReportResource) GetAiResponseId() string`

GetAiResponseId returns the AiResponseId field if non-nil, zero value otherwise.

### GetAiResponseIdOk

`func (o *AiResponseReportResource) GetAiResponseIdOk() (*string, bool)`

GetAiResponseIdOk returns a tuple with the AiResponseId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAiResponseId

`func (o *AiResponseReportResource) SetAiResponseId(v string)`

SetAiResponseId sets AiResponseId field to given value.


### GetTrackedQueryId

`func (o *AiResponseReportResource) GetTrackedQueryId() string`

GetTrackedQueryId returns the TrackedQueryId field if non-nil, zero value otherwise.

### GetTrackedQueryIdOk

`func (o *AiResponseReportResource) GetTrackedQueryIdOk() (*string, bool)`

GetTrackedQueryIdOk returns a tuple with the TrackedQueryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryId

`func (o *AiResponseReportResource) SetTrackedQueryId(v string)`

SetTrackedQueryId sets TrackedQueryId field to given value.


### GetType

`func (o *AiResponseReportResource) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AiResponseReportResource) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AiResponseReportResource) SetType(v string)`

SetType sets Type field to given value.


### GetComment

`func (o *AiResponseReportResource) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *AiResponseReportResource) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *AiResponseReportResource) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *AiResponseReportResource) HasComment() bool`

HasComment returns a boolean if a field has been set.

### SetCommentNil

`func (o *AiResponseReportResource) SetCommentNil(b bool)`

 SetCommentNil sets the value for Comment to be an explicit nil

### UnsetComment
`func (o *AiResponseReportResource) UnsetComment()`

UnsetComment ensures that no value is present for Comment, not even an explicit nil
### GetMissedBrandNames

`func (o *AiResponseReportResource) GetMissedBrandNames() []string`

GetMissedBrandNames returns the MissedBrandNames field if non-nil, zero value otherwise.

### GetMissedBrandNamesOk

`func (o *AiResponseReportResource) GetMissedBrandNamesOk() (*[]string, bool)`

GetMissedBrandNamesOk returns a tuple with the MissedBrandNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMissedBrandNames

`func (o *AiResponseReportResource) SetMissedBrandNames(v []string)`

SetMissedBrandNames sets MissedBrandNames field to given value.


### GetAccepted

`func (o *AiResponseReportResource) GetAccepted() bool`

GetAccepted returns the Accepted field if non-nil, zero value otherwise.

### GetAcceptedOk

`func (o *AiResponseReportResource) GetAcceptedOk() (*bool, bool)`

GetAcceptedOk returns a tuple with the Accepted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccepted

`func (o *AiResponseReportResource) SetAccepted(v bool)`

SetAccepted sets Accepted field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


