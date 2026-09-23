

# MentionSampleResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**trackedQueryId** | **String** |  |  |
|**aiResponseId** | **String** |  |  |
|**engine** | **String** |  |  |
|**competitorId** | **String** |  |  [optional] |
|**sentiment** | **String** |  |  |
|**mentionType** | **String** |  |  |
|**mentionPosition** | **Integer** |  |  |
|**text** | **String** |  |  |
|**detectedAt** | **String** |  |  |
|**queryText** | **String** |  |  |
|**country** | **String** |  |  [optional] |
|**mentionRelation** | **String** | Published because &#x60;competitorId&#x60; alone cannot answer the question. Own-brand AND untracked-competitor mentions both carry a null competitor id - the confusion migration Version20260608130000 was written to end - so a reader that treats a null competitor id as \&quot;us\&quot; silently counts a rival as the brand. |  [optional] |
|**brandName** | **String** |  |  [optional] |



