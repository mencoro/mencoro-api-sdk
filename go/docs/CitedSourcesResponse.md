# CitedSourcesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Sources** | [**[]CitedSourceRow**](CitedSourceRow.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewCitedSourcesResponse

`func NewCitedSourcesResponse(sources []CitedSourceRow, total int32, ) *CitedSourcesResponse`

NewCitedSourcesResponse instantiates a new CitedSourcesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCitedSourcesResponseWithDefaults

`func NewCitedSourcesResponseWithDefaults() *CitedSourcesResponse`

NewCitedSourcesResponseWithDefaults instantiates a new CitedSourcesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSources

`func (o *CitedSourcesResponse) GetSources() []CitedSourceRow`

GetSources returns the Sources field if non-nil, zero value otherwise.

### GetSourcesOk

`func (o *CitedSourcesResponse) GetSourcesOk() (*[]CitedSourceRow, bool)`

GetSourcesOk returns a tuple with the Sources field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSources

`func (o *CitedSourcesResponse) SetSources(v []CitedSourceRow)`

SetSources sets Sources field to given value.


### GetTotal

`func (o *CitedSourcesResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *CitedSourcesResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *CitedSourcesResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


