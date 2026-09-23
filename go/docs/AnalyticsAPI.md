# \AnalyticsAPI

All URIs are relative to *https://api.mencoro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAvailableFilters**](AnalyticsAPI.md#GetAvailableFilters) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/available-filters | Filter values a project is configured for
[**GetCitedSources**](AnalyticsAPI.md#GetCitedSources) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/cited-sources | Domains and pages the AI answers cited
[**GetClusterBreakdown**](AnalyticsAPI.md#GetClusterBreakdown) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/clusters | Rank-tracking metrics per keyword cluster
[**GetCompetitorCoOccurrence**](AnalyticsAPI.md#GetCompetitorCoOccurrence) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/co-occurrence | Head-to-head record of the brand against each tracked competitor
[**GetMentionMix**](AnalyticsAPI.md#GetMentionMix) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions/mix | Composition of a project brand mentions in AI answers
[**GetMentionSamples**](AnalyticsAPI.md#GetMentionSamples) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions | Sample of the raw AI mention texts of a project
[**GetMetricGlossary**](AnalyticsAPI.md#GetMetricGlossary) | **Get** /api/v1/metric-glossary | Map everyday wording to a metric and the operation that serves it
[**GetOrganizationOverview**](AnalyticsAPI.md#GetOrganizationOverview) | **Get** /api/v1/organizations/{organizationId}/overview | Snapshot rank-health board across an organization active projects
[**GetProjectMetrics**](AnalyticsAPI.md#GetProjectMetrics) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics | Headline visibility metrics of a project
[**GetProjectSentiment**](AnalyticsAPI.md#GetProjectSentiment) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/sentiment | Sentiment breakdown of a project brand mentions
[**GetProjectTimeSeries**](AnalyticsAPI.md#GetProjectTimeSeries) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/timeseries | Rank-tracking metrics of a project over time
[**GetQueryMovers**](AnalyticsAPI.md#GetQueryMovers) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/movers | Tracked queries ranked by how much a metric moved
[**GetShareOfVoiceFormula**](AnalyticsAPI.md#GetShareOfVoiceFormula) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/share-of-voice-formula | The constants behind the Share of Voice score
[**GetTrackedQueryTimeSeries**](AnalyticsAPI.md#GetTrackedQueryTimeSeries) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/timeseries | Rank-tracking time series of a single tracked query
[**GetTrackingCoverage**](AnalyticsAPI.md#GetTrackingCoverage) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/coverage | Coverage and staleness of a project tracked queries
[**ListKeywordListings**](AnalyticsAPI.md#ListKeywordListings) | **Get** /api/v1/organizations/{organizationId}/projects/{projectId}/keyword-listings | List a project&#39;s keywords with their windowed metrics



## GetAvailableFilters

> GetAvailableFilters200Response GetAvailableFilters(ctx, organizationId, projectId).Execute()

Filter values a project is configured for



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetAvailableFilters(context.Background(), organizationId, projectId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetAvailableFilters``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAvailableFilters`: GetAvailableFilters200Response
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetAvailableFilters`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAvailableFiltersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**GetAvailableFilters200Response**](GetAvailableFilters200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCitedSources

> CitedSourcesResponse GetCitedSources(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).GroupBy(groupBy).Limit(limit).Offset(offset).Execute()

Domains and pages the AI answers cited



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d.
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. Only the AI engines carry citations. (optional)
	groupBy := "groupBy_example" // string | Grain of the roll-up: \"domain\" by host, \"page\" by exact URL. (optional) (default to "domain")
	limit := int32(56) // int32 | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
	offset := int32(56) // int32 | Number of sources to skip. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetCitedSources(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).GroupBy(groupBy).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetCitedSources``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCitedSources`: CitedSourcesResponse
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetCitedSources`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCitedSourcesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. | 
 **engines** | **[]string** | Repeatable, or comma-separated. Only the AI engines carry citations. | 
 **groupBy** | **string** | Grain of the roll-up: \&quot;domain\&quot; by host, \&quot;page\&quot; by exact URL. | [default to &quot;domain&quot;]
 **limit** | **int32** | Page size. A larger value is rejected, never silently reduced. | [default to 20]
 **offset** | **int32** | Number of sources to skip. | [default to 0]

### Return type

[**CitedSourcesResponse**](CitedSourcesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetClusterBreakdown

> ProjectRankTrackingClusterBreakdown GetClusterBreakdown(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).QueryClusterIds(queryClusterIds).IncludeUngroupedQueries(includeUngroupedQueries).Execute()

Rank-tracking metrics per keyword cluster



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d.
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. (optional)
	countries := []string{"Inner_example"} // []string | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
	queryClusterIds := []string{"Inner_example"} // []string | Restrict to these clusters. Each must belong to the project. (optional)
	includeUngroupedQueries := true // bool | Sent alone, returns only the ungrouped bucket rather than adding it to every cluster. (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetClusterBreakdown(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).QueryClusterIds(queryClusterIds).IncludeUngroupedQueries(includeUngroupedQueries).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetClusterBreakdown``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetClusterBreakdown`: ProjectRankTrackingClusterBreakdown
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetClusterBreakdown`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetClusterBreakdownRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. | 
 **engines** | **[]string** | Repeatable, or comma-separated. | 
 **countries** | **[]string** | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | 
 **queryClusterIds** | **[]string** | Restrict to these clusters. Each must belong to the project. | 
 **includeUngroupedQueries** | **bool** | Sent alone, returns only the ungrouped bucket rather than adding it to every cluster. | [default to false]

### Return type

[**ProjectRankTrackingClusterBreakdown**](ProjectRankTrackingClusterBreakdown.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCompetitorCoOccurrence

> CompetitorCoOccurrenceResponse GetCompetitorCoOccurrence(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).CompetitorId(competitorId).Execute()

Head-to-head record of the brand against each tracked competitor



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d.
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence. (optional)
	countries := []string{"Inner_example"} // []string | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
	competitorId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetCompetitorCoOccurrence(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).CompetitorId(competitorId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetCompetitorCoOccurrence``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCompetitorCoOccurrence`: CompetitorCoOccurrenceResponse
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetCompetitorCoOccurrence`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCompetitorCoOccurrenceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. | 
 **engines** | **[]string** | Repeatable, or comma-separated. SERP and Shopping carry no AI answer text, so they contribute no co-occurrence. | 
 **countries** | **[]string** | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | 
 **competitorId** | **string** | Restricts the answer to a single tracked competitor. Omit it for every tracked competitor. The available-filters endpoint lists the valid ids. | 

### Return type

[**CompetitorCoOccurrenceResponse**](CompetitorCoOccurrenceResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetMentionMix

> ProjectMentionMixResponse GetMentionMix(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).Execute()

Composition of a project brand mentions in AI answers



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d.
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. Non-AI engines contribute no mentions. (optional)
	countries := []string{"Inner_example"} // []string | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetMentionMix(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetMentionMix``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMentionMix`: ProjectMentionMixResponse
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetMentionMix`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetMentionMixRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. | 
 **engines** | **[]string** | Repeatable, or comma-separated. Non-AI engines contribute no mentions. | 
 **countries** | **[]string** | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | 

### Return type

[**ProjectMentionMixResponse**](ProjectMentionMixResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetMentionSamples

> ProjectMentionSamplesResponse GetMentionSamples(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).Sentiment(sentiment).MentionType(mentionType).CompetitorId(competitorId).SortBy(sortBy).Limit(limit).Offset(offset).Execute()

Sample of the raw AI mention texts of a project



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d.
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. Non-AI engines contribute no mentions. (optional)
	countries := []string{"Inner_example"} // []string | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
	sentiment := "sentiment_example" // string | Restrict to one sentiment label. Omit for every sentiment. (optional)
	mentionType := "mentionType_example" // string | Restrict to one mention type. Omit for every type. (optional)
	competitorId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart. (optional)
	sortBy := "sortBy_example" // string | recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default. (optional) (default to "recent")
	limit := int32(56) // int32 | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
	offset := int32(56) // int32 | Number of matching mentions to skip before the page starts. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetMentionSamples(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).Sentiment(sentiment).MentionType(mentionType).CompetitorId(competitorId).SortBy(sortBy).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetMentionSamples``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMentionSamples`: ProjectMentionSamplesResponse
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetMentionSamples`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetMentionSamplesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. | 
 **engines** | **[]string** | Repeatable, or comma-separated. Non-AI engines contribute no mentions. | 
 **countries** | **[]string** | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | 
 **sentiment** | **string** | Restrict to one sentiment label. Omit for every sentiment. | 
 **mentionType** | **string** | Restrict to one mention type. Omit for every type. | 
 **competitorId** | **string** | UUID of a single competitor, as listed by the available-filters endpoint (competitors[].id). Omitted, the page is restricted to mentions storing no competitor id, which is own-brand and untracked-competitor mentions together — see the operation description and read mentionRelation to tell them apart. | 
 **sortBy** | **string** | recent: newest first. negative: negative sentiment first, then neutral, then positive, newest first inside each. engine and country: grouped alphabetically, newest first inside each group. An unknown value is rejected, not replaced by the default. | [default to &quot;recent&quot;]
 **limit** | **int32** | Page size. A larger value is rejected, never silently reduced. | [default to 20]
 **offset** | **int32** | Number of matching mentions to skip before the page starts. | [default to 0]

### Return type

[**ProjectMentionSamplesResponse**](ProjectMentionSamplesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetMetricGlossary

> GetMetricGlossary200Response GetMetricGlossary(ctx).Execute()

Map everyday wording to a metric and the operation that serves it



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetMetricGlossary(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetMetricGlossary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMetricGlossary`: GetMetricGlossary200Response
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetMetricGlossary`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetMetricGlossaryRequest struct via the builder pattern


### Return type

[**GetMetricGlossary200Response**](GetMetricGlossary200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetOrganizationOverview

> GetOrganizationOverview200Response GetOrganizationOverview(ctx, organizationId).Execute()

Snapshot rank-health board across an organization active projects



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetOrganizationOverview(context.Background(), organizationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetOrganizationOverview``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetOrganizationOverview`: GetOrganizationOverview200Response
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetOrganizationOverview`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetOrganizationOverviewRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetOrganizationOverview200Response**](GetOrganizationOverview200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProjectMetrics

> ProjectRankTrackingStats GetProjectMetrics(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).QueryClusterIds(queryClusterIds).IncludeUngroupedQueries(includeUngroupedQueries).Execute()

Headline visibility metrics of a project



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d.
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. (optional)
	countries := []string{"Inner_example"} // []string | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
	queryClusterIds := []string{"Inner_example"} // []string | Restrict to these keyword clusters. Each must belong to this project. (optional)
	includeUngroupedQueries := true // bool | Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster. (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetProjectMetrics(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).QueryClusterIds(queryClusterIds).IncludeUngroupedQueries(includeUngroupedQueries).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetProjectMetrics``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetProjectMetrics`: ProjectRankTrackingStats
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetProjectMetrics`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectMetricsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. | 
 **engines** | **[]string** | Repeatable, or comma-separated. | 
 **countries** | **[]string** | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | 
 **queryClusterIds** | **[]string** | Restrict to these keyword clusters. Each must belong to this project. | 
 **includeUngroupedQueries** | **bool** | Only meaningful together with queryClusterIds: also counts the tracked queries that belong to no cluster. | [default to false]

### Return type

[**ProjectRankTrackingStats**](ProjectRankTrackingStats.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProjectSentiment

> ProjectSentimentBreakdown GetProjectSentiment(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).QueryClusterIds(queryClusterIds).IncludeUngroupedQueries(includeUngroupedQueries).Execute()

Sentiment breakdown of a project brand mentions



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d.
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. (optional)
	countries := []string{"Inner_example"} // []string | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
	queryClusterIds := []string{"Inner_example"} // []string |  (optional)
	includeUngroupedQueries := true // bool |  (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetProjectSentiment(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).QueryClusterIds(queryClusterIds).IncludeUngroupedQueries(includeUngroupedQueries).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetProjectSentiment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetProjectSentiment`: ProjectSentimentBreakdown
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetProjectSentiment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectSentimentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. | 
 **engines** | **[]string** | Repeatable, or comma-separated. | 
 **countries** | **[]string** | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | 
 **queryClusterIds** | **[]string** |  | 
 **includeUngroupedQueries** | **bool** |  | [default to false]

### Return type

[**ProjectSentimentBreakdown**](ProjectSentimentBreakdown.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProjectTimeSeries

> ProjectRankTrackingTimeSeries GetProjectTimeSeries(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Granularity(granularity).Engines(engines).Countries(countries).QueryClusterIds(queryClusterIds).IncludeUngroupedQueries(includeUngroupedQueries).CompetitorIds(competitorIds).Execute()

Rank-tracking metrics of a project over time



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d.
	granularity := "granularity_example" // string | Bucket size of each point. (optional) (default to "daily")
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. (optional)
	countries := []string{"Inner_example"} // []string | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
	queryClusterIds := []string{"Inner_example"} // []string |  (optional)
	includeUngroupedQueries := true // bool | On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them. (optional) (default to false)
	competitorIds := []string{"Inner_example"} // []string | Repeatable, or comma-separated. Each id adds one series under the competitors map of every point. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetProjectTimeSeries(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Granularity(granularity).Engines(engines).Countries(countries).QueryClusterIds(queryClusterIds).IncludeUngroupedQueries(includeUngroupedQueries).CompetitorIds(competitorIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetProjectTimeSeries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetProjectTimeSeries`: ProjectRankTrackingTimeSeries
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetProjectTimeSeries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectTimeSeriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. | 
 **granularity** | **string** | Bucket size of each point. | [default to &quot;daily&quot;]
 **engines** | **[]string** | Repeatable, or comma-separated. | 
 **countries** | **[]string** | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | 
 **queryClusterIds** | **[]string** |  | 
 **includeUngroupedQueries** | **bool** | On its own this NARROWS the series to tracked queries that belong to no cluster; combined with queryClusterIds it widens those clusters to also cover them. | [default to false]
 **competitorIds** | **[]string** | Repeatable, or comma-separated. Each id adds one series under the competitors map of every point. | 

### Return type

[**ProjectRankTrackingTimeSeries**](ProjectRankTrackingTimeSeries.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetQueryMovers

> TrackedQueryMoversResponse GetQueryMovers(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).SortBy(sortBy).SortOrder(sortOrder).Limit(limit).Offset(offset).Execute()

Tracked queries ranked by how much a metric moved



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d.
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. (optional)
	countries := []string{"Inner_example"} // []string | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
	sortBy := "sortBy_example" // string | Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default. (optional) (default to "trend_share_of_voice")
	sortOrder := "sortOrder_example" // string | desc for the top gainers, asc for the top losers. (optional) (default to "desc")
	limit := int32(56) // int32 | Page size. A value above the maximum is rejected, never clamped. (optional) (default to 20)
	offset := int32(56) // int32 |  (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetQueryMovers(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).SortBy(sortBy).SortOrder(sortOrder).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetQueryMovers``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetQueryMovers`: TrackedQueryMoversResponse
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetQueryMovers`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetQueryMoversRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. The comparison window is the equally long stretch immediately before it. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. | 
 **engines** | **[]string** | Repeatable, or comma-separated. | 
 **countries** | **[]string** | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | 
 **sortBy** | **string** | Which trend delta ranks the rows. Positions improve as they fall, so a positive delta is always an improvement whichever key you pick. An unknown value is rejected, not replaced by the default. | [default to &quot;trend_share_of_voice&quot;]
 **sortOrder** | **string** | desc for the top gainers, asc for the top losers. | [default to &quot;desc&quot;]
 **limit** | **int32** | Page size. A value above the maximum is rejected, never clamped. | [default to 20]
 **offset** | **int32** |  | [default to 0]

### Return type

[**TrackedQueryMoversResponse**](TrackedQueryMoversResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetShareOfVoiceFormula

> GetShareOfVoiceFormula200Response GetShareOfVoiceFormula(ctx, organizationId, projectId).Execute()

The constants behind the Share of Voice score



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetShareOfVoiceFormula(context.Background(), organizationId, projectId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetShareOfVoiceFormula``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetShareOfVoiceFormula`: GetShareOfVoiceFormula200Response
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetShareOfVoiceFormula`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetShareOfVoiceFormulaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**GetShareOfVoiceFormula200Response**](GetShareOfVoiceFormula200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTrackedQueryTimeSeries

> TrackedQueryRankTrackingTimeSeries GetTrackedQueryTimeSeries(ctx, organizationId, projectId, trackedQueryId).DateFrom(dateFrom).DateTo(dateTo).Granularity(granularity).CompetitorIds(competitorIds).Execute()

Rank-tracking time series of a single tracked query



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	trackedQueryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Must belong to the project in the path.
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d.
	granularity := "granularity_example" // string | Bucket size. Prefer weekly or monthly for long windows. (optional) (default to "daily")
	competitorIds := []string{"Inner_example"} // []string | Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetTrackedQueryTimeSeries(context.Background(), organizationId, projectId, trackedQueryId).DateFrom(dateFrom).DateTo(dateTo).Granularity(granularity).CompetitorIds(competitorIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetTrackedQueryTimeSeries``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTrackedQueryTimeSeries`: TrackedQueryRankTrackingTimeSeries
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetTrackedQueryTimeSeries`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 
**trackedQueryId** | **string** | Must belong to the project in the path. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTrackedQueryTimeSeriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. | 
 **granularity** | **string** | Bucket size. Prefer weekly or monthly for long windows. | [default to &quot;daily&quot;]
 **competitorIds** | **[]string** | Competitors to add as extra series, repeatable or comma-separated. Valid ids come from the available-filters endpoint. | 

### Return type

[**TrackedQueryRankTrackingTimeSeries**](TrackedQueryRankTrackingTimeSeries.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTrackingCoverage

> GetTrackingCoverage200Response GetTrackingCoverage(ctx, organizationId, projectId).Execute()

Coverage and staleness of a project tracked queries



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.GetTrackingCoverage(context.Background(), organizationId, projectId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.GetTrackingCoverage``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTrackingCoverage`: GetTrackingCoverage200Response
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.GetTrackingCoverage`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTrackingCoverageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**GetTrackingCoverage200Response**](GetTrackingCoverage200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListKeywordListings

> ListKeywordListings200Response ListKeywordListings(ctx, organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).QueryClusterIds(queryClusterIds).IncludeUngroupedQueries(includeUngroupedQueries).Status(status).CheckFrequencies(checkFrequencies).NPasses(nPasses).Search(search).SortBy(sortBy).SortOrder(sortOrder).Limit(limit).Offset(offset).Execute()

List a project's keywords with their windowed metrics



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/mencoro/mencoro-api-sdk/go"
)

func main() {
	organizationId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	projectId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | 
	dateFrom := time.Now() // string | Inclusive start of the window, Y-m-d. Must fall inside the data retention window.
	dateTo := time.Now() // string | Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom.
	engines := []string{"Engines_example"} // []string | Repeatable, or comma-separated. Narrows which variants count towards each row. (optional)
	countries := []string{"Inner_example"} // []string | ISO-3166 alpha-2 codes or English names. Must be configured on the project. (optional)
	queryClusterIds := []string{"Inner_example"} // []string | Restrict to keywords with a variant in these clusters. Each must belong to the project. (optional)
	includeUngroupedQueries := true // bool | Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection. (optional) (default to false)
	status := "status_example" // string | Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \"mixed\". (optional)
	checkFrequencies := []string{"CheckFrequencies_example"} // []string | Repeatable, or comma-separated. (optional)
	nPasses := []int32{int32(123)} // []int32 | Repeatable, or comma-separated. Restrict to variants configured with these pass counts. (optional)
	search := "search_example" // string | Case-insensitive substring match on the keyword text. (optional)
	sortBy := "sortBy_example" // string | Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default. (optional) (default to "keyword")
	sortOrder := "sortOrder_example" // string |  (optional) (default to "asc")
	limit := int32(56) // int32 | Page size. A larger value is rejected, never silently reduced. (optional) (default to 20)
	offset := int32(56) // int32 | Number of matching keywords to skip before the page starts. (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AnalyticsAPI.ListKeywordListings(context.Background(), organizationId, projectId).DateFrom(dateFrom).DateTo(dateTo).Engines(engines).Countries(countries).QueryClusterIds(queryClusterIds).IncludeUngroupedQueries(includeUngroupedQueries).Status(status).CheckFrequencies(checkFrequencies).NPasses(nPasses).Search(search).SortBy(sortBy).SortOrder(sortOrder).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AnalyticsAPI.ListKeywordListings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListKeywordListings`: ListKeywordListings200Response
	fmt.Fprintf(os.Stdout, "Response from `AnalyticsAPI.ListKeywordListings`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**organizationId** | **string** |  | 
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListKeywordListingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dateFrom** | **string** | Inclusive start of the window, Y-m-d. Must fall inside the data retention window. | 
 **dateTo** | **string** | Inclusive end of the window, Y-m-d. The trend compares against the equally long window ending the day before dateFrom. | 
 **engines** | **[]string** | Repeatable, or comma-separated. Narrows which variants count towards each row. | 
 **countries** | **[]string** | ISO-3166 alpha-2 codes or English names. Must be configured on the project. | 
 **queryClusterIds** | **[]string** | Restrict to keywords with a variant in these clusters. Each must belong to the project. | 
 **includeUngroupedQueries** | **bool** | Sent alone, restricts the listing to keywords whose variants belong to no cluster; sent with queryClusterIds, adds them to that selection. | [default to false]
 **status** | **string** | Restrict to variants with this status. A keyword whose variants disagree still reports statusSummary \&quot;mixed\&quot;. | 
 **checkFrequencies** | **[]string** | Repeatable, or comma-separated. | 
 **nPasses** | **[]int32** | Repeatable, or comma-separated. Restrict to variants configured with these pass counts. | 
 **search** | **string** | Case-insensitive substring match on the keyword text. | 
 **sortBy** | **string** | Named after the field it orders by. Rows with no value for the chosen key sort last in either direction. An unknown key is rejected, not replaced by the default. | [default to &quot;keyword&quot;]
 **sortOrder** | **string** |  | [default to &quot;asc&quot;]
 **limit** | **int32** | Page size. A larger value is rejected, never silently reduced. | [default to 20]
 **offset** | **int32** | Number of matching keywords to skip before the page starts. | [default to 0]

### Return type

[**ListKeywordListings200Response**](ListKeywordListings200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

