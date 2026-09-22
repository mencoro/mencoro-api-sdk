# Mencoro.Api.Model.StartKeywordDiscoveryJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Input** | **string** | Free text describing the keywords or topics to expand. | 
**Language** | **string** | Language code. Omit to let the provider detect it from the input. | [optional] 
**Country** | **string** | ISO 3166-1 alpha-2 country. Omit to let the provider infer it. | [optional] 
**ExcludeQueries** | **List&lt;string&gt;** | Extra queries to keep out of the suggestions for this run. Duplicates are collapsed, after the entry count has been checked against maxItems. The project tracked queries are excluded whether or not this is sent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

