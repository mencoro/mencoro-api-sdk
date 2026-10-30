
# KeywordListingResourceCarriedPositions

Per engine family, whether the position figure includes a measurement from before the window. An active variant with no check of its engine in the window contributes the brand\'s position in its latest earlier capture, and nothing when the brand was absent from that capture. An entry is null when no variant behind the figure carried. Every other metric stays window-only.

## Properties

Name | Type
------------ | -------------
`serp` | [KeywordListingResourceCarriedPositionsSerp](KeywordListingResourceCarriedPositionsSerp.md)
`shopping` | [KeywordListingResourceCarriedPositionsSerp](KeywordListingResourceCarriedPositionsSerp.md)
`mention` | [KeywordListingResourceCarriedPositionsSerp](KeywordListingResourceCarriedPositionsSerp.md)
`link` | [KeywordListingResourceCarriedPositionsSerp](KeywordListingResourceCarriedPositionsSerp.md)

## Example

```typescript
import type { KeywordListingResourceCarriedPositions } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "serp": null,
  "shopping": null,
  "mention": null,
  "link": null,
} satisfies KeywordListingResourceCarriedPositions

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as KeywordListingResourceCarriedPositions
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


