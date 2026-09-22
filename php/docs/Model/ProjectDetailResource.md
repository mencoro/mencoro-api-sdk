# ProjectDetailResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**organization_id** | **string** |  |
**name** | **string** |  |
**status** | **string** |  |
**created_at** | **\DateTime** |  |
**website_domains** | **string[]** | Domains the project is monitored for. Empty when the project has no brand monitoring profile yet. |
**brand_names** | **string[]** | Brand names matched in AI answers and search results. Empty when the project has no brand monitoring profile yet. |
**competitors** | [**\Mencoro\Api\Model\ProjectDetailResourceCompetitorsInner[]**](ProjectDetailResourceCompetitorsInner.md) | Competitors this project is measured against. Empty when none are configured. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
