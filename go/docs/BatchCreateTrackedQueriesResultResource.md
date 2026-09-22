# BatchCreateTrackedQueriesResultResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | Pointer to [**[]BatchCreateTrackedQueriesResultResourceSuccessfulInner**](BatchCreateTrackedQueriesResultResourceSuccessfulInner.md) | Tracked queries created by this call, one entry per query text, engine and country combination. | [optional] 
**Failed** | Pointer to [**[]BatchCreateTrackedQueriesResultResourceFailedInner**](BatchCreateTrackedQueriesResultResourceFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 

## Methods

### NewBatchCreateTrackedQueriesResultResource

`func NewBatchCreateTrackedQueriesResultResource() *BatchCreateTrackedQueriesResultResource`

NewBatchCreateTrackedQueriesResultResource instantiates a new BatchCreateTrackedQueriesResultResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchCreateTrackedQueriesResultResourceWithDefaults

`func NewBatchCreateTrackedQueriesResultResourceWithDefaults() *BatchCreateTrackedQueriesResultResource`

NewBatchCreateTrackedQueriesResultResourceWithDefaults instantiates a new BatchCreateTrackedQueriesResultResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSuccessful

`func (o *BatchCreateTrackedQueriesResultResource) GetSuccessful() []BatchCreateTrackedQueriesResultResourceSuccessfulInner`

GetSuccessful returns the Successful field if non-nil, zero value otherwise.

### GetSuccessfulOk

`func (o *BatchCreateTrackedQueriesResultResource) GetSuccessfulOk() (*[]BatchCreateTrackedQueriesResultResourceSuccessfulInner, bool)`

GetSuccessfulOk returns a tuple with the Successful field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccessful

`func (o *BatchCreateTrackedQueriesResultResource) SetSuccessful(v []BatchCreateTrackedQueriesResultResourceSuccessfulInner)`

SetSuccessful sets Successful field to given value.

### HasSuccessful

`func (o *BatchCreateTrackedQueriesResultResource) HasSuccessful() bool`

HasSuccessful returns a boolean if a field has been set.

### GetFailed

`func (o *BatchCreateTrackedQueriesResultResource) GetFailed() []BatchCreateTrackedQueriesResultResourceFailedInner`

GetFailed returns the Failed field if non-nil, zero value otherwise.

### GetFailedOk

`func (o *BatchCreateTrackedQueriesResultResource) GetFailedOk() (*[]BatchCreateTrackedQueriesResultResourceFailedInner, bool)`

GetFailedOk returns a tuple with the Failed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailed

`func (o *BatchCreateTrackedQueriesResultResource) SetFailed(v []BatchCreateTrackedQueriesResultResourceFailedInner)`

SetFailed sets Failed field to given value.

### HasFailed

`func (o *BatchCreateTrackedQueriesResultResource) HasFailed() bool`

HasFailed returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


