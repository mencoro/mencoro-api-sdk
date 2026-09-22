# EntitlementsResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **string** | \&quot;none\&quot; when the organization has never had a subscription contract. | 
**IsEntitled** | **bool** | Whether the organization may use paid features right now: an active contract, or a cancelled one still inside its paid grace window. | 
**CheckBudget** | Pointer to **NullableInt32** | Checks the current cycle allows. Null when there is no plan on file, which is not the same as a budget of zero. | [optional] 
**ChecksConsumed** | Pointer to **NullableInt32** | Checks consumed so far in the current cycle. Null when there is no plan on file. | [optional] 
**ChecksAvailable** | Pointer to **NullableInt32** | Checks left in the current cycle. Null when there is no plan on file. | [optional] 
**BillingCycleType** | Pointer to **NullableString** | How often the allowance renews. Null when there is no plan on file. | [optional] 
**BillingCycleAnchor** | Pointer to **NullableTime** | Start of the current cycle. Null when there is no plan on file. | [optional] 
**NextResetAt** | Pointer to **NullableTime** | When the check budget next resets. Null when there is no plan on file. | [optional] 
**CancelledAt** | Pointer to **NullableTime** | When the subscription was terminally cancelled. Null while it has not been. | [optional] 
**ScheduledToCancelAt** | Pointer to **NullableTime** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. | [optional] 
**GracePeriodEndsAt** | Pointer to **NullableTime** | When paid access ends after a cancellation. Null when the subscription has not been cancelled. | [optional] 

## Methods

### NewEntitlementsResource

`func NewEntitlementsResource(status string, isEntitled bool, ) *EntitlementsResource`

NewEntitlementsResource instantiates a new EntitlementsResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEntitlementsResourceWithDefaults

`func NewEntitlementsResourceWithDefaults() *EntitlementsResource`

NewEntitlementsResourceWithDefaults instantiates a new EntitlementsResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *EntitlementsResource) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *EntitlementsResource) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *EntitlementsResource) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetIsEntitled

`func (o *EntitlementsResource) GetIsEntitled() bool`

GetIsEntitled returns the IsEntitled field if non-nil, zero value otherwise.

### GetIsEntitledOk

`func (o *EntitlementsResource) GetIsEntitledOk() (*bool, bool)`

GetIsEntitledOk returns a tuple with the IsEntitled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsEntitled

`func (o *EntitlementsResource) SetIsEntitled(v bool)`

SetIsEntitled sets IsEntitled field to given value.


### GetCheckBudget

`func (o *EntitlementsResource) GetCheckBudget() int32`

GetCheckBudget returns the CheckBudget field if non-nil, zero value otherwise.

### GetCheckBudgetOk

`func (o *EntitlementsResource) GetCheckBudgetOk() (*int32, bool)`

GetCheckBudgetOk returns a tuple with the CheckBudget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckBudget

`func (o *EntitlementsResource) SetCheckBudget(v int32)`

SetCheckBudget sets CheckBudget field to given value.

### HasCheckBudget

`func (o *EntitlementsResource) HasCheckBudget() bool`

HasCheckBudget returns a boolean if a field has been set.

### SetCheckBudgetNil

`func (o *EntitlementsResource) SetCheckBudgetNil(b bool)`

 SetCheckBudgetNil sets the value for CheckBudget to be an explicit nil

### UnsetCheckBudget
`func (o *EntitlementsResource) UnsetCheckBudget()`

UnsetCheckBudget ensures that no value is present for CheckBudget, not even an explicit nil
### GetChecksConsumed

`func (o *EntitlementsResource) GetChecksConsumed() int32`

GetChecksConsumed returns the ChecksConsumed field if non-nil, zero value otherwise.

### GetChecksConsumedOk

`func (o *EntitlementsResource) GetChecksConsumedOk() (*int32, bool)`

GetChecksConsumedOk returns a tuple with the ChecksConsumed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChecksConsumed

`func (o *EntitlementsResource) SetChecksConsumed(v int32)`

SetChecksConsumed sets ChecksConsumed field to given value.

### HasChecksConsumed

`func (o *EntitlementsResource) HasChecksConsumed() bool`

HasChecksConsumed returns a boolean if a field has been set.

### SetChecksConsumedNil

