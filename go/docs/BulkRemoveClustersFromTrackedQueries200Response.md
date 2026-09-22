# BulkRemoveClustersFromTrackedQueries200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | Pointer to [**[]BatchPauseTrackedQueries200ResponseSuccessfulInner**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries that were removed from every named cluster. | [optional] 
**Failed** | Pointer to [**[]BatchPauseTrackedQueries200ResponseFailedInner**](BatchPauseTrackedQueries200ResponseFailedInner.md) | Tracked queries left untouched, each with the domain error code a single-item call would have returned. | [optional] 

## Methods

### NewBulkRemoveClustersFromTrackedQueries200Response

`func NewBulkRemoveClustersFromTrackedQueries200Response() *BulkRemoveClustersFromTrackedQueries200Response`

NewBulkRemoveClustersFromTrackedQueries200Response instantiates a new BulkRemoveClustersFromTrackedQueries200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBulkRemoveClustersFromTrackedQueries200ResponseWithDefaults

`func NewBulkRemoveClustersFromTrackedQueries200ResponseWithDefaults() *BulkRemoveClustersFromTrackedQueries200Response`

NewBulkRemoveClustersFromTrackedQueries200ResponseWithDefaults instantiates a new BulkRemoveClustersFromTrackedQueries200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSuccessful

`func (o *BulkRemoveClustersFromTrackedQueries200Response) GetSuccessful() []BatchPauseTrackedQueries200ResponseSuccessfulInner`

GetSuccessful returns the Successful field if non-nil, zero value otherwise.

### GetSuccessfulOk

`func (o *BulkRemoveClustersFromTrackedQueries200Response) GetSuccessfulOk() (*[]BatchPauseTrackedQueries200ResponseSuccessfulInner, bool)`

GetSuccessfulOk returns a tuple with the Successful field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccessful

`func (o *BulkRemoveClustersFromTrackedQueries200Response) SetSuccessful(v []BatchPauseTrackedQueries200ResponseSuccessfulInner)`

SetSuccessful sets Successful field to given value.

### HasSuccessful

`func (o *BulkRemoveClustersFromTrackedQueries200Response) HasSuccessful() bool`

HasSuccessful returns a boolean if a field has been set.

### GetFailed

`func (o *BulkRemoveClustersFromTrackedQueries200Response) GetFailed() []BatchPauseTrackedQueries200ResponseFailedInner`

GetFailed returns the Failed field if non-nil, zero value otherwise.

### GetFailedOk

`func (o *BulkRemoveClustersFromTrackedQueries200Response) GetFailedOk() (*[]BatchPauseTrackedQueries200ResponseFailedInner, bool)`

GetFailedOk returns a tuple with the Failed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailed

`func (o *BulkRemoveClustersFromTrackedQueries200Response) SetFailed(v []BatchPauseTrackedQueries200ResponseFailedInner)`

SetFailed sets Failed field to given value.

### HasFailed

`func (o *BulkRemoveClustersFromTrackedQueries200Response) HasFailed() bool`

HasFailed returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


