
# CreateInvitationRequestProjectAccess

Which projects of the organization the invitee reaches once they accept. Omitted or null, they reach every project. An owner always reaches every project, so an owner invitation cannot carry a selection.

## Properties

Name | Type
------------ | -------------
`mode` | string
`projectIds` | Array&lt;string&gt;

## Example

```typescript
import type { CreateInvitationRequestProjectAccess } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "mode": null,
  "projectIds": null,
} satisfies CreateInvitationRequestProjectAccess

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateInvitationRequestProjectAccess
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


