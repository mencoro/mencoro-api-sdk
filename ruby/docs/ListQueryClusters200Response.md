# Mencoro::ListQueryClusters200Response

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **items** | [**Array&lt;QueryClusterResource&gt;**](QueryClusterResource.md) |  | [optional] |
| **total** | **Integer** | Clusters in the project, not the size of this page | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ListQueryClusters200Response.new(
  items: null,
  total: null
)
```

