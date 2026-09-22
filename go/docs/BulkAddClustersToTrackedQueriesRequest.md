# BulkAddClustersToTrackedQueriesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | Pointer to **[]string** | Tracked queries to add. At most 100 distinct ids; duplicates are collapsed. | [optional] 
**QueryClusterIds** | Pointer to **[]string** | Clusters every named tracked query is added to. All must belong to the project in the path. | [optional] 

## Methods

### NewBulkAddClustersToTrackedQueriesRequest

`func NewBulkAddClustersToTrackedQueriesRequest() *BulkAddClustersToTrackedQueriesRequest`

NewBulkAddClustersToTrackedQueriesRequest instantiates a new BulkAddClustersToTrackedQueriesRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBulkAddClustersToTrackedQueriesRequestWithDefaults

`func NewBulkAddClustersToTrackedQueriesRequestWithDefaults() *BulkAddClustersToTrackedQueriesRequest`

NewBulkAddClustersToTrackedQueriesRequestWithDefaults instantiates a new BulkAddClustersToTrackedQueriesRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIds

`func (o *BulkAddClustersToTrackedQueriesRequest) GetIds() []string`

GetIds returns the Ids field if non-nil, zero value otherwise.

### GetIdsOk

`func (o *BulkAddClustersToTrackedQueriesRequest) GetIdsOk() (*[]string, bool)`

GetIdsOk returns a tuple with the Ids field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIds

`func (o *BulkAddClustersToTrackedQueriesRequest) SetIds(v []string)`

SetIds sets Ids field to given value.

### HasIds

`func (o *BulkAddClustersToTrackedQueriesRequest) HasIds() bool`

HasIds returns a boolean if a field has been set.

### GetQueryClusterIds

`func (o *BulkAddClustersToTrackedQueriesRequest) GetQueryClusterIds() []string`

GetQueryClusterIds returns the QueryClusterIds field if non-nil, zero value otherwise.

### GetQueryClusterIdsOk

`func (o *BulkAddClustersToTrackedQueriesRequest) GetQueryClusterIdsOk() (*[]string, bool)`

GetQueryClusterIdsOk returns a tuple with the QueryClusterIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryClusterIds

`func (o *BulkAddClustersToTrackedQueriesRequest) SetQueryClusterIds(v []string)`

SetQueryClusterIds sets QueryClusterIds field to given value.

### HasQueryClusterIds

`func (o *BulkAddClustersToTrackedQueriesRequest) HasQueryClusterIds() bool`

HasQueryClusterIds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


