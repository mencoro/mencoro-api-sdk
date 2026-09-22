

# KeywordListingResource

One keyword of a project, its variants and its metrics over the requested window

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyword** | **String** | The keyword as a human types it, picked from the variants for display. |  |
|**keywordNormalized** | **String** | The grouping key: the keyword lower-cased and unaccented. Unique within the project, and the stable way to match a row across pages. |  |
|**variantCount** | **Integer** | Tracked queries behind this row that the current filters selected. |  |
|**variantIds** | **List&lt;UUID&gt;** | Ids of those tracked queries. Accepted by the single tracked-query operation. |  |
|**engines** | [**List&lt;EnginesEnum&gt;**](#List&lt;EnginesEnum&gt;) | Distinct engines across the variants, not a single engine. |  |
|**countries** | **List&lt;String&gt;** | Distinct ISO-3166 alpha-2 countries across the variants. |  |
|**queryClusterIds** | **List&lt;UUID&gt;** | Distinct keyword clusters the variants belong to. Empty when none of them is clustered. |  |
|**hasUnclusteredVariant** | **Boolean** | Whether at least one variant belongs to no cluster. |  |
|**statusSummary** | [**StatusSummaryEnum**](#StatusSummaryEnum) | \&quot;mixed\&quot; when the variants disagree; otherwise the one status they share. |  |
|**statuses** | [**List&lt;StatusesEnum&gt;**](#List&lt;StatusesEnum&gt;) | Distinct statuses across the variants. |  |
|**checkFrequencies** | [**List&lt;CheckFrequenciesEnum&gt;**](#List&lt;CheckFrequenciesEnum&gt;) | Distinct check frequencies across the variants. |  |
|**nPassesValues** | **List&lt;Integer&gt;** | Distinct pass counts across the variants. A pass is one budget unit per check. |  |
|**lastCheckedAt** | **OffsetDateTime** | The most recent completed check across the variants. Null when none has ever completed — not a check that found nothing. |  [optional] |
|**avgSerpPosition** | **Float** | Average position in traditional search over the window. 1-based, LOWER is better. |  [optional] |
|**trendSerp** | **Float** | Signed improvement in avgSerpPosition against the previous window. Positive is better. |  [optional] |
|**avgShoppingPosition** | **Float** | Average position in shopping results over the window. 1-based, LOWER is better. |  [optional] |
|**trendShopping** | **Float** | Signed improvement in avgShoppingPosition. Positive is better. |  [optional] |
|**avgMentionPosition** | **Float** | Average position of the brand mention inside the AI answer. 1-based, LOWER is better. |  [optional] |
|**trendMention** | **Float** | Signed improvement in avgMentionPosition. Positive is better. |  [optional] |
|**avgLinkPosition** | **Float** | Average position of a cited link to the brand. 1-based, LOWER is better. |  [optional] |
|**trendLink** | **Float** | Signed improvement in avgLinkPosition. Positive is better. |  [optional] |
|**mentionPositionStability** | **Float** | Day-to-day spread of the mention position (a standard deviation): LOWER means steadier. |  [optional] |
|**trendStability** | **Float** | Signed improvement in mentionPositionStability. Positive means steadier than the previous window. |  [optional] |
|**positivityIndex** | **Integer** | 0-100 weighted sentiment score of the mentions; HIGHER is better. Null when there were no mentions to score. |  [optional] |
|**trendPositivity** | **Integer** | Signed improvement in positivityIndex. Positive is better. |  [optional] |
|**mentionRate** | **Integer** | 0-100 share of AI captures in the window that mentioned the brand; HIGHER is better. |  [optional] |
|**trendMentionRate** | **Integer** | Signed improvement in mentionRate. Positive is better. |  [optional] |
|**serpRate** | **Integer** | 0-100 share of traditional-search captures in the window that ranked the brand; HIGHER is better. |  [optional] |
|**trendSerpRate** | **Integer** | Signed improvement in serpRate. Positive is better. |  [optional] |
|**shareOfVoice** | **Float** | 0-100 share of the weighted AI mentions against every tracked brand; HIGHER is better. |  [optional] |
|**trendShareOfVoice** | **Float** | Signed improvement in shareOfVoice. Positive is better. |  [optional] |
|**sentimentPositive** | **Integer** | Positive brand mentions counted in the window. Zero here really is zero. |  |
|**sentimentNeutral** | **Integer** | Neutral brand mentions counted in the window. |  |
|**sentimentNegative** | **Integer** | Negative brand mentions counted in the window. |  |
|**avgMentionCount** | **Float** | Mentions per AI engine per day with a capture, over the window. Not a total: the window total is not part of this contract. |  [optional] |
|**mentionTypeCounts** | [**KeywordListingResourceMentionTypeCounts**](KeywordListingResourceMentionTypeCounts.md) |  |  |



## Enum: List&lt;EnginesEnum&gt;

| Name | Value |
|---- | -----|
| CHATGPT | &quot;chatgpt&quot; |
| PERPLEXITY | &quot;perplexity&quot; |
| GOOGLE_AI_OVERVIEW | &quot;google_ai_overview&quot; |
| GOOGLE_AI_MODE | &quot;google_ai_mode&quot; |
| GOOGLE_SERP | &quot;google_serp&quot; |
| GOOGLE_SHOPPING | &quot;google_shopping&quot; |



## Enum: StatusSummaryEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |
| MIXED | &quot;mixed&quot; |



## Enum: List&lt;StatusesEnum&gt;

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



## Enum: List&lt;CheckFrequenciesEnum&gt;

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| MONTHLY | &quot;monthly&quot; |



