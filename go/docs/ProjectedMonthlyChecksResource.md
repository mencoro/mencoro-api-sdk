# ProjectedMonthlyChecksResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectedMonthlyChecks** | **int32** | Checks a month of the current configuration would consume: for each ACTIVE tracked query, its runs per month (daily 30, weekly 4, monthly 1) multiplied by its nPasses, summed. Never null. | 
**ActiveTrackedQueryCount** | **int32** | Active tracked queries the projection was summed over, across every project of the organization, archived projects included. Paused queries are excluded from both figures. Never null. | 

## Methods

### NewProjectedMonthlyChecksResource

`func NewProjectedMonthlyChecksResource(projectedMonthlyChecks int32, activeTrackedQueryCount int32, ) *ProjectedMonthlyChecksResource`

NewProjectedMonthlyChecksResource instantiates a new ProjectedMonthlyChecksResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectedMonthlyChecksResourceWithDefaults

`func NewProjectedMonthlyChecksResourceWithDefaults() *ProjectedMonthlyChecksResource`

NewProjectedMonthlyChecksResourceWithDefaults instantiates a new ProjectedMonthlyChecksResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjectedMonthlyChecks

`func (o *ProjectedMonthlyChecksResource) GetProjectedMonthlyChecks() int32`

GetProjectedMonthlyChecks returns the ProjectedMonthlyChecks field if non-nil, zero value otherwise.

### GetProjectedMonthlyChecksOk

`func (o *ProjectedMonthlyChecksResource) GetProjectedMonthlyChecksOk() (*int32, bool)`

GetProjectedMonthlyChecksOk returns a tuple with the ProjectedMonthlyChecks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectedMonthlyChecks

`func (o *ProjectedMonthlyChecksResource) SetProjectedMonthlyChecks(v int32)`

SetProjectedMonthlyChecks sets ProjectedMonthlyChecks field to given value.


### GetActiveTrackedQueryCount

`func (o *ProjectedMonthlyChecksResource) GetActiveTrackedQueryCount() int32`

GetActiveTrackedQueryCount returns the ActiveTrackedQueryCount field if non-nil, zero value otherwise.

### GetActiveTrackedQueryCountOk

`func (o *ProjectedMonthlyChecksResource) GetActiveTrackedQueryCountOk() (*int32, bool)`

GetActiveTrackedQueryCountOk returns a tuple with the ActiveTrackedQueryCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActiveTrackedQueryCount

`func (o *ProjectedMonthlyChecksResource) SetActiveTrackedQueryCount(v int32)`

SetActiveTrackedQueryCount sets ActiveTrackedQueryCount field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


