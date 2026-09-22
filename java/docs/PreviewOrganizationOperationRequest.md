

# PreviewOrganizationOperationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) |  |  [optional] |
|**organizationId** | **UUID** | Required for every action except createOrganization. |  [optional] |
|**resourceId** | **UUID** | The member or invitation the action acts on, for the actions that name one. |  [optional] |
|**payload** | **Object** | The body you intend to send to the operation itself. |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| CREATE_ORGANIZATION | &quot;createOrganization&quot; |
| UPDATE_ORGANIZATION | &quot;updateOrganization&quot; |
| ARCHIVE_ORGANIZATION | &quot;archiveOrganization&quot; |
| RESTORE_ORGANIZATION | &quot;restoreOrganization&quot; |
| CHANGE_MEMBER_ROLE | &quot;changeMemberRole&quot; |
| SUSPEND_MEMBER | &quot;suspendMember&quot; |
| REACTIVATE_MEMBER | &quot;reactivateMember&quot; |
| CREATE_INVITATION | &quot;createInvitation&quot; |
| CANCEL_INVITATION | &quot;cancelInvitation&quot; |



