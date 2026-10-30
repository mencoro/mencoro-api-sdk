# Mencoro::CreateInvitation201Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **email** | **String** |  |  |
| **role** | **String** |  |  |
| **state** | **String** |  |  |
| **created_at** | **Time** |  |  |
| **expires_at** | **Time** |  |  |
| **accepted_at** | **Time** |  | [optional] |
| **project_access_mode** | **String** | Which projects of the organization the invitee reaches on accepting: every project, or only projectIds |  |
| **project_ids** | **Array&lt;String&gt;** | The projects a selected access reaches, limited to those still in the organization; empty when the mode is all. It may be empty on selected once its projects left the organization, which grants nothing |  |
| **created** | **Boolean** | Always true on a 201. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::CreateInvitation201Response.new(
  id: null,
  email: null,
  role: null,
  state: null,
  created_at: null,
  expires_at: null,
  accepted_at: null,
  project_access_mode: null,
  project_ids: null,
  created: null
)
```

