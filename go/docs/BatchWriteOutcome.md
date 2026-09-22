# BatchWriteOutcome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | Pointer to [**[]BatchPauseTrackedQueries200ResponseSuccessfulInner**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | The resources the operation was applied to. | [optional] 
**Failed** | Pointer to [**[]BatchWriteOutcomeFailedInner**](BatchWriteOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 

## Methods

### NewBatchWriteOutcome

`func NewBatchWriteOutcome() *BatchWriteOutcome`

NewBatchWriteOutcome instantiates a new BatchWriteOutcome object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchWriteOutcomeWithDefaults

`func NewBatchWriteOutcomeWithDefaults() *BatchWriteOutcome`

NewBatchWriteOutcomeWithDefaults instantiates a new BatchWriteOutcome object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSuccessful

`func (o *BatchWriteOutcome) GetSuccessful() []BatchPauseTrackedQueries200ResponseSuccessfulInner`

GetSuccessful returns the Successful field if non-nil, zero value otherwise.

### GetSuccessfulOk

`func (o *BatchWriteOutcome) GetSuccessfulOk() (*[]BatchPauseTrackedQueries200ResponseSuccessfulInner, bool)`

GetSuccessfulOk returns a tuple with the Successful field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccessful

`func (o *BatchWriteOutcome) SetSuccessful(v []BatchPauseTrackedQueries200ResponseSuccessfulInner)`

SetSuccessful sets Successful field to given value.

### HasSuccessful

`func (o *BatchWriteOutcome) HasSuccessful() bool`

HasSuccessful returns a boolean if a field has been set.

### GetFailed

`func (o *BatchWriteOutcome) GetFailed() []BatchWriteOutcomeFailedInner`

GetFailed returns the Failed field if non-nil, zero value otherwise.

### GetFailedOk

`func (o *BatchWriteOutcome) GetFailedOk() (*[]BatchWriteOutcomeFailedInner, bool)`

GetFailedOk returns a tuple with the Failed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailed

`func (o *BatchWriteOutcome) SetFailed(v []BatchWriteOutcomeFailedInner)`

SetFailed sets Failed field to given value.

### HasFailed

`func (o *BatchWriteOutcome) HasFailed() bool`

HasFailed returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


