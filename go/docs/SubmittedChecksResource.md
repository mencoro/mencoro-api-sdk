# SubmittedChecksResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Submitted** | **int32** | How many tracked queries were submitted. Zero is a valid answer: it means nothing in the project was eligible. | 
**TrackedQueryIds** | **[]string** | The tracked queries submitted, in the order they were submitted (least recently checked first). Poll these to follow progress. | 

## Methods

### NewSubmittedChecksResource

`func NewSubmittedChecksResource(submitted int32, trackedQueryIds []string, ) *SubmittedChecksResource`

NewSubmittedChecksResource instantiates a new SubmittedChecksResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubmittedChecksResourceWithDefaults

`func NewSubmittedChecksResourceWithDefaults() *SubmittedChecksResource`

NewSubmittedChecksResourceWithDefaults instantiates a new SubmittedChecksResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSubmitted

`func (o *SubmittedChecksResource) GetSubmitted() int32`

GetSubmitted returns the Submitted field if non-nil, zero value otherwise.

### GetSubmittedOk

`func (o *SubmittedChecksResource) GetSubmittedOk() (*int32, bool)`

GetSubmittedOk returns a tuple with the Submitted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubmitted

`func (o *SubmittedChecksResource) SetSubmitted(v int32)`

SetSubmitted sets Submitted field to given value.


### GetTrackedQueryIds

`func (o *SubmittedChecksResource) GetTrackedQueryIds() []string`

GetTrackedQueryIds returns the TrackedQueryIds field if non-nil, zero value otherwise.

### GetTrackedQueryIdsOk

`func (o *SubmittedChecksResource) GetTrackedQueryIdsOk() (*[]string, bool)`

GetTrackedQueryIdsOk returns a tuple with the TrackedQueryIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryIds

`func (o *SubmittedChecksResource) SetTrackedQueryIds(v []string)`

SetTrackedQueryIds sets TrackedQueryIds field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


