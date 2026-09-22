# Mencoro::BatchCreateTrackedQueriesRequestData

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **query_texts** | **Array&lt;String&gt;** | Prompts or keywords to track. Stored lower-cased with whitespace collapsed and leading list markers removed. |  |
| **engines** | **Array&lt;String&gt;** | Engines each text is asked in. |  |
| **countries** | **Array&lt;String&gt;** | ISO 3166-1 alpha-2 countries each text is asked from. |  |
| **locale** | **String** | ISO 639-1 language the queries are asked in. Omit it to ask the engine without a language. | [optional] |
| **check_frequency** | **String** | How often every created query is checked. |  |
| **n_passes** | **Integer** | Passes run per check. Applied to AI-engine combinations only: a non-AI engine is always created with 1, whatever is sent here. |  |
| **query_cluster_ids** | **Array&lt;String&gt;** | Clusters every created query joins. Must already exist in the project. A combination that is already tracked has these clusters merged into it. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BatchCreateTrackedQueriesRequestData.new(
  query_texts: null,
  engines: null,
  countries: null,
  locale: null,
  check_frequency: null,
  n_passes: null,
  query_cluster_ids: null
)
```

