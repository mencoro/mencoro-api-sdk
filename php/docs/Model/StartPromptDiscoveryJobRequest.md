# StartPromptDiscoveryJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **string** | Free text describing the topics to turn into prompts. |
**country** | **string** | ISO 3166-1 alpha-2 country the prompts are asked from. |
**language** | **string** | Language code. Omit to let the provider detect it from the input. | [optional]
**exclude_queries** | **string[]** | Extra queries to keep out of the suggestions for this run. Duplicates are collapsed, after the entry count has been checked against maxItems. The project tracked queries are excluded whether or not this is sent. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
