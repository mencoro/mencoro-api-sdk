# PreviewOrganizationOperationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Action** | Pointer to **string** |  | [optional] 
**OrganizationId** | Pointer to **NullableString** | Required for every action except createOrganization. | [optional] 
**ResourceId** | Pointer to **NullableString** | The member or invitation the action acts on, for the actions that name one. | [optional] 
**Payload** | Pointer to **map[string]interface{}** | The body you intend to send to the operation itself. | [optional] 

## Methods

### NewPreviewOrganizationOperationRequest

`func NewPreviewOrganizationOperationRequest() *PreviewOrganizationOperationRequest`

NewPreviewOrganizationOperationRequest instantiates a new PreviewOrganizationOperationRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPreviewOrganizationOperationRequestWithDefaults

`func NewPreviewOrganizationOperationRequestWithDefaults() *PreviewOrganizationOperationRequest`

NewPreviewOrganizationOperationRequestWithDefaults instantiates a new PreviewOrganizationOperationRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAction

`func (o *PreviewOrganizationOperationRequest) GetAction() string`

GetAction returns the Action field if non-nil, zero value otherwise.

### GetActionOk

`func (o *PreviewOrganizationOperationRequest) GetActionOk() (*string, bool)`

GetActionOk returns a tuple with the Action field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAction

`func (o *PreviewOrganizationOperationRequest) SetAction(v string)`

SetAction sets Action field to given value.

### HasAction

`func (o *PreviewOrganizationOperationRequest) HasAction() bool`

HasAction returns a boolean if a field has been set.

### GetOrganizationId

`func (o *PreviewOrganizationOperationRequest) GetOrganizationId() string`

GetOrganizationId returns the OrganizationId field if non-nil, zero value otherwise.

### GetOrganizationIdOk

`func (o *PreviewOrganizationOperationRequest) GetOrganizationIdOk() (*string, bool)`

GetOrganizationIdOk returns a tuple with the OrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationId

`func (o *PreviewOrganizationOperationRequest) SetOrganizationId(v string)`

SetOrganizationId sets OrganizationId field to given value.

### HasOrganizationId

`func (o *PreviewOrganizationOperationRequest) HasOrganizationId() bool`

HasOrganizationId returns a boolean if a field has been set.

### SetOrganizationIdNil

`func (o *PreviewOrganizationOperationRequest) SetOrganizationIdNil(b bool)`

 SetOrganizationIdNil sets the value for OrganizationId to be an explicit nil

### UnsetOrganizationId
`func (o *PreviewOrganizationOperationRequest) UnsetOrganizationId()`

UnsetOrganizationId ensures that no value is present for OrganizationId, not even an explicit nil
### GetResourceId

`func (o *PreviewOrganizationOperationRequest) GetResourceId() string`

GetResourceId returns the ResourceId field if non-nil, zero value otherwise.

### GetResourceIdOk

`func (o *PreviewOrganizationOperationRequest) GetResourceIdOk() (*string, bool)`

GetResourceIdOk returns a tuple with the ResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceId

`func (o *PreviewOrganizationOperationRequest) SetResourceId(v string)`

SetResourceId sets ResourceId field to given value.

### HasResourceId

`func (o *PreviewOrganizationOperationRequest) HasResourceId() bool`

HasResourceId returns a boolean if a field has been set.

### SetResourceIdNil

`func (o *PreviewOrganizationOperationRequest) SetResourceIdNil(b bool)`

 SetResourceIdNil sets the value for ResourceId to be an explicit nil

### UnsetResourceId
`func (o *PreviewOrganizationOperationRequest) UnsetResourceId()`

UnsetResourceId ensures that no value is present for ResourceId, not even an explicit nil
### GetPayload

`func (o *PreviewOrganizationOperationRequest) GetPayload() map[string]interface{}`

GetPayload returns the Payload field if non-nil, zero value otherwise.

### GetPayloadOk

`func (o *PreviewOrganizationOperationRequest) GetPayloadOk() (*map[string]interface{}, bool)`

GetPayloadOk returns a tuple with the Payload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayload

`func (o *PreviewOrganizationOperationRequest) SetPayload(v map[string]interface{})`

SetPayload sets Payload field to given value.

### HasPayload

`func (o *PreviewOrganizationOperationRequest) HasPayload() bool`

HasPayload returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


