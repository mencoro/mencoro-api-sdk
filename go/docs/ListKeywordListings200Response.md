# ListKeywordListings200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | Pointer to [**[]KeywordListingResource**](KeywordListingResource.md) |  | [optional] 
**Total** | Pointer to **int32** | Keywords matching the filters, not the size of this page. | [optional] 
**TotalVariantCount** | Pointer to **int32** | Tracked queries behind the keywords matching every filter EXCEPT &#x60;search&#x60;. With a text search applied this still counts the whole project, so it is not a budget figure for a searched page. | [optional] 
**DataDirtySince** | Pointer to **NullableTime** | When a pending recalculation was triggered. Null when the metrics are up to date. | [optional] 

## Methods

### NewListKeywordListings200Response

`func NewListKeywordListings200Response() *ListKeywordListings200Response`

NewListKeywordListings200Response instantiates a new ListKeywordListings200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListKeywordListings200ResponseWithDefaults

`func NewListKeywordListings200ResponseWithDefaults() *ListKeywordListings200Response`

NewListKeywordListings200ResponseWithDefaults instantiates a new ListKeywordListings200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ListKeywordListings200Response) GetItems() []KeywordListingResource`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ListKeywordListings200Response) GetItemsOk() (*[]KeywordListingResource, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ListKeywordListings200Response) SetItems(v []KeywordListingResource)`

SetItems sets Items field to given value.

### HasItems

`func (o *ListKeywordListings200Response) HasItems() bool`

HasItems returns a boolean if a field has been set.

### GetTotal

`func (o *ListKeywordListings200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListKeywordListings200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListKeywordListings200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *ListKeywordListings200Response) HasTotal() bool`

HasTotal returns a boolean if a field has been set.

### GetTotalVariantCount

`func (o *ListKeywordListings200Response) GetTotalVariantCount() int32`

GetTotalVariantCount returns the TotalVariantCount field if non-nil, zero value otherwise.

### GetTotalVariantCountOk

`func (o *ListKeywordListings200Response) GetTotalVariantCountOk() (*int32, bool)`

GetTotalVariantCountOk returns a tuple with the TotalVariantCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalVariantCount

`func (o *ListKeywordListings200Response) SetTotalVariantCount(v int32)`

SetTotalVariantCount sets TotalVariantCount field to given value.

### HasTotalVariantCount

`func (o *ListKeywordListings200Response) HasTotalVariantCount() bool`

HasTotalVariantCount returns a boolean if a field has been set.

### GetDataDirtySince

`func (o *ListKeywordListings200Response) GetDataDirtySince() time.Time`

GetDataDirtySince returns the DataDirtySince field if non-nil, zero value otherwise.

### GetDataDirtySinceOk

`func (o *ListKeywordListings200Response) GetDataDirtySinceOk() (*time.Time, bool)`

GetDataDirtySinceOk returns a tuple with the DataDirtySince field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataDirtySince

`func (o *ListKeywordListings200Response) SetDataDirtySince(v time.Time)`

SetDataDirtySince sets DataDirtySince field to given value.

### HasDataDirtySince

`func (o *ListKeywordListings200Response) HasDataDirtySince() bool`

HasDataDirtySince returns a boolean if a field has been set.

### SetDataDirtySinceNil

`func (o *ListKeywordListings200Response) SetDataDirtySinceNil(b bool)`

 SetDataDirtySinceNil sets the value for DataDirtySince to be an explicit nil

### UnsetDataDirtySince
`func (o *ListKeywordListings200Response) UnsetDataDirtySince()`

UnsetDataDirtySince ensures that no value is present for DataDirtySince, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


