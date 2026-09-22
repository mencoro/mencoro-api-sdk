# AsyncJobResource

An asynchronous job and, once it has completed, its result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **UUID** |  | 
**type** | **str** | What the job produces, and therefore the shape of &#x60;result&#x60; | 
**status** | **str** | A job in &#x60;pending&#x60;, &#x60;running&#x60; or &#x60;awaiting_retry&#x60; is still in flight; &#x60;completed&#x60; and &#x60;failed&#x60; are terminal. | 
**result** | **object** | The job output, shaped by &#x60;type&#x60;. Null while the job is still in flight and for a job that failed: it means the result is not known, never that the job produced nothing. | [optional] 

## Example

```python
from mencoro.models.async_job_resource import AsyncJobResource

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncJobResource from a JSON string
async_job_resource_instance = AsyncJobResource.from_json(json)
# print the JSON string representation of the object
print(AsyncJobResource.to_json())

# convert the object into a dict
async_job_resource_dict = async_job_resource_instance.to_dict()
# create an instance of AsyncJobResource from a dict
async_job_resource_from_dict = AsyncJobResource.from_dict(async_job_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


