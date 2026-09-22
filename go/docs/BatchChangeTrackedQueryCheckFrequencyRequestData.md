# BatchChangeTrackedQueryCheckFrequencyRequestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | **[]string** | Ids of the tracked queries to change. Duplicates are collapsed. | 
**CheckFrequency** | **string** | How often each query is checked while it is active. | 

## Methods

### NewBatchChangeTrackedQueryCheckFrequencyRequestData

`func NewBatchChangeTrackedQueryCheckFrequencyRequestData(ids []string, checkFrequency string, ) *BatchChangeTrackedQueryCheckFrequencyRequestData`

NewBatchChangeTrackedQueryCheckFrequencyRequestData instantiates a new BatchChangeTrackedQueryCheckFrequencyRequestData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchChangeTrackedQueryCheckFrequencyRequestDataWithDefaults

`func NewBatchChangeTrackedQueryCheckFrequencyRequestDataWithDefaults() *BatchChangeTrackedQueryCheckFrequencyRequestData`

NewBatchChangeTrackedQueryCheckFrequencyRequestDataWithDefaults instantiates a new BatchChangeTrackedQueryCheckFrequencyRequestData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIds

`func (o *BatchChangeTrackedQueryCheckFrequencyRequestData) GetIds() []string`

GetIds returns the Ids field if non-nil, zero value otherwise.

### GetIdsOk

`func (o *BatchChangeTrackedQueryCheckFrequencyRequestData) GetIdsOk() (*[]string, bool)`

GetIdsOk returns a tuple with the Ids field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIds

`func (o *BatchChangeTrackedQueryCheckFrequencyRequestData) SetIds(v []string)`

SetIds sets Ids field to given value.


### GetCheckFrequency

`func (o *BatchChangeTrackedQueryCheckFrequencyRequestData) GetCheckFrequency() string`

GetCheckFrequency returns the CheckFrequency field if non-nil, zero value otherwise.

### GetCheckFrequencyOk

`func (o *BatchChangeTrackedQueryCheckFrequencyRequestData) GetCheckFrequencyOk() (*string, bool)`

GetCheckFrequencyOk returns a tuple with the CheckFrequency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckFrequency

`func (o *BatchChangeTrackedQueryCheckFrequencyRequestData) SetCheckFrequency(v string)`

SetCheckFrequency sets CheckFrequency field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


