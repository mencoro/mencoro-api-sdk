# OperationEffect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | Stable machine-readable identifier for this effect | 
**Summary** | **string** | Human-readable description, safe to show to whoever must approve the operation | 
**Targets** | Pointer to **[]string** |  | [optional] [default to {}]

## Methods

### NewOperationEffect

`func NewOperationEffect(code string, summary string, ) *OperationEffect`

NewOperationEffect instantiates a new OperationEffect object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOperationEffectWithDefaults

`func NewOperationEffectWithDefaults() *OperationEffect`

NewOperationEffectWithDefaults instantiates a new OperationEffect object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *OperationEffect) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *OperationEffect) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *OperationEffect) SetCode(v string)`

SetCode sets Code field to given value.


### GetSummary

`func (o *OperationEffect) GetSummary() string`

GetSummary returns the Summary field if non-nil, zero value otherwise.

### GetSummaryOk

`func (o *OperationEffect) GetSummaryOk() (*string, bool)`

GetSummaryOk returns a tuple with the Summary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSummary

`func (o *OperationEffect) SetSummary(v string)`

SetSummary sets Summary field to given value.


### GetTargets

`func (o *OperationEffect) GetTargets() []string`

GetTargets returns the Targets field if non-nil, zero value otherwise.

### GetTargetsOk

`func (o *OperationEffect) GetTargetsOk() (*[]string, bool)`

GetTargetsOk returns a tuple with the Targets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargets

`func (o *OperationEffect) SetTargets(v []string)`

SetTargets sets Targets field to given value.

### HasTargets

`func (o *OperationEffect) HasTargets() bool`

HasTargets returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


