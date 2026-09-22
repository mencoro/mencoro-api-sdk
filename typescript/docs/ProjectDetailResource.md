
# ProjectDetailResource

A project and the brand monitoring configuration its checks run against

## Properties

Name | Type
------------ | -------------
`id` | string
`organizationId` | string
`name` | string
`status` | string
`createdAt` | Date
`websiteDomains` | Array&lt;string&gt;
`brandNames` | Array&lt;string&gt;
`competitors` | [Array&lt;ProjectDetailResourceCompetitorsInner&gt;](ProjectDetailResourceCompetitorsInner.md)

## Example

```typescript
import type { ProjectDetailResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "organizationId": null,
  "name": null,
  "status": null,
  "createdAt": null,
  "websiteDomains": null,
  "brandNames": null,
  "competitors": null,
} satisfies ProjectDetailResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectDetailResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


