# Mencoro::SetMemberProjectAccessRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **mode** | **String** |  |  |
| **project_ids** | **Array&lt;String&gt;** | The projects of the organization a selected access reaches: at least one and at most 500. Omit it, or send an empty list, for all. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::SetMemberProjectAccessRequest.new(
  mode: null,
  project_ids: null
)
```

