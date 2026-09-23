# Mencoro::ProjectSentimentBreakdown

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **per_engine** | [**Array&lt;PerEngineSentiment&gt;**](PerEngineSentiment.md) |  |  |
| **per_competitor** | [**Array&lt;PerCompetitorSentiment&gt;**](PerCompetitorSentiment.md) |  |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ProjectSentimentBreakdown.new(
  per_engine: null,
  per_competitor: null
)
```

