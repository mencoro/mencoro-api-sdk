# ReportAiResponseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | What is wrong with the capture. | 
**Comment** | Pointer to **NullableString** | Optional note for the reviewer, at most 1000 characters. An empty string is stored as no comment. | [optional] 
**MissedBrandNames** | Pointer to **[]string** | Brands the engine mentioned that the pipeline did not record. Most useful with type \&quot;missed_mention\&quot;; accepted with either. At most 50 distinct names of 255 characters each. | [optional] 

## Methods

### NewReportAiResponseRequest

`func NewReportAiResponseRequest(type_ string, ) *ReportAiResponseRequest`

NewReportAiResponseRequest instantiates a new ReportAiResponseRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewReportAiResponseRequestWithDefaults

`func NewReportAiResponseRequestWithDefaults() *ReportAiResponseRequest`

NewReportAiResponseRequestWithDefaults instantiates a new ReportAiResponseRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *ReportAiResponseRequest) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ReportAiResponseRequest) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ReportAiResponseRequest) SetType(v string)`

SetType sets Type field to given value.


### GetComment

`func (o *ReportAiResponseRequest) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *ReportAiResponseRequest) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *ReportAiResponseRequest) SetComment(v string)`

SetComment sets Comment field to given value.

### HasComment

`func (o *ReportAiResponseRequest) HasComment() bool`

HasComment returns a boolean if a field has been set.

### SetCommentNil

`func (o *ReportAiResponseRequest) SetCommentNil(b bool)`

 SetCommentNil sets the value for Comment to be an explicit nil

### UnsetComment
`func (o *ReportAiResponseRequest) UnsetComment()`

UnsetComment ensures that no value is present for Comment, not even an explicit nil
### GetMissedBrandNames

`func (o *ReportAiResponseRequest) GetMissedBrandNames() []string`

GetMissedBrandNames returns the MissedBrandNames field if non-nil, zero value otherwise.

### GetMissedBrandNamesOk

`func (o *ReportAiResponseRequest) GetMissedBrandNamesOk() (*[]string, bool)`

GetMissedBrandNamesOk returns a tuple with the MissedBrandNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMissedBrandNames

`func (o *ReportAiResponseRequest) SetMissedBrandNames(v []string)`

SetMissedBrandNames sets MissedBrandNames field to given value.

### HasMissedBrandNames

`func (o *ReportAiResponseRequest) HasMissedBrandNames() bool`

HasMissedBrandNames returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


