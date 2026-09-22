# Mencoro::AiResponseResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **project_id** | **String** | The project this capture belongs to |  |
| **tracked_query_id** | **String** | The tracked query that was asked |  |
| **engine** | **String** | The AI engine that answered |  |
| **response_text** | **String** | The full answer text as the engine produced it |  |
| **citations** | [**Array&lt;CitationResource&gt;**](CitationResource.md) | Sources the engine cited, in the order it cited them |  |
| **captured_at** | **Time** | When the answer was captured, UTC |  |
| **model_name** | **String** | Engine-reported model, when it reported one. Absent on captures taken before engines exposed it | [optional] |
| **pass_index** | **Integer** | Which sampling pass of the run this answer is, starting at 0 |  |
| **pass_count** | **Integer** | How many passes that run took. Rows of one run share trackedQueryId and capturedAt |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::AiResponseResource.new(
  id: null,
  project_id: null,
  tracked_query_id: null,
  engine: null,
  response_text: null,
  citations: null,
  captured_at: null,
  model_name: null,
  pass_index: null,
  pass_count: null
)
```

