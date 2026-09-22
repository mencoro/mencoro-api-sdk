# Mencoro::GetTrackingCoverage200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | **String** |  | [optional] |
| **total** | **Integer** | Every tracked query on the project, whatever its status | [optional] |
| **active** | **Integer** | Tracked queries currently being checked | [optional] |
| **paused** | **Integer** | Tracked queries whose checks are suspended | [optional] |
| **never_checked** | **Integer** | Active queries that have never run yet | [optional] |
| **overdue** | **Integer** | Active queries past their check-frequency interval, never-checked ones excluded | [optional] |
| **sample** | [**Array&lt;GetTrackingCoverage200ResponseSampleInner&gt;**](GetTrackingCoverage200ResponseSampleInner.md) | Up to 20 overdue queries, oldest check first | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetTrackingCoverage200Response.new(
  project_id: null,
  total: null,
  active: null,
  paused: null,
  never_checked: null,
  overdue: null,
  sample: null
)
```

