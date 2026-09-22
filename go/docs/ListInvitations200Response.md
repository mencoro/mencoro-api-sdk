# ListInvitations200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | Pointer to [**[]InvitationResource**](InvitationResource.md) |  | [optional] 
**Total** | Pointer to **int32** |  | [optional] 

## Methods

### NewListInvitations200Response

`func NewListInvitations200Response() *ListInvitations200Response`

NewListInvitations200Response instantiates a new ListInvitations200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListInvitations200ResponseWithDefaults

`func NewListInvitations200ResponseWithDefaults() *ListInvitations200Response`

NewListInvitations200ResponseWithDefaults instantiates a new ListInvitations200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListInvitations200Response) GetItems() []InvitationResource`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListInvitations200Response) GetItemsOk() (*[]InvitationResource, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListInvitations200Response) SetItems(v []InvitationResource)`

SetItems sets Items field to given value.

### HasItems

`func (o *ListInvitations200Response) HasItems() bool`

HasItems returns a boolean if a field has been set.

### GetTotal

`func (o *ListInvitations200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListInvitations200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListInvitations200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *ListInvitations200Response) HasTotal() bool`

HasTotal returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


