# Mencoro.Api.Model.BatchCreateTrackedQueriesRequestData
Tracked queries to create, as a cross product of texts, engines and countries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**QueryTexts** | **List&lt;string&gt;** | Prompts or keywords to track. Stored lower-cased with whitespace collapsed and leading list markers removed. | 
**Engines** | **List&lt;BatchCreateTrackedQueriesRequestData.EnginesEnum&gt;** | Engines each text is asked in. | 
**Countries** | **List&lt;string&gt;** | ISO 3166-1 alpha-2 countries each text is asked from. | 
**Locale** | **string** | ISO 639-1 language the queries are asked in. Omit it to ask the engine without a language. | [optional] 
**CheckFrequency** | **string** | How often every created query is checked. | 
**NPasses** | **int** | Passes run per check. Applied to AI-engine combinations only: a non-AI engine is always created with 1, whatever is sent here. | 
**QueryClusterIds** | **List&lt;Guid&gt;** | Clusters every created query joins. Must already exist in the project. A combination that is already tracked has these clusters merged into it. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

