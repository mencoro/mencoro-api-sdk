# Mencoro::BatchCreateQueryClustersRequestData

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **names** | **Array&lt;String&gt;** | Cluster names to create, already trimmed and lower-cased on the server. Duplicates are collapsed. |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::BatchCreateQueryClustersRequestData.new(
  names: null
)
```

