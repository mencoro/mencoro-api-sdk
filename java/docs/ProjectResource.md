

# ProjectResource

A project and its headline metrics

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**trackedQueryCount** | **Integer** | Number of tracked queries in the project |  |
|**avgSerpPosition** | **Float** | Average position in traditional search results. Null when unknown. |  [optional] |
|**avgShoppingPosition** | **Float** | Average position in shopping results. Null when unknown. |  [optional] |
|**avgMentionPosition** | **Float** | Average position of the brand mention inside AI answers. Null when unknown. |  [optional] |
|**avgLinkPosition** | **Float** | Average position of a cited link to the brand. Null when unknown. |  [optional] |
|**mentionRate** | **Integer** | Share of checks where the brand was mentioned. Null when unknown. |  [optional] |
|**serpRate** | **Integer** |  |  [optional] |
|**shoppingRate** | **Integer** |  |  [optional] |
|**positivityIndex** | **Integer** | Sentiment balance of the brand&#39;s mentions. Null when unknown. |  [optional] |
|**shareOfVoice** | **Float** | Share of voice against the tracked competitors. Null when unknown. |  [optional] |
|**serpPositionStability** | **Float** |  |  [optional] |
|**shoppingPositionStability** | **Float** |  |  [optional] |
|**lastRankDetectedAt** | **OffsetDateTime** | When a rank was last detected for this project. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



