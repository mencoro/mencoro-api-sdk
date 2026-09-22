# GetOrganizationStats200ResponseProjects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Total** | Pointer to **int32** | Every project in the organization, archived ones included. | [optional] 
**Active** | Pointer to **int32** | Projects that are not archived; never greater than &#x60;total&#x60;. | [optional] 

## Methods

### NewGetOrganizationStats200ResponseProjects

`func NewGetOrganizationStats200ResponseProjects() *GetOrganizationStats200ResponseProjects`

NewGetOrganizationStats200ResponseProjects instantiates a new GetOrganizationStats200ResponseProjects object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetOrganizationStats200ResponseProjectsWithDefaults

`func NewGetOrganizationStats200ResponseProjectsWithDefaults() *GetOrganizationStats200ResponseProjects`

NewGetOrganizationStats200ResponseProjectsWithDefaults instantiates a new GetOrganizationStats200ResponseProjects object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTotal

`func (o *GetOrganizationStats200ResponseProjects) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *GetOrganizationStats200ResponseProjects) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *GetOrganizationStats200ResponseProjects) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *GetOrganizationStats200ResponseProjects) HasTotal() bool`

HasTotal returns a boolean if a field has been set.

### GetActive

`func (o *GetOrganizationStats200ResponseProjects) GetActive() int32`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *GetOrganizationStats200ResponseProjects) GetActiveOk() (*int32, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *GetOrganizationStats200ResponseProjects) SetActive(v int32)`

SetActive sets Active field to given value.

### HasActive

`func (o *GetOrganizationStats200ResponseProjects) HasActive() bool`

HasActive returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


