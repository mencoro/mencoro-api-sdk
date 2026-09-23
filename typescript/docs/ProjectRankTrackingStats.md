
# ProjectRankTrackingStats


## Properties

Name | Type
------------ | -------------
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
`mentionCount` | number
`aiTrackedQueryCount` | number
`aiQueriesWithMention` | number
`serpTrackedQueryCount` | number
`serpQueriesWithResult` | number
`shoppingTrackedQueryCount` | number
`shoppingQueriesWithResult` | number
`mentionTypeCounts` | [MentionTypeCounts](MentionTypeCounts.md)
`dataDirtySince` | string
`mentionPositionDistribution` | [Array&lt;PositionDistributionBucket&gt;](PositionDistributionBucket.md)
`serpPositionDistribution` | [Array&lt;PositionDistributionBucket&gt;](PositionDistributionBucket.md)
`shoppingPositionDistribution` | [Array&lt;PositionDistributionBucket&gt;](PositionDistributionBucket.md)
`competitorShareOfVoice` | [Array&lt;CompetitorShareOfVoice&gt;](CompetitorShareOfVoice.md)

## Example

```typescript
import type { ProjectRankTrackingStats } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
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
  "mentionCount": null,
  "aiTrackedQueryCount": null,
  "aiQueriesWithMention": null,
  "serpTrackedQueryCount": null,
  "serpQueriesWithResult": null,
  "shoppingTrackedQueryCount": null,
  "shoppingQueriesWithResult": null,
  "mentionTypeCounts": null,
  "dataDirtySince": null,
  "mentionPositionDistribution": null,
  "serpPositionDistribution": null,
  "shoppingPositionDistribution": null,
  "competitorShareOfVoice": null,
} satisfies ProjectRankTrackingStats

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectRankTrackingStats
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


