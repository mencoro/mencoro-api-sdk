# Mencoro::AcceptedJobResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **job_id** | **String** | The job to poll. May name a job started by an earlier, equivalent request. |  |
| **deduplicated** | **Boolean** | Whether this call started the job, or joined one that was already running |  |
| **tracking_url** | **String** | Poll this until the job reaches a terminal status |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::AcceptedJobResource.new(
  job_id: null,
  deduplicated: null,
  tracking_url: null
)
```

