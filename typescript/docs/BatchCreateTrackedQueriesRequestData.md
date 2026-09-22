
# BatchCreateTrackedQueriesRequestData

Tracked queries to create, as a cross product of texts, engines and countries

## Properties

Name | Type
------------ | -------------
`queryTexts` | Array&lt;string&gt;
`engines` | Array&lt;string&gt;
`countries` | Array&lt;string&gt;
`locale` | string
`checkFrequency` | string
`nPasses` | number
`queryClusterIds` | Array&lt;string&gt;

## Example

```typescript
import type { BatchCreateTrackedQueriesRequestData } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "queryTexts": null,
  "engines": null,
  "countries": null,
  "locale": null,
  "checkFrequency": null,
  "nPasses": null,
  "queryClusterIds": null,
} satisfies BatchCreateTrackedQueriesRequestData

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BatchCreateTrackedQueriesRequestData
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


