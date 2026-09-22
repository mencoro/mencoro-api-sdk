# Mencoro::GetMeStats200ResponseProjects

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **total** | **Integer** | Projects across those organizations, archived ones included. | [optional] |
| **active** | **Integer** | How many of those are active; the remainder are archived. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::GetMeStats200ResponseProjects.new(
  total: 25,
  active: 18
)
```

