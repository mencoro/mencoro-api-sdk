# Mencoro::ReportAiResponseRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **type** | **String** | What is wrong with the capture. |  |
| **comment** | **String** | Optional note for the reviewer, at most 1000 characters. An empty string is stored as no comment. | [optional] |
| **missed_brand_names** | **Array&lt;String&gt;** | Brands the engine mentioned that the pipeline did not record. Most useful with type \&quot;missed_mention\&quot;; accepted with either. At most 50 distinct names of 255 characters each. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ReportAiResponseRequest.new(
  type: null,
  comment: null,
  missed_brand_names: null
)
```

