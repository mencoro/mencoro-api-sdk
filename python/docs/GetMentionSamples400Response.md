# GetMentionSamples400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Machine-readable reason. &#x60;validation_error&#x60; when the request was rejected; otherwise the domain error code. | 
**message** | **str** | Human-readable reason. A 4xx carries the real message; a 5xx carries a fixed sentence and the detail goes to the logs only. | 
**request_id** | **UUID** | Correlation id, also returned in the X-Request-Id header. | 
**details** | **Dict[str, List[GetMentionSamples400ResponseDetailsValueInner]]** | Present only on a validation failure: one entry per rejected field, each an array of errors. | [optional] 

## Example

```python
from mencoro.models.get_mention_samples400_response import GetMentionSamples400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMentionSamples400Response from a JSON string
get_mention_samples400_response_instance = GetMentionSamples400Response.from_json(json)
# print the JSON string representation of the object
print(GetMentionSamples400Response.to_json())

# convert the object into a dict
get_mention_samples400_response_dict = get_mention_samples400_response_instance.to_dict()
# create an instance of GetMentionSamples400Response from a dict
get_mention_samples400_response_from_dict = GetMentionSamples400Response.from_dict(get_mention_samples400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


