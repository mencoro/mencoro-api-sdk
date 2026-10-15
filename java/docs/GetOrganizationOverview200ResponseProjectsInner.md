

# GetOrganizationOverview200ResponseProjectsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectId** | **UUID** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**trackedQueryCount** | **Integer** |  |  [optional] |
|**shareOfVoice** | **Float** | 0-100 percentage share of weighted AI mentions against all tracked brands; higher is better. Null when the project has no rank data yet. |  [optional] |
|**mentionRate** | **Integer** | 0-100 percentage of AI checks (one per tracked query x engine x UTC day) across all retained data that mentioned the brand, each check counted as the share of its passes that did; higher is better. Null when the project has no rank data yet. |  [optional] |
|**avgMentionPosition** | **Float** | 1-based average rank of the brand within the answer; LOWER is better. Null when the project has no rank data yet. |  [optional] |
|**positivityIndex** | **Integer** | 0-100 sentiment score; higher is better. Null when the project has no rank data yet. |  [optional] |



