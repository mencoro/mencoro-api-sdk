
# GetAvailableFilters200Response


## Properties

Name | Type
------------ | -------------
`engines` | Array&lt;string&gt;
`countries` | Array&lt;string&gt;
`clusters` | [Array&lt;GetAvailableFilters200ResponseClustersInner&gt;](GetAvailableFilters200ResponseClustersInner.md)

## Example

```typescript
import type { GetAvailableFilters200Response } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "engines": null,
  "countries": null,
  "clusters": null,
} satisfies GetAvailableFilters200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GetAvailableFilters200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


