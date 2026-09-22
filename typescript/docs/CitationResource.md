
# CitationResource

A source cited inside one AI answer

## Properties

Name | Type
------------ | -------------
`url` | string
`position` | number
`anchorText` | string
`title` | string
`snippet` | string
`publicationDate` | string
`thumbnailUrl` | string
`domain` | string
`sourceName` | string
`unresolved` | boolean

## Example

```typescript
import type { CitationResource } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "url": null,
  "position": null,
  "anchorText": null,
  "title": null,
  "snippet": null,
  "publicationDate": null,
  "thumbnailUrl": null,
  "domain": null,
  "sourceName": null,
  "unresolved": null,
} satisfies CitationResource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CitationResource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


