# SubscriptionResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **string** | Contract state. \&quot;none\&quot; when the organization has never held a subscription. | 
**TierCode** | Pointer to **NullableString** | Public tier identifier derived from the check budget. | [optional] 
**BillingCycleType** | Pointer to **NullableString** | Billing interval of the contract. | [optional] 
**BillingCycleAnchor** | Pointer to **NullableTime** | Instant the billing cycle is anchored to. | [optional] 
**CheckBudget** | Pointer to **NullableInt32** | Checks the current cycle grants. Null when there is no subscription, never a stand-in for zero. | [optional] 
**ChecksConsumed** | Pointer to **NullableInt32** | Checks consumed so far in the current cycle. Null when there is no subscription; zero means none consumed yet. | [optional] 
**ChecksAvailable** | Pointer to **NullableInt32** | Checks still available in the current cycle. Null when there is no subscription; zero means the budget is exhausted. | [optional] 
**NextResetAt** | Pointer to **NullableTime** | When the check budget resets next. | [optional] 
**CancelledAt** | Pointer to **NullableTime** | When the subscription was terminally cancelled. Null while it has not been. | [optional] 
**ScheduledToCancelAt** | Pointer to **NullableTime** | When a scheduled cancellation takes effect, while the subscription is still running. Null when none is scheduled. | [optional] 
**GracePeriodEndsAt** | Pointer to **NullableTime** | When paid access ends after a cancellation. Null when the subscription is not cancelled. | [optional] 
**DeactivationReason** | Pointer to **NullableString** | Why the subscription is currently inactive. Null for an active subscription, and meaningless once \&quot;cancelledAt\&quot; is set - the cancellation supersedes it. | [optional] 
**IsEntitled** | **bool** | Whether the organization may use paid features right now: active, or cancelled but still inside its paid grace window. | 

## Methods

### NewSubscriptionResource

`func NewSubscriptionResource(status string, isEntitled bool, ) *SubscriptionResource`

NewSubscriptionResource instantiates a new SubscriptionResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSubscriptionResourceWithDefaults

`func NewSubscriptionResourceWithDefaults() *SubscriptionResource`

NewSubscriptionResourceWithDefaults instantiates a new SubscriptionResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *SubscriptionResource) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SubscriptionResource) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SubscriptionResource) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetTierCode

`func (o *SubscriptionResource) GetTierCode() string`

GetTierCode returns the TierCode field if non-nil, zero value otherwise.

### GetTierCodeOk

`func (o *SubscriptionResource) GetTierCodeOk() (*string, bool)`

GetTierCodeOk returns a tuple with the TierCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTierCode

`func (o *SubscriptionResource) SetTierCode(v string)`

SetTierCode sets TierCode field to given value.

### HasTierCode

`func (o *SubscriptionResource) HasTierCode() bool`

HasTierCode returns a boolean if a field has been set.

### SetTierCodeNil

`func (o *SubscriptionResource) SetTierCodeNil(b bool)`

 SetTierCodeNil sets the value for TierCode to be an explicit nil

### UnsetTierCode
`func (o *SubscriptionResource) UnsetTierCode()`

UnsetTierCode ensures that no value is present for TierCode, not even an explicit nil
### GetBillingCycleType

`func (o *SubscriptionResource) GetBillingCycleType() string`

GetBillingCycleType returns the BillingCycleType field if non-nil, zero value otherwise.

### GetBillingCycleTypeOk

`func (o *SubscriptionResource) GetBillingCycleTypeOk() (*string, bool)`

GetBillingCycleTypeOk returns a tuple with the BillingCycleType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBillingCycleType

`func (o *SubscriptionResource) SetBillingCycleType(v string)`

SetBillingCycleType sets BillingCycleType field to given value.

### HasBillingCycleType

`func (o *SubscriptionResource) HasBillingCycleType() bool`

HasBillingCycleType returns a boolean if a field has been set.

### SetBillingCycleTypeNil

`func (o *SubscriptionResource) SetBillingCycleTypeNil(b bool)`

 SetBillingCycleTypeNil sets the value for BillingCycleType to be an explicit nil

### UnsetBillingCycleType
`func (o *SubscriptionResource) UnsetBillingCycleType()`

UnsetBillingCycleType ensures that no value is present for BillingCycleType, not even an explicit nil
### GetBillingCycleAnchor

`func (o *SubscriptionResource) GetBillingCycleAnchor() time.Time`

GetBillingCycleAnchor returns the BillingCycleAnchor field if non-nil, zero value otherwise.

### GetBillingCycleAnchorOk

`func (o *SubscriptionResource) GetBillingCycleAnchorOk() (*time.Time, bool)`

GetBillingCycleAnchorOk returns a tuple with the BillingCycleAnchor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBillingCycleAnchor

`func (o *SubscriptionResource) SetBillingCycleAnchor(v time.Time)`

SetBillingCycleAnchor sets BillingCycleAnchor field to given value.

### HasBillingCycleAnchor

`func (o *SubscriptionResource) HasBillingCycleAnchor() bool`

