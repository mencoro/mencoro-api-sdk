# Mencoro.Api.Model.KeywordListingResource
One keyword of a project, its variants and its metrics over the requested window

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Keyword** | **string** | The keyword as a human types it, picked from the variants for display. | 
**KeywordNormalized** | **string** | The grouping key: the keyword lower-cased and unaccented. Unique within the project, and the stable way to match a row across pages. | 
**VariantCount** | **int** | Tracked queries behind this row that the current filters selected. | 
**VariantIds** | **List&lt;Guid&gt;** | Ids of those tracked queries. Accepted by the single tracked-query operation. | 
**Engines** | **List&lt;KeywordListingResource.EnginesEnum&gt;** | Distinct engines across the variants, not a single engine. | 
**Countries** | **List&lt;string&gt;** | Distinct ISO-3166 alpha-2 countries across the variants. | 
**QueryClusterIds** | **List&lt;Guid&gt;** | Distinct keyword clusters the variants belong to. Empty when none of them is clustered. | 
**HasUnclusteredVariant** | **bool** | Whether at least one variant belongs to no cluster. | 
**StatusSummary** | **string** | \&quot;mixed\&quot; when the variants disagree; otherwise the one status they share. | 
**Statuses** | **List&lt;KeywordListingResource.StatusesEnum&gt;** | Distinct statuses across the variants. | 
**CheckFrequencies** | **List&lt;KeywordListingResource.CheckFrequenciesEnum&gt;** | Distinct check frequencies across the variants. | 
**NPassesValues** | **List&lt;int&gt;** | Distinct pass counts across the variants. A pass is one budget unit per check. | 
**LastCheckedAt** | **DateTime?** | The most recent completed check across the variants. Null when none has ever completed — not a check that found nothing. | [optional] 
**AvgSerpPosition** | **float?** | Average position in traditional search over the window. 1-based, LOWER is better. | [optional] 
**TrendSerp** | **float?** | Signed improvement in avgSerpPosition against the previous window. Positive is better. | [optional] 
**AvgShoppingPosition** | **float?** | Average position in shopping results over the window. 1-based, LOWER is better. | [optional] 
**TrendShopping** | **float?** | Signed improvement in avgShoppingPosition. Positive is better. | [optional] 
**AvgMentionPosition** | **float?** | Average position of the brand mention inside the AI answer. 1-based, LOWER is better. | [optional] 
**TrendMention** | **float?** | Signed improvement in avgMentionPosition. Positive is better. | [optional] 
**AvgLinkPosition** | **float?** | Average position of a cited link to the brand. 1-based, LOWER is better. | [optional] 
**TrendLink** | **float?** | Signed improvement in avgLinkPosition. Positive is better. | [optional] 
**MentionPositionStability** | **float?** | Day-to-day spread of the mention position (a standard deviation): LOWER means steadier. | [optional] 
**TrendStability** | **float?** | Signed improvement in mentionPositionStability. Positive means steadier than the previous window. | [optional] 
**PositivityIndex** | **int?** | 0-100 weighted sentiment score of the mentions; HIGHER is better. Null when there were no mentions to score. | [optional] 
**TrendPositivity** | **int?** | Signed improvement in positivityIndex. Positive is better. | [optional] 
**MentionRate** | **int?** | 0-100 share of AI captures in the window that mentioned the brand; HIGHER is better. | [optional] 
**TrendMentionRate** | **int?** | Signed improvement in mentionRate. Positive is better. | [optional] 
**SerpRate** | **int?** | 0-100 share of traditional-search captures in the window that ranked the brand; HIGHER is better. | [optional] 
**TrendSerpRate** | **int?** | Signed improvement in serpRate. Positive is better. | [optional] 
**ShareOfVoice** | **float?** | 0-100 share of the weighted AI mentions against every tracked brand; HIGHER is better. | [optional] 
**TrendShareOfVoice** | **float?** | Signed improvement in shareOfVoice. Positive is better. | [optional] 
**SentimentPositive** | **int** | Positive brand mentions counted in the window. Zero here really is zero. | 
**SentimentNeutral** | **int** | Neutral brand mentions counted in the window. | 
**SentimentNegative** | **int** | Negative brand mentions counted in the window. | 
**AvgMentionCount** | **float?** | Mentions per AI engine per day with a capture, over the window. Not a total: the window total is not part of this contract. | [optional] 
**MentionTypeCounts** | [**KeywordListingResourceMentionTypeCounts**](KeywordListingResourceMentionTypeCounts.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

