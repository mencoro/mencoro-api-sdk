# AcceptedJobResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobId** | **string** | The job to poll. May name a job started by an earlier, equivalent request. | 
**Deduplicated** | **bool** | Whether this call started the job, or joined one that was already running | 
**TrackingUrl** | **string** | Poll this until the job reaches a terminal status | 

## Methods

### NewAcceptedJobResource

`func NewAcceptedJobResource(jobId string, deduplicated bool, trackingUrl string, ) *AcceptedJobResource`

NewAcceptedJobResource instantiates a new AcceptedJobResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAcceptedJobResourceWithDefaults

`func NewAcceptedJobResourceWithDefaults() *AcceptedJobResource`

NewAcceptedJobResourceWithDefaults instantiates a new AcceptedJobResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetJobId

`func (o *AcceptedJobResource) GetJobId() string`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *AcceptedJobResource) GetJobIdOk() (*string, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobId

`func (o *AcceptedJobResource) SetJobId(v string)`

SetJobId sets JobId field to given value.


### GetDeduplicated

`func (o *AcceptedJobResource) GetDeduplicated() bool`

GetDeduplicated returns the Deduplicated field if non-nil, zero value otherwise.

### GetDeduplicatedOk

`func (o *AcceptedJobResource) GetDeduplicatedOk() (*bool, bool)`

GetDeduplicatedOk returns a tuple with the Deduplicated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeduplicated

`func (o *AcceptedJobResource) SetDeduplicated(v bool)`

SetDeduplicated sets Deduplicated field to given value.


### GetTrackingUrl

`func (o *AcceptedJobResource) GetTrackingUrl() string`

GetTrackingUrl returns the TrackingUrl field if non-nil, zero value otherwise.

### GetTrackingUrlOk

`func (o *AcceptedJobResource) GetTrackingUrlOk() (*string, bool)`

GetTrackingUrlOk returns a tuple with the TrackingUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackingUrl

`func (o *AcceptedJobResource) SetTrackingUrl(v string)`

SetTrackingUrl sets TrackingUrl field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


