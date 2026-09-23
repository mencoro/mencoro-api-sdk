# Mencoro::PerCompetitorSentiment

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **competitor_id** | **String** |  |  |
| **positive** | **Integer** |  |  |
| **neutral** | **Integer** |  |  |
| **negative** | **Integer** |  |  |
| **mention_count** | **Integer** |  |  |
| **positivity_index** | **Integer** |  | [optional] |
| **mention_type_counts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::PerCompetitorSentiment.new(
  competitor_id: null,
  positive: null,
  neutral: null,
  negative: null,
  mention_count: null,
  positivity_index: null,
  mention_type_counts: null
)
```

