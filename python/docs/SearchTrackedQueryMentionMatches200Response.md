# SearchTrackedQueryMentionMatches200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MentionMatchResource]**](MentionMatchResource.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mencoro.models.search_tracked_query_mention_matches200_response import SearchTrackedQueryMentionMatches200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTrackedQueryMentionMatches200Response from a JSON string
search_tracked_query_mention_matches200_response_instance = SearchTrackedQueryMentionMatches200Response.from_json(json)
# print the JSON string representation of the object
print(SearchTrackedQueryMentionMatches200Response.to_json())

# convert the object into a dict
search_tracked_query_mention_matches200_response_dict = search_tracked_query_mention_matches200_response_instance.to_dict()
# create an instance of SearchTrackedQueryMentionMatches200Response from a dict
search_tracked_query_mention_matches200_response_from_dict = SearchTrackedQueryMentionMatches200Response.from_dict(search_tracked_query_mention_matches200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


