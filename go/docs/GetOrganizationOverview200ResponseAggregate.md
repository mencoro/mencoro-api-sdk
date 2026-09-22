# GetOrganizationOverview200ResponseAggregate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectCount** | Pointer to **int32** | Active projects in the organization, the length of &#x60;projects&#x60;. | [optional] 
**ProjectsWithData** | Pointer to **int32** | How many of those have a share of voice; the averages below are means over the projects that report each metric, never over the ones still null. | [optional] 
**TotalTrackedQueries** | Pointer to **int32** |  | [optional] 
**AvgShareOfVoice** | Pointer to **NullableFloat32** | Null when no project reports a share of voice. | [optional] 
**AvgMentionRate** | Pointer to **NullableInt32** |  | [optional] 
**AvgMentionPosition** | Pointer to **NullableFloat32** | 1-based rank; LOWER is better. | [optional] 
**AvgPositivityIndex** | Pointer to **NullableInt32** |  | [optional] 

## Methods

### NewGetOrganizationOverview200ResponseAggregate

`func NewGetOrganizationOverview200ResponseAggregate() *GetOrganizationOverview200ResponseAggregate`

NewGetOrganizationOverview200ResponseAggregate instantiates a new GetOrganizationOverview200ResponseAggregate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetOrganizationOverview200ResponseAggregateWithDefaults

`func NewGetOrganizationOverview200ResponseAggregateWithDefaults() *GetOrganizationOverview200ResponseAggregate`

NewGetOrganizationOverview200ResponseAggregateWithDefaults instantiates a new GetOrganizationOverview200ResponseAggregate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjectCount

`func (o *GetOrganizationOverview200ResponseAggregate) GetProjectCount() int32`

GetProjectCount returns the ProjectCount field if non-nil, zero value otherwise.

### GetProjectCountOk

`func (o *GetOrganizationOverview200ResponseAggregate) GetProjectCountOk() (*int32, bool)`

GetProjectCountOk returns a tuple with the ProjectCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectCount

`func (o *GetOrganizationOverview200ResponseAggregate) SetProjectCount(v int32)`

SetProjectCount sets ProjectCount field to given value.

### HasProjectCount

`func (o *GetOrganizationOverview200ResponseAggregate) HasProjectCount() bool`

HasProjectCount returns a boolean if a field has been set.

### GetProjectsWithData

`func (o *GetOrganizationOverview200ResponseAggregate) GetProjectsWithData() int32`

GetProjectsWithData returns the ProjectsWithData field if non-nil, zero value otherwise.

### GetProjectsWithDataOk

`func (o *GetOrganizationOverview200ResponseAggregate) GetProjectsWithDataOk() (*int32, bool)`

GetProjectsWithDataOk returns a tuple with the ProjectsWithData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectsWithData

`func (o *GetOrganizationOverview200ResponseAggregate) SetProjectsWithData(v int32)`

SetProjectsWithData sets ProjectsWithData field to given value.

### HasProjectsWithData

`func (o *GetOrganizationOverview200ResponseAggregate) HasProjectsWithData() bool`

HasProjectsWithData returns a boolean if a field has been set.

### GetTotalTrackedQueries

`func (o *GetOrganizationOverview200ResponseAggregate) GetTotalTrackedQueries() int32`

GetTotalTrackedQueries returns the TotalTrackedQueries field if non-nil, zero value otherwise.

### GetTotalTrackedQueriesOk

`func (o *GetOrganizationOverview200ResponseAggregate) GetTotalTrackedQueriesOk() (*int32, bool)`

GetTotalTrackedQueriesOk returns a tuple with the TotalTrackedQueries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalTrackedQueries

`func (o *GetOrganizationOverview200ResponseAggregate) SetTotalTrackedQueries(v int32)`

SetTotalTrackedQueries sets TotalTrackedQueries field to given value.

### HasTotalTrackedQueries

`func (o *GetOrganizationOverview200ResponseAggregate) HasTotalTrackedQueries() bool`

HasTotalTrackedQueries returns a boolean if a field has been set.

### GetAvgShareOfVoice

`func (o *GetOrganizationOverview200ResponseAggregate) GetAvgShareOfVoice() float32`

GetAvgShareOfVoice returns the AvgShareOfVoice field if non-nil, zero value otherwise.

### GetAvgShareOfVoiceOk

`func (o *GetOrganizationOverview200ResponseAggregate) GetAvgShareOfVoiceOk() (*float32, bool)`

GetAvgShareOfVoiceOk returns a tuple with the AvgShareOfVoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgShareOfVoice

`func (o *GetOrganizationOverview200ResponseAggregate) SetAvgShareOfVoice(v float32)`

SetAvgShareOfVoice sets AvgShareOfVoice field to given value.