HasBillingCycleAnchor returns a boolean if a field has been set.

### SetBillingCycleAnchorNil

`func (o *SubscriptionResource) SetBillingCycleAnchorNil(b bool)`

 SetBillingCycleAnchorNil sets the value for BillingCycleAnchor to be an explicit nil

### UnsetBillingCycleAnchor
`func (o *SubscriptionResource) UnsetBillingCycleAnchor()`

UnsetBillingCycleAnchor ensures that no value is present for BillingCycleAnchor, not even an explicit nil
### GetCheckBudget

`func (o *SubscriptionResource) GetCheckBudget() int32`

GetCheckBudget returns the CheckBudget field if non-nil, zero value otherwise.

### GetCheckBudgetOk

`func (o *SubscriptionResource) GetCheckBudgetOk() (*int32, bool)`

GetCheckBudgetOk returns a tuple with the CheckBudget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckBudget

`func (o *SubscriptionResource) SetCheckBudget(v int32)`

SetCheckBudget sets CheckBudget field to given value.

### HasCheckBudget

`func (o *SubscriptionResource) HasCheckBudget() bool`

HasCheckBudget returns a boolean if a field has been set.

### SetCheckBudgetNil

`func (o *SubscriptionResource) SetCheckBudgetNil(b bool)`

 SetCheckBudgetNil sets the value for CheckBudget to be an explicit nil

### UnsetCheckBudget
`func (o *SubscriptionResource) UnsetCheckBudget()`

UnsetCheckBudget ensures that no value is present for CheckBudget, not even an explicit nil
### GetChecksConsumed

`func (o *SubscriptionResource) GetChecksConsumed() int32`

GetChecksConsumed returns the ChecksConsumed field if non-nil, zero value otherwise.

### GetChecksConsumedOk

`func (o *SubscriptionResource) GetChecksConsumedOk() (*int32, bool)`

GetChecksConsumedOk returns a tuple with the ChecksConsumed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChecksConsumed

`func (o *SubscriptionResource) SetChecksConsumed(v int32)`

SetChecksConsumed sets ChecksConsumed field to given value.

### HasChecksConsumed

`func (o *SubscriptionResource) HasChecksConsumed() bool`

HasChecksConsumed returns a boolean if a field has been set.

### SetChecksConsumedNil

`func (o *SubscriptionResource) SetChecksConsumedNil(b bool)`

 SetChecksConsumedNil sets the value for ChecksConsumed to be an explicit nil

### UnsetChecksConsumed
`func (o *SubscriptionResource) UnsetChecksConsumed()`

UnsetChecksConsumed ensures that no value is present for ChecksConsumed, not even an explicit nil
### GetChecksAvailable

`func (o *SubscriptionResource) GetChecksAvailable() int32`

GetChecksAvailable returns the ChecksAvailable field if non-nil, zero value otherwise.

### GetChecksAvailableOk

`func (o *SubscriptionResource) GetChecksAvailableOk() (*int32, bool)`

GetChecksAvailableOk returns a tuple with the ChecksAvailable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChecksAvailable

`func (o *SubscriptionResource) SetChecksAvailable(v int32)`

SetChecksAvailable sets ChecksAvailable field to given value.

### HasChecksAvailable

`func (o *SubscriptionResource) HasChecksAvailable() bool`

HasChecksAvailable returns a boolean if a field has been set.

### SetChecksAvailableNil

`func (o *SubscriptionResource) SetChecksAvailableNil(b bool)`

 SetChecksAvailableNil sets the value for ChecksAvailable to be an explicit nil

### UnsetChecksAvailable
`func (o *SubscriptionResource) UnsetChecksAvailable()`

UnsetChecksAvailable ensures that no value is present for ChecksAvailable, not even an explicit nil
### GetNextResetAt

`func (o *SubscriptionResource) GetNextResetAt() time.Time`

GetNextResetAt returns the NextResetAt field if non-nil, zero value otherwise.

### GetNextResetAtOk

`func (o *SubscriptionResource) GetNextResetAtOk() (*time.Time, bool)`

GetNextResetAtOk returns a tuple with the NextResetAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextResetAt

`func (o *SubscriptionResource) SetNextResetAt(v time.Time)`

SetNextResetAt sets NextResetAt field to given value.

### HasNextResetAt

`func (o *SubscriptionResource) HasNextResetAt() bool`

HasNextResetAt returns a boolean if a field has been set.

### SetNextResetAtNil

`func (o *SubscriptionResource) SetNextResetAtNil(b bool)`

 SetNextResetAtNil sets the value for NextResetAt to be an explicit nil

### UnsetNextResetAt
`func (o *SubscriptionResource) UnsetNextResetAt()`

UnsetNextResetAt ensures that no value is present for NextResetAt, not even an explicit nil
### GetCancelledAt

`func (o *SubscriptionResource) GetCancelledAt() time.Time`

GetCancelledAt returns the CancelledAt field if non-nil, zero value otherwise.

### GetCancelledAtOk

