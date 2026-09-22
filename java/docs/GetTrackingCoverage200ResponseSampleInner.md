

# GetTrackingCoverage200ResponseSampleInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**trackedQueryId** | **UUID** |  |  [optional] |
|**queryText** | **String** |  |  [optional] |
|**engine** | **String** |  |  [optional] |
|**country** | **String** | ISO-3166 alpha-2 code |  [optional] |
|**checkFrequency** | [**CheckFrequencyEnum**](#CheckFrequencyEnum) |  |  [optional] |
|**lastCheckedAt** | **OffsetDateTime** | RFC 3339 timestamp of the last check. Null means never checked, which this sample never contains. |  [optional] |



## Enum: CheckFrequencyEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| MONTHLY | &quot;monthly&quot; |



