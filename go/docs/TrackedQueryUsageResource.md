# TrackedQueryUsageResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TrackedQueryCount** | **int32** | Tracked queries across every project of the organization, archived projects included, counting active and paused queries alike. Never null; 0 means none are configured. | 

## Methods

### NewTrackedQueryUsageResource

`func NewTrackedQueryUsageResource(trackedQueryCount int32, ) *TrackedQueryUsageResource`

NewTrackedQueryUsageResource instantiates a new TrackedQueryUsageResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrackedQueryUsageResourceWithDefaults

`func NewTrackedQueryUsageResourceWithDefaults() *TrackedQueryUsageResource`

NewTrackedQueryUsageResourceWithDefaults instantiates a new TrackedQueryUsageResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTrackedQueryCount

`func (o *TrackedQueryUsageResource) GetTrackedQueryCount() int32`

GetTrackedQueryCount returns the TrackedQueryCount field if non-nil, zero value otherwise.

### GetTrackedQueryCountOk

`func (o *TrackedQueryUsageResource) GetTrackedQueryCountOk() (*int32, bool)`

GetTrackedQueryCountOk returns a tuple with the TrackedQueryCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryCount

`func (o *TrackedQueryUsageResource) SetTrackedQueryCount(v int32)`

SetTrackedQueryCount sets TrackedQueryCount field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


