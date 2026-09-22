# BatchChangeTrackedQueryPassesRequestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | **[]string** | Ids of the tracked queries to change. Duplicates are collapsed. | 
**NPasses** | **int32** | Passes run per check. Only an AI engine accepts more than one; a non-AI target is reported under \&quot;failed\&quot;. | 

## Methods

### NewBatchChangeTrackedQueryPassesRequestData

`func NewBatchChangeTrackedQueryPassesRequestData(ids []string, nPasses int32, ) *BatchChangeTrackedQueryPassesRequestData`

NewBatchChangeTrackedQueryPassesRequestData instantiates a new BatchChangeTrackedQueryPassesRequestData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchChangeTrackedQueryPassesRequestDataWithDefaults

`func NewBatchChangeTrackedQueryPassesRequestDataWithDefaults() *BatchChangeTrackedQueryPassesRequestData`

NewBatchChangeTrackedQueryPassesRequestDataWithDefaults instantiates a new BatchChangeTrackedQueryPassesRequestData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIds

`func (o *BatchChangeTrackedQueryPassesRequestData) GetIds() []string`

GetIds returns the Ids field if non-nil, zero value otherwise.

### GetIdsOk

`func (o *BatchChangeTrackedQueryPassesRequestData) GetIdsOk() (*[]string, bool)`

GetIdsOk returns a tuple with the Ids field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIds

`func (o *BatchChangeTrackedQueryPassesRequestData) SetIds(v []string)`

SetIds sets Ids field to given value.


### GetNPasses

`func (o *BatchChangeTrackedQueryPassesRequestData) GetNPasses() int32`

GetNPasses returns the NPasses field if non-nil, zero value otherwise.

### GetNPassesOk

`func (o *BatchChangeTrackedQueryPassesRequestData) GetNPassesOk() (*int32, bool)`

GetNPassesOk returns a tuple with the NPasses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNPasses

`func (o *BatchChangeTrackedQueryPassesRequestData) SetNPasses(v int32)`

SetNPasses sets NPasses field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


