

# GetMetricGlossary200ResponseMetricsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metric** | **String** |  |  [optional] |
|**aliases** | **List&lt;String&gt;** |  |  [optional] |
|**unit** | **String** |  |  [optional] |
|**range** | **String** |  |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**operation** | **String** | The operationId that returns this metric |  [optional] |
|**exampleQuestions** | **List&lt;String&gt;** |  |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| HIGHER_IS_BETTER | &quot;higher_is_better&quot; |
| LOWER_IS_BETTER | &quot;lower_is_better&quot; |
| N_A | &quot;n/a&quot; |



