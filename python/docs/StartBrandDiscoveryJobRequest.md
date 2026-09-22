# StartBrandDiscoveryJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shopping_enabled** | **bool** | Adds a shopping discovery pass. Set it only for a project that tracks a shopping engine: on any other project the pass spends provider budget on results nothing will use. | [optional] [default to False]
**country** | **str** | ISO 3166-1 alpha-2 country used to localize the discovery. | [optional] 

## Example

```python
from mencoro.models.start_brand_discovery_job_request import StartBrandDiscoveryJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartBrandDiscoveryJobRequest from a JSON string
start_brand_discovery_job_request_instance = StartBrandDiscoveryJobRequest.from_json(json)
# print the JSON string representation of the object
print(StartBrandDiscoveryJobRequest.to_json())

# convert the object into a dict
start_brand_discovery_job_request_dict = start_brand_discovery_job_request_instance.to_dict()
# create an instance of StartBrandDiscoveryJobRequest from a dict
start_brand_discovery_job_request_from_dict = StartBrandDiscoveryJobRequest.from_dict(start_brand_discovery_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


