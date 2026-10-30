# Mencoro.Api.Model.CreateInvitationRequestProjectAccess
Which projects of the organization the invitee reaches once they accept. Omitted or null, they reach every project. An owner always reaches every project, so an owner invitation cannot carry a selection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Mode** | **string** |  | 
**ProjectIds** | **List&lt;Guid&gt;** | For selected: at least one and at most 500 projects of the organization. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

