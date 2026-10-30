

# InvitationResource

An invitation to join an organization

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**email** | **String** |  |  |
|**role** | [**RoleEnum**](#RoleEnum) |  |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**expiresAt** | **OffsetDateTime** |  |  |
|**acceptedAt** | **OffsetDateTime** |  |  [optional] |
|**projectAccessMode** | [**ProjectAccessModeEnum**](#ProjectAccessModeEnum) | Which projects of the organization the invitee reaches on accepting: every project, or only projectIds |  |
|**projectIds** | **List&lt;UUID&gt;** | The projects a selected access reaches, limited to those still in the organization; empty when the mode is all. It may be empty on selected once its projects left the organization, which grants nothing |  |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| OWNER | &quot;owner&quot; |
| MANAGER | &quot;manager&quot; |
| VIEWER | &quot;viewer&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| ACCEPTED | &quot;accepted&quot; |
| REJECTED | &quot;rejected&quot; |
| EXPIRED | &quot;expired&quot; |
| CANCELLED | &quot;cancelled&quot; |



## Enum: ProjectAccessModeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SELECTED | &quot;selected&quot; |



