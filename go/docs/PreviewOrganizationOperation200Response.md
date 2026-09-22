# PreviewOrganizationOperation200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Action** | Pointer to **string** |  | [optional] 
**Organization** | Pointer to [**NullablePreviewOrganizationOperation200ResponseOrganization**](PreviewOrganizationOperation200ResponseOrganization.md) |  | [optional] 
**ResourceId** | Pointer to **NullableString** | The member or invitation the action acts on; null for the actions that name none. | [optional] 
**Changes** | Pointer to [**[]OperationEffect**](OperationEffect.md) | What the operation itself will do. | [optional] 
**SideEffects** | Pointer to [**[]OperationEffect**](OperationEffect.md) | What else it will cause, with the records it will touch in &#x60;targets&#x60;. | [optional] 
**Warnings** | Pointer to [**[]OperationEffect**](OperationEffect.md) | How the system behaves around it. Not part of the effects digest: rewording one does not invalidate a confirmation. | [optional] 
**Conditions** | Pointer to [**[]OperationEffect**](OperationEffect.md) | What must hold for the operation to be allowed. | [optional] 
**Actor** | Pointer to **map[string]interface{}** | Who the confirmation is issued to: the user and the API key. It is valid for that pair only. | [optional] 
**Confirmation** | Pointer to **map[string]interface{}** | The token to send back, the header to send it in, and how long it lives. | [optional] 

## Methods

### NewPreviewOrganizationOperation200Response

`func NewPreviewOrganizationOperation200Response() *PreviewOrganizationOperation200Response`

NewPreviewOrganizationOperation200Response instantiates a new PreviewOrganizationOperation200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPreviewOrganizationOperation200ResponseWithDefaults

`func NewPreviewOrganizationOperation200ResponseWithDefaults() *PreviewOrganizationOperation200Response`

NewPreviewOrganizationOperation200ResponseWithDefaults instantiates a new PreviewOrganizationOperation200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAction

`func (o *PreviewOrganizationOperation200Response) GetAction() string`

GetAction returns the Action field if non-nil, zero value otherwise.

### GetActionOk

`func (o *PreviewOrganizationOperation200Response) GetActionOk() (*string, bool)`

GetActionOk returns a tuple with the Action field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAction

`func (o *PreviewOrganizationOperation200Response) SetAction(v string)`

SetAction sets Action field to given value.

### HasAction

`func (o *PreviewOrganizationOperation200Response) HasAction() bool`

HasAction returns a boolean if a field has been set.

### GetOrganization

`func (o *PreviewOrganizationOperation200Response) GetOrganization() PreviewOrganizationOperation200ResponseOrganization`

GetOrganization returns the Organization field if non-nil, zero value otherwise.

### GetOrganizationOk

`func (o *PreviewOrganizationOperation200Response) GetOrganizationOk() (*PreviewOrganizationOperation200ResponseOrganization, bool)`

GetOrganizationOk returns a tuple with the Organization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganization

`func (o *PreviewOrganizationOperation200Response) SetOrganization(v PreviewOrganizationOperation200ResponseOrganization)`

SetOrganization sets Organization field to given value.

### HasOrganization

`func (o *PreviewOrganizationOperation200Response) HasOrganization() bool`

HasOrganization returns a boolean if a field has been set.

### SetOrganizationNil

`func (o *PreviewOrganizationOperation200Response) SetOrganizationNil(b bool)`

 SetOrganizationNil sets the value for Organization to be an explicit nil

### UnsetOrganization
`func (o *PreviewOrganizationOperation200Response) UnsetOrganization()`

UnsetOrganization ensures that no value is present for Organization, not even an explicit nil
### GetResourceId

`func (o *PreviewOrganizationOperation200Response) GetResourceId() string`

GetResourceId returns the ResourceId field if non-nil, zero value otherwise.

### GetResourceIdOk

`func (o *PreviewOrganizationOperation200Response) GetResourceIdOk() (*string, bool)`

GetResourceIdOk returns a tuple with the ResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceId

`func (o *PreviewOrganizationOperation200Response) SetResourceId(v string)`

SetResourceId sets ResourceId field to given value.

### HasResourceId

`func (o *PreviewOrganizationOperation200Response) HasResourceId() bool`

HasResourceId returns a boolean if a field has been set.

### SetResourceIdNil

