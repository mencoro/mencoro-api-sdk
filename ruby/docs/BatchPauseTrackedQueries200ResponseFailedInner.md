# Mencoro::BatchPauseTrackedQueries200ResponseFailedInner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **error_code** | **String** |  | [optional] |
| **error_message** | **String** |  | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BatchPauseTrackedQueries200ResponseFailedInner.new(
  id: null,
  error_code: tracked_query_not_found,
  error_message: null
)
```

