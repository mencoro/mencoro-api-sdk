# Mencoro::AsyncJobResourceError

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **String** | A stable code for the kind of failure: &#x60;timed_out&#x60;, &#x60;provider_failed&#x60;, &#x60;submission_failed&#x60; or &#x60;internal_error&#x60;. |  |
| **message** | **String** | A fixed, readable explanation of the code. It is the same for every job that failed with that code. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::AsyncJobResourceError.new(
  code: null,
  message: null
)
```

