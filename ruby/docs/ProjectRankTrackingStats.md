# Mencoro::ProjectRankTrackingStats

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **avg_serp_position** | **Float** |  | [optional] |
| **trend_serp** | **Float** |  | [optional] |
| **avg_shopping_position** | **Float** |  | [optional] |
| **trend_shopping** | **Float** |  | [optional] |
| **avg_mention_position** | **Float** |  | [optional] |
| **trend_mention** | **Float** |  | [optional] |
| **avg_link_position** | **Float** |  | [optional] |
| **trend_link** | **Float** |  | [optional] |
| **mention_position_stability** | **Float** |  | [optional] |
| **trend_stability** | **Float** |  | [optional] |
| **serp_position_stability** | **Float** |  | [optional] |
| **trend_serp_stability** | **Float** |  | [optional] |
| **shopping_position_stability** | **Float** |  | [optional] |
| **trend_shopping_stability** | **Float** |  | [optional] |
| **positivity_index** | **Integer** |  | [optional] |
| **trend_positivity** | **Integer** |  | [optional] |
| **mention_rate** | **Integer** |  | [optional] |
| **trend_mention_rate** | **Integer** |  | [optional] |
| **serp_rate** | **Integer** |  | [optional] |
| **trend_serp_rate** | **Integer** |  | [optional] |
| **shopping_rate** | **Integer** |  | [optional] |
| **trend_shopping_rate** | **Integer** |  | [optional] |
| **share_of_voice** | **Float** |  | [optional] |
| **trend_share_of_voice** | **Float** |  | [optional] |
| **sentiment_positive** | **Integer** |  |  |
| **sentiment_neutral** | **Integer** |  |  |
| **sentiment_negative** | **Integer** |  |  |
| **mention_count** | **Integer** |  |  |
| **ai_tracked_query_count** | **Integer** |  |  |
| **ai_queries_with_mention** | **Integer** |  |  |
| **serp_tracked_query_count** | **Integer** |  |  |
| **serp_queries_with_result** | **Integer** |  |  |
| **shopping_tracked_query_count** | **Integer** |  |  |
| **shopping_queries_with_result** | **Integer** |  |  |
| **mention_type_counts** | [**MentionTypeCounts**](MentionTypeCounts.md) |  |  |
| **data_dirty_since** | **String** |  | [optional] |
| **mention_position_distribution** | [**Array&lt;PositionDistributionBucket&gt;**](PositionDistributionBucket.md) |  | [optional] |
| **serp_position_distribution** | [**Array&lt;PositionDistributionBucket&gt;**](PositionDistributionBucket.md) |  | [optional] |
| **shopping_position_distribution** | [**Array&lt;PositionDistributionBucket&gt;**](PositionDistributionBucket.md) |  | [optional] |
| **competitor_share_of_voice** | [**Array&lt;CompetitorShareOfVoice&gt;**](CompetitorShareOfVoice.md) |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ProjectRankTrackingStats.new(
  avg_serp_position: null,
  trend_serp: null,
  avg_shopping_position: null,
  trend_shopping: null,
  avg_mention_position: null,
  trend_mention: null,
  avg_link_position: null,
  trend_link: null,
  mention_position_stability: null,
  trend_stability: null,
  serp_position_stability: null,
  trend_serp_stability: null,
  shopping_position_stability: null,
  trend_shopping_stability: null,
  positivity_index: null,
  trend_positivity: null,
  mention_rate: null,
  trend_mention_rate: null,
  serp_rate: null,
  trend_serp_rate: null,
  shopping_rate: null,
  trend_shopping_rate: null,
  share_of_voice: null,
  trend_share_of_voice: null,
  sentiment_positive: null,
  sentiment_neutral: null,
  sentiment_negative: null,
  mention_count: null,
  ai_tracked_query_count: null,
  ai_queries_with_mention: null,
  serp_tracked_query_count: null,
  serp_queries_with_result: null,
  shopping_tracked_query_count: null,
  shopping_queries_with_result: null,
  mention_type_counts: null,
  data_dirty_since: null,
  mention_position_distribution: null,
  serp_position_distribution: null,
  shopping_position_distribution: null,
  competitor_share_of_voice: null
)
```

