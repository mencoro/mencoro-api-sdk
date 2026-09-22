

# TrackedQueryResource

A tracked query and the metrics of its most recent check

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**queryText** | **String** | The keyword or prompt being tracked |  |
|**engine** | [**EngineEnum**](#EngineEnum) |  |  |
|**country** | **String** | ISO-3166 alpha-2 country code the query is tracked in |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**queryClusterIds** | **List&lt;UUID&gt;** | Ids of the keyword clusters this query belongs to |  |
|**checkFrequency** | [**CheckFrequencyEnum**](#CheckFrequencyEnum) | How often the query is checked |  |
|**nPasses** | **Integer** | How many times the query is asked per check |  |
|**lastSerpPosition** | **Integer** | Position in traditional search results at the last check. 1-based, LOWER is better. Null when not known yet. |  [optional] |
|**lastMentionPosition** | **Integer** | Position of the brand mention inside the AI answer at the last check. 1-based, LOWER is better. Null when not known yet. |  [optional] |
|**lastLinkPosition** | **Integer** | Position of a cited link to the brand at the last check. 1-based, LOWER is better. Null when not known yet. |  [optional] |
|**lastShoppingPosition** | **Integer** | Position in shopping results at the last check. 1-based, LOWER is better. Null when not known yet. |  [optional] |
|**lastShareOfVoice** | **Float** | 0-100 share of the weighted AI mentions against every tracked brand; HIGHER is better. Null when not known yet, which is not a share of zero. |  [optional] |
|**lastPositivityIndex** | **Integer** | 0-100 sentiment score of the brand mentions; HIGHER is better. Null when there were no mentions to score, which is not a score of zero. |  [optional] |
|**lastPositiveMentionCount** | **Integer** | Positive brand mentions at the last check. Null when not known yet. |  [optional] |
|**lastNeutralMentionCount** | **Integer** | Neutral brand mentions at the last check. Null when not known yet. |  [optional] |
|**lastNegativeMentionCount** | **Integer** | Negative brand mentions at the last check. Null when not known yet. |  [optional] |
|**lastCheckedAt** | **OffsetDateTime** | When the query was last checked. Null when it never has been. |  [optional] |



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



