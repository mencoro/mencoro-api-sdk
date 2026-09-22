

# TrackedQueryDetailResource

A tracked query and how it is checked

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**projectId** | **UUID** | The project this tracked query belongs to |  |
|**queryText** | **String** | The prompt or keyword sent to the engine |  |
|**engine** | [**EngineEnum**](#EngineEnum) |  |  |
|**locale** | **String** | Language tag the query is asked in. Null when the engine is asked without one. |  [optional] |
|**country** | **String** | ISO-3166 alpha-2 country the query is asked from |  |
|**queryClusterIds** | **List&lt;UUID&gt;** | Clusters (groups) this query belongs to. Empty when it is ungrouped. |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**checkFrequency** | [**CheckFrequencyEnum**](#CheckFrequencyEnum) | How often the query is checked while active |  |
|**nPasses** | **Integer** | Passes run per check. Greater than 1 only for AI engines. |  |
|**lastCheckedAt** | **OffsetDateTime** | When a check last completed. Null means no check has completed yet, which is not the same as a check that found nothing. |  [optional] |



## Enum: EngineEnum

| Name | Value |
|---- | -----|
| CHATGPT | &quot;chatgpt&quot; |
| PERPLEXITY | &quot;perplexity&quot; |
| GOOGLE_AI_OVERVIEW | &quot;google_ai_overview&quot; |
| GOOGLE_AI_MODE | &quot;google_ai_mode&quot; |
| GOOGLE_SERP | &quot;google_serp&quot; |
| GOOGLE_SHOPPING | &quot;google_shopping&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



## Enum: CheckFrequencyEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| MONTHLY | &quot;monthly&quot; |



