
# MentionTypeCounts


## Properties

Name | Type
------------ | -------------
`recommendation` | number
`comparison` | number
`listing` | number
`example` | number
`reference` | number

## Example

```typescript
import type { MentionTypeCounts } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "recommendation": null,
  "comparison": null,
  "listing": null,
  "example": null,
  "reference": null,
} satisfies MentionTypeCounts

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MentionTypeCounts
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


