# QueryClusterResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Pass this value in the queryClusterIds filter of the analytics operations | 
**ProjectId** | **string** | The project this cluster belongs to | 
**Name** | **string** | Unique within the project, stored lower-cased | 

## Methods

### NewQueryClusterResource

`func NewQueryClusterResource(id string, projectId string, name string, ) *QueryClusterResource`

NewQueryClusterResource instantiates a new QueryClusterResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQueryClusterResourceWithDefaults

`func NewQueryClusterResourceWithDefaults() *QueryClusterResource`

NewQueryClusterResourceWithDefaults instantiates a new QueryClusterResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *QueryClusterResource) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *QueryClusterResource) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *QueryClusterResource) SetId(v string)`

SetId sets Id field to given value.


### GetProjectId

`func (o *QueryClusterResource) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *QueryClusterResource) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *QueryClusterResource) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.


### GetName

`func (o *QueryClusterResource) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *QueryClusterResource) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *QueryClusterResource) SetName(v string)`

SetName sets Name field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


