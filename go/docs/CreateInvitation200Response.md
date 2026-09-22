# CreateInvitation200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Created** | Pointer to **bool** | Always false on a 200. | [optional] 
**Reason** | Pointer to **string** | Why nothing was created. | [optional] 
**Email** | Pointer to **string** | The address as it was normalised. | [optional] 

## Methods

### NewCreateInvitation200Response

`func NewCreateInvitation200Response() *CreateInvitation200Response`

NewCreateInvitation200Response instantiates a new CreateInvitation200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateInvitation200ResponseWithDefaults

`func NewCreateInvitation200ResponseWithDefaults() *CreateInvitation200Response`

NewCreateInvitation200ResponseWithDefaults instantiates a new CreateInvitation200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreated

`func (o *CreateInvitation200Response) GetCreated() bool`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *CreateInvitation200Response) GetCreatedOk() (*bool, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *CreateInvitation200Response) SetCreated(v bool)`

SetCreated sets Created field to given value.

### HasCreated

`func (o *CreateInvitation200Response) HasCreated() bool`

HasCreated returns a boolean if a field has been set.

### GetReason

`func (o *CreateInvitation200Response) GetReason() string`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *CreateInvitation200Response) GetReasonOk() (*string, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *CreateInvitation200Response) SetReason(v string)`

SetReason sets Reason field to given value.

### HasReason

`func (o *CreateInvitation200Response) HasReason() bool`

HasReason returns a boolean if a field has been set.

### GetEmail

`func (o *CreateInvitation200Response) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *CreateInvitation200Response) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *CreateInvitation200Response) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *CreateInvitation200Response) HasEmail() bool`

HasEmail returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


