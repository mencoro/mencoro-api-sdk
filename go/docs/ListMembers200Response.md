# ListMembers200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | Pointer to [**[]MemberResource**](MemberResource.md) |  | [optional] 
**Total** | Pointer to **int32** |  | [optional] 

## Methods

### NewListMembers200Response

`func NewListMembers200Response() *ListMembers200Response`

NewListMembers200Response instantiates a new ListMembers200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListMembers200ResponseWithDefaults

`func NewListMembers200ResponseWithDefaults() *ListMembers200Response`

NewListMembers200ResponseWithDefaults instantiates a new ListMembers200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListMembers200Response) GetItems() []MemberResource`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListMembers200Response) GetItemsOk() (*[]MemberResource, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListMembers200Response) SetItems(v []MemberResource)`

SetItems sets Items field to given value.

### HasItems

`func (o *ListMembers200Response) HasItems() bool`

HasItems returns a boolean if a field has been set.

### GetTotal

`func (o *ListMembers200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListMembers200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListMembers200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *ListMembers200Response) HasTotal() bool`

HasTotal returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


