

# CreateInvitation201Response


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
|**created** | **Boolean** | Always true on a 201. |  [optional] |



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



