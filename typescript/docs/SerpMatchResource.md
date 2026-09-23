
# SerpMatchResource

A stored serp match; no provider credentials or operational metadata

## Properties

Name | Type
------------ | -------------
`trackedQueryId` | string
`projectId` | string
`engine` | string
`searchPageId` | string
`competitorId` | string
`position` | number
`detectedAt` | Date

## Example

```typescript
import type { SerpMatchResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "trackedQueryId": null,
  "projectId": null,
  "engine": null,
  "searchPageId": null,
  "competitorId": null,
  "position": null,
  "detectedAt": null,
} satisfies SerpMatchResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SerpMatchResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


