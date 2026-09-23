
# TimeSeriesPoint


## Properties

Name | Type
------------ | -------------
`rawDate` | string
`brand` | [PerEntityMetrics](PerEntityMetrics.md)
`competitors` | [{ [key: string]: PerEntityMetrics; }](PerEntityMetrics.md)

## Example

```typescript
import type { TimeSeriesPoint } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "rawDate": null,
  "brand": null,
  "competitors": null,
} satisfies TimeSeriesPoint

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TimeSeriesPoint
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


