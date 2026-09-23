# Mencoro::MentionSampleResponse

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **tracked_query_id** | **String** |  |  |
| **ai_response_id** | **String** |  |  |
| **engine** | **String** |  |  |
| **competitor_id** | **String** |  | [optional] |
| **sentiment** | **String** |  |  |
| **mention_type** | **String** |  |  |
| **mention_position** | **Integer** |  |  |
| **text** | **String** |  |  |
| **detected_at** | **String** |  |  |
| **query_text** | **String** |  |  |
| **country** | **String** |  | [optional] |
| **mention_relation** | **String** | Published because &#x60;competitorId&#x60; alone cannot answer the question. Own-brand AND untracked-competitor mentions both carry a null competitor id - the confusion migration Version20260608130000 was written to end - so a reader that treats a null competitor id as \&quot;us\&quot; silently counts a rival as the brand. | [optional] |
| **brand_name** | **String** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::MentionSampleResponse.new(
  id: null,
  tracked_query_id: null,
  ai_response_id: null,
  engine: null,
  competitor_id: null,
  sentiment: null,
  mention_type: null,
  mention_position: null,
  text: null,
  detected_at: null,
  query_text: null,
  country: null,
  mention_relation: null,
  brand_name: null
)
```

