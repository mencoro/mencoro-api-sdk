# Mencoro::ApplyClusteringJobOutcome

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **successful** | [**Array&lt;ApplyClusteringJobOutcomeSuccessfulInner&gt;**](ApplyClusteringJobOutcomeSuccessfulInner.md) | Tracked queries written, each with the cluster ids it ended up with - the resulting state, not the delta. | [optional] |
| **failed** | [**Array&lt;ApplyClusteringJobOutcomeFailedInner&gt;**](ApplyClusteringJobOutcomeFailedInner.md) | Always present, empty list included: read it rather than inferring success from the status code. | [optional] |
| **clusters** | [**Array&lt;ApplyClusteringJobOutcomeClustersInner&gt;**](ApplyClusteringJobOutcomeClustersInner.md) | Every cluster the assignments referred to, and whether this call created it. | [optional] |
| **skipped_clusters** | [**Array&lt;ApplyClusteringJobOutcomeSkippedClustersInner&gt;**](ApplyClusteringJobOutcomeSkippedClustersInner.md) | Proposed names the store cannot hold. A tracked query whose proposed cluster was skipped ends up with fewer clusters than the proposal showed. | [optional] |
| **unassigned** | **Array&lt;String&gt;** | Tracked queries the job produced no assignment for. Nothing was written for them and they keep the clusters they already had, under every merge mode. | [optional] |

## Example

```ruby
require 'mencoro'

instance = Mencoro::ApplyClusteringJobOutcome.new(
  successful: null,
  failed: null,
  clusters: null,
  skipped_clusters: null,
  unassigned: null
)
```

