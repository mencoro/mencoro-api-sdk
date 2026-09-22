

# GetShareOfVoiceFormula200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mentionTypeWeights** | **Map&lt;String, Float&gt;** | Base weight per mention type; higher means a structurally stronger brand association. |  [optional] |
|**sentimentMultipliers** | **Map&lt;String, Float&gt;** | Multiplier per tone, applied on top of the base weight. |  [optional] |
|**directMultiplier** | **Float** | Applied when the mention carries no condition. |  [optional] |
|**conditionalMultiplier** | **Float** | Applied instead when the answer hedged the mention with a condition. |  [optional] |



