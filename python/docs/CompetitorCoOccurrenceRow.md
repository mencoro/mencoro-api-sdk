# CompetitorCoOccurrenceRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competitor_id** | **str** |  | 
**shared_response_count** | **int** |  | 
**brand_wins** | **int** |  | 
**competitor_wins** | **int** |  | 
**ties** | **int** |  | 
**win_rate** | **int** |  | [optional] 
**avg_own_position** | **float** |  | [optional] 
**avg_competitor_position** | **float** |  | [optional] 
**example_query_text** | **str** |  | [optional] 
**example_ai_response_id** | **str** |  | [optional] 

## Example

```python
from mencoro.models.competitor_co_occurrence_row import CompetitorCoOccurrenceRow

# TODO update the JSON string below
json = "{}"
# create an instance of CompetitorCoOccurrenceRow from a JSON string
competitor_co_occurrence_row_instance = CompetitorCoOccurrenceRow.from_json(json)
# print the JSON string representation of the object
print(CompetitorCoOccurrenceRow.to_json())

# convert the object into a dict
competitor_co_occurrence_row_dict = competitor_co_occurrence_row_instance.to_dict()
# create an instance of CompetitorCoOccurrenceRow from a dict
competitor_co_occurrence_row_from_dict = CompetitorCoOccurrenceRow.from_dict(competitor_co_occurrence_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


