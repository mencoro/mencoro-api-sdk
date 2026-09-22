# BatchCreateTrackedQueriesRequestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_texts** | **string[]** | Prompts or keywords to track. Stored lower-cased with whitespace collapsed and leading list markers removed. |
**engines** | **string[]** | Engines each text is asked in. |
**countries** | **string[]** | ISO 3166-1 alpha-2 countries each text is asked from. |
**locale** | **string** | ISO 639-1 language the queries are asked in. Omit it to ask the engine without a language. | [optional]
**check_frequency** | **string** | How often every created query is checked. |
**n_passes** | **int** | Passes run per check. Applied to AI-engine combinations only: a non-AI engine is always created with 1, whatever is sent here. |
**query_cluster_ids** | **string[]** | Clusters every created query joins. Must already exist in the project. A combination that is already tracked has these clusters merged into it. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
