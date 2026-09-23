
# CompetitorCoOccurrenceRow


## Properties

Name | Type
------------ | -------------
`competitorId` | string
`sharedResponseCount` | number
`brandWins` | number
`competitorWins` | number
`ties` | number
`winRate` | number
`avgOwnPosition` | number
`avgCompetitorPosition` | number
`exampleQueryText` | string
`exampleAiResponseId` | string

## Example

```typescript
import type { CompetitorCoOccurrenceRow } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "competitorId": null,
  "sharedResponseCount": null,
  "brandWins": null,
  "competitorWins": null,
  "ties": null,
  "winRate": null,
  "avgOwnPosition": null,
  "avgCompetitorPosition": null,
  "exampleQueryText": null,
  "exampleAiResponseId": null,
} satisfies CompetitorCoOccurrenceRow

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CompetitorCoOccurrenceRow
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


