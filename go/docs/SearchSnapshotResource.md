# SearchSnapshotResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**ProjectId** | **string** | The project this capture belongs to | 
**TrackedQueryId** | **string** | The tracked query that was searched | 
**Engine** | **string** | The search engine that was captured | 
**Results** | [**[]SearchResultResource**](SearchResultResource.md) | Organic results in rank order | 
**CapturedAt** | **time.Time** | When the page was captured, UTC | 

## Methods

### NewSearchSnapshotResource

`func NewSearchSnapshotResource(id string, projectId string, trackedQueryId string, engine string, results []SearchResultResource, capturedAt time.Time, ) *SearchSnapshotResource`

NewSearchSnapshotResource instantiates a new SearchSnapshotResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSearchSnapshotResourceWithDefaults

`func NewSearchSnapshotResourceWithDefaults() *SearchSnapshotResource`

NewSearchSnapshotResourceWithDefaults instantiates a new SearchSnapshotResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SearchSnapshotResource) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SearchSnapshotResource) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SearchSnapshotResource) SetId(v string)`

SetId sets Id field to given value.


### GetProjectId

`func (o *SearchSnapshotResource) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *SearchSnapshotResource) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *SearchSnapshotResource) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.


### GetTrackedQueryId

`func (o *SearchSnapshotResource) GetTrackedQueryId() string`

GetTrackedQueryId returns the TrackedQueryId field if non-nil, zero value otherwise.

### GetTrackedQueryIdOk

`func (o *SearchSnapshotResource) GetTrackedQueryIdOk() (*string, bool)`

GetTrackedQueryIdOk returns a tuple with the TrackedQueryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackedQueryId

`func (o *SearchSnapshotResource) SetTrackedQueryId(v string)`

SetTrackedQueryId sets TrackedQueryId field to given value.


### GetEngine

`func (o *SearchSnapshotResource) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *SearchSnapshotResource) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *SearchSnapshotResource) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetResults

`func (o *SearchSnapshotResource) GetResults() []SearchResultResource`

GetResults returns the Results field if non-nil, zero value otherwise.

### GetResultsOk

`func (o *SearchSnapshotResource) GetResultsOk() (*[]SearchResultResource, bool)`

GetResultsOk returns a tuple with the Results field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResults

`func (o *SearchSnapshotResource) SetResults(v []SearchResultResource)`

SetResults sets Results field to given value.


### GetCapturedAt

`func (o *SearchSnapshotResource) GetCapturedAt() time.Time`

GetCapturedAt returns the CapturedAt field if non-nil, zero value otherwise.

### GetCapturedAtOk

`func (o *SearchSnapshotResource) GetCapturedAtOk() (*time.Time, bool)`

GetCapturedAtOk returns a tuple with the CapturedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCapturedAt

`func (o *SearchSnapshotResource) SetCapturedAt(v time.Time)`

SetCapturedAt sets CapturedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


