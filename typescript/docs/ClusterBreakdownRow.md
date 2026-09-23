
# ClusterBreakdownRow


## Properties

Name | Type
------------ | -------------
`clusterId` | string
`clusterName` | string
`queryCount` | number
`keywordCount` | number
`avgSerpPosition` | number
`trendSerp` | number
`avgShoppingPosition` | number
`trendShopping` | number
`avgMentionPosition` | number
`trendMention` | number
`avgLinkPosition` | number
`trendLink` | number
`mentionPositionStability` | number
`trendStability` | number
`serpPositionStability` | number
`trendSerpStability` | number
`shoppingPositionStability` | number
`trendShoppingStability` | number
`positivityIndex` | number
`trendPositivity` | number
`mentionRate` | number
`trendMentionRate` | number
`serpRate` | number
`trendSerpRate` | number
`shoppingRate` | number
`trendShoppingRate` | number
`shareOfVoice` | number
`trendShareOfVoice` | number
`sentimentPositive` | number
`sentimentNeutral` | number
`sentimentNegative` | number
`avgMentionCount` | number
`mentionTypeCounts` | [MentionTypeCounts](MentionTypeCounts.md)

## Example

```typescript
import type { ClusterBreakdownRow } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "clusterId": null,
  "clusterName": null,
  "queryCount": null,
  "keywordCount": null,
  "avgSerpPosition": null,
  "trendSerp": null,
  "avgShoppingPosition": null,
  "trendShopping": null,
  "avgMentionPosition": null,
  "trendMention": null,
  "avgLinkPosition": null,
  "trendLink": null,
  "mentionPositionStability": null,
  "trendStability": null,
  "serpPositionStability": null,
  "trendSerpStability": null,
  "shoppingPositionStability": null,
  "trendShoppingStability": null,
  "positivityIndex": null,
  "trendPositivity": null,
  "mentionRate": null,
  "trendMentionRate": null,
  "serpRate": null,
  "trendSerpRate": null,
  "shoppingRate": null,
  "trendShoppingRate": null,
  "shareOfVoice": null,
  "trendShareOfVoice": null,
  "sentimentPositive": null,
  "sentimentNeutral": null,
  "sentimentNegative": null,
  "avgMentionCount": null,
  "mentionTypeCounts": null,
} satisfies ClusterBreakdownRow

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ClusterBreakdownRow
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


