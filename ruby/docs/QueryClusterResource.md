# Mencoro::QueryClusterResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Pass this value in the queryClusterIds filter of the analytics operations |  |
| **project_id** | **String** | The project this cluster belongs to |  |
| **name** | **String** | Unique within the project, stored lower-cased |  |

## Example

```ruby
require 'mencoro'

instance = Mencoro::QueryClusterResource.new(
  id: null,
  project_id: null,
  name: null
)
```

