# ListSearchSnapshots200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | Pointer to [**[]SearchSnapshotResource**](SearchSnapshotResource.md) |  | [optional] 
**Total** | Pointer to **int32** | Captures matching the filter, not the size of this page | [optional] 

## Methods

### NewListSearchSnapshots200Response

`func NewListSearchSnapshots200Response() *ListSearchSnapshots200Response`

NewListSearchSnapshots200Response instantiates a new ListSearchSnapshots200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListSearchSnapshots200ResponseWithDefaults

`func NewListSearchSnapshots200ResponseWithDefaults() *ListSearchSnapshots200Response`

NewListSearchSnapshots200ResponseWithDefaults instantiates a new ListSearchSnapshots200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListSearchSnapshots200Response) GetItems() []SearchSnapshotResource`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListSearchSnapshots200Response) GetItemsOk() (*[]SearchSnapshotResource, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListSearchSnapshots200Response) SetItems(v []SearchSnapshotResource)`

SetItems sets Items field to given value.

### HasItems

`func (o *ListSearchSnapshots200Response) HasItems() bool`

HasItems returns a boolean if a field has been set.

### GetTotal

`func (o *ListSearchSnapshots200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListSearchSnapshots200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListSearchSnapshots200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *ListSearchSnapshots200Response) HasTotal() bool`

HasTotal returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


