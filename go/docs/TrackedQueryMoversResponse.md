# TrackedQueryMoversResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Rows** | [**[]TrackedQueryMoverRow**](TrackedQueryMoverRow.md) |  | 
**Total** | **int32** |  | 
**DataDirtySince** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewTrackedQueryMoversResponse

`func NewTrackedQueryMoversResponse(rows []TrackedQueryMoverRow, total int32, ) *TrackedQueryMoversResponse`

NewTrackedQueryMoversResponse instantiates a new TrackedQueryMoversResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrackedQueryMoversResponseWithDefaults

`func NewTrackedQueryMoversResponseWithDefaults() *TrackedQueryMoversResponse`

NewTrackedQueryMoversResponseWithDefaults instantiates a new TrackedQueryMoversResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRows

`func (o *TrackedQueryMoversResponse) GetRows() []TrackedQueryMoverRow`

GetRows returns the Rows field if non-nil, zero value otherwise.

### GetRowsOk

`func (o *TrackedQueryMoversResponse) GetRowsOk() (*[]TrackedQueryMoverRow, bool)`

GetRowsOk returns a tuple with the Rows field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRows

`func (o *TrackedQueryMoversResponse) SetRows(v []TrackedQueryMoverRow)`

SetRows sets Rows field to given value.


### GetTotal

`func (o *TrackedQueryMoversResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *TrackedQueryMoversResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *TrackedQueryMoversResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetDataDirtySince

`func (o *TrackedQueryMoversResponse) GetDataDirtySince() string`

GetDataDirtySince returns the DataDirtySince field if non-nil, zero value otherwise.

### GetDataDirtySinceOk

`func (o *TrackedQueryMoversResponse) GetDataDirtySinceOk() (*string, bool)`

GetDataDirtySinceOk returns a tuple with the DataDirtySince field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataDirtySince

`func (o *TrackedQueryMoversResponse) SetDataDirtySince(v string)`

SetDataDirtySince sets DataDirtySince field to given value.

### HasDataDirtySince

`func (o *TrackedQueryMoversResponse) HasDataDirtySince() bool`

HasDataDirtySince returns a boolean if a field has been set.

### SetDataDirtySinceNil

`func (o *TrackedQueryMoversResponse) SetDataDirtySinceNil(b bool)`

 SetDataDirtySinceNil sets the value for DataDirtySince to be an explicit nil

### UnsetDataDirtySince
`func (o *TrackedQueryMoversResponse) UnsetDataDirtySince()`

UnsetDataDirtySince ensures that no value is present for DataDirtySince, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