### HasAvgShareOfVoice

`func (o *GetOrganizationOverview200ResponseAggregate) HasAvgShareOfVoice() bool`

HasAvgShareOfVoice returns a boolean if a field has been set.

### SetAvgShareOfVoiceNil

`func (o *GetOrganizationOverview200ResponseAggregate) SetAvgShareOfVoiceNil(b bool)`

 SetAvgShareOfVoiceNil sets the value for AvgShareOfVoice to be an explicit nil

### UnsetAvgShareOfVoice
`func (o *GetOrganizationOverview200ResponseAggregate) UnsetAvgShareOfVoice()`

UnsetAvgShareOfVoice ensures that no value is present for AvgShareOfVoice, not even an explicit nil
### GetAvgMentionRate

`func (o *GetOrganizationOverview200ResponseAggregate) GetAvgMentionRate() int32`

GetAvgMentionRate returns the AvgMentionRate field if non-nil, zero value otherwise.

### GetAvgMentionRateOk

`func (o *GetOrganizationOverview200ResponseAggregate) GetAvgMentionRateOk() (*int32, bool)`

GetAvgMentionRateOk returns a tuple with the AvgMentionRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgMentionRate

`func (o *GetOrganizationOverview200ResponseAggregate) SetAvgMentionRate(v int32)`

SetAvgMentionRate sets AvgMentionRate field to given value.

### HasAvgMentionRate

`func (o *GetOrganizationOverview200ResponseAggregate) HasAvgMentionRate() bool`

HasAvgMentionRate returns a boolean if a field has been set.

### SetAvgMentionRateNil

`func (o *GetOrganizationOverview200ResponseAggregate) SetAvgMentionRateNil(b bool)`

 SetAvgMentionRateNil sets the value for AvgMentionRate to be an explicit nil

### UnsetAvgMentionRate
`func (o *GetOrganizationOverview200ResponseAggregate) UnsetAvgMentionRate()`

UnsetAvgMentionRate ensures that no value is present for AvgMentionRate, not even an explicit nil
### GetAvgMentionPosition

`func (o *GetOrganizationOverview200ResponseAggregate) GetAvgMentionPosition() float32`

GetAvgMentionPosition returns the AvgMentionPosition field if non-nil, zero value otherwise.

### GetAvgMentionPositionOk

`func (o *GetOrganizationOverview200ResponseAggregate) GetAvgMentionPositionOk() (*float32, bool)`

GetAvgMentionPositionOk returns a tuple with the AvgMentionPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgMentionPosition

`func (o *GetOrganizationOverview200ResponseAggregate) SetAvgMentionPosition(v float32)`

SetAvgMentionPosition sets AvgMentionPosition field to given value.

### HasAvgMentionPosition

`func (o *GetOrganizationOverview200ResponseAggregate) HasAvgMentionPosition() bool`

HasAvgMentionPosition returns a boolean if a field has been set.

### SetAvgMentionPositionNil

`func (o *GetOrganizationOverview200ResponseAggregate) SetAvgMentionPositionNil(b bool)`

 SetAvgMentionPositionNil sets the value for AvgMentionPosition to be an explicit nil

### UnsetAvgMentionPosition
`func (o *GetOrganizationOverview200ResponseAggregate) UnsetAvgMentionPosition()`

UnsetAvgMentionPosition ensures that no value is present for AvgMentionPosition, not even an explicit nil
### GetAvgPositivityIndex

`func (o *GetOrganizationOverview200ResponseAggregate) GetAvgPositivityIndex() int32`

GetAvgPositivityIndex returns the AvgPositivityIndex field if non-nil, zero value otherwise.

### GetAvgPositivityIndexOk

`func (o *GetOrganizationOverview200ResponseAggregate) GetAvgPositivityIndexOk() (*int32, bool)`

GetAvgPositivityIndexOk returns a tuple with the AvgPositivityIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgPositivityIndex

`func (o *GetOrganizationOverview200ResponseAggregate) SetAvgPositivityIndex(v int32)`

SetAvgPositivityIndex sets AvgPositivityIndex field to given value.

### HasAvgPositivityIndex

`func (o *GetOrganizationOverview200ResponseAggregate) HasAvgPositivityIndex() bool`

HasAvgPositivityIndex returns a boolean if a field has been set.

### SetAvgPositivityIndexNil

`func (o *GetOrganizationOverview200ResponseAggregate) SetAvgPositivityIndexNil(b bool)`

 SetAvgPositivityIndexNil sets the value for AvgPositivityIndex to be an explicit nil

### UnsetAvgPositivityIndex
`func (o *GetOrganizationOverview200ResponseAggregate) UnsetAvgPositivityIndex()`

UnsetAvgPositivityIndex ensures that no value is present for AvgPositivityIndex, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


