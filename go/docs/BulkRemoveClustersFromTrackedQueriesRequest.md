# BulkRemoveClustersFromTrackedQueriesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | Pointer to **[]string** | Tracked queries to remove. At most 100 distinct ids; duplicates are collapsed. | [optional] 
**QueryClusterIds** | Pointer to **[]string** | Clusters every named tracked query is removed from. All must belong to the project in the path. | [optional] 

## Methods

### NewBulkRemoveClustersFromTrackedQueriesRequest

`func NewBulkRemoveClustersFromTrackedQueriesRequest() *BulkRemoveClustersFromTrackedQueriesRequest`

NewBulkRemoveClustersFromTrackedQueriesRequest instantiates a new BulkRemoveClustersFromTrackedQueriesRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBulkRemoveClustersFromTrackedQueriesRequestWithDefaults

`func NewBulkRemoveClustersFromTrackedQueriesRequestWithDefaults() *BulkRemoveClustersFromTrackedQueriesRequest`

NewBulkRemoveClustersFromTrackedQueriesRequestWithDefaults instantiates a new BulkRemoveClustersFromTrackedQueriesRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIds

`func (o *BulkRemoveClustersFromTrackedQueriesRequest) GetIds() []string`

GetIds returns the Ids field if non-nil, zero value otherwise.

### GetIdsOk

`func (o *BulkRemoveClustersFromTrackedQueriesRequest) GetIdsOk() (*[]string, bool)`

GetIdsOk returns a tuple with the Ids field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIds

`func (o *BulkRemoveClustersFromTrackedQueriesRequest) SetIds(v []string)`

SetIds sets Ids field to given value.

### HasIds

`func (o *BulkRemoveClustersFromTrackedQueriesRequest) HasIds() bool`

HasIds returns a boolean if a field has been set.

### GetQueryClusterIds

`func (o *BulkRemoveClustersFromTrackedQueriesRequest) GetQueryClusterIds() []string`

GetQueryClusterIds returns the QueryClusterIds field if non-nil, zero value otherwise.

### GetQueryClusterIdsOk

`func (o *BulkRemoveClustersFromTrackedQueriesRequest) GetQueryClusterIdsOk() (*[]string, bool)`

GetQueryClusterIdsOk returns a tuple with the QueryClusterIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryClusterIds

`func (o *BulkRemoveClustersFromTrackedQueriesRequest) SetQueryClusterIds(v []string)`

SetQueryClusterIds sets QueryClusterIds field to given value.

### HasQueryClusterIds

`func (o *BulkRemoveClustersFromTrackedQueriesRequest) HasQueryClusterIds() bool`

HasQueryClusterIds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


