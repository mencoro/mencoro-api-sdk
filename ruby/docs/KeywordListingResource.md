# Mencoro::KeywordListingResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **keyword** | **String** | The keyword as a human types it, picked from the variants for display. |  |
| **keyword_normalized** | **String** | The grouping key: the keyword lower-cased and unaccented. Unique within the project, and the stable way to match a row across pages. |  |
| **variant_count** | **Integer** | Tracked queries behind this row that the current filters selected. |  |
| **variant_ids** | **Array&lt;String&gt;** | Ids of those tracked queries. Accepted by the single tracked-query operation. |  |
| **engines** | **Array&lt;String&gt;** | Distinct engines across the variants, not a single engine. |  |
| **countries** | **Array&lt;String&gt;** | Distinct ISO-3166 alpha-2 countries across the variants. |  |
| **query_cluster_ids** | **Array&lt;String&gt;** | Distinct keyword clusters the variants belong to. Empty when none of them is clustered. |  |
| **has_unclustered_variant** | **Boolean** | Whether at least one variant belongs to no cluster. |  |
| **status_summary** | **String** | \&quot;mixed\&quot; when the variants disagree; otherwise the one status they share. |  |
| **statuses** | **Array&lt;String&gt;** | Distinct statuses across the variants. |  |
| **check_frequencies** | **Array&lt;String&gt;** | Distinct check frequencies across the variants. |  |
| **n_passes_values** | **Array&lt;Integer&gt;** | Distinct pass counts across the variants. A pass is one budget unit per check. |  |
| **last_checked_at** | **Time** | The most recent completed check across the variants. Null when none has ever completed — not a check that found nothing. | [optional] |
| **avg_serp_position** | **Float** | Average position in traditional search over the window. 1-based, LOWER is better. | [optional] |
| **trend_serp** | **Float** | Signed improvement in avgSerpPosition against the previous window. Positive is better. | [optional] |
| **avg_shopping_position** | **Float** | Average position in shopping results over the window. 1-based, LOWER is better. | [optional] |
| **trend_shopping** | **Float** | Signed improvement in avgShoppingPosition. Positive is better. | [optional] |
| **avg_mention_position** | **Float** | Average position of the brand mention inside the AI answer. 1-based, LOWER is better. | [optional] |
| **trend_mention** | **Float** | Signed improvement in avgMentionPosition. Positive is better. | [optional] |
| **avg_link_position** | **Float** | Average position of a cited link to the brand. 1-based, LOWER is better. | [optional] |
| **trend_link** | **Float** | Signed improvement in avgLinkPosition. Positive is better. | [optional] |
| **mention_position_stability** | **Float** | Day-to-day spread of the mention position (a standard deviation): LOWER means steadier. | [optional] |
| **trend_stability** | **Float** | Signed improvement in mentionPositionStability. Positive means steadier than the previous window. | [optional] |
| **positivity_index** | **Integer** | 0-100 weighted sentiment score of the mentions; HIGHER is better. Null when there were no mentions to score. | [optional] |
| **trend_positivity** | **Integer** | Signed improvement in positivityIndex. Positive is better. | [optional] |
| **mention_rate** | **Integer** | 0-100 share of AI captures in the window that mentioned the brand; HIGHER is better. | [optional] |
| **trend_mention_rate** | **Integer** | Signed improvement in mentionRate. Positive is better. | [optional] |
| **serp_rate** | **Integer** | 0-100 share of traditional-search captures in the window that ranked the brand; HIGHER is better. | [optional] |
| **trend_serp_rate** | **Integer** | Signed improvement in serpRate. Positive is better. | [optional] |
| **share_of_voice** | **Float** | 0-100 share of the weighted AI mentions against every tracked brand; HIGHER is better. | [optional] |
| **trend_share_of_voice** | **Float** | Signed improvement in shareOfVoice. Positive is better. | [optional] |
| **sentiment_positive** | **Integer** | Positive brand mentions counted in the window. Zero here really is zero. |  |
| **sentiment_neutral** | **Integer** | Neutral brand mentions counted in the window. |  |
| **sentiment_negative** | **Integer** | Negative brand mentions counted in the window. |  |
| **avg_mention_count** | **Float** | Mentions per AI engine per day with a capture, over the window. Not a total: the window total is not part of this contract. | [optional] |
| **mention_type_counts** | [**KeywordListingResourceMentionTypeCounts**](KeywordListingResourceMentionTypeCounts.md) |  |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::KeywordListingResource.new(
  keyword: null,
  keyword_normalized: null,
  variant_count: null,
  variant_ids: null,
  engines: null,
  countries: null,
  query_cluster_ids: null,
  has_unclustered_variant: null,
  status_summary: null,
  statuses: null,
  check_frequencies: null,
  n_passes_values: null,
  last_checked_at: null,
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
  positivity_index: null,
  trend_positivity: null,
  mention_rate: null,
  trend_mention_rate: null,
  serp_rate: null,
  trend_serp_rate: null,
  share_of_voice: null,
  trend_share_of_voice: null,
  sentiment_positive: null,
  sentiment_neutral: null,
  sentiment_negative: null,
  avg_mention_count: null,
  mention_type_counts: null
)
```

