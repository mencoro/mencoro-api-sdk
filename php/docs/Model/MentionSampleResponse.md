# MentionSampleResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**tracked_query_id** | **string** |  |
**ai_response_id** | **string** |  |
**engine** | **string** |  |
**competitor_id** | **string** |  | [optional]
**sentiment** | **string** |  |
**mention_type** | **string** |  |
**mention_position** | **int** |  |
**text** | **string** |  |
**detected_at** | **string** |  |
**query_text** | **string** |  |
**country** | **string** |  | [optional]
**mention_relation** | **string** | Published because &#x60;competitorId&#x60; alone cannot answer the question. Own-brand AND untracked-competitor mentions both carry a null competitor id - the confusion migration Version20260608130000 was written to end - so a reader that treats a null competitor id as \&quot;us\&quot; silently counts a rival as the brand. | [optional]
**brand_name** | **string** |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
