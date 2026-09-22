# MemberResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**UserId** | **string** | The user this membership belongs to | 
**Role** | **string** |  | 
**State** | **string** |  | 
**IsActive** | **bool** |  | 
**JoinedAt** | **time.Time** |  | 

## Methods

### NewMemberResource

`func NewMemberResource(id string, userId string, role string, state string, isActive bool, joinedAt time.Time, ) *MemberResource`

NewMemberResource instantiates a new MemberResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMemberResourceWithDefaults

`func NewMemberResourceWithDefaults() *MemberResource`

NewMemberResourceWithDefaults instantiates a new MemberResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *MemberResource) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *MemberResource) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *MemberResource) SetId(v string)`

SetId sets Id field to given value.


### GetUserId

`func (o *MemberResource) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *MemberResource) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *MemberResource) SetUserId(v string)`

SetUserId sets UserId field to given value.


### GetRole

`func (o *MemberResource) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *MemberResource) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *MemberResource) SetRole(v string)`

SetRole sets Role field to given value.


### GetState

`func (o *MemberResource) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *MemberResource) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *MemberResource) SetState(v string)`

SetState sets State field to given value.


### GetIsActive

`func (o *MemberResource) GetIsActive() bool`

GetIsActive returns the IsActive field if non-nil, zero value otherwise.

### GetIsActiveOk

`func (o *MemberResource) GetIsActiveOk() (*bool, bool)`

GetIsActiveOk returns a tuple with the IsActive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsActive

`func (o *MemberResource) SetIsActive(v bool)`

SetIsActive sets IsActive field to given value.


### GetJoinedAt

`func (o *MemberResource) GetJoinedAt() time.Time`

GetJoinedAt returns the JoinedAt field if non-nil, zero value otherwise.

### GetJoinedAtOk

`func (o *MemberResource) GetJoinedAtOk() (*time.Time, bool)`

GetJoinedAtOk returns a tuple with the JoinedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJoinedAt

`func (o *MemberResource) SetJoinedAt(v time.Time)`

SetJoinedAt sets JoinedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


