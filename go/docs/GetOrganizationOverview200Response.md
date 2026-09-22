# GetOrganizationOverview200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Projects** | Pointer to [**[]GetOrganizationOverview200ResponseProjectsInner**](GetOrganizationOverview200ResponseProjectsInner.md) |  | [optional] 
**Aggregate** | Pointer to [**GetOrganizationOverview200ResponseAggregate**](GetOrganizationOverview200ResponseAggregate.md) |  | [optional] 

## Methods

### NewGetOrganizationOverview200Response

`func NewGetOrganizationOverview200Response() *GetOrganizationOverview200Response`

NewGetOrganizationOverview200Response instantiates a new GetOrganizationOverview200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetOrganizationOverview200ResponseWithDefaults

`func NewGetOrganizationOverview200ResponseWithDefaults() *GetOrganizationOverview200Response`

NewGetOrganizationOverview200ResponseWithDefaults instantiates a new GetOrganizationOverview200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjects

`func (o *GetOrganizationOverview200Response) GetProjects() []GetOrganizationOverview200ResponseProjectsInner`

GetProjects returns the Projects field if non-nil, zero value otherwise.

### GetProjectsOk

`func (o *GetOrganizationOverview200Response) GetProjectsOk() (*[]GetOrganizationOverview200ResponseProjectsInner, bool)`

GetProjectsOk returns a tuple with the Projects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjects

`func (o *GetOrganizationOverview200Response) SetProjects(v []GetOrganizationOverview200ResponseProjectsInner)`

SetProjects sets Projects field to given value.

### HasProjects

`func (o *GetOrganizationOverview200Response) HasProjects() bool`

HasProjects returns a boolean if a field has been set.

### GetAggregate

`func (o *GetOrganizationOverview200Response) GetAggregate() GetOrganizationOverview200ResponseAggregate`

GetAggregate returns the Aggregate field if non-nil, zero value otherwise.

### GetAggregateOk

`func (o *GetOrganizationOverview200Response) GetAggregateOk() (*GetOrganizationOverview200ResponseAggregate, bool)`

GetAggregateOk returns a tuple with the Aggregate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAggregate

`func (o *GetOrganizationOverview200Response) SetAggregate(v GetOrganizationOverview200ResponseAggregate)`

SetAggregate sets Aggregate field to given value.

### HasAggregate

`func (o *GetOrganizationOverview200Response) HasAggregate() bool`

HasAggregate returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


