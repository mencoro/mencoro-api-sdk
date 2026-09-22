# Mencoro.Api.Model.GetMembershipStats200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActiveMembersCount** | **int** | Members in the active state. | [optional] 
**SuspendedMembersCount** | **int** | Members in the suspended state. | [optional] 
**TotalMembersCount** | **int** | Every membership record, suspended ones included. | [optional] 
**ActiveProjectsCount** | **int** | Projects in the active state. | [optional] 
**TotalProjectsCount** | **int** | Every project, archived ones included. | [optional] 
**PendingInvitationsCount** | **int** | Invitations still pending and not yet expired. | [optional] 
**ComputedAt** | **string** | When the snapshot was computed. A database timestamp, not an ISO-8601 instant. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

