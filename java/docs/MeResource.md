

# MeResource

The authenticated user and the API key the request was made with

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**userId** | **UUID** |  |  |
|**fullName** | **String** |  |  |
|**email** | **String** |  |  |
|**language** | **String** | IETF language tag the user reads the product in |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**apiKeyId** | **UUID** | The API key this request authenticated with |  |
|**capabilities** | [**List&lt;CapabilitiesEnum&gt;**](#List&lt;CapabilitiesEnum&gt;) |  |  |
|**scopeMode** | [**ScopeModeEnum**](#ScopeModeEnum) |  |  |
|**organizationIds** | **List&lt;UUID&gt;** | Organizations the key names. Empty for a key scoped to all organizations, which instead follows the owner&#39;s membership. |  |



## Enum: List&lt;CapabilitiesEnum&gt;

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ORGANIZATION_MANAGE | &quot;organization:manage&quot; |



## Enum: ScopeModeEnum

| Name | Value |
|---- | -----|
| SELECTED | &quot;selected&quot; |
| ALL_ORGANIZATIONS | &quot;all_organizations&quot; |



