
# OrganizationResource

An organization the caller is a member of

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`status` | string
`imageUrl` | string
`contactEmail` | string
`role` | string
`createdAt` | Date

## Example

```typescript
import type { OrganizationResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "status": null,
  "imageUrl": null,
  "contactEmail": null,
  "role": null,
  "createdAt": null,
} satisfies OrganizationResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OrganizationResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


