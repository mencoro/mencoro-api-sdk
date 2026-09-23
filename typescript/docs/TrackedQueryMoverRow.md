
# TrackedQueryMoverRow


## Properties

Name | Type
------------ | -------------
`trackedQueryId` | string
`queryText` | string
`engine` | string
`country` | string
`avgSerpPosition` | number
`trendSerp` | number
`avgShoppingPosition` | number
`trendShopping` | number
`avgMentionPosition` | number
`trendMention` | number
`avgLinkPosition` | number
`trendLink` | number
`shareOfVoice` | number
`trendShareOfVoice` | number
`positivityIndex` | number
`trendPositivity` | number
`sentimentPositive` | number
`sentimentNeutral` | number
`sentimentNegative` | number
`mentionCount` | number
`mentionTypeCounts` | [MentionTypeCounts](MentionTypeCounts.md)

## Example

```typescript
import type { TrackedQueryMoverRow } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "trackedQueryId": null,
  "queryText": null,
  "engine": null,
  "country": null,
  "avgSerpPosition": null,
  "trendSerp": null,
  "avgShoppingPosition": null,
  "trendShopping": null,
  "avgMentionPosition": null,
  "trendMention": null,
  "avgLinkPosition": null,
  "trendLink": null,
  "shareOfVoice": null,
  "trendShareOfVoice": null,
  "positivityIndex": null,
  "trendPositivity": null,
  "sentimentPositive": null,
  "sentimentNeutral": null,
  "sentimentNegative": null,
  "mentionCount": null,
  "mentionTypeCounts": null,
} satisfies TrackedQueryMoverRow

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TrackedQueryMoverRow
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


