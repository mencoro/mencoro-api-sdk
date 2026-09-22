# ListCompetitors200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | Pointer to [**[]CompetitorResource**](CompetitorResource.md) |  | [optional] 
**Total** | Pointer to **int32** | Number of competitors configured on the project | [optional] 

## Methods

### NewListCompetitors200Response

`func NewListCompetitors200Response() *ListCompetitors200Response`

NewListCompetitors200Response instantiates a new ListCompetitors200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListCompetitors200ResponseWithDefaults

`func NewListCompetitors200ResponseWithDefaults() *ListCompetitors200Response`

NewListCompetitors200ResponseWithDefaults instantiates a new ListCompetitors200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListCompetitors200Response) GetItems() []CompetitorResource`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListCompetitors200Response) GetItemsOk() (*[]CompetitorResource, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListCompetitors200Response) SetItems(v []CompetitorResource)`

SetItems sets Items field to given value.

### HasItems

`func (o *ListCompetitors200Response) HasItems() bool`

HasItems returns a boolean if a field has been set.

### GetTotal

`func (o *ListCompetitors200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListCompetitors200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListCompetitors200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *ListCompetitors200Response) HasTotal() bool`

HasTotal returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


