
# ProjectSentimentBreakdown


## Properties

Name | Type
------------ | -------------
`perEngine` | [Array&lt;PerEngineSentiment&gt;](PerEngineSentiment.md)
`perCompetitor` | [Array&lt;PerCompetitorSentiment&gt;](PerCompetitorSentiment.md)

## Example

```typescript
import type { ProjectSentimentBreakdown } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "perEngine": null,
  "perCompetitor": null,
} satisfies ProjectSentimentBreakdown

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectSentimentBreakdown
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


