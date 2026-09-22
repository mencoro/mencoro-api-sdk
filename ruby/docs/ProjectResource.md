# Mencoro::ProjectResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **name** | **String** |  |  |
| **status** | **String** |  |  |
| **created_at** | **Time** |  |  |
| **tracked_query_count** | **Integer** | Number of tracked queries in the project |  |
| **avg_serp_position** | **Float** | Average position in traditional search results. Null when unknown. | [optional] |
| **avg_shopping_position** | **Float** | Average position in shopping results. Null when unknown. | [optional] |
| **avg_mention_position** | **Float** | Average position of the brand mention inside AI answers. Null when unknown. | [optional] |
| **avg_link_position** | **Float** | Average position of a cited link to the brand. Null when unknown. | [optional] |
| **mention_rate** | **Integer** | Share of checks where the brand was mentioned. Null when unknown. | [optional] |
| **serp_rate** | **Integer** |  | [optional] |
| **shopping_rate** | **Integer** |  | [optional] |
| **positivity_index** | **Integer** | Sentiment balance of the brand&#39;s mentions. Null when unknown. | [optional] |
| **share_of_voice** | **Float** | Share of voice against the tracked competitors. Null when unknown. | [optional] |
| **serp_position_stability** | **Float** |  | [optional] |
| **shopping_position_stability** | **Float** |  | [optional] |
| **last_rank_detected_at** | **Time** | When a rank was last detected for this project. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ProjectResource.new(
  id: null,
  name: null,
  status: null,
  created_at: null,
  tracked_query_count: null,
  avg_serp_position: null,
  avg_shopping_position: null,
  avg_mention_position: null,
  avg_link_position: null,
  mention_rate: null,
  serp_rate: null,
  shopping_rate: null,
  positivity_index: null,
  share_of_voice: null,
  serp_position_stability: null,
  shopping_position_stability: null,
  last_rank_detected_at: null
)
```

