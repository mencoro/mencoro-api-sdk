

# PreviewOrganizationOperation200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** |  |  [optional] |
|**organization** | [**PreviewOrganizationOperation200ResponseOrganization**](PreviewOrganizationOperation200ResponseOrganization.md) |  |  [optional] |
|**resourceId** | **UUID** | The member or invitation the action acts on; null for the actions that name none. |  [optional] |
|**changes** | [**List&lt;OperationEffect&gt;**](OperationEffect.md) | What the operation itself will do. |  [optional] |
|**sideEffects** | [**List&lt;OperationEffect&gt;**](OperationEffect.md) | What else it will cause, with the records it will touch in &#x60;targets&#x60;. |  [optional] |
|**warnings** | [**List&lt;OperationEffect&gt;**](OperationEffect.md) | How the system behaves around it. Not part of the effects digest: rewording one does not invalidate a confirmation. |  [optional] |
|**conditions** | [**List&lt;OperationEffect&gt;**](OperationEffect.md) | What must hold for the operation to be allowed. |  [optional] |
|**actor** | **Object** | Who the confirmation is issued to: the user and the API key. It is valid for that pair only. |  [optional] |
|**confirmation** | **Object** | The token to send back, the header to send it in, and how long it lives. |  [optional] |



