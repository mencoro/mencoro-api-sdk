

# MemberResource

A membership of an organization

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**userId** | **UUID** | The user this membership belongs to |  |
|**role** | [**RoleEnum**](#RoleEnum) |  |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**isActive** | **Boolean** |  |  |
|**joinedAt** | **OffsetDateTime** |  |  |
|**projectAccessMode** | [**ProjectAccessModeEnum**](#ProjectAccessModeEnum) | Which projects of the organization the member reaches: every project, or only projectIds |  |
|**projectIds** | **List&lt;UUID&gt;** | The projects a selected access reaches; empty when the mode is all |  |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| OWNER | &quot;owner&quot; |
| MANAGER | &quot;manager&quot; |
| VIEWER | &quot;viewer&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| SUSPENDED | &quot;suspended&quot; |



## Enum: ProjectAccessModeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SELECTED | &quot;selected&quot; |



