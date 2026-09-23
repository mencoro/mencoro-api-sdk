
# MentionMatchResource

A stored mention match; no provider credentials or operational metadata

## Properties

Name | Type
------------ | -------------
`trackedQueryId` | string
`projectId` | string
`engine` | string
`aiResponseId` | string
`competitorId` | string
`mentionPosition` | number
`sentiment` | string
`mentionType` | string
`mentionTypeCondition` | string
`responseContext` | string
`detectedAt` | Date
`mentionRelation` | string
`brandName` | string
`brandNameAsMentioned` | string

## Example

```typescript
import type { MentionMatchResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "trackedQueryId": null,
  "projectId": null,
  "engine": null,
  "aiResponseId": null,
  "competitorId": null,
  "mentionPosition": null,
  "sentiment": null,
  "mentionType": null,
  "mentionTypeCondition": null,
  "responseContext": null,
  "detectedAt": null,
  "mentionRelation": null,
  "brandName": null,
  "brandNameAsMentioned": null,
} satisfies MentionMatchResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MentionMatchResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


