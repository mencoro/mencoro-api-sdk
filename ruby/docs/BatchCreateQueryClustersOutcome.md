# Mencoro::BatchCreateQueryClustersOutcome

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **successful** | [**Array&lt;BatchCreateQueryClustersOutcomeSuccessfulInner&gt;**](BatchCreateQueryClustersOutcomeSuccessfulInner.md) | Clusters created by this call. | [optional] |
| **failed** | [**Array&lt;BatchCreateQueryClustersOutcomeFailedInner&gt;**](BatchCreateQueryClustersOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BatchCreateQueryClustersOutcome.new(
  successful: null,
  failed: null
)
```

