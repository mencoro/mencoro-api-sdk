# Mencoro::ListProjects200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **items** | [**Array&lt;ProjectResource&gt;**](ProjectResource.md) |  | [optional] |
| **total** | **Integer** | Every project matching the filters, not the size of this page. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ListProjects200Response.new(
  items: null,
  total: null
)
```

