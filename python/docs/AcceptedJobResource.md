# AcceptedJobResource

Background work accepted for processing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **UUID** | The job to poll. May name a job started by an earlier, equivalent request. | 
**deduplicated** | **bool** | Whether this call started the job, or joined one that was already running | 
**tracking_url** | **str** | Poll this until the job reaches a terminal status | 

## Example

```python
from mencoro.models.accepted_job_resource import AcceptedJobResource

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedJobResource from a JSON string
accepted_job_resource_instance = AcceptedJobResource.from_json(json)
# print the JSON string representation of the object
print(AcceptedJobResource.to_json())

# convert the object into a dict
accepted_job_resource_dict = accepted_job_resource_instance.to_dict()
# create an instance of AcceptedJobResource from a dict
accepted_job_resource_from_dict = AcceptedJobResource.from_dict(accepted_job_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


