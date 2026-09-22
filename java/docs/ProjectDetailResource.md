

# ProjectDetailResource

A project and the brand monitoring configuration its checks run against

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**organizationId** | **UUID** |  |  |
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**websiteDomains** | **List&lt;String&gt;** | Domains the project is monitored for. Empty when the project has no brand monitoring profile yet. |  |
|**brandNames** | **List&lt;String&gt;** | Brand names matched in AI answers and search results. Empty when the project has no brand monitoring profile yet. |  |
|**competitors** | [**List&lt;ProjectDetailResourceCompetitorsInner&gt;**](ProjectDetailResourceCompetitorsInner.md) | Competitors this project is measured against. Empty when none are configured. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



