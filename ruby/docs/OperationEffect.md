# Mencoro::OperationEffect

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **String** | Stable machine-readable identifier for this effect |  |
| **summary** | **String** | Human-readable description, safe to show to whoever must approve the operation |  |
| **targets** | **Array&lt;String&gt;** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::OperationEffect.new(
  code: projects_will_be_archived,
  summary: null,
  targets: null
)
```

