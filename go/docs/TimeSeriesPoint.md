# TimeSeriesPoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RawDate** | **string** |  | 
**Brand** | [**PerEntityMetrics**](PerEntityMetrics.md) |  | 
**Competitors** | [**map[string]PerEntityMetrics**](PerEntityMetrics.md) |  | 

## Methods

### NewTimeSeriesPoint

`func NewTimeSeriesPoint(rawDate string, brand PerEntityMetrics, competitors map[string]PerEntityMetrics, ) *TimeSeriesPoint`

NewTimeSeriesPoint instantiates a new TimeSeriesPoint object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTimeSeriesPointWithDefaults

`func NewTimeSeriesPointWithDefaults() *TimeSeriesPoint`

NewTimeSeriesPointWithDefaults instantiates a new TimeSeriesPoint object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRawDate

`func (o *TimeSeriesPoint) GetRawDate() string`

GetRawDate returns the RawDate field if non-nil, zero value otherwise.

### GetRawDateOk

`func (o *TimeSeriesPoint) GetRawDateOk() (*string, bool)`

GetRawDateOk returns a tuple with the RawDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRawDate

`func (o *TimeSeriesPoint) SetRawDate(v string)`

SetRawDate sets RawDate field to given value.


### GetBrand

`func (o *TimeSeriesPoint) GetBrand() PerEntityMetrics`

GetBrand returns the Brand field if non-nil, zero value otherwise.

### GetBrandOk

`func (o *TimeSeriesPoint) GetBrandOk() (*PerEntityMetrics, bool)`

GetBrandOk returns a tuple with the Brand field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrand

`func (o *TimeSeriesPoint) SetBrand(v PerEntityMetrics)`

SetBrand sets Brand field to given value.


### GetCompetitors

`func (o *TimeSeriesPoint) GetCompetitors() map[string]PerEntityMetrics`

GetCompetitors returns the Competitors field if non-nil, zero value otherwise.

### GetCompetitorsOk

`func (o *TimeSeriesPoint) GetCompetitorsOk() (*map[string]PerEntityMetrics, bool)`

GetCompetitorsOk returns a tuple with the Competitors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitors

`func (o *TimeSeriesPoint) SetCompetitors(v map[string]PerEntityMetrics)`

SetCompetitors sets Competitors field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


