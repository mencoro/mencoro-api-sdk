

# BatchCreateTrackedQueriesRequestData

Tracked queries to create, as a cross product of texts, engines and countries

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**queryTexts** | **List&lt;String&gt;** | Prompts or keywords to track. Stored lower-cased with whitespace collapsed and leading list markers removed. |  |
|**engines** | [**List&lt;EnginesEnum&gt;**](#List&lt;EnginesEnum&gt;) | Engines each text is asked in. |  |
|**countries** | **List&lt;String&gt;** | ISO 3166-1 alpha-2 countries each text is asked from. |  |
|**locale** | **String** | ISO 639-1 language the queries are asked in. Omit it to ask the engine without a language. |  [optional] |
|**checkFrequency** | [**CheckFrequencyEnum**](#CheckFrequencyEnum) | How often every created query is checked. |  |
|**nPasses** | **Integer** | Passes run per check. Applied to AI-engine combinations only: a non-AI engine is always created with 1, whatever is sent here. |  |
|**queryClusterIds** | **List&lt;UUID&gt;** | Clusters every created query joins. Must already exist in the project. A combination that is already tracked has these clusters merged into it. |  |



## Enum: List&lt;EnginesEnum&gt;

| Name | Value |
|---- | -----|
| CHATGPT | &quot;chatgpt&quot; |
| PERPLEXITY | &quot;perplexity&quot; |
| GOOGLE_AI_OVERVIEW | &quot;google_ai_overview&quot; |
| GOOGLE_AI_MODE | &quot;google_ai_mode&quot; |
| GOOGLE_SERP | &quot;google_serp&quot; |
| GOOGLE_SHOPPING | &quot;google_shopping&quot; |



## Enum: CheckFrequencyEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| MONTHLY | &quot;monthly&quot; |



