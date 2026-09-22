# GetMentionSamples400Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | Machine-readable reason. &#x60;validation_error&#x60; when the request was rejected; otherwise the domain error code. | 
**Message** | **string** | Human-readable reason. A 4xx carries the real message; a 5xx carries a fixed sentence and the detail goes to the logs only. | 
**RequestId** | **string** | Correlation id, also returned in the X-Request-Id header. | 
**Details** | Pointer to [**map[string][]GetMentionSamples400ResponseDetailsValueInner**](array.md) | Present only on a validation failure: one entry per rejected field, each an array of errors. | [optional] 

## Methods

### NewGetMentionSamples400Response

`func NewGetMentionSamples400Response(code string, message string, requestId string, ) *GetMentionSamples400Response`

NewGetMentionSamples400Response instantiates a new GetMentionSamples400Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetMentionSamples400ResponseWithDefaults

`func NewGetMentionSamples400ResponseWithDefaults() *GetMentionSamples400Response`

NewGetMentionSamples400ResponseWithDefaults instantiates a new GetMentionSamples400Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *GetMentionSamples400Response) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *GetMentionSamples400Response) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *GetMentionSamples400Response) SetCode(v string)`

SetCode sets Code field to given value.


### GetMessage

`func (o *GetMentionSamples400Response) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *GetMentionSamples400Response) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *GetMentionSamples400Response) SetMessage(v string)`

SetMessage sets Message field to given value.


### GetRequestId

`func (o *GetMentionSamples400Response) GetRequestId() string`

GetRequestId returns the RequestId field if non-nil, zero value otherwise.

### GetRequestIdOk

`func (o *GetMentionSamples400Response) GetRequestIdOk() (*string, bool)`

GetRequestIdOk returns a tuple with the RequestId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestId

`func (o *GetMentionSamples400Response) SetRequestId(v string)`

SetRequestId sets RequestId field to given value.


### GetDetails

`func (o *GetMentionSamples400Response) GetDetails() map[string][]GetMentionSamples400ResponseDetailsValueInner`

GetDetails returns the Details field if non-nil, zero value otherwise.

### GetDetailsOk

`func (o *GetMentionSamples400Response) GetDetailsOk() (*map[string][]GetMentionSamples400ResponseDetailsValueInner, bool)`

GetDetailsOk returns a tuple with the Details field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetails

`func (o *GetMentionSamples400Response) SetDetails(v map[string][]GetMentionSamples400ResponseDetailsValueInner)`

SetDetails sets Details field to given value.

### HasDetails

`func (o *GetMentionSamples400Response) HasDetails() bool`

HasDetails returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


