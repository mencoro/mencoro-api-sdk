# KeywordListingResourceMentionTypeCounts

Mentions counted in the window by the role the mention plays in the answer. Totals, not averages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation** | **int** |  | [optional] 
**comparison** | **int** |  | [optional] 
**listing** | **int** |  | [optional] 
**example** | **int** |  | [optional] 
**reference** | **int** |  | [optional] 

## Example

```python
from mencoro.models.keyword_listing_resource_mention_type_counts import KeywordListingResourceMentionTypeCounts

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordListingResourceMentionTypeCounts from a JSON string
keyword_listing_resource_mention_type_counts_instance = KeywordListingResourceMentionTypeCounts.from_json(json)
# print the JSON string representation of the object
print(KeywordListingResourceMentionTypeCounts.to_json())

# convert the object into a dict
keyword_listing_resource_mention_type_counts_dict = keyword_listing_resource_mention_type_counts_instance.to_dict()
# create an instance of KeywordListingResourceMentionTypeCounts from a dict
keyword_listing_resource_mention_type_counts_from_dict = KeywordListingResourceMentionTypeCounts.from_dict(keyword_listing_resource_mention_type_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


