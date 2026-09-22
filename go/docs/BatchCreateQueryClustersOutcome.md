# BatchCreateQueryClustersOutcome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | Pointer to [**[]BatchCreateQueryClustersOutcomeSuccessfulInner**](BatchCreateQueryClustersOutcomeSuccessfulInner.md) | Clusters created by this call. | [optional] 
**Failed** | Pointer to [**[]BatchCreateQueryClustersOutcomeFailedInner**](BatchCreateQueryClustersOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 

## Methods

### NewBatchCreateQueryClustersOutcome

`func NewBatchCreateQueryClustersOutcome() *BatchCreateQueryClustersOutcome`

NewBatchCreateQueryClustersOutcome instantiates a new BatchCreateQueryClustersOutcome object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchCreateQueryClustersOutcomeWithDefaults

`func NewBatchCreateQueryClustersOutcomeWithDefaults() *BatchCreateQueryClustersOutcome`

NewBatchCreateQueryClustersOutcomeWithDefaults instantiates a new BatchCreateQueryClustersOutcome object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSuccessful

`func (o *BatchCreateQueryClustersOutcome) GetSuccessful() []BatchCreateQueryClustersOutcomeSuccessfulInner`

GetSuccessful returns the Successful field if non-nil, zero value otherwise.

### GetSuccessfulOk

`func (o *BatchCreateQueryClustersOutcome) GetSuccessfulOk() (*[]BatchCreateQueryClustersOutcomeSuccessfulInner, bool)`

GetSuccessfulOk returns a tuple with the Successful field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccessful

`func (o *BatchCreateQueryClustersOutcome) SetSuccessful(v []BatchCreateQueryClustersOutcomeSuccessfulInner)`

SetSuccessful sets Successful field to given value.

### HasSuccessful

`func (o *BatchCreateQueryClustersOutcome) HasSuccessful() bool`

HasSuccessful returns a boolean if a field has been set.

### GetFailed

`func (o *BatchCreateQueryClustersOutcome) GetFailed() []BatchCreateQueryClustersOutcomeFailedInner`

GetFailed returns the Failed field if non-nil, zero value otherwise.

### GetFailedOk

`func (o *BatchCreateQueryClustersOutcome) GetFailedOk() (*[]BatchCreateQueryClustersOutcomeFailedInner, bool)`

GetFailedOk returns a tuple with the Failed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailed

`func (o *BatchCreateQueryClustersOutcome) SetFailed(v []BatchCreateQueryClustersOutcomeFailedInner)`

SetFailed sets Failed field to given value.

### HasFailed

`func (o *BatchCreateQueryClustersOutcome) HasFailed() bool`

HasFailed returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


