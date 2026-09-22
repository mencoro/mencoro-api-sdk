
# ShoppingOfferResource

One offer of a captured shopping page

## Properties

Name | Type
------------ | -------------
`rank` | number
`title` | string
`productUrl` | string
`sellerName` | string
`sellerDomain` | string
`productId` | string
`thumbnailUrl` | string
`price` | number
`currency` | string
`rating` | number
`ratingVotes` | number

## Example

```typescript
import type { ShoppingOfferResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "rank": null,
  "title": null,
  "productUrl": null,
  "sellerName": null,
  "sellerDomain": null,
  "productId": null,
  "thumbnailUrl": null,
  "price": null,
  "currency": null,
  "rating": null,
  "ratingVotes": null,
} satisfies ShoppingOfferResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ShoppingOfferResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


