
# CitedSourceRow


## Properties

Name | Type
------------ | -------------
`groupKey` | string
`domain` | string
`citationCount` | number
`distinctQueryCount` | number
`distinctResponseCount` | number
`avgPosition` | number
`sampleTitle` | string
`sampleUrl` | string

## Example

```typescript
import type { CitedSourceRow } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "groupKey": null,
  "domain": null,
  "citationCount": null,
  "distinctQueryCount": null,
  "distinctResponseCount": null,
  "avgPosition": null,
  "sampleTitle": null,
  "sampleUrl": null,
} satisfies CitedSourceRow

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CitedSourceRow
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


