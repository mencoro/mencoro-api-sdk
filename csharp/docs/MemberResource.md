# Mencoro.Api.Model.MemberResource
A membership of an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**UserId** | **Guid** | The user this membership belongs to | 
**Role** | **string** |  | 
**State** | **string** |  | 
**IsActive** | **bool** |  | 
**JoinedAt** | **DateTime** |  | 
**ProjectAccessMode** | **string** | Which projects of the organization the member reaches: every project, or only projectIds | 
**ProjectIds** | **List&lt;Guid&gt;** | The projects a selected access reaches; empty when the mode is all | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