`func (o *SubscriptionResource) GetCancelledAtOk() (*time.Time, bool)`

GetCancelledAtOk returns a tuple with the CancelledAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCancelledAt

`func (o *SubscriptionResource) SetCancelledAt(v time.Time)`

SetCancelledAt sets CancelledAt field to given value.

### HasCancelledAt

`func (o *SubscriptionResource) HasCancelledAt() bool`

HasCancelledAt returns a boolean if a field has been set.

### SetCancelledAtNil

`func (o *SubscriptionResource) SetCancelledAtNil(b bool)`

 SetCancelledAtNil sets the value for CancelledAt to be an explicit nil

### UnsetCancelledAt
`func (o *SubscriptionResource) UnsetCancelledAt()`

UnsetCancelledAt ensures that no value is present for CancelledAt, not even an explicit nil
### GetScheduledToCancelAt

`func (o *SubscriptionResource) GetScheduledToCancelAt() time.Time`

GetScheduledToCancelAt returns the ScheduledToCancelAt field if non-nil, zero value otherwise.

### GetScheduledToCancelAtOk

`func (o *SubscriptionResource) GetScheduledToCancelAtOk() (*time.Time, bool)`

GetScheduledToCancelAtOk returns a tuple with the ScheduledToCancelAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledToCancelAt

`func (o *SubscriptionResource) SetScheduledToCancelAt(v time.Time)`

SetScheduledToCancelAt sets ScheduledToCancelAt field to given value.

### HasScheduledToCancelAt

`func (o *SubscriptionResource) HasScheduledToCancelAt() bool`

HasScheduledToCancelAt returns a boolean if a field has been set.

### SetScheduledToCancelAtNil

`func (o *SubscriptionResource) SetScheduledToCancelAtNil(b bool)`

 SetScheduledToCancelAtNil sets the value for ScheduledToCancelAt to be an explicit nil

### UnsetScheduledToCancelAt
`func (o *SubscriptionResource) UnsetScheduledToCancelAt()`

UnsetScheduledToCancelAt ensures that no value is present for ScheduledToCancelAt, not even an explicit nil
### GetGracePeriodEndsAt

`func (o *SubscriptionResource) GetGracePeriodEndsAt() time.Time`

GetGracePeriodEndsAt returns the GracePeriodEndsAt field if non-nil, zero value otherwise.

### GetGracePeriodEndsAtOk

`func (o *SubscriptionResource) GetGracePeriodEndsAtOk() (*time.Time, bool)`

GetGracePeriodEndsAtOk returns a tuple with the GracePeriodEndsAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGracePeriodEndsAt

`func (o *SubscriptionResource) SetGracePeriodEndsAt(v time.Time)`

SetGracePeriodEndsAt sets GracePeriodEndsAt field to given value.

### HasGracePeriodEndsAt

`func (o *SubscriptionResource) HasGracePeriodEndsAt() bool`

HasGracePeriodEndsAt returns a boolean if a field has been set.

### SetGracePeriodEndsAtNil

`func (o *SubscriptionResource) SetGracePeriodEndsAtNil(b bool)`

 SetGracePeriodEndsAtNil sets the value for GracePeriodEndsAt to be an explicit nil

### UnsetGracePeriodEndsAt
`func (o *SubscriptionResource) UnsetGracePeriodEndsAt()`

UnsetGracePeriodEndsAt ensures that no value is present for GracePeriodEndsAt, not even an explicit nil
### GetDeactivationReason

`func (o *SubscriptionResource) GetDeactivationReason() string`

GetDeactivationReason returns the DeactivationReason field if non-nil, zero value otherwise.

### GetDeactivationReasonOk

`func (o *SubscriptionResource) GetDeactivationReasonOk() (*string, bool)`

GetDeactivationReasonOk returns a tuple with the DeactivationReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeactivationReason

`func (o *SubscriptionResource) SetDeactivationReason(v string)`

SetDeactivationReason sets DeactivationReason field to given value.

### HasDeactivationReason

`func (o *SubscriptionResource) HasDeactivationReason() bool`

HasDeactivationReason returns a boolean if a field has been set.

### SetDeactivationReasonNil

`func (o *SubscriptionResource) SetDeactivationReasonNil(b bool)`

 SetDeactivationReasonNil sets the value for DeactivationReason to be an explicit nil

### UnsetDeactivationReason
`func (o *SubscriptionResource) UnsetDeactivationReason()`

UnsetDeactivationReason ensures that no value is present for DeactivationReason, not even an explicit nil
### GetIsEntitled

`func (o *SubscriptionResource) GetIsEntitled() bool`

GetIsEntitled returns the IsEntitled field if non-nil, zero value otherwise.

### GetIsEntitledOk

`func (o *SubscriptionResource) GetIsEntitledOk() (*bool, bool)`

GetIsEntitledOk returns a tuple with the IsEntitled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsEntitled

`func (o *SubscriptionResource) SetIsEntitled(v bool)`

SetIsEntitled sets IsEntitled field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


