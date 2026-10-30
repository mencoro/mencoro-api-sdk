# CreateInvitationRequestProjectAccess

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Mode** | **string** |  | 
**ProjectIds** | Pointer to **[]string** | For selected: at least one and at most 500 projects of the organization. | [optional] 

## Methods

### NewCreateInvitationRequestProjectAccess

`func NewCreateInvitationRequestProjectAccess(mode string, ) *CreateInvitationRequestProjectAccess`

NewCreateInvitationRequestProjectAccess instantiates a new CreateInvitationRequestProjectAccess object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateInvitationRequestProjectAccessWithDefaults

`func NewCreateInvitationRequestProjectAccessWithDefaults() *CreateInvitationRequestProjectAccess`

NewCreateInvitationRequestProjectAccessWithDefaults instantiates a new CreateInvitationRequestProjectAccess object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMode

`func (o *CreateInvitationRequestProjectAccess) GetMode() string`

GetMode returns the Mode field if non-nil, zero value otherwise.

### GetModeOk

`func (o *CreateInvitationRequestProjectAccess) GetModeOk() (*string, bool)`

GetModeOk returns a tuple with the Mode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMode

`func (o *CreateInvitationRequestProjectAccess) SetMode(v string)`

SetMode sets Mode field to given value.


### GetProjectIds

`func (o *CreateInvitationRequestProjectAccess) GetProjectIds() []string`

GetProjectIds returns the ProjectIds field if non-nil, zero value otherwise.

### GetProjectIdsOk

`func (o *CreateInvitationRequestProjectAccess) GetProjectIdsOk() (*[]string, bool)`

GetProjectIdsOk returns a tuple with the ProjectIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectIds

`func (o *CreateInvitationRequestProjectAccess) SetProjectIds(v []string)`

SetProjectIds sets ProjectIds field to given value.

### HasProjectIds

`func (o *CreateInvitationRequestProjectAccess) HasProjectIds() bool`

HasProjectIds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


