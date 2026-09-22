# GetMeStats200ResponseProjects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Total** | Pointer to **int32** | Projects across those organizations, archived ones included. | [optional] 
**Active** | Pointer to **int32** | How many of those are active; the remainder are archived. | [optional] 

## Methods

### NewGetMeStats200ResponseProjects

`func NewGetMeStats200ResponseProjects() *GetMeStats200ResponseProjects`

NewGetMeStats200ResponseProjects instantiates a new GetMeStats200ResponseProjects object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetMeStats200ResponseProjectsWithDefaults

`func NewGetMeStats200ResponseProjectsWithDefaults() *GetMeStats200ResponseProjects`

NewGetMeStats200ResponseProjectsWithDefaults instantiates a new GetMeStats200ResponseProjects object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTotal

`func (o *GetMeStats200ResponseProjects) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *GetMeStats200ResponseProjects) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *GetMeStats200ResponseProjects) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *GetMeStats200ResponseProjects) HasTotal() bool`

HasTotal returns a boolean if a field has been set.

### GetActive

`func (o *GetMeStats200ResponseProjects) GetActive() int32`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *GetMeStats200ResponseProjects) GetActiveOk() (*int32, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *GetMeStats200ResponseProjects) SetActive(v int32)`

SetActive sets Active field to given value.

### HasActive

`func (o *GetMeStats200ResponseProjects) HasActive() bool`

HasActive returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


