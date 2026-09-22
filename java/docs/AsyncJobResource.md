

# AsyncJobResource

An asynchronous job and, once it has completed, its result

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobId** | **UUID** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | What the job produces, and therefore the shape of &#x60;result&#x60; |  |
|**status** | [**StatusEnum**](#StatusEnum) | A job in &#x60;pending&#x60;, &#x60;running&#x60; or &#x60;awaiting_retry&#x60; is still in flight; &#x60;completed&#x60; and &#x60;failed&#x60; are terminal. |  |
|**result** | **Object** | The job output, shaped by &#x60;type&#x60;. Null while the job is still in flight and for a job that failed: it means the result is not known, never that the job produced nothing. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GEO_PROMPTS | &quot;geo_prompts&quot; |
| KEYWORDS | &quot;keywords&quot; |
| QUERY_CLUSTERING | &quot;query_clustering&quot; |
| BRAND_DISCOVERY | &quot;brand_discovery&quot; |
| BRAND_NAME_SUGGESTION | &quot;brand_name_suggestion&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| RUNNING | &quot;running&quot; |
| AWAITING_RETRY | &quot;awaiting_retry&quot; |
| COMPLETED | &quot;completed&quot; |
| FAILED | &quot;failed&quot; |



