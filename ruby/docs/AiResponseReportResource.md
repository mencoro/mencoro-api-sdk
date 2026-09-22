# Mencoro::AiResponseReportResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ai_response_id** | **String** | The captured AI answer the report is about |  |
| **tracked_query_id** | **String** | The tracked query that answer was captured for |  |
| **type** | **String** | The kind of problem reported |  |
| **comment** | **String** | The note as stored. An empty or whitespace-only comment is stored as null. | [optional] |
| **missed_brand_names** | **Array&lt;String&gt;** | Brand names reported as missed, de-duplicated and trimmed. |  |
| **accepted** | **Boolean** | True once the report has been accepted for review. It is never false: a report that could not be delivered answers with an error instead. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::AiResponseReportResource.new(
  ai_response_id: null,
  tracked_query_id: null,
  type: null,
  comment: null,
  missed_brand_names: null,
  accepted: null
)
```

