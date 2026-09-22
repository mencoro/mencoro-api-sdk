# Mencoro::BatchWriteOutcome

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **successful** | [**Array&lt;BatchPauseTrackedQueries200ResponseSuccessfulInner&gt;**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | The resources the operation was applied to. | [optional] |
| **failed** | [**Array&lt;BatchWriteOutcomeFailedInner&gt;**](BatchWriteOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BatchWriteOutcome.new(
  successful: null,
  failed: null
)
```

