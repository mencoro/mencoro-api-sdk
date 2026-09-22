
# GetShareOfVoiceFormula200Response


## Properties

Name | Type
------------ | -------------
`mentionTypeWeights` | { [key: string]: number; }
`sentimentMultipliers` | { [key: string]: number; }
`directMultiplier` | number
`conditionalMultiplier` | number

## Example

```typescript
import type { GetShareOfVoiceFormula200Response } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "mentionTypeWeights": null,
  "sentimentMultipliers": null,
  "directMultiplier": null,
  "conditionalMultiplier": null,
} satisfies GetShareOfVoiceFormula200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetShareOfVoiceFormula200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


