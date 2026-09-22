
# MemberResource

A membership of an organization

## Properties

Name | Type
------------ | -------------
`id` | string
`userId` | string
`role` | string
`state` | string
`isActive` | boolean
`joinedAt` | Date

## Example

```typescript
import type { MemberResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "userId": null,
  "role": null,
  "state": null,
  "isActive": null,
  "joinedAt": null,
} satisfies MemberResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MemberResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


