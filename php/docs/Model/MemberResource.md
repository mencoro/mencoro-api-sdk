# MemberResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**user_id** | **string** | The user this membership belongs to |
**role** | **string** |  |
**state** | **string** |  |
**is_active** | **bool** |  |
**joined_at** | **\DateTime** |  |
**project_access_mode** | **string** | Which projects of the organization the member reaches: every project, or only projectIds |
**project_ids** | **string[]** | The projects a selected access reaches; empty when the mode is all |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
