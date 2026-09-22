# Mencoro::AsyncJobResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **job_id** | **String** |  |  |
| **type** | **String** | What the job produces, and therefore the shape of &#x60;result&#x60; |  |
| **status** | **String** | A job in &#x60;pending&#x60;, &#x60;running&#x60; or &#x60;awaiting_retry&#x60; is still in flight; &#x60;completed&#x60; and &#x60;failed&#x60; are terminal. |  |
| **result** | **Object** | The job output, shaped by &#x60;type&#x60;. Null while the job is still in flight and for a job that failed: it means the result is not known, never that the job produced nothing. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::AsyncJobResource.new(
  job_id: null,
  type: null,
  status: null,
  result: null
)
```

