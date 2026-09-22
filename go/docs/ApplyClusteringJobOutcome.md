# ApplyClusteringJobOutcome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Successful** | Pointer to [**[]ApplyClusteringJobOutcomeSuccessfulInner**](ApplyClusteringJobOutcomeSuccessfulInner.md) | Tracked queries written, each with the cluster ids it ended up with - the resulting state, not the delta. | [optional] 
**Failed** | Pointer to [**[]ApplyClusteringJobOutcomeFailedInner**](ApplyClusteringJobOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] 
**Clusters** | Pointer to [**[]ApplyClusteringJobOutcomeClustersInner**](ApplyClusteringJobOutcomeClustersInner.md) | Every cluster the assignments referred to, and whether this call created it. | [optional] 
**SkippedClusters** | Pointer to [**[]ApplyClusteringJobOutcomeSkippedClustersInner**](ApplyClusteringJobOutcomeSkippedClustersInner.md) | Proposed names the store cannot hold. A tracked query whose proposed cluster was skipped ends up with fewer clusters than the proposal showed. | [optional] 
**Unassigned** | Pointer to **[]string** | Tracked queries the job produced no assignment for. Nothing was written for them and they keep the clusters they already had, under every merge mode. | [optional] 

## Methods

### NewApplyClusteringJobOutcome

`func NewApplyClusteringJobOutcome() *ApplyClusteringJobOutcome`

NewApplyClusteringJobOutcome instantiates a new ApplyClusteringJobOutcome object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewApplyClusteringJobOutcomeWithDefaults

`func NewApplyClusteringJobOutcomeWithDefaults() *ApplyClusteringJobOutcome`

NewApplyClusteringJobOutcomeWithDefaults instantiates a new ApplyClusteringJobOutcome object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSuccessful

`func (o *ApplyClusteringJobOutcome) GetSuccessful() []ApplyClusteringJobOutcomeSuccessfulInner`

GetSuccessful returns the Successful field if non-nil, zero value otherwise.

### GetSuccessfulOk

`func (o *ApplyClusteringJobOutcome) GetSuccessfulOk() (*[]ApplyClusteringJobOutcomeSuccessfulInner, bool)`

GetSuccessfulOk returns a tuple with the Successful field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccessful

`func (o *ApplyClusteringJobOutcome) SetSuccessful(v []ApplyClusteringJobOutcomeSuccessfulInner)`

SetSuccessful sets Successful field to given value.

### HasSuccessful

`func (o *ApplyClusteringJobOutcome) HasSuccessful() bool`

HasSuccessful returns a boolean if a field has been set.

### GetFailed

`func (o *ApplyClusteringJobOutcome) GetFailed() []ApplyClusteringJobOutcomeFailedInner`

GetFailed returns the Failed field if non-nil, zero value otherwise.

### GetFailedOk

`func (o *ApplyClusteringJobOutcome) GetFailedOk() (*[]ApplyClusteringJobOutcomeFailedInner, bool)`

GetFailedOk returns a tuple with the Failed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailed

`func (o *ApplyClusteringJobOutcome) SetFailed(v []ApplyClusteringJobOutcomeFailedInner)`

SetFailed sets Failed field to given value.

### HasFailed

`func (o *ApplyClusteringJobOutcome) HasFailed() bool`

HasFailed returns a boolean if a field has been set.

### GetClusters

`func (o *ApplyClusteringJobOutcome) GetClusters() []ApplyClusteringJobOutcomeClustersInner`

GetClusters returns the Clusters field if non-nil, zero value otherwise.

### GetClustersOk

`func (o *ApplyClusteringJobOutcome) GetClustersOk() (*[]ApplyClusteringJobOutcomeClustersInner, bool)`

GetClustersOk returns a tuple with the Clusters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClusters

`func (o *ApplyClusteringJobOutcome) SetClusters(v []ApplyClusteringJobOutcomeClustersInner)`

SetClusters sets Clusters field to given value.

### HasClusters

`func (o *ApplyClusteringJobOutcome) HasClusters() bool`

HasClusters returns a boolean if a field has been set.

### GetSkippedClusters

`func (o *ApplyClusteringJobOutcome) GetSkippedClusters() []ApplyClusteringJobOutcomeSkippedClustersInner`

GetSkippedClusters returns the SkippedClusters field if non-nil, zero value otherwise.

### GetSkippedClustersOk

`func (o *ApplyClusteringJobOutcome) GetSkippedClustersOk() (*[]ApplyClusteringJobOutcomeSkippedClustersInner, bool)`

GetSkippedClustersOk returns a tuple with the SkippedClusters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSkippedClusters

`func (o *ApplyClusteringJobOutcome) SetSkippedClusters(v []ApplyClusteringJobOutcomeSkippedClustersInner)`

SetSkippedClusters sets SkippedClusters field to given value.

### HasSkippedClusters

`func (o *ApplyClusteringJobOutcome) HasSkippedClusters() bool`

HasSkippedClusters returns a boolean if a field has been set.

### GetUnassigned

`func (o *ApplyClusteringJobOutcome) GetUnassigned() []string`

GetUnassigned returns the Unassigned field if non-nil, zero value otherwise.

### GetUnassignedOk

`func (o *ApplyClusteringJobOutcome) GetUnassignedOk() (*[]string, bool)`

GetUnassignedOk returns a tuple with the Unassigned field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnassigned

`func (o *ApplyClusteringJobOutcome) SetUnassigned(v []string)`

SetUnassigned sets Unassigned field to given value.

### HasUnassigned

`func (o *ApplyClusteringJobOutcome) HasUnassigned() bool`

HasUnassigned returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


