

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



