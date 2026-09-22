# Mencoro::GetMembershipStats200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **active_members_count** | **Integer** | Members in the active state. | [optional] |
| **suspended_members_count** | **Integer** | Members in the suspended state. | [optional] |
| **total_members_count** | **Integer** | Every membership record, suspended ones included. | [optional] |
| **active_projects_count** | **Integer** | Projects in the active state. | [optional] |
| **total_projects_count** | **Integer** | Every project, archived ones included. | [optional] |
| **pending_invitations_count** | **Integer** | Invitations still pending and not yet expired. | [optional] |
| **computed_at** | **String** | When the snapshot was computed. A database timestamp, not an ISO-8601 instant. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetMembershipStats200Response.new(
  active_members_count: 85,
  suspended_members_count: 3,
  total_members_count: 88,
  active_projects_count: 18,
  total_projects_count: 25,
  pending_invitations_count: 5,
  computed_at: 2026-02-12 10:30:00
)
```

