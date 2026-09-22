# Mencoro::BatchCreateTrackedQueriesResultResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **successful** | [**Array&lt;BatchCreateTrackedQueriesResultResourceSuccessfulInner&gt;**](BatchCreateTrackedQueriesResultResourceSuccessfulInner.md) | Tracked queries created by this call, one entry per query text, engine and country combination. | [optional] |
| **failed** | [**Array&lt;BatchCreateTrackedQueriesResultResourceFailedInner&gt;**](BatchCreateTrackedQueriesResultResourceFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BatchCreateTrackedQueriesResultResource.new(
  successful: null,
  failed: null
)
```

