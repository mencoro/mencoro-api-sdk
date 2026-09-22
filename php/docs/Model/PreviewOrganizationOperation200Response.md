# PreviewOrganizationOperation200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **string** |  | [optional]
**organization** | [**\Mencoro\Api\Model\PreviewOrganizationOperation200ResponseOrganization**](PreviewOrganizationOperation200ResponseOrganization.md) |  | [optional]
**resource_id** | **string** | The member or invitation the action acts on; null for the actions that name none. | [optional]
**changes** | [**\Mencoro\Api\Model\OperationEffect[]**](OperationEffect.md) | What the operation itself will do. | [optional]
**side_effects** | [**\Mencoro\Api\Model\OperationEffect[]**](OperationEffect.md) | What else it will cause, with the records it will touch in &#x60;targets&#x60;. | [optional]
**warnings** | [**\Mencoro\Api\Model\OperationEffect[]**](OperationEffect.md) | How the system behaves around it. Not part of the effects digest: rewording one does not invalidate a confirmation. | [optional]
**conditions** | [**\Mencoro\Api\Model\OperationEffect[]**](OperationEffect.md) | What must hold for the operation to be allowed. | [optional]
**actor** | **object** | Who the confirmation is issued to: the user and the API key. It is valid for that pair only. | [optional]
**confirmation** | **object** | The token to send back, the header to send it in, and how long it lives. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
