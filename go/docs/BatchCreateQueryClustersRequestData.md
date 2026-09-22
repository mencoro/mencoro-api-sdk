# BatchCreateQueryClustersRequestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Names** | **[]string** | Cluster names to create, already trimmed and lower-cased on the server. Duplicates are collapsed. | 

## Methods

### NewBatchCreateQueryClustersRequestData

`func NewBatchCreateQueryClustersRequestData(names []string, ) *BatchCreateQueryClustersRequestData`

NewBatchCreateQueryClustersRequestData instantiates a new BatchCreateQueryClustersRequestData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchCreateQueryClustersRequestDataWithDefaults

`func NewBatchCreateQueryClustersRequestDataWithDefaults() *BatchCreateQueryClustersRequestData`

NewBatchCreateQueryClustersRequestDataWithDefaults instantiates a new BatchCreateQueryClustersRequestData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetNames

`func (o *BatchCreateQueryClustersRequestData) GetNames() []string`

GetNames returns the Names field if non-nil, zero value otherwise.

### GetNamesOk

`func (o *BatchCreateQueryClustersRequestData) GetNamesOk() (*[]string, bool)`

GetNamesOk returns a tuple with the Names field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNames

`func (o *BatchCreateQueryClustersRequestData) SetNames(v []string)`

SetNames sets Names field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