`func (o *EntitlementsResource) SetChecksConsumedNil(b bool)`

 SetChecksConsumedNil sets the value for ChecksConsumed to be an explicit nil

### UnsetChecksConsumed
`func (o *EntitlementsResource) UnsetChecksConsumed()`

UnsetChecksConsumed ensures that no value is present for ChecksConsumed, not even an explicit nil
### GetChecksAvailable

`func (o *EntitlementsResource) GetChecksAvailable() int32`

GetChecksAvailable returns the ChecksAvailable field if non-nil, zero value otherwise.

### GetChecksAvailableOk

`func (o *EntitlementsResource) GetChecksAvailableOk() (*int32, bool)`

GetChecksAvailableOk returns a tuple with the ChecksAvailable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChecksAvailable

`func (o *EntitlementsResource) SetChecksAvailable(v int32)`

SetChecksAvailable sets ChecksAvailable field to given value.

### HasChecksAvailable

`func (o *EntitlementsResource) HasChecksAvailable() bool`

HasChecksAvailable returns a boolean if a field has been set.

### SetChecksAvailableNil

`func (o *EntitlementsResource) SetChecksAvailableNil(b bool)`

 SetChecksAvailableNil sets the value for ChecksAvailable to be an explicit nil

### UnsetChecksAvailable
`func (o *EntitlementsResource) UnsetChecksAvailable()`

UnsetChecksAvailable ensures that no value is present for ChecksAvailable, not even an explicit nil
### GetBillingCycleType

`func (o *EntitlementsResource) GetBillingCycleType() string`

GetBillingCycleType returns the BillingCycleType field if non-nil, zero value otherwise.

### GetBillingCycleTypeOk

`func (o *EntitlementsResource) GetBillingCycleTypeOk() (*string, bool)`

GetBillingCycleTypeOk returns a tuple with the BillingCycleType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBillingCycleType

`func (o *EntitlementsResource) SetBillingCycleType(v string)`

SetBillingCycleType sets BillingCycleType field to given value.

### HasBillingCycleType

`func (o *EntitlementsResource) HasBillingCycleType() bool`

HasBillingCycleType returns a boolean if a field has been set.

### SetBillingCycleTypeNil

`func (o *EntitlementsResource) SetBillingCycleTypeNil(b bool)`

 SetBillingCycleTypeNil sets the value for BillingCycleType to be an explicit nil

### UnsetBillingCycleType
`func (o *EntitlementsResource) UnsetBillingCycleType()`

UnsetBillingCycleType ensures that no value is present for BillingCycleType, not even an explicit nil
### GetBillingCycleAnchor

`func (o *EntitlementsResource) GetBillingCycleAnchor() time.Time`

GetBillingCycleAnchor returns the BillingCycleAnchor field if non-nil, zero value otherwise.

### GetBillingCycleAnchorOk

`func (o *EntitlementsResource) GetBillingCycleAnchorOk() (*time.Time, bool)`

GetBillingCycleAnchorOk returns a tuple with the BillingCycleAnchor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBillingCycleAnchor

`func (o *EntitlementsResource) SetBillingCycleAnchor(v time.Time)`

SetBillingCycleAnchor sets BillingCycleAnchor field to given value.

### HasBillingCycleAnchor

`func (o *EntitlementsResource) HasBillingCycleAnchor() bool`

HasBillingCycleAnchor returns a boolean if a field has been set.

### SetBillingCycleAnchorNil

`func (o *EntitlementsResource) SetBillingCycleAnchorNil(b bool)`

 SetBillingCycleAnchorNil sets the value for BillingCycleAnchor to be an explicit nil

### UnsetBillingCycleAnchor
`func (o *EntitlementsResource) UnsetBillingCycleAnchor()`

UnsetBillingCycleAnchor ensures that no value is present for BillingCycleAnchor, not even an explicit nil
### GetNextResetAt

`func (o *EntitlementsResource) GetNextResetAt() time.Time`

GetNextResetAt returns the NextResetAt field if non-nil, zero value otherwise.

### GetNextResetAtOk

`func (o *EntitlementsResource) GetNextResetAtOk() (*time.Time, bool)`

GetNextResetAtOk returns a tuple with the NextResetAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextResetAt

