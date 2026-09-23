# Mencoro.Api.Model.MentionSampleResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**TrackedQueryId** | **string** |  | 
**AiResponseId** | **string** |  | 
**Engine** | **string** |  | 
**CompetitorId** | **string** |  | [optional] 
**Sentiment** | **string** |  | 
**MentionType** | **string** |  | 
**MentionPosition** | **int** |  | 
**Text** | **string** |  | 
**DetectedAt** | **string** |  | 
**QueryText** | **string** |  | 
**Country** | **string** |  | [optional] 
**MentionRelation** | **string** | Published because &#x60;competitorId&#x60; alone cannot answer the question. Own-brand AND untracked-competitor mentions both carry a null competitor id - the confusion migration Version20260608130000 was written to end - so a reader that treats a null competitor id as \&quot;us\&quot; silently counts a rival as the brand. | [optional] 
**BrandName** | **string** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

