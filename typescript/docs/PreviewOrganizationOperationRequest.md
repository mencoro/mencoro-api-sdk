
# PreviewOrganizationOperationRequest


## Properties

Name | Type
------------ | -------------
`action` | string
`organizationId` | string
`resourceId` | string
`payload` | object

## Example

```typescript
import type { PreviewOrganizationOperationRequest } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "action": null,
  "organizationId": null,
  "resourceId": null,
  "payload": null,
} satisfies PreviewOrganizationOperationRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PreviewOrganizationOperationRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


