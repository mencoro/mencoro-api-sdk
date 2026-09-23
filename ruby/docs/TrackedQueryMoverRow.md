# Mencoro::TrackedQueryMoverRow

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tracked_query_id** | **String** |  |  |
| **query_text** | **String** |  |  |
| **engine** | **String** |  |  |
| **country** | **String** |  |  |
| **avg_serp_position** | **Float** |  | [optional] |
| **trend_serp** | **Float** |  | [optional] |
| **avg_shopping_position** | **Float** |  | [optional] |
| **trend_shopping** | **Float** |  | [optional] |
| **avg_mention_position** | **Float** |  | [optional] |
| **trend_mention** | **Float** |  | [optional] |
| **avg_link_position** | **Float** |  | [optional] |
| **trend_link** | **Float** |  | [optional] |
| **share_of_voice** | **Float** |  | [optional] |
| **trend_share_of_voice** | **Float** |  | [optional] |
| **positivity_index** | **Integer** |  | [optional] |
| **trend_positivity** | **Integer** |  | [optional] |
| **sentiment_positive** | **Integer** |  |  |
| **sentiment_neutral** | **Integer** |  |  |
| **sentiment_negative** | **Integer** |  |  |
| **mention_count** | **Integer** |  |  |
| **mention_type_counts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::TrackedQueryMoverRow.new(
  tracked_query_id: null,
  query_text: null,
  engine: null,
  country: null,
  avg_serp_position: null,
  trend_serp: null,
  avg_shopping_position: null,
  trend_shopping: null,
  avg_mention_position: null,
  trend_mention: null,
  avg_link_position: null,
  trend_link: null,
  share_of_voice: null,
  trend_share_of_voice: null,
  positivity_index: null,
  trend_positivity: null,
  sentiment_positive: null,
  sentiment_neutral: null,
  sentiment_negative: null,
  mention_count: null,
  mention_type_counts: null
)
```

