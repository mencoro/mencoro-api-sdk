# Mencoro.Api.Model.TrackedQueryResource
A tracked query and the metrics of its most recent check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**QueryText** | **string** | The keyword or prompt being tracked | 
**Engine** | **string** |  | 
**Country** | **string** | ISO-3166 alpha-2 country code the query is tracked in | 
**Status** | **string** |  | 
**QueryClusterIds** | **List&lt;Guid&gt;** | Ids of the keyword clusters this query belongs to | 
**CheckFrequency** | **string** | How often the query is checked | 
**NPasses** | **int** | How many times the query is asked per check | 
**LastSerpPosition** | **int?** | Position in traditional search results at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**LastMentionPosition** | **int?** | Position of the brand mention inside the AI answer at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**LastLinkPosition** | **int?** | Position of a cited link to the brand at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**LastShoppingPosition** | **int?** | Position in shopping results at the last check. 1-based, LOWER is better. Null when not known yet. | [optional] 
**LastShareOfVoice** | **float?** | 0-100 share of the weighted AI mentions against every tracked brand; HIGHER is better. Null when not known yet, which is not a share of zero. | [optional] 
**LastPositivityIndex** | **int?** | 0-100 sentiment score of the brand mentions; HIGHER is better. Null when there were no mentions to score, which is not a score of zero. | [optional] 
**LastPositiveMentionCount** | **int?** | Positive brand mentions at the last check. Null when not known yet. | [optional] 
**LastNeutralMentionCount** | **int?** | Neutral brand mentions at the last check. Null when not known yet. | [optional] 
**LastNegativeMentionCount** | **int?** | Negative brand mentions at the last check. Null when not known yet. | [optional] 
**LastCheckedAt** | **DateTime?** | When the query was last checked. Null when it never has been. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

