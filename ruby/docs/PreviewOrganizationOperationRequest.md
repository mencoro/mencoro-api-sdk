# Mencoro::PreviewOrganizationOperationRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **action** | **String** |  | [optional] |
| **organization_id** | **String** | Required for every action except createOrganization. | [optional] |
| **resource_id** | **String** | The member or invitation the action acts on, for the actions that name one. | [optional] |
| **payload** | **Object** | The body you intend to send to the operation itself. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::PreviewOrganizationOperationRequest.new(
  action: null,
  organization_id: null,
  resource_id: null,
  payload: null
)
```

