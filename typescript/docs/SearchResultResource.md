
# SearchResultResource

One organic result of a captured search page

## Properties

Name | Type
------------ | -------------
`position` | number
`url` | string
`title` | string
`snippet` | string
`domain` | string
`rating` | number
`ratingVotes` | number
`unresolved` | boolean

## Example

```typescript
import type { SearchResultResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "position": null,
  "url": null,
  "title": null,
  "snippet": null,
  "domain": null,
  "rating": null,
  "ratingVotes": null,
  "unresolved": null,
} satisfies SearchResultResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SearchResultResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