`func (o *PreviewOrganizationOperation200Response) SetResourceIdNil(b bool)`

 SetResourceIdNil sets the value for ResourceId to be an explicit nil

### UnsetResourceId
`func (o *PreviewOrganizationOperation200Response) UnsetResourceId()`

UnsetResourceId ensures that no value is present for ResourceId, not even an explicit nil
### GetChanges

`func (o *PreviewOrganizationOperation200Response) GetChanges() []OperationEffect`

GetChanges returns the Changes field if non-nil, zero value otherwise.

### GetChangesOk

`func (o *PreviewOrganizationOperation200Response) GetChangesOk() (*[]OperationEffect, bool)`

GetChangesOk returns a tuple with the Changes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChanges

`func (o *PreviewOrganizationOperation200Response) SetChanges(v []OperationEffect)`

SetChanges sets Changes field to given value.

### HasChanges

`func (o *PreviewOrganizationOperation200Response) HasChanges() bool`

HasChanges returns a boolean if a field has been set.

### GetSideEffects

`func (o *PreviewOrganizationOperation200Response) GetSideEffects() []OperationEffect`

GetSideEffects returns the SideEffects field if non-nil, zero value otherwise.

### GetSideEffectsOk

`func (o *PreviewOrganizationOperation200Response) GetSideEffectsOk() (*[]OperationEffect, bool)`

GetSideEffectsOk returns a tuple with the SideEffects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSideEffects

`func (o *PreviewOrganizationOperation200Response) SetSideEffects(v []OperationEffect)`

SetSideEffects sets SideEffects field to given value.

### HasSideEffects

`func (o *PreviewOrganizationOperation200Response) HasSideEffects() bool`

HasSideEffects returns a boolean if a field has been set.

### GetWarnings

`func (o *PreviewOrganizationOperation200Response) GetWarnings() []OperationEffect`

GetWarnings returns the Warnings field if non-nil, zero value otherwise.

### GetWarningsOk

`func (o *PreviewOrganizationOperation200Response) GetWarningsOk() (*[]OperationEffect, bool)`

GetWarningsOk returns a tuple with the Warnings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWarnings

`func (o *PreviewOrganizationOperation200Response) SetWarnings(v []OperationEffect)`

SetWarnings sets Warnings field to given value.

### HasWarnings

`func (o *PreviewOrganizationOperation200Response) HasWarnings() bool`

HasWarnings returns a boolean if a field has been set.

### GetConditions

`func (o *PreviewOrganizationOperation200Response) GetConditions() []OperationEffect`

GetConditions returns the Conditions field if non-nil, zero value otherwise.

### GetConditionsOk

`func (o *PreviewOrganizationOperation200Response) GetConditionsOk() (*[]OperationEffect, bool)`

GetConditionsOk returns a tuple with the Conditions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditions

`func (o *PreviewOrganizationOperation200Response) SetConditions(v []OperationEffect)`

SetConditions sets Conditions field to given value.

### HasConditions

`func (o *PreviewOrganizationOperation200Response) HasConditions() bool`

HasConditions returns a boolean if a field has been set.

### GetActor

`func (o *PreviewOrganizationOperation200Response) GetActor() map[string]interface{}`

GetActor returns the Actor field if non-nil, zero value otherwise.

### GetActorOk

`func (o *PreviewOrganizationOperation200Response) GetActorOk() (*map[string]interface{}, bool)`

GetActorOk returns a tuple with the Actor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActor

`func (o *PreviewOrganizationOperation200Response) SetActor(v map[string]interface{})`

SetActor sets Actor field to given value.

### HasActor

`func (o *PreviewOrganizationOperation200Response) HasActor() bool`

HasActor returns a boolean if a field has been set.

### GetConfirmation

`func (o *PreviewOrganizationOperation200Response) GetConfirmation() map[string]interface{}`

GetConfirmation returns the Confirmation field if non-nil, zero value otherwise.

### GetConfirmationOk

`func (o *PreviewOrganizationOperation200Response) GetConfirmationOk() (*map[string]interface{}, bool)`

GetConfirmationOk returns a tuple with the Confirmation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfirmation

`func (o *PreviewOrganizationOperation200Response) SetConfirmation(v map[string]interface{})`

SetConfirmation sets Confirmation field to given value.

### HasConfirmation

`func (o *PreviewOrganizationOperation200Response) HasConfirmation() bool`

HasConfirmation returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


