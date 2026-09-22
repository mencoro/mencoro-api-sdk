# GetTrackingCoverage200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectId** | Pointer to **string** |  | [optional] 
**Total** | Pointer to **int32** | Every tracked query on the project, whatever its status | [optional] 
**Active** | Pointer to **int32** | Tracked queries currently being checked | [optional] 
**Paused** | Pointer to **int32** | Tracked queries whose checks are suspended | [optional] 
**NeverChecked** | Pointer to **int32** | Active queries that have never run yet | [optional] 
**Overdue** | Pointer to **int32** | Active queries past their check-frequency interval, never-checked ones excluded | [optional] 
**Sample** | Pointer to [**[]GetTrackingCoverage200ResponseSampleInner**](GetTrackingCoverage200ResponseSampleInner.md) | Up to 20 overdue queries, oldest check first | [optional] 

## Methods

### NewGetTrackingCoverage200Response

`func NewGetTrackingCoverage200Response() *GetTrackingCoverage200Response`

NewGetTrackingCoverage200Response instantiates a new GetTrackingCoverage200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetTrackingCoverage200ResponseWithDefaults

`func NewGetTrackingCoverage200ResponseWithDefaults() *GetTrackingCoverage200Response`

NewGetTrackingCoverage200ResponseWithDefaults instantiates a new GetTrackingCoverage200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjectId

`func (o *GetTrackingCoverage200Response) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *GetTrackingCoverage200Response) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *GetTrackingCoverage200Response) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *GetTrackingCoverage200Response) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### GetTotal

`func (o *GetTrackingCoverage200Response) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *GetTrackingCoverage200Response) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *GetTrackingCoverage200Response) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *GetTrackingCoverage200Response) HasTotal() bool`

HasTotal returns a boolean if a field has been set.

### GetActive

`func (o *GetTrackingCoverage200Response) GetActive() int32`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *GetTrackingCoverage200Response) GetActiveOk() (*int32, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *GetTrackingCoverage200Response) SetActive(v int32)`

SetActive sets Active field to given value.

### HasActive

`func (o *GetTrackingCoverage200Response) HasActive() bool`

HasActive returns a boolean if a field has been set.

### GetPaused

`func (o *GetTrackingCoverage200Response) GetPaused() int32`

GetPaused returns the Paused field if non-nil, zero value otherwise.

### GetPausedOk

`func (o *GetTrackingCoverage200Response) GetPausedOk() (*int32, bool)`

GetPausedOk returns a tuple with the Paused field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaused

`func (o *GetTrackingCoverage200Response) SetPaused(v int32)`

SetPaused sets Paused field to given value.

### HasPaused

`func (o *GetTrackingCoverage200Response) HasPaused() bool`

HasPaused returns a boolean if a field has been set.

### GetNeverChecked

`func (o *GetTrackingCoverage200Response) GetNeverChecked() int32`

GetNeverChecked returns the NeverChecked field if non-nil, zero value otherwise.

### GetNeverCheckedOk

`func (o *GetTrackingCoverage200Response) GetNeverCheckedOk() (*int32, bool)`

GetNeverCheckedOk returns a tuple with the NeverChecked field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeverChecked

`func (o *GetTrackingCoverage200Response) SetNeverChecked(v int32)`

SetNeverChecked sets NeverChecked field to given value.

### HasNeverChecked

`func (o *GetTrackingCoverage200Response) HasNeverChecked() bool`

HasNeverChecked returns a boolean if a field has been set.

### GetOverdue

`func (o *GetTrackingCoverage200Response) GetOverdue() int32`

GetOverdue returns the Overdue field if non-nil, zero value otherwise.

### GetOverdueOk

`func (o *GetTrackingCoverage200Response) GetOverdueOk() (*int32, bool)`

GetOverdueOk returns a tuple with the Overdue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverdue

`func (o *GetTrackingCoverage200Response) SetOverdue(v int32)`

SetOverdue sets Overdue field to given value.

### HasOverdue

`func (o *GetTrackingCoverage200Response) HasOverdue() bool`

HasOverdue returns a boolean if a field has been set.

### GetSample

`func (o *GetTrackingCoverage200Response) GetSample() []GetTrackingCoverage200ResponseSampleInner`

GetSample returns the Sample field if non-nil, zero value otherwise.

### GetSampleOk

`func (o *GetTrackingCoverage200Response) GetSampleOk() (*[]GetTrackingCoverage200ResponseSampleInner, bool)`

GetSampleOk returns a tuple with the Sample field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSample

`func (o *GetTrackingCoverage200Response) SetSample(v []GetTrackingCoverage200ResponseSampleInner)`

SetSample sets Sample field to given value.

### HasSample

`func (o *GetTrackingCoverage200Response) HasSample() bool`

HasSample returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


