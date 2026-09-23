# ProjectSentimentBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_engine** | [**List[PerEngineSentiment]**](PerEngineSentiment.md) |  | 
**per_competitor** | [**List[PerCompetitorSentiment]**](PerCompetitorSentiment.md) |  | 

## Example

```python
from mencoro.models.project_sentiment_breakdown import ProjectSentimentBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSentimentBreakdown from a JSON string
project_sentiment_breakdown_instance = ProjectSentimentBreakdown.from_json(json)
# print the JSON string representation of the object
print(ProjectSentimentBreakdown.to_json())

# convert the object into a dict
project_sentiment_breakdown_dict = project_sentiment_breakdown_instance.to_dict()
# create an instance of ProjectSentimentBreakdown from a dict
project_sentiment_breakdown_from_dict = ProjectSentimentBreakdown.from_dict(project_sentiment_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


