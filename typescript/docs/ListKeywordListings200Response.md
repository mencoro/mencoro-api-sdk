
# ListKeywordListings200Response


## Properties

Name | Type
------------ | -------------
`items` | [Array&lt;KeywordListingResource&gt;](KeywordListingResource.md)
`total` | number
`totalVariantCount` | number
`dataDirtySince` | Date

## Example

```typescript
import type { ListKeywordListings200Response } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "items": null,
  "total": null,
  "totalVariantCount": null,
  "dataDirtySince": null,
} satisfies ListKeywordListings200Response

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ListKeywordListings200Response
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


