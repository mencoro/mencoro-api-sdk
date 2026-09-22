
# GetOrganizationOverview200ResponseAggregate


## Properties

Name | Type
------------ | -------------
`projectCount` | number
`projectsWithData` | number
`totalTrackedQueries` | number
`avgShareOfVoice` | number
`avgMentionRate` | number
`avgMentionPosition` | number
`avgPositivityIndex` | number

## Example

```typescript
import type { GetOrganizationOverview200ResponseAggregate } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "projectCount": null,
  "projectsWithData": null,
  "totalTrackedQueries": null,
  "avgShareOfVoice": null,
  "avgMentionRate": null,
  "avgMentionPosition": null,
  "avgPositivityIndex": null,
} satisfies GetOrganizationOverview200ResponseAggregate

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetOrganizationOverview200ResponseAggregate
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


