

# AiResponseResource

One captured AI answer with its citations

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**projectId** | **UUID** | The project this capture belongs to |  |
|**trackedQueryId** | **UUID** | The tracked query that was asked |  |
|**engine** | **String** | The AI engine that answered |  |
|**responseText** | **String** | The full answer text as the engine produced it |  |
|**citations** | [**List&lt;CitationResource&gt;**](CitationResource.md) | Sources the engine cited, in the order it cited them |  |
|**capturedAt** | **OffsetDateTime** | When the answer was captured, UTC |  |
|**modelName** | **String** | Engine-reported model, when it reported one. Absent on captures taken before engines exposed it |  [optional] |
|**passIndex** | **Integer** | Which sampling pass of the run this answer is, starting at 0 |  |
|**passCount** | **Integer** | How many passes that run took. Rows of one run share trackedQueryId and capturedAt |  |



