# Mencoro::BatchResumeTrackedQueries200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **successful** | [**Array&lt;BatchPauseTrackedQueries200ResponseSuccessfulInner&gt;**](BatchPauseTrackedQueries200ResponseSuccessfulInner.md) | Tracked queries that are now active, including ones that already were. | [optional] |
| **failed** | [**Array&lt;BatchPauseTrackedQueries200ResponseFailedInner&gt;**](BatchPauseTrackedQueries200ResponseFailedInner.md) | Tracked queries left untouched, each with the domain error code a single-item call would have returned. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BatchResumeTrackedQueries200Response.new(
  successful: null,
  failed: null
)
```

