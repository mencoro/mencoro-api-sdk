# Mencoro.Api.Model.InvitationResource
An invitation to join an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Email** | **string** |  | 
**Role** | **string** |  | 
**State** | **string** |  | 
**CreatedAt** | **DateTime** |  | 
**ExpiresAt** | **DateTime** |  | 
**AcceptedAt** | **DateTime?** |  | [optional] 
**ProjectAccessMode** | **string** | Which projects of the organization the invitee reaches on accepting: every project, or only projectIds | 
**ProjectIds** | **List&lt;Guid&gt;** | The projects a selected access reaches, limited to those still in the organization; empty when the mode is all. It may be empty on selected once its projects left the organization, which grants nothing | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

