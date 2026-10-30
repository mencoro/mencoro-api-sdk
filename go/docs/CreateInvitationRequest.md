# CreateInvitationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Email** | Pointer to **string** |  | [optional] 
**Role** | Pointer to **string** |  | [optional] [default to "viewer"]
**ProjectAccess** | Pointer to [**NullableCreateInvitationRequestProjectAccess**](CreateInvitationRequestProjectAccess.md) |  | [optional] 

## Methods

### NewCreateInvitationRequest

`func NewCreateInvitationRequest() *CreateInvitationRequest`

NewCreateInvitationRequest instantiates a new CreateInvitationRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateInvitationRequestWithDefaults

`func NewCreateInvitationRequestWithDefaults() *CreateInvitationRequest`

NewCreateInvitationRequestWithDefaults instantiates a new CreateInvitationRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEmail

`func (o *CreateInvitationRequest) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *CreateInvitationRequest) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *CreateInvitationRequest) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *CreateInvitationRequest) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetRole

`func (o *CreateInvitationRequest) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *CreateInvitationRequest) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *CreateInvitationRequest) SetRole(v string)`

SetRole sets Role field to given value.

### HasRole

`func (o *CreateInvitationRequest) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetProjectAccess

`func (o *CreateInvitationRequest) GetProjectAccess() CreateInvitationRequestProjectAccess`

GetProjectAccess returns the ProjectAccess field if non-nil, zero value otherwise.

### GetProjectAccessOk

`func (o *CreateInvitationRequest) GetProjectAccessOk() (*CreateInvitationRequestProjectAccess, bool)`

GetProjectAccessOk returns a tuple with the ProjectAccess field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectAccess

`func (o *CreateInvitationRequest) SetProjectAccess(v CreateInvitationRequestProjectAccess)`

SetProjectAccess sets ProjectAccess field to given value.

### HasProjectAccess

`func (o *CreateInvitationRequest) HasProjectAccess() bool`

HasProjectAccess returns a boolean if a field has been set.

### SetProjectAccessNil

`func (o *CreateInvitationRequest) SetProjectAccessNil(b bool)`

 SetProjectAccessNil sets the value for ProjectAccess to be an explicit nil

### UnsetProjectAccess
`func (o *CreateInvitationRequest) UnsetProjectAccess()`

UnsetProjectAccess ensures that no value is present for ProjectAccess, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


