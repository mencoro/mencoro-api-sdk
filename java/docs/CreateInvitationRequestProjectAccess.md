

# CreateInvitationRequestProjectAccess

Which projects of the organization the invitee reaches once they accept. Omitted or null, they reach every project. An owner always reaches every project, so an owner invitation cannot carry a selection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) |  |  |
|**projectIds** | **List&lt;UUID&gt;** | For selected: at least one and at most 500 projects of the organization. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| SELECTED | &quot;selected&quot; |



