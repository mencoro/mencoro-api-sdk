

# AcceptedJobResource

Background work accepted for processing

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobId** | **UUID** | The job to poll. May name a job started by an earlier, equivalent request. |  |
|**deduplicated** | **Boolean** | Whether this call started the job, or joined one that was already running |  |
|**trackingUrl** | **URI** | Poll this until the job reaches a terminal status |  |



