
# MeResource

The authenticated user and the API key the request was made with

## Properties

Name | Type
------------ | -------------
`userId` | string
`fullName` | string
`email` | string
`language` | string
`createdAt` | Date
`apiKeyId` | string
`capabilities` | Array&lt;string&gt;
`scopeMode` | string
`organizationIds` | Array&lt;string&gt;

## Example

```typescript
import type { MeResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "userId": null,
  "fullName": null,
  "email": null,
  "language": en,
  "createdAt": null,
  "apiKeyId": null,
  "capabilities": null,
  "scopeMode": null,
  "organizationIds": null,
} satisfies MeResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MeResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


