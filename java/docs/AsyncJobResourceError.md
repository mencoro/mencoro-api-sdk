

# AsyncJobResourceError

Why the job failed, and what to do next. Null unless `status` is `failed`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | A stable code for the kind of failure: &#x60;timed_out&#x60;, &#x60;provider_failed&#x60;, &#x60;submission_failed&#x60; or &#x60;internal_error&#x60;. |  |
|**message** | **String** | A fixed, readable explanation of the code. It is the same for every job that failed with that code. |  |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| TIMED_OUT | &quot;timed_out&quot; |
| PROVIDER_FAILED | &quot;provider_failed&quot; |
| SUBMISSION_FAILED | &quot;submission_failed&quot; |
| INTERNAL_ERROR | &quot;internal_error&quot; |



