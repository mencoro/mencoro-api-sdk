# GetMembershipStats200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_members_count** | **int** | Members in the active state. | [optional]
**suspended_members_count** | **int** | Members in the suspended state. | [optional]
**total_members_count** | **int** | Every membership record, suspended ones included. | [optional]
**active_projects_count** | **int** | Projects in the active state. | [optional]
**total_projects_count** | **int** | Every project, archived ones included. | [optional]
**pending_invitations_count** | **int** | Invitations still pending and not yet expired. | [optional]
**computed_at** | **string** | When the snapshot was computed. A database timestamp, not an ISO-8601 instant. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
