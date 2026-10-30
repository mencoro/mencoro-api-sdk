# Mencoro.Api.Model.GetOrganizationOverview200ResponseProjectsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectId** | **Guid** |  | [optional] 
**Name** | **string** |  | [optional] 
**Status** | **string** |  | [optional] 
**TrackedQueryCount** | **int** | Configured tracked queries of the project, paused ones included. | [optional] 
**AiTrackedQueryCount** | **int** | How many of trackedQueryCount run on an AI answer engine (ChatGPT, Claude, Perplexity, Google AI Overview, Google AI Mode). | [optional] 
**SerpTrackedQueryCount** | **int** | How many of trackedQueryCount run on classic Google SERP. | [optional] 
**ShoppingTrackedQueryCount** | **int** | How many of trackedQueryCount run on Google Shopping. | [optional] 
**ShareOfVoice** | **float?** | 0-100 percentage share of weighted AI mentions against all tracked brands; higher is better. Null when the project has no rank data yet. | [optional] 
**MentionRate** | **int?** | 0-100 percentage of AI checks (one per tracked query x engine x UTC day) across all retained data that mentioned the brand, each check counted as the share of its passes that did; higher is better. Null when the project has no rank data yet. | [optional] 
**AvgMentionPosition** | **float?** | 1-based average rank of the brand within the answer; LOWER is better. Null when the project has no rank data yet. | [optional] 
**PositivityIndex** | **int?** | 0-100 sentiment score; higher is better. Null when the project has no rank data yet. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

