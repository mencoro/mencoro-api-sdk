# ClusterMembershipRequestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**QueryClusterIds** | **[]string** | Ids of the query clusters. Duplicates are collapsed. Every id must belong to the project in the path. | 

## Methods

### NewClusterMembershipRequestData

`func NewClusterMembershipRequestData(queryClusterIds []string, ) *ClusterMembershipRequestData`

NewClusterMembershipRequestData instantiates a new ClusterMembershipRequestData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClusterMembershipRequestDataWithDefaults

`func NewClusterMembershipRequestDataWithDefaults() *ClusterMembershipRequestData`

NewClusterMembershipRequestDataWithDefaults instantiates a new ClusterMembershipRequestData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetQueryClusterIds

`func (o *ClusterMembershipRequestData) GetQueryClusterIds() []string`

GetQueryClusterIds returns the QueryClusterIds field if non-nil, zero value otherwise.

### GetQueryClusterIdsOk

`func (o *ClusterMembershipRequestData) GetQueryClusterIdsOk() (*[]string, bool)`

GetQueryClusterIdsOk returns a tuple with the QueryClusterIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryClusterIds

`func (o *ClusterMembershipRequestData) SetQueryClusterIds(v []string)`

SetQueryClusterIds sets QueryClusterIds field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