`func (o *EntitlementsResource) SetNextResetAt(v time.Time)`

SetNextResetAt sets NextResetAt field to given value.

### HasNextResetAt

`func (o *EntitlementsResource) HasNextResetAt() bool`

HasNextResetAt returns a boolean if a field has been set.

### SetNextResetAtNil

`func (o *EntitlementsResource) SetNextResetAtNil(b bool)`

 SetNextResetAtNil sets the value for NextResetAt to be an explicit nil

### UnsetNextResetAt
`func (o *EntitlementsResource) UnsetNextResetAt()`

UnsetNextResetAt ensures that no value is present for NextResetAt, not even an explicit nil
### GetCancelledAt

`func (o *EntitlementsResource) GetCancelledAt() time.Time`

GetCancelledAt returns the CancelledAt field if non-nil, zero value otherwise.

### GetCancelledAtOk

`func (o *EntitlementsResource) GetCancelledAtOk() (*time.Time, bool)`

GetCancelledAtOk returns a tuple with the CancelledAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCancelledAt

`func (o *EntitlementsResource) SetCancelledAt(v time.Time)`

SetCancelledAt sets CancelledAt field to given value.

### HasCancelledAt

`func (o *EntitlementsResource) HasCancelledAt() bool`

HasCancelledAt returns a boolean if a field has been set.

### SetCancelledAtNil

`func (o *EntitlementsResource) SetCancelledAtNil(b bool)`

 SetCancelledAtNil sets the value for CancelledAt to be an explicit nil

### UnsetCancelledAt
`func (o *EntitlementsResource) UnsetCancelledAt()`

UnsetCancelledAt ensures that no value is present for CancelledAt, not even an explicit nil
### GetScheduledToCancelAt

`func (o *EntitlementsResource) GetScheduledToCancelAt() time.Time`

GetScheduledToCancelAt returns the ScheduledToCancelAt field if non-nil, zero value otherwise.

### GetScheduledToCancelAtOk

`func (o *EntitlementsResource) GetScheduledToCancelAtOk() (*time.Time, bool)`

GetScheduledToCancelAtOk returns a tuple with the ScheduledToCancelAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledToCancelAt

`func (o *EntitlementsResource) SetScheduledToCancelAt(v time.Time)`

SetScheduledToCancelAt sets ScheduledToCancelAt field to given value.

### HasScheduledToCancelAt

`func (o *EntitlementsResource) HasScheduledToCancelAt() bool`

HasScheduledToCancelAt returns a boolean if a field has been set.

### SetScheduledToCancelAtNil

`func (o *EntitlementsResource) SetScheduledToCancelAtNil(b bool)`

 SetScheduledToCancelAtNil sets the value for ScheduledToCancelAt to be an explicit nil

### UnsetScheduledToCancelAt
`func (o *EntitlementsResource) UnsetScheduledToCancelAt()`

UnsetScheduledToCancelAt ensures that no value is present for ScheduledToCancelAt, not even an explicit nil
### GetGracePeriodEndsAt

`func (o *EntitlementsResource) GetGracePeriodEndsAt() time.Time`

GetGracePeriodEndsAt returns the GracePeriodEndsAt field if non-nil, zero value otherwise.

### GetGracePeriodEndsAtOk

`func (o *EntitlementsResource) GetGracePeriodEndsAtOk() (*time.Time, bool)`

GetGracePeriodEndsAtOk returns a tuple with the GracePeriodEndsAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGracePeriodEndsAt

`func (o *EntitlementsResource) SetGracePeriodEndsAt(v time.Time)`

SetGracePeriodEndsAt sets GracePeriodEndsAt field to given value.

### HasGracePeriodEndsAt

`func (o *EntitlementsResource) HasGracePeriodEndsAt() bool`

HasGracePeriodEndsAt returns a boolean if a field has been set.

### SetGracePeriodEndsAtNil

`func (o *EntitlementsResource) SetGracePeriodEndsAtNil(b bool)`

 SetGracePeriodEndsAtNil sets the value for GracePeriodEndsAt to be an explicit nil

### UnsetGracePeriodEndsAt
`func (o *EntitlementsResource) UnsetGracePeriodEndsAt()`

UnsetGracePeriodEndsAt ensures that no value is present for GracePeriodEndsAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


