# AsyncJobResourceError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | A stable code for the kind of failure: &#x60;timed_out&#x60;, &#x60;provider_failed&#x60;, &#x60;submission_failed&#x60; or &#x60;internal_error&#x60;. | 
**Message** | **string** | A fixed, readable explanation of the code. It is the same for every job that failed with that code. | 

## Methods

### NewAsyncJobResourceError

`func NewAsyncJobResourceError(code string, message string, ) *AsyncJobResourceError`

NewAsyncJobResourceError instantiates a new AsyncJobResourceError object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAsyncJobResourceErrorWithDefaults

`func NewAsyncJobResourceErrorWithDefaults() *AsyncJobResourceError`

NewAsyncJobResourceErrorWithDefaults instantiates a new AsyncJobResourceError object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *AsyncJobResourceError) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *AsyncJobResourceError) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *AsyncJobResourceError) SetCode(v string)`

SetCode sets Code field to given value.


### GetMessage

`func (o *AsyncJobResourceError) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *AsyncJobResourceError) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *AsyncJobResourceError) SetMessage(v string)`

SetMessage sets Message field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


