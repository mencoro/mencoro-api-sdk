
# GetOrganizationOverview200ResponseProjectsInner


## Properties

Name | Type
------------ | -------------
`projectId` | string
`name` | string
`status` | string
`trackedQueryCount` | number
`shareOfVoice` | number
`mentionRate` | number
`avgMentionPosition` | number
`positivityIndex` | number

## Example

```typescript
import type { GetOrganizationOverview200ResponseProjectsInner } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "projectId": null,
  "name": null,
  "status": null,
  "trackedQueryCount": null,
  "shareOfVoice": null,
  "mentionRate": null,
  "avgMentionPosition": null,
  "positivityIndex": null,
} satisfies GetOrganizationOverview200ResponseProjectsInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetOrganizationOverview200ResponseProjectsInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


