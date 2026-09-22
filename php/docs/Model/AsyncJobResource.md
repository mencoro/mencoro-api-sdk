# AsyncJobResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **string** |  |
**type** | **string** | What the job produces, and therefore the shape of &#x60;result&#x60; |
**status** | **string** | A job in &#x60;pending&#x60;, &#x60;running&#x60; or &#x60;awaiting_retry&#x60; is still in flight; &#x60;completed&#x60; and &#x60;failed&#x60; are terminal. |
**result** | **object** | The job output, shaped by &#x60;type&#x60;. Null while the job is still in flight and for a job that failed: it means the result is not known, never that the job produced nothing. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
