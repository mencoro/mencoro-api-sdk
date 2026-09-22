

# OrganizationResource

An organization the caller is a member of

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**imageUrl** | **URI** |  |  [optional] |
|**contactEmail** | **String** |  |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | The caller&#39;s current role in this organization |  |
|**createdAt** | **OffsetDateTime** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| OWNER | &quot;owner&quot; |
| MANAGER | &quot;manager&quot; |
| VIEWER | &quot;viewer&quot; |



