# InvitationResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**email** | **string** |  |
**role** | **string** |  |
**state** | **string** |  |
**created_at** | **\DateTime** |  |
**expires_at** | **\DateTime** |  |
**accepted_at** | **\DateTime** |  | [optional]
**project_access_mode** | **string** | Which projects of the organization the invitee reaches on accepting: every project, or only projectIds |
**project_ids** | **string[]** | The projects a selected access reaches, limited to those still in the organization; empty when the mode is all. It may be empty on selected once its projects left the organization, which grants nothing |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
