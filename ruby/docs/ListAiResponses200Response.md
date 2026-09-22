# Mencoro::ListAiResponses200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **items** | [**Array&lt;AiResponseResource&gt;**](AiResponseResource.md) |  | [optional] |
| **total** | **Integer** | Captures matching the filter, not the size of this page | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ListAiResponses200Response.new(
  items: null,
  total: null
)
```

