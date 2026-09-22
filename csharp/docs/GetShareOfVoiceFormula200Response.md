# Mencoro.Api.Model.GetShareOfVoiceFormula200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MentionTypeWeights** | **Dictionary&lt;string, float&gt;** | Base weight per mention type; higher means a structurally stronger brand association. | [optional] 
**SentimentMultipliers** | **Dictionary&lt;string, float&gt;** | Multiplier per tone, applied on top of the base weight. | [optional] 
**DirectMultiplier** | **float** | Applied when the mention carries no condition. | [optional] 
**ConditionalMultiplier** | **float** | Applied instead when the answer hedged the mention with a condition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

