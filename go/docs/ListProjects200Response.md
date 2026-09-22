# ListProjects200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | Pointer to [**[]ProjectResource**](ProjectResource.md) |  | [optional] 
**Total** | Pointer to **int32** | Every project matching the filters, not the size of this page. | [optional] 

## Methods

### NewListProjects200Response

`func NewListProjects200Response() *ListProjects200Response`

NewListProjects200Response instantiates a new ListProjects200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListProjects200ResponseWithDefaults

`func NewListProjects200ResponseWithDefaults() *ListProjects200Response`

NewListProjects200ResponseWithDefaults instantiates a new ListProjects200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListProjects200Response) GetItems() []ProjectResource`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListProjects200Response) GetItemsOk() (*[]ProjectResource, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListProjects200Response) SetItems(v []ProjectResource)`

SetItems sets Items field to given value.

### HasItems

`func (o *ListProjects200Response) HasItems() bool`

HasItems returns a boolean if a field has been set.

### GetTotal

`func (o *ListProjects200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListProjects200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListProjects200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *ListProjects200Response) HasTotal() bool`

HasTotal returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


