# AsyncJobResourceError

Why the job failed, and what to do next. Null unless `status` is `failed`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A stable code for the kind of failure: &#x60;timed_out&#x60;, &#x60;provider_failed&#x60;, &#x60;submission_failed&#x60; or &#x60;internal_error&#x60;. | 
**message** | **str** | A fixed, readable explanation of the code. It is the same for every job that failed with that code. | 

## Example

```python
from mencoro.models.async_job_resource_error import AsyncJobResourceError

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncJobResourceError from a JSON string
async_job_resource_error_instance = AsyncJobResourceError.from_json(json)
# print the JSON string representation of the object
print(AsyncJobResourceError.to_json())

# convert the object into a dict
async_job_resource_error_dict = async_job_resource_error_instance.to_dict()
# create an instance of AsyncJobResourceError from a dict
async_job_resource_error_from_dict = AsyncJobResourceError.from_dict(async_job_resource_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


