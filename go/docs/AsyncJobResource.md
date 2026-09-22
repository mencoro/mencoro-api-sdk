# AsyncJobResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobId** | **string** |  | 
**Type** | **string** | What the job produces, and therefore the shape of &#x60;result&#x60; | 
**Status** | **string** | A job in &#x60;pending&#x60;, &#x60;running&#x60; or &#x60;awaiting_retry&#x60; is still in flight; &#x60;completed&#x60; and &#x60;failed&#x60; are terminal. | 
**Result** | Pointer to **map[string]interface{}** | The job output, shaped by &#x60;type&#x60;. Null while the job is still in flight and for a job that failed: it means the result is not known, never that the job produced nothing. | [optional] 

## Methods

### NewAsyncJobResource

`func NewAsyncJobResource(jobId string, type_ string, status string, ) *AsyncJobResource`

NewAsyncJobResource instantiates a new AsyncJobResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAsyncJobResourceWithDefaults

`func NewAsyncJobResourceWithDefaults() *AsyncJobResource`

NewAsyncJobResourceWithDefaults instantiates a new AsyncJobResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetJobId

`func (o *AsyncJobResource) GetJobId() string`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *AsyncJobResource) GetJobIdOk() (*string, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobId

`func (o *AsyncJobResource) SetJobId(v string)`

SetJobId sets JobId field to given value.


### GetType

`func (o *AsyncJobResource) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AsyncJobResource) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AsyncJobResource) SetType(v string)`

SetType sets Type field to given value.


### GetStatus

`func (o *AsyncJobResource) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *AsyncJobResource) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *AsyncJobResource) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetResult

`func (o *AsyncJobResource) GetResult() map[string]interface{}`

GetResult returns the Result field if non-nil, zero value otherwise.

### GetResultOk

`func (o *AsyncJobResource) GetResultOk() (*map[string]interface{}, bool)`

GetResultOk returns a tuple with the Result field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResult

`func (o *AsyncJobResource) SetResult(v map[string]interface{})`

SetResult sets Result field to given value.

### HasResult

`func (o *AsyncJobResource) HasResult() bool`

HasResult returns a boolean if a field has been set.

### SetResultNil

`func (o *AsyncJobResource) SetResultNil(b bool)`

 SetResultNil sets the value for Result to be an explicit nil

### UnsetResult
`func (o *AsyncJobResource) UnsetResult()`

UnsetResult ensures that no value is present for Result, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


