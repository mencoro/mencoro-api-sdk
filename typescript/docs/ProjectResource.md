
# ProjectResource

A project and its headline metrics

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`status` | string
`createdAt` | Date
`trackedQueryCount` | number
`avgSerpPosition` | number
`avgShoppingPosition` | number
`avgMentionPosition` | number
`avgLinkPosition` | number
`mentionRate` | number
`serpRate` | number
`shoppingRate` | number
`positivityIndex` | number
`shareOfVoice` | number
`serpPositionStability` | number
`shoppingPositionStability` | number
`lastRankDetectedAt` | Date

## Example

```typescript
import type { ProjectResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "status": null,
  "createdAt": null,
  "trackedQueryCount": null,
  "avgSerpPosition": null,
  "avgShoppingPosition": null,
  "avgMentionPosition": null,
  "avgLinkPosition": null,
  "mentionRate": null,
  "serpRate": null,
  "shoppingRate": null,
  "positivityIndex": null,
  "shareOfVoice": null,
  "serpPositionStability": null,
  "shoppingPositionStability": null,
  "lastRankDetectedAt": null,
} satisfies ProjectResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


