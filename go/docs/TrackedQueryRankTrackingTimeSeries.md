# TrackedQueryRankTrackingTimeSeries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Points** | [**[]TimeSeriesPoint**](TimeSeriesPoint.md) |  | 
**DataDirtySince** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewTrackedQueryRankTrackingTimeSeries

`func NewTrackedQueryRankTrackingTimeSeries(points []TimeSeriesPoint, ) *TrackedQueryRankTrackingTimeSeries`

NewTrackedQueryRankTrackingTimeSeries instantiates a new TrackedQueryRankTrackingTimeSeries object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrackedQueryRankTrackingTimeSeriesWithDefaults

`func NewTrackedQueryRankTrackingTimeSeriesWithDefaults() *TrackedQueryRankTrackingTimeSeries`

NewTrackedQueryRankTrackingTimeSeriesWithDefaults instantiates a new TrackedQueryRankTrackingTimeSeries object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPoints

`func (o *TrackedQueryRankTrackingTimeSeries) GetPoints() []TimeSeriesPoint`

GetPoints returns the Points field if non-nil, zero value otherwise.

### GetPointsOk

`func (o *TrackedQueryRankTrackingTimeSeries) GetPointsOk() (*[]TimeSeriesPoint, bool)`

GetPointsOk returns a tuple with the Points field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPoints

`func (o *TrackedQueryRankTrackingTimeSeries) SetPoints(v []TimeSeriesPoint)`

SetPoints sets Points field to given value.


### GetDataDirtySince

`func (o *TrackedQueryRankTrackingTimeSeries) GetDataDirtySince() string`

GetDataDirtySince returns the DataDirtySince field if non-nil, zero value otherwise.

### GetDataDirtySinceOk

`func (o *TrackedQueryRankTrackingTimeSeries) GetDataDirtySinceOk() (*string, bool)`

GetDataDirtySinceOk returns a tuple with the DataDirtySince field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataDirtySince

`func (o *TrackedQueryRankTrackingTimeSeries) SetDataDirtySince(v string)`

SetDataDirtySince sets DataDirtySince field to given value.

### HasDataDirtySince

`func (o *TrackedQueryRankTrackingTimeSeries) HasDataDirtySince() bool`

HasDataDirtySince returns a boolean if a field has been set.

### SetDataDirtySinceNil

`func (o *TrackedQueryRankTrackingTimeSeries) SetDataDirtySinceNil(b bool)`

 SetDataDirtySinceNil sets the value for DataDirtySince to be an explicit nil

### UnsetDataDirtySince
`func (o *TrackedQueryRankTrackingTimeSeries) UnsetDataDirtySince()`

UnsetDataDirtySince ensures that no value is present for DataDirtySince, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


