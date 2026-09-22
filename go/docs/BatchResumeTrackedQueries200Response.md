# BatchResumeTrackedQueries200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | Pointer to [**[]BatchPauseTrackedQueries200ResponseSuccessfulInner**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries that are now active, including ones that already were. | [optional] 
**Failed** | Pointer to [**[]BatchPauseTrackedQueries200ResponseFailedInner**](BatchPauseTrackedQueries200ResponseFailedInner.md) | Tracked queries left untouched, each with the domain error code a single-item call would have returned. | [optional] 

## Methods

### NewBatchResumeTrackedQueries200Response

`func NewBatchResumeTrackedQueries200Response() *BatchResumeTrackedQueries200Response`

NewBatchResumeTrackedQueries200Response instantiates a new BatchResumeTrackedQueries200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchResumeTrackedQueries200ResponseWithDefaults

`func NewBatchResumeTrackedQueries200ResponseWithDefaults() *BatchResumeTrackedQueries200Response`

NewBatchResumeTrackedQueries200ResponseWithDefaults instantiates a new BatchResumeTrackedQueries200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSuccessful

`func (o *BatchResumeTrackedQueries200Response) GetSuccessful() []BatchPauseTrackedQueries200ResponseSuccessfulInner`

GetSuccessful returns the Successful field if non-nil, zero value otherwise.

### GetSuccessfulOk

`func (o *BatchResumeTrackedQueries200Response) GetSuccessfulOk() (*[]BatchPauseTrackedQueries200ResponseSuccessfulInner, bool)`

GetSuccessfulOk returns a tuple with the Successful field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccessful

`func (o *BatchResumeTrackedQueries200Response) SetSuccessful(v []BatchPauseTrackedQueries200ResponseSuccessfulInner)`

SetSuccessful sets Successful field to given value.

### HasSuccessful

`func (o *BatchResumeTrackedQueries200Response) HasSuccessful() bool`

HasSuccessful returns a boolean if a field has been set.

### GetFailed

`func (o *BatchResumeTrackedQueries200Response) GetFailed() []BatchPauseTrackedQueries200ResponseFailedInner`

GetFailed returns the Failed field if non-nil, zero value otherwise.

### GetFailedOk

`func (o *BatchResumeTrackedQueries200Response) GetFailedOk() (*[]BatchPauseTrackedQueries200ResponseFailedInner, bool)`

GetFailedOk returns a tuple with the Failed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailed

`func (o *BatchResumeTrackedQueries200Response) SetFailed(v []BatchPauseTrackedQueries200ResponseFailedInner)`

SetFailed sets Failed field to given value.

### HasFailed

`func (o *BatchResumeTrackedQueries200Response) HasFailed() bool`

HasFailed returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


