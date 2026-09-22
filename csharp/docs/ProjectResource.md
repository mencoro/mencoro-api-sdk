# Mencoro.Api.Model.ProjectResource
A project and its headline metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Name** | **string** |  | 
**Status** | **string** |  | 
**CreatedAt** | **DateTime** |  | 
**TrackedQueryCount** | **int** | Number of tracked queries in the project | 
**AvgSerpPosition** | **float?** | Average position in traditional search results. Null when unknown. | [optional] 
**AvgShoppingPosition** | **float?** | Average position in shopping results. Null when unknown. | [optional] 
**AvgMentionPosition** | **float?** | Average position of the brand mention inside AI answers. Null when unknown. | [optional] 
**AvgLinkPosition** | **float?** | Average position of a cited link to the brand. Null when unknown. | [optional] 
**MentionRate** | **int?** | Share of checks where the brand was mentioned. Null when unknown. | [optional] 
**SerpRate** | **int?** |  | [optional] 
**ShoppingRate** | **int?** |  | [optional] 
**PositivityIndex** | **int?** | Sentiment balance of the brand&#39;s mentions. Null when unknown. | [optional] 
**ShareOfVoice** | **float?** | Share of voice against the tracked competitors. Null when unknown. | [optional] 
**SerpPositionStability** | **float?** |  | [optional] 
**ShoppingPositionStability** | **float?** |  | [optional] 
**LastRankDetectedAt** | **DateTime?** | When a rank was last detected for this project. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

