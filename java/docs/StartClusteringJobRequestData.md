

# StartClusteringJobRequestData

What a clustering job should group, and how

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**trackedQueryIds** | **List&lt;UUID&gt;** | The tracked queries to cluster. Duplicates are collapsed. |  |
|**mode** | [**ModeEnum**](#ModeEnum) | fill_gaps groups only tracked queries that belong to no cluster; add_on_top adds the new clusters to whatever each query already has; full_regroup replaces the current clusters with the job&#39;s. |  |
|**restrictToExistingClusters** | **Boolean** | When true the job may only use clusters the project already has, and leaves a query ungrouped rather than inventing a name for it. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| FILL_GAPS | &quot;fill_gaps&quot; |
| FULL_REGROUP | &quot;full_regroup&quot; |
| ADD_ON_TOP | &quot;add_on_top&quot; |



