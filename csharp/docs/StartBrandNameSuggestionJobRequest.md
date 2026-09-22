# Mencoro.Api.Model.StartBrandNameSuggestionJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | The display name of the entity to find aliases for. | 
**WebsiteDomains** | **List&lt;string&gt;** | The entity website domains. At least one is required: the web search is grounded on them, and without one the name alone is ambiguous. Duplicates are collapsed, after the entry count has been checked against maxItems. | 
**EnteredBrandNames** | **List&lt;string&gt;** | Names already known, excluded from the suggestions. Duplicates are collapsed, after the entry count has been checked against maxItems. | [optional] 
**Country** | **string** | ISO 3166-1 alpha-2 country used to localize the web search. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

