# OpenAPIClient-php

Public API for Mencoro customers. Authenticate with an API key: `Authorization: Bearer mencoro_sk_...`.

For more information, please visit [https://mencoro.com/contact/](https://mencoro.com/contact/).

## Installation & Usage

### Requirements

PHP 8.1 and later.

### Composer

To install the bindings via [Composer](https://getcomposer.org/), add the following to `composer.json`:

```json
{
  "repositories": [
    {
      "type": "vcs",
      "url": "https://github.com/mencoro/mencoro-api-sdk.git"
    }
  ],
  "require": {
    "mencoro/mencoro-api-sdk": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
<?php
require_once('/path/to/OpenAPIClient-php/vendor/autoload.php');
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



// Configure Bearer authorization: ApiKey
$config = Mencoro\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Mencoro\Api\Api\AccountApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getMe();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountApi->getMe: ', $e->getMessage(), PHP_EOL;
}

```

## API Endpoints

All URIs are relative to *https://api.mencoro.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**getMe**](docs/Api/AccountApi.md#getme) | **GET** /api/v1/me | Get the authenticated identity
*AccountApi* | [**getMeStats**](docs/Api/AccountApi.md#getmestats) | **GET** /api/v1/me/stats | Counts across everything the key can reach
*AnalyticsApi* | [**getAvailableFilters**](docs/Api/AnalyticsApi.md#getavailablefilters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/available-filters | Filter values a project is configured for
*AnalyticsApi* | [**getCitedSources**](docs/Api/AnalyticsApi.md#getcitedsources) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/cited-sources | Domains and pages the AI answers cited
*AnalyticsApi* | [**getClusterBreakdown**](docs/Api/AnalyticsApi.md#getclusterbreakdown) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/clusters | Rank-tracking metrics per keyword cluster
*AnalyticsApi* | [**getCompetitorCoOccurrence**](docs/Api/AnalyticsApi.md#getcompetitorcooccurrence) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/co-occurrence | Head-to-head record of the brand against each tracked competitor
*AnalyticsApi* | [**getMentionMix**](docs/Api/AnalyticsApi.md#getmentionmix) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions/mix | Composition of a project brand mentions in AI answers
*AnalyticsApi* | [**getMentionSamples**](docs/Api/AnalyticsApi.md#getmentionsamples) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions | Sample of the raw AI mention texts of a project
*AnalyticsApi* | [**getMetricGlossary**](docs/Api/AnalyticsApi.md#getmetricglossary) | **GET** /api/v1/metric-glossary | Map everyday wording to a metric and the operation that serves it
*AnalyticsApi* | [**getOrganizationOverview**](docs/Api/AnalyticsApi.md#getorganizationoverview) | **GET** /api/v1/organizations/{organizationId}/overview | Snapshot rank-health board across an organization active projects
*AnalyticsApi* | [**getProjectMetrics**](docs/Api/AnalyticsApi.md#getprojectmetrics) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics | Headline visibility metrics of a project
*AnalyticsApi* | [**getProjectSentiment**](docs/Api/AnalyticsApi.md#getprojectsentiment) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/sentiment | Sentiment breakdown of a project brand mentions
*AnalyticsApi* | [**getProjectTimeSeries**](docs/Api/AnalyticsApi.md#getprojecttimeseries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/timeseries | Rank-tracking metrics of a project over time
*AnalyticsApi* | [**getQueryMovers**](docs/Api/AnalyticsApi.md#getquerymovers) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/movers | Tracked queries ranked by how much a metric moved
*AnalyticsApi* | [**getShareOfVoiceFormula**](docs/Api/AnalyticsApi.md#getshareofvoiceformula) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/share-of-voice-formula | The constants behind the Share of Voice score
*AnalyticsApi* | [**getTrackedQueryTimeSeries**](docs/Api/AnalyticsApi.md#gettrackedquerytimeseries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/timeseries | Rank-tracking time series of a single tracked query
*AnalyticsApi* | [**getTrackingCoverage**](docs/Api/AnalyticsApi.md#gettrackingcoverage) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/coverage | Coverage and staleness of a project tracked queries
*AnalyticsApi* | [**listKeywordListings**](docs/Api/AnalyticsApi.md#listkeywordlistings) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/keyword-listings | List a project&#39;s keywords with their windowed metrics
*BillingApi* | [**getSubscription**](docs/Api/BillingApi.md#getsubscription) | **GET** /api/v1/organizations/{organizationId}/subscription | Get the subscription of an organization
*CapturesApi* | [**listAiResponses**](docs/Api/CapturesApi.md#listairesponses) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/ai-responses | List captured AI answers
*CapturesApi* | [**listSearchSnapshots**](docs/Api/CapturesApi.md#listsearchsnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/search-snapshots | List captured search-results pages
*CapturesApi* | [**listShoppingSnapshots**](docs/Api/CapturesApi.md#listshoppingsnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/shopping-snapshots | List captured shopping-results pages
*ClustersApi* | [**applyClusteringJob**](docs/Api/ClustersApi.md#applyclusteringjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs/{jobId}/apply | Apply the result of a clustering job
*ClustersApi* | [**batchCreateQueryClusters**](docs/Api/ClustersApi.md#batchcreatequeryclusters) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/batch | Create several keyword clusters at once
*ClustersApi* | [**createQueryCluster**](docs/Api/ClustersApi.md#createquerycluster) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | Create a keyword cluster
*ClustersApi* | [**deleteQueryCluster**](docs/Api/ClustersApi.md#deletequerycluster) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Delete a keyword cluster
*ClustersApi* | [**getQueryCluster**](docs/Api/ClustersApi.md#getquerycluster) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Get one of a project&#39;s keyword clusters
*ClustersApi* | [**renameQueryCluster**](docs/Api/ClustersApi.md#renamequerycluster) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Rename a keyword cluster
*ClustersApi* | [**startClusteringJob**](docs/Api/ClustersApi.md#startclusteringjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs | Start a keyword clustering job
*DiscoveryApi* | [**startBrandDiscoveryJob**](docs/Api/DiscoveryApi.md#startbranddiscoveryjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/brands | Start a brand discovery job for a project
*DiscoveryApi* | [**startBrandNameSuggestionJob**](docs/Api/DiscoveryApi.md#startbrandnamesuggestionjob) | **POST** /api/v1/organizations/{organizationId}/brand-name-suggestions | Start a brand-name alias suggestion job
*DiscoveryApi* | [**startKeywordDiscoveryJob**](docs/Api/DiscoveryApi.md#startkeyworddiscoveryjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/keywords | Start a keyword discovery job for a project
*DiscoveryApi* | [**startPromptDiscoveryJob**](docs/Api/DiscoveryApi.md#startpromptdiscoveryjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/prompts | Start a geo prompt discovery job for a project
*InvitationsApi* | [**cancelInvitation**](docs/Api/InvitationsApi.md#cancelinvitation) | **POST** /api/v1/organizations/{organizationId}/invitations/{invitationId}/cancel | Cancel a pending invitation
*InvitationsApi* | [**createInvitation**](docs/Api/InvitationsApi.md#createinvitation) | **POST** /api/v1/organizations/{organizationId}/invitations | Invite somebody to an organization
*InvitationsApi* | [**listInvitations**](docs/Api/InvitationsApi.md#listinvitations) | **GET** /api/v1/organizations/{organizationId}/invitations | List an organization&#39;s invitations
*JobsApi* | [**getAsyncJob**](docs/Api/JobsApi.md#getasyncjob) | **GET** /api/v1/organizations/{organizationId}/jobs/{jobId} | Get an asynchronous job
*MembersApi* | [**changeMemberRole**](docs/Api/MembersApi.md#changememberrole) | **PATCH** /api/v1/organizations/{organizationId}/members/{memberId} | Change a member role
*MembersApi* | [**getMember**](docs/Api/MembersApi.md#getmember) | **GET** /api/v1/organizations/{organizationId}/members/{memberId} | Get one organization membership
*MembersApi* | [**listMembers**](docs/Api/MembersApi.md#listmembers) | **GET** /api/v1/organizations/{organizationId}/members | List an organization&#39;s members
*MembersApi* | [**reactivateMember**](docs/Api/MembersApi.md#reactivatemember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/reactivate | Reactivate a suspended member
*MembersApi* | [**suspendMember**](docs/Api/MembersApi.md#suspendmember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/suspend | Suspend a member
*OrganizationOperationsApi* | [**previewOrganizationOperation**](docs/Api/OrganizationOperationsApi.md#previeworganizationoperation) | **POST** /api/v1/organization-operation-previews | Preview an organization operation and obtain a confirmation
*OrganizationsApi* | [**archiveOrganization**](docs/Api/OrganizationsApi.md#archiveorganization) | **POST** /api/v1/organizations/{organizationId}/archive | Archive an organization
*OrganizationsApi* | [**countOrganizationTrackedQueries**](docs/Api/OrganizationsApi.md#countorganizationtrackedqueries) | **GET** /api/v1/organizations/{organizationId}/usage/tracked-queries | Count the tracked queries an organization has configured
*OrganizationsApi* | [**createOrganization**](docs/Api/OrganizationsApi.md#createorganization) | **POST** /api/v1/organizations | Create an organization
*OrganizationsApi* | [**getEntitlements**](docs/Api/OrganizationsApi.md#getentitlements) | **GET** /api/v1/organizations/{organizationId}/entitlements | Get an organization&#39;s plan allowance and consumption
*OrganizationsApi* | [**getMembershipStats**](docs/Api/OrganizationsApi.md#getmembershipstats) | **GET** /api/v1/organizations/{organizationId}/membership-stats | Membership, project and invitation counts for an organization
*OrganizationsApi* | [**getOrganization**](docs/Api/OrganizationsApi.md#getorganization) | **GET** /api/v1/organizations/{organizationId} | Get an organization
*OrganizationsApi* | [**getOrganizationProjectedMonthlyChecks**](docs/Api/OrganizationsApi.md#getorganizationprojectedmonthlychecks) | **GET** /api/v1/organizations/{organizationId}/usage/projected-monthly-checks | Project a month of check consumption from the current tracking configuration
*OrganizationsApi* | [**getOrganizationStats**](docs/Api/OrganizationsApi.md#getorganizationstats) | **GET** /api/v1/organizations/{organizationId}/stats | Headline counts for an organization
*OrganizationsApi* | [**listOrganizations**](docs/Api/OrganizationsApi.md#listorganizations) | **GET** /api/v1/organizations | List accessible organizations
*OrganizationsApi* | [**restoreOrganization**](docs/Api/OrganizationsApi.md#restoreorganization) | **POST** /api/v1/organizations/{organizationId}/restore | Restore an archived organization
*OrganizationsApi* | [**updateOrganization**](docs/Api/OrganizationsApi.md#updateorganization) | **PATCH** /api/v1/organizations/{organizationId} | Update an organization profile
*ProjectsApi* | [**archiveProject**](docs/Api/ProjectsApi.md#archiveproject) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/archive | Archive a project
*ProjectsApi* | [**createCompetitor**](docs/Api/ProjectsApi.md#createcompetitor) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | Add a competitor to a project
*ProjectsApi* | [**createProject**](docs/Api/ProjectsApi.md#createproject) | **POST** /api/v1/organizations/{organizationId}/projects | Create a project and the brand monitoring profile its checks run against
*ProjectsApi* | [**deleteCompetitor**](docs/Api/ProjectsApi.md#deletecompetitor) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Remove a competitor from a project
*ProjectsApi* | [**getBrandProfile**](docs/Api/ProjectsApi.md#getbrandprofile) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Get a project&#39;s brand monitoring profile
*ProjectsApi* | [**getCompetitor**](docs/Api/ProjectsApi.md#getcompetitor) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Get one of a project&#39;s competitors
*ProjectsApi* | [**getProject**](docs/Api/ProjectsApi.md#getproject) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId} | Get a project and its brand monitoring configuration
*ProjectsApi* | [**listCompetitors**](docs/Api/ProjectsApi.md#listcompetitors) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | List the competitors tracked by a project
*ProjectsApi* | [**listProjects**](docs/Api/ProjectsApi.md#listprojects) | **GET** /api/v1/organizations/{organizationId}/projects | List an organization&#39;s projects
*ProjectsApi* | [**listQueryClusters**](docs/Api/ProjectsApi.md#listqueryclusters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | List the keyword clusters of a project
*ProjectsApi* | [**restoreProject**](docs/Api/ProjectsApi.md#restoreproject) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/restore | Restore an archived project
*ProjectsApi* | [**updateCompetitor**](docs/Api/ProjectsApi.md#updatecompetitor) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Replace a competitor
*ProjectsApi* | [**updateProject**](docs/Api/ProjectsApi.md#updateproject) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId} | Rename a project
*ProjectsApi* | [**updateProjectBrandProfile**](docs/Api/ProjectsApi.md#updateprojectbrandprofile) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Replace a project&#39;s brand monitoring profile
*TrackedQueriesApi* | [**addClustersToTrackedQuery**](docs/Api/TrackedQueriesApi.md#addclusterstotrackedquery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Add a tracked query to clusters
*TrackedQueriesApi* | [**batchChangeTrackedQueriesCheckFrequency**](docs/Api/TrackedQueriesApi.md#batchchangetrackedqueriescheckfrequency) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/check-frequency | Change how often several tracked queries are checked
*TrackedQueriesApi* | [**batchChangeTrackedQueriesNPasses**](docs/Api/TrackedQueriesApi.md#batchchangetrackedqueriesnpasses) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/passes | Change how many passes several tracked queries run per check
*TrackedQueriesApi* | [**batchCreateTrackedQueries**](docs/Api/TrackedQueriesApi.md#batchcreatetrackedqueries) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Create tracked queries
*TrackedQueriesApi* | [**batchForceCheckTrackedQueries**](docs/Api/TrackedQueriesApi.md#batchforcechecktrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check | Check several tracked queries now
*TrackedQueriesApi* | [**batchPauseTrackedQueries**](docs/Api/TrackedQueriesApi.md#batchpausetrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/pause | Pause several tracked queries
*TrackedQueriesApi* | [**batchResumeTrackedQueries**](docs/Api/TrackedQueriesApi.md#batchresumetrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/resume | Resume several tracked queries
*TrackedQueriesApi* | [**bulkAddClustersToTrackedQueries**](docs/Api/TrackedQueriesApi.md#bulkaddclusterstotrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Add many tracked queries to clusters
*TrackedQueriesApi* | [**bulkDeleteTrackedQueries**](docs/Api/TrackedQueriesApi.md#bulkdeletetrackedqueries) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk-delete | Delete tracked queries
*TrackedQueriesApi* | [**bulkRemoveClustersFromTrackedQueries**](docs/Api/TrackedQueriesApi.md#bulkremoveclustersfromtrackedqueries) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Remove many tracked queries from clusters
*TrackedQueriesApi* | [**changeTrackedQueryCheckFrequency**](docs/Api/TrackedQueriesApi.md#changetrackedquerycheckfrequency) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/check-frequency | Change how often a tracked query is checked
*TrackedQueriesApi* | [**changeTrackedQueryNPasses**](docs/Api/TrackedQueriesApi.md#changetrackedquerynpasses) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/passes | Change how many passes a tracked query runs per check
*TrackedQueriesApi* | [**countTrackedQueries**](docs/Api/TrackedQueriesApi.md#counttrackedqueries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/count | Count a project&#39;s tracked queries and price checking them
*TrackedQueriesApi* | [**forceCheckAllActiveTrackedQueries**](docs/Api/TrackedQueriesApi.md#forcecheckallactivetrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check-all | Check every eligible tracked query of a project now
*TrackedQueriesApi* | [**getTrackedQuery**](docs/Api/TrackedQueriesApi.md#gettrackedquery) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId} | Get a tracked query
*TrackedQueriesApi* | [**pauseTrackedQuery**](docs/Api/TrackedQueriesApi.md#pausetrackedquery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/pause | Pause a tracked query
*TrackedQueriesApi* | [**removeClustersFromTrackedQuery**](docs/Api/TrackedQueriesApi.md#removeclustersfromtrackedquery) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Remove a tracked query from clusters
*TrackedQueriesApi* | [**reportAiResponse**](docs/Api/TrackedQueriesApi.md#reportairesponse) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/responses/{aiResponseId}/report | Report a problem with a captured AI answer
*TrackedQueriesApi* | [**resumeTrackedQuery**](docs/Api/TrackedQueriesApi.md#resumetrackedquery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/resume | Resume a tracked query
*TrackedQueriesApi* | [**searchTrackedQueries**](docs/Api/TrackedQueriesApi.md#searchtrackedqueries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Search a project&#39;s tracked queries
*TrackedQueriesApi* | [**searchTrackedQueryMentionMatches**](docs/Api/TrackedQueriesApi.md#searchtrackedquerymentionmatches) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/mention-matches | List stored mention matches of a tracked query
*TrackedQueriesApi* | [**searchTrackedQuerySerpMatches**](docs/Api/TrackedQueriesApi.md#searchtrackedqueryserpmatches) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/serp-matches | List stored serp matches of a tracked query

## Models

- [AcceptedJobResource](docs/Model/AcceptedJobResource.md)
- [AiResponseReportResource](docs/Model/AiResponseReportResource.md)
- [AiResponseResource](docs/Model/AiResponseResource.md)
- [ApplyClusteringJobOutcome](docs/Model/ApplyClusteringJobOutcome.md)
- [ApplyClusteringJobOutcomeClustersInner](docs/Model/ApplyClusteringJobOutcomeClustersInner.md)
- [ApplyClusteringJobOutcomeFailedInner](docs/Model/ApplyClusteringJobOutcomeFailedInner.md)
- [ApplyClusteringJobOutcomeSkippedClustersInner](docs/Model/ApplyClusteringJobOutcomeSkippedClustersInner.md)
- [ApplyClusteringJobOutcomeSuccessfulInner](docs/Model/ApplyClusteringJobOutcomeSuccessfulInner.md)
- [AsyncJobResource](docs/Model/AsyncJobResource.md)
- [BatchChangeTrackedQueryCheckFrequencyRequestData](docs/Model/BatchChangeTrackedQueryCheckFrequencyRequestData.md)
- [BatchChangeTrackedQueryPassesRequestData](docs/Model/BatchChangeTrackedQueryPassesRequestData.md)
- [BatchCreateQueryClustersOutcome](docs/Model/BatchCreateQueryClustersOutcome.md)
- [BatchCreateQueryClustersOutcomeFailedInner](docs/Model/BatchCreateQueryClustersOutcomeFailedInner.md)
- [BatchCreateQueryClustersOutcomeSuccessfulInner](docs/Model/BatchCreateQueryClustersOutcomeSuccessfulInner.md)
- [BatchCreateQueryClustersRequestData](docs/Model/BatchCreateQueryClustersRequestData.md)
- [BatchCreateTrackedQueriesRequestData](docs/Model/BatchCreateTrackedQueriesRequestData.md)
- [BatchCreateTrackedQueriesResultResource](docs/Model/BatchCreateTrackedQueriesResultResource.md)
- [BatchCreateTrackedQueriesResultResourceFailedInner](docs/Model/BatchCreateTrackedQueriesResultResourceFailedInner.md)
- [BatchCreateTrackedQueriesResultResourceSuccessfulInner](docs/Model/BatchCreateTrackedQueriesResultResourceSuccessfulInner.md)
- [BatchForceCheckTrackedQueries200Response](docs/Model/BatchForceCheckTrackedQueries200Response.md)
- [BatchForceCheckTrackedQueries200ResponseFailedInner](docs/Model/BatchForceCheckTrackedQueries200ResponseFailedInner.md)
- [BatchPauseTrackedQueries200Response](docs/Model/BatchPauseTrackedQueries200Response.md)
- [BatchPauseTrackedQueries200ResponseFailedInner](docs/Model/BatchPauseTrackedQueries200ResponseFailedInner.md)
- [BatchPauseTrackedQueries200ResponseSuccessfulInner](docs/Model/BatchPauseTrackedQueries200ResponseSuccessfulInner.md)
- [BatchResumeTrackedQueries200Response](docs/Model/BatchResumeTrackedQueries200Response.md)
- [BatchTargetsRequestData](docs/Model/BatchTargetsRequestData.md)
- [BatchWriteOutcome](docs/Model/BatchWriteOutcome.md)
- [BatchWriteOutcomeFailedInner](docs/Model/BatchWriteOutcomeFailedInner.md)
- [BrandProfileResource](docs/Model/BrandProfileResource.md)
- [BulkAddClustersToTrackedQueries200Response](docs/Model/BulkAddClustersToTrackedQueries200Response.md)
- [BulkAddClustersToTrackedQueriesRequest](docs/Model/BulkAddClustersToTrackedQueriesRequest.md)
- [BulkRemoveClustersFromTrackedQueries200Response](docs/Model/BulkRemoveClustersFromTrackedQueries200Response.md)
- [BulkRemoveClustersFromTrackedQueriesRequest](docs/Model/BulkRemoveClustersFromTrackedQueriesRequest.md)
- [ChangeMemberRoleRequest](docs/Model/ChangeMemberRoleRequest.md)
- [ChangeTrackedQueryCheckFrequencyRequestData](docs/Model/ChangeTrackedQueryCheckFrequencyRequestData.md)
- [ChangeTrackedQueryPassesRequestData](docs/Model/ChangeTrackedQueryPassesRequestData.md)
- [CitationResource](docs/Model/CitationResource.md)
- [CitedSourceRow](docs/Model/CitedSourceRow.md)
- [CitedSourcesResponse](docs/Model/CitedSourcesResponse.md)
- [ClusterBreakdownRow](docs/Model/ClusterBreakdownRow.md)
- [ClusterMembershipRequestData](docs/Model/ClusterMembershipRequestData.md)
- [CompetitorCoOccurrenceResponse](docs/Model/CompetitorCoOccurrenceResponse.md)
- [CompetitorCoOccurrenceRow](docs/Model/CompetitorCoOccurrenceRow.md)
- [CompetitorResource](docs/Model/CompetitorResource.md)
- [CompetitorShareOfVoice](docs/Model/CompetitorShareOfVoice.md)
- [CreateCompetitorRequest](docs/Model/CreateCompetitorRequest.md)
- [CreateInvitation200Response](docs/Model/CreateInvitation200Response.md)
- [CreateInvitation201Response](docs/Model/CreateInvitation201Response.md)
- [CreateInvitationRequest](docs/Model/CreateInvitationRequest.md)
- [CreateOrganization201Response](docs/Model/CreateOrganization201Response.md)
- [CreateOrganizationRequest](docs/Model/CreateOrganizationRequest.md)
- [CreateProjectRequest](docs/Model/CreateProjectRequest.md)
- [CreateProjectRequestCompetitorsInner](docs/Model/CreateProjectRequestCompetitorsInner.md)
- [CreateQueryCluster409Response](docs/Model/CreateQueryCluster409Response.md)
- [CreateQueryClusterRequest](docs/Model/CreateQueryClusterRequest.md)
- [DeleteQueryCluster200Response](docs/Model/DeleteQueryCluster200Response.md)
- [EntitlementsResource](docs/Model/EntitlementsResource.md)
- [GetAvailableFilters200Response](docs/Model/GetAvailableFilters200Response.md)
- [GetAvailableFilters200ResponseClustersInner](docs/Model/GetAvailableFilters200ResponseClustersInner.md)
- [GetMeStats200Response](docs/Model/GetMeStats200Response.md)
- [GetMeStats200ResponseOrganizations](docs/Model/GetMeStats200ResponseOrganizations.md)
- [GetMeStats200ResponseProjects](docs/Model/GetMeStats200ResponseProjects.md)
- [GetMembershipStats200Response](docs/Model/GetMembershipStats200Response.md)
- [GetMentionSamples400Response](docs/Model/GetMentionSamples400Response.md)
- [GetMentionSamples400ResponseDetailsValueInner](docs/Model/GetMentionSamples400ResponseDetailsValueInner.md)
- [GetMetricGlossary200Response](docs/Model/GetMetricGlossary200Response.md)
- [GetMetricGlossary200ResponseMetricsInner](docs/Model/GetMetricGlossary200ResponseMetricsInner.md)
- [GetOrganizationOverview200Response](docs/Model/GetOrganizationOverview200Response.md)
- [GetOrganizationOverview200ResponseAggregate](docs/Model/GetOrganizationOverview200ResponseAggregate.md)
- [GetOrganizationOverview200ResponseProjectsInner](docs/Model/GetOrganizationOverview200ResponseProjectsInner.md)
- [GetOrganizationStats200Response](docs/Model/GetOrganizationStats200Response.md)
- [GetOrganizationStats200ResponseInvitations](docs/Model/GetOrganizationStats200ResponseInvitations.md)
- [GetOrganizationStats200ResponseMembers](docs/Model/GetOrganizationStats200ResponseMembers.md)
- [GetOrganizationStats200ResponseProjects](docs/Model/GetOrganizationStats200ResponseProjects.md)
- [GetShareOfVoiceFormula200Response](docs/Model/GetShareOfVoiceFormula200Response.md)
- [GetTrackingCoverage200Response](docs/Model/GetTrackingCoverage200Response.md)
- [GetTrackingCoverage200ResponseSampleInner](docs/Model/GetTrackingCoverage200ResponseSampleInner.md)
- [InvitationResource](docs/Model/InvitationResource.md)
- [KeywordListingResource](docs/Model/KeywordListingResource.md)
- [KeywordListingResourceMentionTypeCounts](docs/Model/KeywordListingResourceMentionTypeCounts.md)
- [ListAiResponses200Response](docs/Model/ListAiResponses200Response.md)
- [ListCompetitors200Response](docs/Model/ListCompetitors200Response.md)
- [ListInvitations200Response](docs/Model/ListInvitations200Response.md)
- [ListKeywordListings200Response](docs/Model/ListKeywordListings200Response.md)
- [ListMembers200Response](docs/Model/ListMembers200Response.md)
- [ListOrganizations200Response](docs/Model/ListOrganizations200Response.md)
- [ListProjects200Response](docs/Model/ListProjects200Response.md)
- [ListQueryClusters200Response](docs/Model/ListQueryClusters200Response.md)
- [ListSearchSnapshots200Response](docs/Model/ListSearchSnapshots200Response.md)
- [ListShoppingSnapshots200Response](docs/Model/ListShoppingSnapshots200Response.md)
- [MeResource](docs/Model/MeResource.md)
- [MemberResource](docs/Model/MemberResource.md)
- [MentionMatchResource](docs/Model/MentionMatchResource.md)
- [MentionSampleResponse](docs/Model/MentionSampleResponse.md)
- [MentionTypeCounts](docs/Model/MentionTypeCounts.md)
- [OperationEffect](docs/Model/OperationEffect.md)
- [OrganizationResource](docs/Model/OrganizationResource.md)
- [PerCompetitorSentiment](docs/Model/PerCompetitorSentiment.md)
- [PerEngineSentiment](docs/Model/PerEngineSentiment.md)
- [PerEntityMetrics](docs/Model/PerEntityMetrics.md)
- [PositionDistributionBucket](docs/Model/PositionDistributionBucket.md)
- [PreviewOrganizationOperation200Response](docs/Model/PreviewOrganizationOperation200Response.md)
- [PreviewOrganizationOperation200ResponseOrganization](docs/Model/PreviewOrganizationOperation200ResponseOrganization.md)
- [PreviewOrganizationOperationRequest](docs/Model/PreviewOrganizationOperationRequest.md)
- [ProjectDetailResource](docs/Model/ProjectDetailResource.md)
- [ProjectDetailResourceCompetitorsInner](docs/Model/ProjectDetailResourceCompetitorsInner.md)
- [ProjectMentionMixResponse](docs/Model/ProjectMentionMixResponse.md)
- [ProjectMentionSamplesResponse](docs/Model/ProjectMentionSamplesResponse.md)
- [ProjectRankTrackingClusterBreakdown](docs/Model/ProjectRankTrackingClusterBreakdown.md)
- [ProjectRankTrackingStats](docs/Model/ProjectRankTrackingStats.md)
- [ProjectRankTrackingTimeSeries](docs/Model/ProjectRankTrackingTimeSeries.md)
- [ProjectResource](docs/Model/ProjectResource.md)
- [ProjectSentimentBreakdown](docs/Model/ProjectSentimentBreakdown.md)
- [ProjectedMonthlyChecksResource](docs/Model/ProjectedMonthlyChecksResource.md)
- [QueryClusterResource](docs/Model/QueryClusterResource.md)
- [ReportAiResponseRequest](docs/Model/ReportAiResponseRequest.md)
- [SearchResultResource](docs/Model/SearchResultResource.md)
- [SearchSnapshotResource](docs/Model/SearchSnapshotResource.md)
- [SearchTrackedQueries200Response](docs/Model/SearchTrackedQueries200Response.md)
- [SearchTrackedQueryMentionMatches200Response](docs/Model/SearchTrackedQueryMentionMatches200Response.md)
- [SearchTrackedQuerySerpMatches200Response](docs/Model/SearchTrackedQuerySerpMatches200Response.md)
- [SerpMatchResource](docs/Model/SerpMatchResource.md)
- [ShoppingOfferResource](docs/Model/ShoppingOfferResource.md)
- [ShoppingSnapshotResource](docs/Model/ShoppingSnapshotResource.md)
- [StartBrandDiscoveryJobRequest](docs/Model/StartBrandDiscoveryJobRequest.md)
- [StartBrandNameSuggestionJobRequest](docs/Model/StartBrandNameSuggestionJobRequest.md)
- [StartClusteringJobRequestData](docs/Model/StartClusteringJobRequestData.md)
- [StartKeywordDiscoveryJobRequest](docs/Model/StartKeywordDiscoveryJobRequest.md)
- [StartPromptDiscoveryJobRequest](docs/Model/StartPromptDiscoveryJobRequest.md)
- [SubmittedChecksResource](docs/Model/SubmittedChecksResource.md)
- [SubscriptionResource](docs/Model/SubscriptionResource.md)
- [TimeSeriesPoint](docs/Model/TimeSeriesPoint.md)
- [TrackedQueryCountResource](docs/Model/TrackedQueryCountResource.md)
- [TrackedQueryDetailResource](docs/Model/TrackedQueryDetailResource.md)
- [TrackedQueryMoverRow](docs/Model/TrackedQueryMoverRow.md)
- [TrackedQueryMoversResponse](docs/Model/TrackedQueryMoversResponse.md)
- [TrackedQueryRankTrackingTimeSeries](docs/Model/TrackedQueryRankTrackingTimeSeries.md)
- [TrackedQueryResource](docs/Model/TrackedQueryResource.md)
- [TrackedQueryUsageResource](docs/Model/TrackedQueryUsageResource.md)
- [UpdateOrganizationRequest](docs/Model/UpdateOrganizationRequest.md)
- [UpdateProjectBrandProfileRequest](docs/Model/UpdateProjectBrandProfileRequest.md)
- [UpdateProjectRequest](docs/Model/UpdateProjectRequest.md)

## Authorization

Authentication schemes defined for the API:
### ApiKey

- **Type**: Bearer authentication

## Tests

To run the tests, use:

```bash
composer install
vendor/bin/phpunit
```

## Author

support@mencoro.com

## About this package

This PHP package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `1.0.0`
    - Generator version: `7.24.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
