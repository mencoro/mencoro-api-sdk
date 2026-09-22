# ListAiResponses200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | Pointer to [**[]AiResponseResource**](AiResponseResource.md) |  | [optional] 
**Total** | Pointer to **int32** | Captures matching the filter, not the size of this page | [optional] 

## Methods

### NewListAiResponses200Response

`func NewListAiResponses200Response() *ListAiResponses200Response`

NewListAiResponses200Response instantiates a new ListAiResponses200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListAiResponses200ResponseWithDefaults

`func NewListAiResponses200ResponseWithDefaults() *ListAiResponses200Response`

NewListAiResponses200ResponseWithDefaults instantiates a new ListAiResponses200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListAiResponses200Response) GetItems() []AiResponseResource`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListAiResponses200Response) GetItemsOk() (*[]AiResponseResource, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListAiResponses200Response) SetItems(v []AiResponseResource)`

SetItems sets Items field to given value.

### HasItems

`func (o *ListAiResponses200Response) HasItems() bool`

HasItems returns a boolean if a field has been set.

### GetTotal

`func (o *ListAiResponses200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListAiResponses200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListAiResponses200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *ListAiResponses200Response) HasTotal() bool`

HasTotal returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


