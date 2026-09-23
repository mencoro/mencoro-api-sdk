
# CitedSourcesResponse


## Properties

Name | Type
------------ | -------------
`sources` | [Array&lt;CitedSourceRow&gt;](CitedSourceRow.md)
`total` | number

## Example

```typescript
import type { CitedSourcesResponse } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "sources": null,
  "total": null,
} satisfies CitedSourcesResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CitedSourcesResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


