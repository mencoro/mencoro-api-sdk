# BatchForceCheckTrackedQueries200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | Pointer to [**[]BatchPauseTrackedQueries200ResponseSuccessfulInner**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries whose check was accepted for submission. Accepted is not completed. | [optional] 
**Failed** | Pointer to [**[]BatchForceCheckTrackedQueries200ResponseFailedInner**](BatchForceCheckTrackedQueries200ResponseFailedInner.md) | Tracked queries no check was submitted for, each with the reason: check_budget_forecast_exhausted, subscription_not_found, tracked_query_already_paused or tracked_query_not_found. | [optional] 

## Methods

### NewBatchForceCheckTrackedQueries200Response

`func NewBatchForceCheckTrackedQueries200Response() *BatchForceCheckTrackedQueries200Response`

NewBatchForceCheckTrackedQueries200Response instantiates a new BatchForceCheckTrackedQueries200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchForceCheckTrackedQueries200ResponseWithDefaults

`func NewBatchForceCheckTrackedQueries200ResponseWithDefaults() *BatchForceCheckTrackedQueries200Response`

NewBatchForceCheckTrackedQueries200ResponseWithDefaults instantiates a new BatchForceCheckTrackedQueries200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSuccessful

`func (o *BatchForceCheckTrackedQueries200Response) GetSuccessful() []BatchPauseTrackedQueries200ResponseSuccessfulInner`

GetSuccessful returns the Successful field if non-nil, zero value otherwise.

### GetSuccessfulOk

`func (o *BatchForceCheckTrackedQueries200Response) GetSuccessfulOk() (*[]BatchPauseTrackedQueries200ResponseSuccessfulInner, bool)`

GetSuccessfulOk returns a tuple with the Successful field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccessful

`func (o *BatchForceCheckTrackedQueries200Response) SetSuccessful(v []BatchPauseTrackedQueries200ResponseSuccessfulInner)`

SetSuccessful sets Successful field to given value.

### HasSuccessful

`func (o *BatchForceCheckTrackedQueries200Response) HasSuccessful() bool`

HasSuccessful returns a boolean if a field has been set.

### GetFailed

`func (o *BatchForceCheckTrackedQueries200Response) GetFailed() []BatchForceCheckTrackedQueries200ResponseFailedInner`

GetFailed returns the Failed field if non-nil, zero value otherwise.

### GetFailedOk

`func (o *BatchForceCheckTrackedQueries200Response) GetFailedOk() (*[]BatchForceCheckTrackedQueries200ResponseFailedInner, bool)`

GetFailedOk returns a tuple with the Failed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailed

`func (o *BatchForceCheckTrackedQueries200Response) SetFailed(v []BatchForceCheckTrackedQueries200ResponseFailedInner)`

SetFailed sets Failed field to given value.

### HasFailed

`func (o *BatchForceCheckTrackedQueries200Response) HasFailed() bool`

HasFailed returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


