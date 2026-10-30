

# SetMemberProjectAccessRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) |  |  |
|**projectIds** | **List&lt;UUID&gt;** | The projects of the organization a selected access reaches: at least one and at most 500. Omit it, or send an empty list, for all. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SELECTED | &quot;selected&quot; |



