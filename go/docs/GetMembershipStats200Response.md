# GetMembershipStats200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActiveMembersCount** | Pointer to **int32** | Members in the active state. | [optional] 
**SuspendedMembersCount** | Pointer to **int32** | Members in the suspended state. | [optional] 
**TotalMembersCount** | Pointer to **int32** | Every membership record, suspended ones included. | [optional] 
**ActiveProjectsCount** | Pointer to **int32** | Projects in the active state. | [optional] 
**TotalProjectsCount** | Pointer to **int32** | Every project, archived ones included. | [optional] 
**PendingInvitationsCount** | Pointer to **int32** | Invitations still pending and not yet expired. | [optional] 
**ComputedAt** | Pointer to **string** | When the snapshot was computed. A database timestamp, not an ISO-8601 instant. | [optional] 

## Methods

### NewGetMembershipStats200Response

`func NewGetMembershipStats200Response() *GetMembershipStats200Response`

NewGetMembershipStats200Response instantiates a new GetMembershipStats200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetMembershipStats200ResponseWithDefaults

`func NewGetMembershipStats200ResponseWithDefaults() *GetMembershipStats200Response`

NewGetMembershipStats200ResponseWithDefaults instantiates a new GetMembershipStats200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActiveMembersCount

`func (o *GetMembershipStats200Response) GetActiveMembersCount() int32`

GetActiveMembersCount returns the ActiveMembersCount field if non-nil, zero value otherwise.

### GetActiveMembersCountOk

`func (o *GetMembershipStats200Response) GetActiveMembersCountOk() (*int32, bool)`

GetActiveMembersCountOk returns a tuple with the ActiveMembersCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActiveMembersCount

`func (o *GetMembershipStats200Response) SetActiveMembersCount(v int32)`

SetActiveMembersCount sets ActiveMembersCount field to given value.

### HasActiveMembersCount

`func (o *GetMembershipStats200Response) HasActiveMembersCount() bool`

HasActiveMembersCount returns a boolean if a field has been set.

### GetSuspendedMembersCount

`func (o *GetMembershipStats200Response) GetSuspendedMembersCount() int32`

GetSuspendedMembersCount returns the SuspendedMembersCount field if non-nil, zero value otherwise.

### GetSuspendedMembersCountOk

`func (o *GetMembershipStats200Response) GetSuspendedMembersCountOk() (*int32, bool)`

GetSuspendedMembersCountOk returns a tuple with the SuspendedMembersCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuspendedMembersCount

`func (o *GetMembershipStats200Response) SetSuspendedMembersCount(v int32)`

SetSuspendedMembersCount sets SuspendedMembersCount field to given value.

### HasSuspendedMembersCount

`func (o *GetMembershipStats200Response) HasSuspendedMembersCount() bool`

HasSuspendedMembersCount returns a boolean if a field has been set.

### GetTotalMembersCount

`func (o *GetMembershipStats200Response) GetTotalMembersCount() int32`

GetTotalMembersCount returns the TotalMembersCount field if non-nil, zero value otherwise.

### GetTotalMembersCountOk

`func (o *GetMembershipStats200Response) GetTotalMembersCountOk() (*int32, bool)`

GetTotalMembersCountOk returns a tuple with the TotalMembersCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalMembersCount

`func (o *GetMembershipStats200Response) SetTotalMembersCount(v int32)`

SetTotalMembersCount sets TotalMembersCount field to given value.

### HasTotalMembersCount

`func (o *GetMembershipStats200Response) HasTotalMembersCount() bool`

HasTotalMembersCount returns a boolean if a field has been set.

### GetActiveProjectsCount

`func (o *GetMembershipStats200Response) GetActiveProjectsCount() int32`

GetActiveProjectsCount returns the ActiveProjectsCount field if non-nil, zero value otherwise.

### GetActiveProjectsCountOk

`func (o *GetMembershipStats200Response) GetActiveProjectsCountOk() (*int32, bool)`

GetActiveProjectsCountOk returns a tuple with the ActiveProjectsCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActiveProjectsCount

`func (o *GetMembershipStats200Response) SetActiveProjectsCount(v int32)`

SetActiveProjectsCount sets ActiveProjectsCount field to given value.

### HasActiveProjectsCount

`func (o *GetMembershipStats200Response) HasActiveProjectsCount() bool`

HasActiveProjectsCount returns a boolean if a field has been set.

### GetTotalProjectsCount

`func (o *GetMembershipStats200Response) GetTotalProjectsCount() int32`

GetTotalProjectsCount returns the TotalProjectsCount field if non-nil, zero value otherwise.

### GetTotalProjectsCountOk

`func (o *GetMembershipStats200Response) GetTotalProjectsCountOk() (*int32, bool)`

GetTotalProjectsCountOk returns a tuple with the TotalProjectsCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalProjectsCount

`func (o *GetMembershipStats200Response) SetTotalProjectsCount(v int32)`

SetTotalProjectsCount sets TotalProjectsCount field to given value.

### HasTotalProjectsCount

`func (o *GetMembershipStats200Response) HasTotalProjectsCount() bool`

HasTotalProjectsCount returns a boolean if a field has been set.

### GetPendingInvitationsCount

`func (o *GetMembershipStats200Response) GetPendingInvitationsCount() int32`

GetPendingInvitationsCount returns the PendingInvitationsCount field if non-nil, zero value otherwise.

### GetPendingInvitationsCountOk

`func (o *GetMembershipStats200Response) GetPendingInvitationsCountOk() (*int32, bool)`

GetPendingInvitationsCountOk returns a tuple with the PendingInvitationsCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPendingInvitationsCount

`func (o *GetMembershipStats200Response) SetPendingInvitationsCount(v int32)`

SetPendingInvitationsCount sets PendingInvitationsCount field to given value.

### HasPendingInvitationsCount

`func (o *GetMembershipStats200Response) HasPendingInvitationsCount() bool`

HasPendingInvitationsCount returns a boolean if a field has been set.

### GetComputedAt

`func (o *GetMembershipStats200Response) GetComputedAt() string`

GetComputedAt returns the ComputedAt field if non-nil, zero value otherwise.

### GetComputedAtOk

`func (o *GetMembershipStats200Response) GetComputedAtOk() (*string, bool)`

GetComputedAtOk returns a tuple with the ComputedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComputedAt

`func (o *GetMembershipStats200Response) SetComputedAt(v string)`

SetComputedAt sets ComputedAt field to given value.

### HasComputedAt

`func (o *GetMembershipStats200Response) HasComputedAt() bool`

HasComputedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


