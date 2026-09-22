# Mencoro.Api.Api.OrganizationsApi

All URIs are relative to *https://api.mencoro.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ArchiveOrganization**](OrganizationsApi.md#archiveorganization) | **POST** /api/v1/organizations/{organizationId}/archive | Archive an organization |
| [**CountOrganizationTrackedQueries**](OrganizationsApi.md#countorganizationtrackedqueries) | **GET** /api/v1/organizations/{organizationId}/usage/tracked-queries | Count the tracked queries an organization has configured |
| [**CreateOrganization**](OrganizationsApi.md#createorganization) | **POST** /api/v1/organizations | Create an organization |
| [**GetEntitlements**](OrganizationsApi.md#getentitlements) | **GET** /api/v1/organizations/{organizationId}/entitlements | Get an organization&#39;s plan allowance and consumption |
| [**GetMembershipStats**](OrganizationsApi.md#getmembershipstats) | **GET** /api/v1/organizations/{organizationId}/membership-stats | Membership, project and invitation counts for an organization |
| [**GetOrganization**](OrganizationsApi.md#getorganization) | **GET** /api/v1/organizations/{organizationId} | Get an organization |
| [**GetOrganizationProjectedMonthlyChecks**](OrganizationsApi.md#getorganizationprojectedmonthlychecks) | **GET** /api/v1/organizations/{organizationId}/usage/projected-monthly-checks | Project a month of check consumption from the current tracking configuration |
| [**GetOrganizationStats**](OrganizationsApi.md#getorganizationstats) | **GET** /api/v1/organizations/{organizationId}/stats | Headline counts for an organization |
| [**ListOrganizations**](OrganizationsApi.md#listorganizations) | **GET** /api/v1/organizations | List accessible organizations |
| [**RestoreOrganization**](OrganizationsApi.md#restoreorganization) | **POST** /api/v1/organizations/{organizationId}/restore | Restore an archived organization |
| [**UpdateOrganization**](OrganizationsApi.md#updateorganization) | **PATCH** /api/v1/organizations/{organizationId} | Update an organization profile |

<a id="archiveorganization"></a>
# **ArchiveOrganization**
> OrganizationResource ArchiveOrganization (Guid organizationId, string xMencoroConfirmation, string idempotencyKey)

Archive an organization

Minimum role: owner. Archiving also archives the active projects of the organization, cancels its pending invitations and cancels its subscription at the end of the current billing period. Those effects are applied by background subscribers, so a 200 means the organization was archived, not that every effect has finished. Preview it first to see exactly what will be touched.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class ArchiveOrganizationExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var xMencoroConfirmation = mencoro_conf_VmajQznkILZjvFf63JexmT1AKX7iYZjOGSrBZYxlUTk;  // string | The `confirmation.token` returned by POST /api/v1/organization-operation-previews for this exact action, organization and body. Single use, valid for five minutes, and bound to the effects the preview declared: if the organization gained a project or lost an invitation in between, it is refused with 409 rather than doing more than was agreed. Without it the call answers 428.
            var idempotencyKey = 5c1b8e42-0d7f-4a93-8c61-9b2e4d0a7f38;  // string | Repeat it to retry a lost response. The replay is answered from the record without claiming the confirmation again, so a retry is never refused for presenting a confirmation the first attempt already spent.

            try
            {
                // Archive an organization
                OrganizationResource result = apiInstance.ArchiveOrganization(organizationId, xMencoroConfirmation, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.ArchiveOrganization: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ArchiveOrganizationWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Archive an organization
    ApiResponse<OrganizationResource> response = apiInstance.ArchiveOrganizationWithHttpInfo(organizationId, xMencoroConfirmation, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.ArchiveOrganizationWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **xMencoroConfirmation** | **string** | The &#x60;confirmation.token&#x60; returned by POST /api/v1/organization-operation-previews for this exact action, organization and body. Single use, valid for five minutes, and bound to the effects the preview declared: if the organization gained a project or lost an invitation in between, it is refused with 409 rather than doing more than was agreed. Without it the call answers 428. |  |
| **idempotencyKey** | **string** | Repeat it to retry a lost response. The replay is answered from the record without claiming the confirmation again, so a retry is never refused for presenting a confirmation the first attempt already spent. |  |

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The confirmation is invalid, expired, already used, or its declared effects changed; or the status transition is not allowed |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="countorganizationtrackedqueries"></a>
# **CountOrganizationTrackedQueries**
> TrackedQueryUsageResource CountOrganizationTrackedQueries (Guid organizationId)

Count the tracked queries an organization has configured

Minimum role: viewer. How many tracked queries the organization has configured, counted live in PostgreSQL — the write model — over EVERY project it owns, archived projects included, and over every tracked query in them, active and paused alike. It is deliberately a DIFFERENT number from `aggregate.totalTrackedQueries` in getOrganizationOverview: that one sums a per-project copy held in the Elasticsearch read model and covers ACTIVE projects only, so it excludes archived projects and can lag behind a change that already shows here. Expect the two to disagree and do not treat either as wrong. This figure does reconcile exactly with countTrackedQueries, which counts one project through the same counter in the same store: sum its unfiltered `count` over every project, archived included, and you get this number. For the ACTIVE subset and what it will consume, call getOrganizationProjectedMonthlyChecks, which ranges over the same projects. Do NOT derive the paused count by subtracting one from the other: this number is read live from Postgres while that one is served from a cache invalidated by background subscribers, so the two can disagree while that invalidation catches up and the difference is then a count of nothing. For how many projects this ranges over, read `projects.total` and `projects.active` from getOrganizationStats. The value is never null: 0 means none are configured. This operation takes no query parameters — the population is fixed, and a parameter it cannot honour is rejected with 400 rather than silently ignored.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class CountOrganizationTrackedQueriesExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 

            try
            {
                // Count the tracked queries an organization has configured
                TrackedQueryUsageResource result = apiInstance.CountOrganizationTrackedQueries(organizationId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.CountOrganizationTrackedQueries: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the CountOrganizationTrackedQueriesWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Count the tracked queries an organization has configured
    ApiResponse<TrackedQueryUsageResource> response = apiInstance.CountOrganizationTrackedQueriesWithHttpInfo(organizationId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.CountOrganizationTrackedQueriesWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |

### Return type

[**TrackedQueryUsageResource**](TrackedQueryUsageResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization&#39;s tracked-query count |  -  |
| **400** | A query parameter was sent to an operation that accepts none; the details name it |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="createorganization"></a>
# **CreateOrganization**
> CreateOrganization201Response CreateOrganization (string xMencoroConfirmation, string idempotencyKey, CreateOrganizationRequest createOrganizationRequest)

Create an organization

Requires a key scoped to all organizations and the \"organization:manage\" capability: a key limited to named organizations cannot widen its own reach by creating one. Preview it first and send the confirmation in X-Mencoro-Confirmation together with an Idempotency-Key.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class CreateOrganizationExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var xMencoroConfirmation = "xMencoroConfirmation_example";  // string | 
            var idempotencyKey = "idempotencyKey_example";  // string | 
            var createOrganizationRequest = new CreateOrganizationRequest(); // CreateOrganizationRequest | 

            try
            {
                // Create an organization
                CreateOrganization201Response result = apiInstance.CreateOrganization(xMencoroConfirmation, idempotencyKey, createOrganizationRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.CreateOrganization: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the CreateOrganizationWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Create an organization
    ApiResponse<CreateOrganization201Response> response = apiInstance.CreateOrganizationWithHttpInfo(xMencoroConfirmation, idempotencyKey, createOrganizationRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.CreateOrganizationWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **xMencoroConfirmation** | **string** |  |  |
| **idempotencyKey** | **string** |  |  |
| **createOrganizationRequest** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md) |  |  |

### Return type

[**CreateOrganization201Response**](CreateOrganization201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Organization created. Your owner membership follows asynchronously, so a read immediately afterwards can answer 404 until it lands. |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key is not scoped to all organizations, or lacks \&quot;organization:manage\&quot; |  -  |
| **409** | The confirmation is invalid, expired, already used, or its effects changed |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getentitlements"></a>
# **GetEntitlements**
> EntitlementsResource GetEntitlements (Guid organizationId)

Get an organization's plan allowance and consumption

Minimum role: owner. Returns what the current plan allows, how much of it has been consumed and when the allowance next resets, taken from the most recent subscription contract whether it is running or cancelled. An organization that has never subscribed answers `status: \"none\"` with every budget and consumption field null — null means \"no plan on file, so not known\", which is deliberately distinct from a budget or a consumption of zero. Commercial and provider details (prices, Stripe identifiers, internal tier codes) are not part of this contract.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class GetEntitlementsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 

            try
            {
                // Get an organization's plan allowance and consumption
                EntitlementsResource result = apiInstance.GetEntitlements(organizationId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.GetEntitlements: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetEntitlementsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get an organization's plan allowance and consumption
    ApiResponse<EntitlementsResource> response = apiInstance.GetEntitlementsWithHttpInfo(organizationId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.GetEntitlementsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |

### Return type

[**EntitlementsResource**](EntitlementsResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization&#39;s allowance and consumption |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller owns under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getmembershipstats"></a>
# **GetMembershipStats**
> GetMembershipStats200Response GetMembershipStats (Guid organizationId)

Membership, project and invitation counts for an organization

Minimum role: owner. Pre-computed counts of the organization's members, projects and outstanding invitations, read from a materialized view that is refreshed periodically — `computedAt` says when the snapshot was taken, so a member added since the last refresh is not counted yet. Every count is always an integer and a zero means zero; an organization whose row has not been computed yet answers 404 with code `organization_membership_stats_not_found`, never a body of zeros, so \"none\" and \"not known yet\" are never confused. Counts cover the whole organization, active and inactive alike: `totalMembersCount` includes suspended members, and `totalProjectsCount` includes archived projects. `pendingInvitationsCount` counts only invitations that are still pending and not yet expired.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class GetMembershipStatsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 

            try
            {
                // Membership, project and invitation counts for an organization
                GetMembershipStats200Response result = apiInstance.GetMembershipStats(organizationId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.GetMembershipStats: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetMembershipStatsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Membership, project and invitation counts for an organization
    ApiResponse<GetMembershipStats200Response> response = apiInstance.GetMembershipStatsWithHttpInfo(organizationId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.GetMembershipStatsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |

### Return type

[**GetMembershipStats200Response**](GetMembershipStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization&#39;s membership snapshot |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller owns under this id (code &#x60;organization_not_found&#x60;), or the snapshot has not been computed for it yet (code &#x60;organization_membership_stats_not_found&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getorganization"></a>
# **GetOrganization**
> OrganizationResource GetOrganization (Guid organizationId)

Get an organization

Minimum role: viewer. An organization outside the key's scope, or one the caller is not an active member of, answers 404 - the API never confirms that an inaccessible organization exists.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class GetOrganizationExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 

            try
            {
                // Get an organization
                OrganizationResource result = apiInstance.GetOrganization(organizationId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.GetOrganization: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetOrganizationWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get an organization
    ApiResponse<OrganizationResource> response = apiInstance.GetOrganizationWithHttpInfo(organizationId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.GetOrganizationWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getorganizationprojectedmonthlychecks"></a>
# **GetOrganizationProjectedMonthlyChecks**
> ProjectedMonthlyChecksResource GetOrganizationProjectedMonthlyChecks (Guid organizationId)

Project a month of check consumption from the current tracking configuration

Minimum role: viewer. What the organization's current configuration would consume in a month, in check budget units — the same unit `checkBudget` and `checksAvailable` are counted in by the entitlements operation — so the two are directly comparable when sizing a plan. The arithmetic is published so it can be reproduced rather than trusted: for each ACTIVE tracked query, runs per month (daily 30, weekly 4, monthly 1) multiplied by its nPasses, summed. A weekly query bills 4, not 4.345: a month is modelled as 30 days and 4 weeks, a planning convention rather than a calendar. Take `checkFrequency` and `nPasses` from the tracked-query listing and the arithmetic will match — though the two sides are read from different places and settle at different times: this figure is computed in the Postgres write model and served from a cache that background subscribers invalidate, while that listing reads an Elasticsearch projection. Immediately after a write the two can disagree; neither is wrong, they are catching up. PAUSED queries are excluded from both figures; archived PROJECTS are not — archiving a project does not pause its tracked queries, so they still count here, exactly as they do in countOrganizationTrackedQueries. `activeTrackedQueryCount` describes the same population as that count, minus the paused queries — but do not compute the difference to learn how many are paused: THIS OPERATION IS CACHED and that one is read live, so the two can disagree while the cache is invalidated in the background. This is a projection of the configuration, not a forecast of what will actually be spent: it does not look at the remaining plan budget, does not know which checks will be skipped or retried, and reserves and debits nothing. It is also not the `checkCost` of countTrackedQueries, which prices one round over one project rather than a month over the organization. Both values are never null: 0 means nothing is scheduled. This operation takes no query parameters — the population is fixed, and a parameter it cannot honour is rejected with 400 rather than silently ignored.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class GetOrganizationProjectedMonthlyChecksExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 

            try
            {
                // Project a month of check consumption from the current tracking configuration
                ProjectedMonthlyChecksResource result = apiInstance.GetOrganizationProjectedMonthlyChecks(organizationId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.GetOrganizationProjectedMonthlyChecks: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetOrganizationProjectedMonthlyChecksWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Project a month of check consumption from the current tracking configuration
    ApiResponse<ProjectedMonthlyChecksResource> response = apiInstance.GetOrganizationProjectedMonthlyChecksWithHttpInfo(organizationId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.GetOrganizationProjectedMonthlyChecksWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |

### Return type

[**ProjectedMonthlyChecksResource**](ProjectedMonthlyChecksResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The projected monthly checks and the active tracked queries behind them |  -  |
| **400** | A query parameter was sent to an operation that accepts none; the details name it |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getorganizationstats"></a>
# **GetOrganizationStats**
> GetOrganizationStats200Response GetOrganizationStats (Guid organizationId)

Headline counts for an organization

Minimum role: viewer. Active members, projects (total and active) and pending invitations, in one call. Every value is a count and is always known: 0 means the organization really has none of that thing, and no field is ever null. `members.total` counts ACTIVE memberships only, so a suspended member is not included; `projects.total` counts every project including archived ones, and `projects.active` the non-archived subset. This is a current-state snapshot and takes no date window.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class GetOrganizationStatsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 

            try
            {
                // Headline counts for an organization
                GetOrganizationStats200Response result = apiInstance.GetOrganizationStats(organizationId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.GetOrganizationStats: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetOrganizationStatsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Headline counts for an organization
    ApiResponse<GetOrganizationStats200Response> response = apiInstance.GetOrganizationStatsWithHttpInfo(organizationId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.GetOrganizationStatsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |

### Return type

[**GetOrganizationStats200Response**](GetOrganizationStats200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization counts |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |
| **404** | No organization the caller can access under this id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="listorganizations"></a>
# **ListOrganizations**
> ListOrganizations200Response ListOrganizations (int? limit = null, int? offset = null, string? search = null, string? status = null, string? sortBy = null, string? sortOrder = null)

List accessible organizations

Returns the organizations the key's owner is an active member of, narrowed to the key's scope. A key scoped to all organizations also sees organizations joined after it was created.Send `Accept: text/csv` to receive the same page as a CSV download instead of JSON: same filters, same authorization, same page window and the same maximum of 100 rows — it is this page in another format, not a bulk export, so a whole collection is still read by paging. The CSV carries no `total`, because a table whose every row is a record has nowhere to put one; read it from the JSON representation of the same request. Cells beginning with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet treats them as text rather than running them as formulas.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class ListOrganizationsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var limit = 20;  // int? |  (optional)  (default to 20)
            var offset = 0;  // int? |  (optional)  (default to 0)
            var search = "search_example";  // string? |  (optional) 
            var status = "active";  // string? |  (optional) 
            var sortBy = "createdAt";  // string? |  (optional)  (default to createdAt)
            var sortOrder = "asc";  // string? |  (optional)  (default to desc)

            try
            {
                // List accessible organizations
                ListOrganizations200Response result = apiInstance.ListOrganizations(limit, offset, search, status, sortBy, sortOrder);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.ListOrganizations: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ListOrganizationsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // List accessible organizations
    ApiResponse<ListOrganizations200Response> response = apiInstance.ListOrganizationsWithHttpInfo(limit, offset, search, status, sortBy, sortOrder);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.ListOrganizationsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **limit** | **int?** |  | [optional] [default to 20] |
| **offset** | **int?** |  | [optional] [default to 0] |
| **search** | **string?** |  | [optional]  |
| **status** | **string?** |  | [optional]  |
| **sortBy** | **string?** |  | [optional] [default to createdAt] |
| **sortOrder** | **string?** |  | [optional] [default to desc] |

### Return type

[**ListOrganizations200Response**](ListOrganizations200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accessible organizations |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the read capability |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="restoreorganization"></a>
# **RestoreOrganization**
> OrganizationResource RestoreOrganization (Guid organizationId, string xMencoroConfirmation, string idempotencyKey)

Restore an archived organization

Minimum role: owner. Restoring reinstates the projects that were archived as part of archiving this organization - projects archived on their own stay archived - and aborts a pending subscription cancellation. Invitations cancelled by the archive are not reinstated. Preview it first to see which effects are reversible.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class RestoreOrganizationExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var xMencoroConfirmation = "xMencoroConfirmation_example";  // string | 
            var idempotencyKey = "idempotencyKey_example";  // string | 

            try
            {
                // Restore an archived organization
                OrganizationResource result = apiInstance.RestoreOrganization(organizationId, xMencoroConfirmation, idempotencyKey);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.RestoreOrganization: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the RestoreOrganizationWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Restore an archived organization
    ApiResponse<OrganizationResource> response = apiInstance.RestoreOrganizationWithHttpInfo(organizationId, xMencoroConfirmation, idempotencyKey);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.RestoreOrganizationWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **xMencoroConfirmation** | **string** |  |  |
| **idempotencyKey** | **string** |  |  |

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The organization in its new state |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The confirmation is invalid, expired, already used, or its declared effects changed; or the status transition is not allowed |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="updateorganization"></a>
# **UpdateOrganization**
> OrganizationResource UpdateOrganization (Guid organizationId, string xMencoroConfirmation, string idempotencyKey, UpdateOrganizationRequest updateOrganizationRequest)

Update an organization profile

Minimum role: owner. A partial update: omit a field to leave it alone, send it as null to clear it. Preview it first; the confirmation is bound to the current values, so an edit made by somebody else in between invalidates it rather than being silently overwritten. The organization image is deliberately NOT writable here, although the Mencoro app accepts one in the equivalent call: a published JSON API is the wrong place to carry a 10MB base64 blob in a body that also has to be fingerprinted for idempotency and digested for the confirmation. The image stays readable as `imageUrl`; changing it is done in the app.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Mencoro.Api.Api;
using Mencoro.Api.Client;
using Mencoro.Api.Model;

namespace Example
{
    public class UpdateOrganizationExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.mencoro.com";
            // Configure Bearer token for authorization: ApiKey
            config.AccessToken = "YOUR_BEARER_TOKEN";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new OrganizationsApi(httpClient, config, httpClientHandler);
            var organizationId = "organizationId_example";  // Guid | 
            var xMencoroConfirmation = "xMencoroConfirmation_example";  // string | 
            var idempotencyKey = "idempotencyKey_example";  // string | 
            var updateOrganizationRequest = new UpdateOrganizationRequest(); // UpdateOrganizationRequest | 

            try
            {
                // Update an organization profile
                OrganizationResource result = apiInstance.UpdateOrganization(organizationId, xMencoroConfirmation, idempotencyKey, updateOrganizationRequest);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling OrganizationsApi.UpdateOrganization: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateOrganizationWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Update an organization profile
    ApiResponse<OrganizationResource> response = apiInstance.UpdateOrganizationWithHttpInfo(organizationId, xMencoroConfirmation, idempotencyKey, updateOrganizationRequest);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OrganizationsApi.UpdateOrganizationWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **organizationId** | **Guid** |  |  |
| **xMencoroConfirmation** | **string** |  |  |
| **idempotencyKey** | **string** |  |  |
| **updateOrganizationRequest** | [**UpdateOrganizationRequest**](UpdateOrganizationRequest.md) |  |  |

### Return type

[**OrganizationResource**](OrganizationResource.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated organization |  -  |
| **401** | Missing or invalid API key |  -  |
| **403** | The key lacks the organization:manage capability |  -  |
| **404** | No organization the caller can access under this id |  -  |
| **409** | The confirmation is invalid, expired, already used, or the organization changed since the preview |  -  |
| **428** | No confirmation was sent; preview the operation first |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

