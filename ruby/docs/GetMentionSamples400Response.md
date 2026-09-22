# Mencoro::GetMentionSamples400Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **String** | Machine-readable reason. &#x60;validation_error&#x60; when the request was rejected; otherwise the domain error code. |  |
| **message** | **String** | Human-readable reason. A 4xx carries the real message; a 5xx carries a fixed sentence and the detail goes to the logs only. |  |
| **request_id** | **String** | Correlation id, also returned in the X-Request-Id header. |  |
| **details** | **Hash&lt;String, Array&lt;GetMentionSamples400ResponseDetailsValueInner&gt;&gt;** | Present only on a validation failure: one entry per rejected field, each an array of errors. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetMentionSamples400Response.new(
  code: null,
  message: null,
  request_id: null,
  details: null
)
```

