# AiResponseResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**project_id** | **string** | The project this capture belongs to |
**tracked_query_id** | **string** | The tracked query that was asked |
**engine** | **string** | The AI engine that answered |
**response_text** | **string** | The full answer text as the engine produced it |
**citations** | [**\Mencoro\Api\Model\CitationResource[]**](CitationResource.md) | Sources the engine cited, in the order it cited them |
**captured_at** | **\DateTime** | When the answer was captured, UTC |
**engineModelName** | **string** | Engine-reported model, when it reported one. Absent on captures taken before engines exposed it | [optional]
**pass_index** | **int** | Which sampling pass of the run this answer is, starting at 0 |
**pass_count** | **int** | How many passes that run took. Rows of one run share trackedQueryId and capturedAt |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
