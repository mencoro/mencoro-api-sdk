# StartClusteringJobRequestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackedQueryIds** | **[]string** | The tracked queries to cluster. Duplicates are collapsed. | 
**Mode** | **string** | fill_gaps groups only tracked queries that belong to no cluster; add_on_top adds the new clusters to whatever each query already has; full_regroup replaces the current clusters with the job&#39;s. | 
**RestrictToExistingClusters** | Pointer to **bool** | When true the job may only use clusters the project already has, and leaves a query ungrouped rather than inventing a name for it. | [optional] [default to false]

## Methods

### NewStartClusteringJobRequestData

`func NewStartClusteringJobRequestData(trackedQueryIds []string, mode string, ) *StartClusteringJobRequestData`

NewStartClusteringJobRequestData instantiates a new StartClusteringJobRequestData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStartClusteringJobRequestDataWithDefaults

`func NewStartClusteringJobRequestDataWithDefaults() *StartClusteringJobRequestData`

NewStartClusteringJobRequestDataWithDefaults instantiates a new StartClusteringJobRequestData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTrackedQueryIds

`func (o *StartClusteringJobRequestData) GetTrackedQueryIds() []string`

GetTrackedQueryIds returns the TrackedQueryIds field if non-nil, zero value otherwise.

### GetTrackedQueryIdsOk

`func (o *StartClusteringJobRequestData) GetTrackedQueryIdsOk() (*[]string, bool)`

GetTrackedQueryIdsOk returns a tuple with the TrackedQueryIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryIds

`func (o *StartClusteringJobRequestData) SetTrackedQueryIds(v []string)`

SetTrackedQueryIds sets TrackedQueryIds field to given value.


### GetMode

`func (o *StartClusteringJobRequestData) GetMode() string`

GetMode returns the Mode field if non-nil, zero value otherwise.

### GetModeOk

`func (o *StartClusteringJobRequestData) GetModeOk() (*string, bool)`

GetModeOk returns a tuple with the Mode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMode

`func (o *StartClusteringJobRequestData) SetMode(v string)`

SetMode sets Mode field to given value.


### GetRestrictToExistingClusters

`func (o *StartClusteringJobRequestData) GetRestrictToExistingClusters() bool`

GetRestrictToExistingClusters returns the RestrictToExistingClusters field if non-nil, zero value otherwise.

### GetRestrictToExistingClustersOk

`func (o *StartClusteringJobRequestData) GetRestrictToExistingClustersOk() (*bool, bool)`

GetRestrictToExistingClustersOk returns a tuple with the RestrictToExistingClusters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestrictToExistingClusters

`func (o *StartClusteringJobRequestData) SetRestrictToExistingClusters(v bool)`

SetRestrictToExistingClusters sets RestrictToExistingClusters field to given value.

### HasRestrictToExistingClusters

`func (o *StartClusteringJobRequestData) HasRestrictToExistingClusters() bool`

HasRestrictToExistingClusters returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


