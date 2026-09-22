# GetShareOfVoiceFormula200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mention_type_weights** | **array<string,float>** | Base weight per mention type; higher means a structurally stronger brand association. | [optional]
**sentiment_multipliers** | **array<string,float>** | Multiplier per tone, applied on top of the base weight. | [optional]
**direct_multiplier** | **float** | Applied when the mention carries no condition. | [optional]
**conditional_multiplier** | **float** | Applied instead when the answer hedged the mention with a condition. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
