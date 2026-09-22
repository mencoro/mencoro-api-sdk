# Mencoro::BatchWriteOutcomeFailedInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **error_code** | **String** | The same code a single-item call returns for this problem. | [optional] |
| **error_message** | **String** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BatchWriteOutcomeFailedInner.new(
  id: null,
  error_code: null,
  error_message: null
)
```

