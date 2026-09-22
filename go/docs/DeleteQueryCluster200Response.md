# DeleteQueryCluster200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | The cluster that was deleted | [optional] 
**Name** | Pointer to **string** | Its name at the moment it was deleted | [optional] 
**Deleted** | Pointer to **bool** | Always true; present so the body is self-describing | [optional] 

## Methods

### NewDeleteQueryCluster200Response

`func NewDeleteQueryCluster200Response() *DeleteQueryCluster200Response`

NewDeleteQueryCluster200Response instantiates a new DeleteQueryCluster200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDeleteQueryCluster200ResponseWithDefaults

`func NewDeleteQueryCluster200ResponseWithDefaults() *DeleteQueryCluster200Response`

NewDeleteQueryCluster200ResponseWithDefaults instantiates a new DeleteQueryCluster200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DeleteQueryCluster200Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DeleteQueryCluster200Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DeleteQueryCluster200Response) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *DeleteQueryCluster200Response) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *DeleteQueryCluster200Response) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *DeleteQueryCluster200Response) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *DeleteQueryCluster200Response) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *DeleteQueryCluster200Response) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDeleted

`func (o *DeleteQueryCluster200Response) GetDeleted() bool`

GetDeleted returns the Deleted field if non-nil, zero value otherwise.

### GetDeletedOk

`func (o *DeleteQueryCluster200Response) GetDeletedOk() (*bool, bool)`

GetDeletedOk returns a tuple with the Deleted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeleted

`func (o *DeleteQueryCluster200Response) SetDeleted(v bool)`

SetDeleted sets Deleted field to given value.

### HasDeleted

`func (o *DeleteQueryCluster200Response) HasDeleted() bool`

HasDeleted returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


