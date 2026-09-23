
# TrackedQueryMoversResponse


## Properties

Name | Type
------------ | -------------
`rows` | [Array&lt;TrackedQueryMoverRow&gt;](TrackedQueryMoverRow.md)
`total` | number
`dataDirtySince` | string

## Example

```typescript
import type { TrackedQueryMoversResponse } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "rows": null,
  "total": null,
  "dataDirtySince": null,
} satisfies TrackedQueryMoversResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TrackedQueryMoversResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


