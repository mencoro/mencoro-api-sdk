# Mencoro::SubmittedChecksResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **submitted** | **Integer** | How many tracked queries were submitted. Zero is a valid answer: it means nothing in the project was eligible. |  |
| **tracked_query_ids** | **Array&lt;String&gt;** | The tracked queries submitted, in the order they were submitted (least recently checked first). Poll these to follow progress. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::SubmittedChecksResource.new(
  submitted: null,
  tracked_query_ids: null
)
```

