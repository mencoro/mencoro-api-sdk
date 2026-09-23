# CompetitorCoOccurrenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competitors** | [**List[CompetitorCoOccurrenceRow]**](CompetitorCoOccurrenceRow.md) |  | 

## Example

```python
from mencoro.models.competitor_co_occurrence_response import CompetitorCoOccurrenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompetitorCoOccurrenceResponse from a JSON string
competitor_co_occurrence_response_instance = CompetitorCoOccurrenceResponse.from_json(json)
# print the JSON string representation of the object
print(CompetitorCoOccurrenceResponse.to_json())

# convert the object into a dict
competitor_co_occurrence_response_dict = competitor_co_occurrence_response_instance.to_dict()
# create an instance of CompetitorCoOccurrenceResponse from a dict
competitor_co_occurrence_response_from_dict = CompetitorCoOccurrenceResponse.from_dict(competitor_co_occurrence_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


