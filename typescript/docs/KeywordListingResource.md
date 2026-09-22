
# KeywordListingResource

One keyword of a project, its variants and its metrics over the requested window

## Properties

Name | Type
------------ | -------------
`keyword` | string
`keywordNormalized` | string
`variantCount` | number
`variantIds` | Array&lt;string&gt;
`engines` | Array&lt;string&gt;
`countries` | Array&lt;string&gt;
`queryClusterIds` | Array&lt;string&gt;
`hasUnclusteredVariant` | boolean
`statusSummary` | string
`statuses` | Array&lt;string&gt;
`checkFrequencies` | Array&lt;string&gt;
`nPassesValues` | Array&lt;number&gt;
`lastCheckedAt` | Date
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
`positivityIndex` | number
`trendPositivity` | number
`mentionRate` | number
`trendMentionRate` | number
`serpRate` | number
`trendSerpRate` | number
`shareOfVoice` | number
`trendShareOfVoice` | number
`sentimentPositive` | number
`sentimentNeutral` | number
`sentimentNegative` | number
`avgMentionCount` | number
`mentionTypeCounts` | [KeywordListingResourceMentionTypeCounts](KeywordListingResourceMentionTypeCounts.md)

## Example

```typescript
import type { KeywordListingResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "keyword": null,
  "keywordNormalized": null,
  "variantCount": null,
  "variantIds": null,
  "engines": null,
  "countries": null,
  "queryClusterIds": null,
  "hasUnclusteredVariant": null,
  "statusSummary": null,
  "statuses": null,
  "checkFrequencies": null,
  "nPassesValues": null,
  "lastCheckedAt": null,
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
  "positivityIndex": null,
  "trendPositivity": null,
  "mentionRate": null,
  "trendMentionRate": null,
  "serpRate": null,
  "trendSerpRate": null,
  "shareOfVoice": null,
  "trendShareOfVoice": null,
  "sentimentPositive": null,
  "sentimentNeutral": null,
  "sentimentNegative": null,
  "avgMentionCount": null,
  "mentionTypeCounts": null,
} satisfies KeywordListingResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as KeywordListingResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


