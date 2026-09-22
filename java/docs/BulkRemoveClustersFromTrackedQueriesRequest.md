

# BulkRemoveClustersFromTrackedQueriesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ids** | **List&lt;UUID&gt;** | Tracked queries to remove. At most 100 distinct ids; duplicates are collapsed. |  [optional] |
|**queryClusterIds** | **List&lt;UUID&gt;** | Clusters every named tracked query is removed from. All must belong to the project in the path. |  [optional] |



