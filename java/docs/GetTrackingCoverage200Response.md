

# GetTrackingCoverage200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectId** | **UUID** |  |  [optional] |
|**total** | **Integer** | Every tracked query on the project, whatever its status |  [optional] |
|**active** | **Integer** | Tracked queries currently being checked |  [optional] |
|**paused** | **Integer** | Tracked queries whose checks are suspended |  [optional] |
|**neverChecked** | **Integer** | Active queries that have never run yet |  [optional] |
|**overdue** | **Integer** | Active queries past their check-frequency interval, never-checked ones excluded |  [optional] |
|**sample** | [**List&lt;GetTrackingCoverage200ResponseSampleInner&gt;**](GetTrackingCoverage200ResponseSampleInner.md) | Up to 20 overdue queries, oldest check first |  [optional] |



