# TrackedQueryCountResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Count** | **int32** | Tracked queries in the project matching the status filter. Every status when none was sent. | 
**CheckCost** | **int32** | Budget cost of force-checking exactly those tracked queries, in check budget units: the sum of each one&#39;s configured passes. One unit per pass, the same unit the plan allowance is counted in. Reserves nothing and debits nothing. | 

## Methods

### NewTrackedQueryCountResource

`func NewTrackedQueryCountResource(count int32, checkCost int32, ) *TrackedQueryCountResource`

NewTrackedQueryCountResource instantiates a new TrackedQueryCountResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrackedQueryCountResourceWithDefaults

`func NewTrackedQueryCountResourceWithDefaults() *TrackedQueryCountResource`

NewTrackedQueryCountResourceWithDefaults instantiates a new TrackedQueryCountResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCount

`func (o *TrackedQueryCountResource) GetCount() int32`

GetCount returns the Count field if non-nil, zero value otherwise.

### GetCountOk

`func (o *TrackedQueryCountResource) GetCountOk() (*int32, bool)`

GetCountOk returns a tuple with the Count field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCount

`func (o *TrackedQueryCountResource) SetCount(v int32)`

SetCount sets Count field to given value.


### GetCheckCost

`func (o *TrackedQueryCountResource) GetCheckCost() int32`

GetCheckCost returns the CheckCost field if non-nil, zero value otherwise.

### GetCheckCostOk

`func (o *TrackedQueryCountResource) GetCheckCostOk() (*int32, bool)`

GetCheckCostOk returns a tuple with the CheckCost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckCost

`func (o *TrackedQueryCountResource) SetCheckCost(v int32)`

SetCheckCost sets CheckCost field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


