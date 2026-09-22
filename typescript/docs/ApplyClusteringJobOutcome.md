
# ApplyClusteringJobOutcome

Per-tracked-query results of applying a clustering job

## Properties

Name | Type
------------ | -------------
`successful` | [Array&lt;ApplyClusteringJobOutcomeSuccessfulInner&gt;](ApplyClusteringJobOutcomeSuccessfulInner.md)
`failed` | [Array&lt;ApplyClusteringJobOutcomeFailedInner&gt;](ApplyClusteringJobOutcomeFailedInner.md)
`clusters` | [Array&lt;ApplyClusteringJobOutcomeClustersInner&gt;](ApplyClusteringJobOutcomeClustersInner.md)
`skippedClusters` | [Array&lt;ApplyClusteringJobOutcomeSkippedClustersInner&gt;](ApplyClusteringJobOutcomeSkippedClustersInner.md)
`unassigned` | Array&lt;string&gt;

## Example

```typescript
import type { ApplyClusteringJobOutcome } from '@mencoro/api'

// TODO: Update the object below with actual values
const example = {
  "successful": null,
  "failed": null,
  "clusters": null,
  "skippedClusters": null,
  "unassigned": null,
} satisfies ApplyClusteringJobOutcome

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ApplyClusteringJobOutcome
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


