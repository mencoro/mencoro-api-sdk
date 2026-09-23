# CitedSourceRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_key** | **str** |  | 
**domain** | **str** |  | [optional] 
**citation_count** | **int** |  | 
**distinct_query_count** | **int** |  | 
**distinct_response_count** | **int** |  | 
**avg_position** | **float** |  | [optional] 
**sample_title** | **str** |  | [optional] 
**sample_url** | **str** |  | 

## Example

```python
from mencoro.models.cited_source_row import CitedSourceRow

# TODO update the JSON string below
json = "{}"
# create an instance of CitedSourceRow from a JSON string
cited_source_row_instance = CitedSourceRow.from_json(json)
# print the JSON string representation of the object
print(CitedSourceRow.to_json())

# convert the object into a dict
cited_source_row_dict = cited_source_row_instance.to_dict()
# create an instance of CitedSourceRow from a dict
cited_source_row_from_dict = CitedSourceRow.from_dict(cited_source_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


