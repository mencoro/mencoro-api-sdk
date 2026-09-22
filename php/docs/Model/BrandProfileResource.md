# BrandProfileResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **string** | The project this profile belongs to |
**brand_names** | **string[]** | The brand terms a mention in an AI answer is matched against. Empty when none has been configured yet. |
**website_domains** | **string[]** | The domains a cited link or a search result is matched against. Empty when none has been configured yet. |
**description** | **string** | What the brand does, as generated from its names and domains. Null means it has not been generated yet, which is not the same as an empty description. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
