

# BatchChangeTrackedQueryCheckFrequencyRequestData

Tracked queries to retune, and the check frequency to set on them

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ids** | **List&lt;UUID&gt;** | Ids of the tracked queries to change. Duplicates are collapsed. |  |
|**checkFrequency** | [**CheckFrequencyEnum**](#CheckFrequencyEnum) | How often each query is checked while it is active. |  |



## Enum: CheckFrequencyEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| MONTHLY | &quot;monthly&quot; |



