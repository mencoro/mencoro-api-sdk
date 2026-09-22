
# GetMembershipStats200Response


## Properties

Name | Type
------------ | -------------
`activeMembersCount` | number
`suspendedMembersCount` | number
`totalMembersCount` | number
`activeProjectsCount` | number
`totalProjectsCount` | number
`pendingInvitationsCount` | number
`computedAt` | string

## Example

```typescript
import type { GetMembershipStats200Response } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "activeMembersCount": 85,
  "suspendedMembersCount": 3,
  "totalMembersCount": 88,
  "activeProjectsCount": 18,
  "totalProjectsCount": 25,
  "pendingInvitationsCount": 5,
  "computedAt": 2026-02-12 10:30:00,
} satisfies GetMembershipStats200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetMembershipStats200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


