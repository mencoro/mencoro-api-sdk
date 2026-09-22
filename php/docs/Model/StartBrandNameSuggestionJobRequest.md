# StartBrandNameSuggestionJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **string** | The display name of the entity to find aliases for. |
**website_domains** | **string[]** | The entity website domains. At least one is required: the web search is grounded on them, and without one the name alone is ambiguous. Duplicates are collapsed, after the entry count has been checked against maxItems. |
**entered_brand_names** | **string[]** | Names already known, excluded from the suggestions. Duplicates are collapsed, after the entry count has been checked against maxItems. | [optional]
**country** | **string** | ISO 3166-1 alpha-2 country used to localize the web search. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
