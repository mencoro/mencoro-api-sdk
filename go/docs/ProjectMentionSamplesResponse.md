# ProjectMentionSamplesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Samples** | [**[]MentionSampleResponse**](MentionSampleResponse.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewProjectMentionSamplesResponse

`func NewProjectMentionSamplesResponse(samples []MentionSampleResponse, total int32, ) *ProjectMentionSamplesResponse`

NewProjectMentionSamplesResponse instantiates a new ProjectMentionSamplesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectMentionSamplesResponseWithDefaults

`func NewProjectMentionSamplesResponseWithDefaults() *ProjectMentionSamplesResponse`

NewProjectMentionSamplesResponseWithDefaults instantiates a new ProjectMentionSamplesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSamples

`func (o *ProjectMentionSamplesResponse) GetSamples() []MentionSampleResponse`

GetSamples returns the Samples field if non-nil, zero value otherwise.

### GetSamplesOk

`func (o *ProjectMentionSamplesResponse) GetSamplesOk() (*[]MentionSampleResponse, bool)`

GetSamplesOk returns a tuple with the Samples field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSamples

`func (o *ProjectMentionSamplesResponse) SetSamples(v []MentionSampleResponse)`

SetSamples sets Samples field to given value.


### GetTotal

`func (o *ProjectMentionSamplesResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ProjectMentionSamplesResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ProjectMentionSamplesResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


