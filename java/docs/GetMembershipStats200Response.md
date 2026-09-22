

# GetMembershipStats200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeMembersCount** | **Integer** | Members in the active state. |  [optional] |
|**suspendedMembersCount** | **Integer** | Members in the suspended state. |  [optional] |
|**totalMembersCount** | **Integer** | Every membership record, suspended ones included. |  [optional] |
|**activeProjectsCount** | **Integer** | Projects in the active state. |  [optional] |
|**totalProjectsCount** | **Integer** | Every project, archived ones included. |  [optional] |
|**pendingInvitationsCount** | **Integer** | Invitations still pending and not yet expired. |  [optional] |
|**computedAt** | **String** | When the snapshot was computed. A database timestamp, not an ISO-8601 instant. |  [optional] |



