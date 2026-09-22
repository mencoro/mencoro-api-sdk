# Mencoro.Api.Model.PreviewOrganizationOperation200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Action** | **string** |  | [optional] 
**Organization** | [**PreviewOrganizationOperation200ResponseOrganization**](PreviewOrganizationOperation200ResponseOrganization.md) |  | [optional] 
**ResourceId** | **Guid?** | The member or invitation the action acts on; null for the actions that name none. | [optional] 
**Changes** | [**List&lt;OperationEffect&gt;**](OperationEffect.md) | What the operation itself will do. | [optional] 
**SideEffects** | [**List&lt;OperationEffect&gt;**](OperationEffect.md) | What else it will cause, with the records it will touch in &#x60;targets&#x60;. | [optional] 
**Warnings** | [**List&lt;OperationEffect&gt;**](OperationEffect.md) | How the system behaves around it. Not part of the effects digest: rewording one does not invalidate a confirmation. | [optional] 
**Conditions** | [**List&lt;OperationEffect&gt;**](OperationEffect.md) | What must hold for the operation to be allowed. | [optional] 
**Actor** | **Object** | Who the confirmation is issued to: the user and the API key. It is valid for that pair only. | [optional] 
**Confirmation** | **Object** | The token to send back, the header to send it in, and how long it lives. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

