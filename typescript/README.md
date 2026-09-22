# @mencoro/api@1.0.1

A TypeScript SDK client for the api.mencoro.com API.

## Usage

First, install the SDK from npm.

```bash
npm install @mencoro/api --save
```

Next, try it out.


```ts
import {
  Configuration,
  AccountApi,
} from '@mencoro/api';
import type { GetMeRequest } from '@mencoro/api';

async function example() {
  console.log("🚀 Testing @mencoro/api SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: ApiKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AccountApi(config);

  try {
    const data = await api.getMe();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```


## Documentation

### API Endpoints

All URIs are relative to *https://api.mencoro.com*

| Class | Method | HTTP request | Description
| ----- | ------ | ------------ | -------------
*AccountApi* | [**getMe**](docs/AccountApi.md#getme) | **GET** /api/v1/me | Get the authenticated identity
*AccountApi* | [**getMeStats**](docs/AccountApi.md#getmestats) | **GET** /api/v1/me/stats | Counts across everything the key can reach
*AnalyticsApi* | [**getAvailableFilters**](docs/AnalyticsApi.md#getavailablefilters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/available-filters | Filter values a project is configured for
*AnalyticsApi* | [**getCitedSources**](docs/AnalyticsApi.md#getcitedsources) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/cited-sources | Domains and pages the AI answers cited
*AnalyticsApi* | [**getClusterBreakdown**](docs/AnalyticsApi.md#getclusterbreakdown) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/clusters | Rank-tracking metrics per keyword cluster
*AnalyticsApi* | [**getCompetitorCoOccurrence**](docs/AnalyticsApi.md#getcompetitorcooccurrence) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/co-occurrence | Head-to-head record of the brand against each tracked competitor
*AnalyticsApi* | [**getMentionMix**](docs/AnalyticsApi.md#getmentionmix) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions/mix | Composition of a project brand mentions in AI answers
*AnalyticsApi* | [**getMentionSamples**](docs/AnalyticsApi.md#getmentionsamples) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/mentions | Sample of the raw AI mention texts of a project
*AnalyticsApi* | [**getMetricGlossary**](docs/AnalyticsApi.md#getmetricglossary) | **GET** /api/v1/metric-glossary | Map everyday wording to a metric and the operation that serves it
*AnalyticsApi* | [**getOrganizationOverview**](docs/AnalyticsApi.md#getorganizationoverview) | **GET** /api/v1/organizations/{organizationId}/overview | Snapshot rank-health board across an organization active projects
*AnalyticsApi* | [**getProjectMetrics**](docs/AnalyticsApi.md#getprojectmetrics) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics | Headline visibility metrics of a project
*AnalyticsApi* | [**getProjectSentiment**](docs/AnalyticsApi.md#getprojectsentiment) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/sentiment | Sentiment breakdown of a project brand mentions
*AnalyticsApi* | [**getProjectTimeSeries**](docs/AnalyticsApi.md#getprojecttimeseries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/timeseries | Rank-tracking metrics of a project over time
*AnalyticsApi* | [**getQueryMovers**](docs/AnalyticsApi.md#getquerymovers) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/movers | Tracked queries ranked by how much a metric moved
*AnalyticsApi* | [**getShareOfVoiceFormula**](docs/AnalyticsApi.md#getshareofvoiceformula) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/metrics/share-of-voice-formula | The constants behind the Share of Voice score
*AnalyticsApi* | [**getTrackedQueryTimeSeries**](docs/AnalyticsApi.md#gettrackedquerytimeseries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/timeseries | Rank-tracking time series of a single tracked query
*AnalyticsApi* | [**getTrackingCoverage**](docs/AnalyticsApi.md#gettrackingcoverage) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/coverage | Coverage and staleness of a project tracked queries
*AnalyticsApi* | [**listKeywordListings**](docs/AnalyticsApi.md#listkeywordlistings) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/keyword-listings | List a project\&#39;s keywords with their windowed metrics
*BillingApi* | [**getSubscription**](docs/BillingApi.md#getsubscription) | **GET** /api/v1/organizations/{organizationId}/subscription | Get the subscription of an organization
*CapturesApi* | [**listAiResponses**](docs/CapturesApi.md#listairesponses) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/ai-responses | List captured AI answers
*CapturesApi* | [**listSearchSnapshots**](docs/CapturesApi.md#listsearchsnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/search-snapshots | List captured search-results pages
*CapturesApi* | [**listShoppingSnapshots**](docs/CapturesApi.md#listshoppingsnapshots) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/shopping-snapshots | List captured shopping-results pages
*ClustersApi* | [**applyClusteringJob**](docs/ClustersApi.md#applyclusteringjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs/{jobId}/apply | Apply the result of a clustering job
*ClustersApi* | [**batchCreateQueryClusters**](docs/ClustersApi.md#batchcreatequeryclusters) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/batch | Create several keyword clusters at once
*ClustersApi* | [**createQueryCluster**](docs/ClustersApi.md#createqueryclusteroperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | Create a keyword cluster
*ClustersApi* | [**deleteQueryCluster**](docs/ClustersApi.md#deletequerycluster) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Delete a keyword cluster
*ClustersApi* | [**getQueryCluster**](docs/ClustersApi.md#getquerycluster) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Get one of a project\&#39;s keyword clusters
*ClustersApi* | [**renameQueryCluster**](docs/ClustersApi.md#renamequerycluster) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId} | Rename a keyword cluster
*ClustersApi* | [**startClusteringJob**](docs/ClustersApi.md#startclusteringjob) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters/jobs | Start a keyword clustering job
*DiscoveryApi* | [**startBrandDiscoveryJob**](docs/DiscoveryApi.md#startbranddiscoveryjoboperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/brands | Start a brand discovery job for a project
*DiscoveryApi* | [**startBrandNameSuggestionJob**](docs/DiscoveryApi.md#startbrandnamesuggestionjoboperation) | **POST** /api/v1/organizations/{organizationId}/brand-name-suggestions | Start a brand-name alias suggestion job
*DiscoveryApi* | [**startKeywordDiscoveryJob**](docs/DiscoveryApi.md#startkeyworddiscoveryjoboperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/keywords | Start a keyword discovery job for a project
*DiscoveryApi* | [**startPromptDiscoveryJob**](docs/DiscoveryApi.md#startpromptdiscoveryjoboperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/discovery/prompts | Start a geo prompt discovery job for a project
*InvitationsApi* | [**cancelInvitation**](docs/InvitationsApi.md#cancelinvitation) | **POST** /api/v1/organizations/{organizationId}/invitations/{invitationId}/cancel | Cancel a pending invitation
*InvitationsApi* | [**createInvitation**](docs/InvitationsApi.md#createinvitationoperation) | **POST** /api/v1/organizations/{organizationId}/invitations | Invite somebody to an organization
*InvitationsApi* | [**listInvitations**](docs/InvitationsApi.md#listinvitations) | **GET** /api/v1/organizations/{organizationId}/invitations | List an organization\&#39;s invitations
*JobsApi* | [**getAsyncJob**](docs/JobsApi.md#getasyncjob) | **GET** /api/v1/organizations/{organizationId}/jobs/{jobId} | Get an asynchronous job
*MembersApi* | [**changeMemberRole**](docs/MembersApi.md#changememberroleoperation) | **PATCH** /api/v1/organizations/{organizationId}/members/{memberId} | Change a member role
*MembersApi* | [**getMember**](docs/MembersApi.md#getmember) | **GET** /api/v1/organizations/{organizationId}/members/{memberId} | Get one organization membership
*MembersApi* | [**listMembers**](docs/MembersApi.md#listmembers) | **GET** /api/v1/organizations/{organizationId}/members | List an organization\&#39;s members
*MembersApi* | [**reactivateMember**](docs/MembersApi.md#reactivatemember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/reactivate | Reactivate a suspended member
*MembersApi* | [**suspendMember**](docs/MembersApi.md#suspendmember) | **POST** /api/v1/organizations/{organizationId}/members/{memberId}/suspend | Suspend a member
*OrganizationOperationsApi* | [**previewOrganizationOperation**](docs/OrganizationOperationsApi.md#previeworganizationoperationoperation) | **POST** /api/v1/organization-operation-previews | Preview an organization operation and obtain a confirmation
*OrganizationsApi* | [**archiveOrganization**](docs/OrganizationsApi.md#archiveorganization) | **POST** /api/v1/organizations/{organizationId}/archive | Archive an organization
*OrganizationsApi* | [**countOrganizationTrackedQueries**](docs/OrganizationsApi.md#countorganizationtrackedqueries) | **GET** /api/v1/organizations/{organizationId}/usage/tracked-queries | Count the tracked queries an organization has configured
*OrganizationsApi* | [**createOrganization**](docs/OrganizationsApi.md#createorganizationoperation) | **POST** /api/v1/organizations | Create an organization
*OrganizationsApi* | [**getEntitlements**](docs/OrganizationsApi.md#getentitlements) | **GET** /api/v1/organizations/{organizationId}/entitlements | Get an organization\&#39;s plan allowance and consumption
*OrganizationsApi* | [**getMembershipStats**](docs/OrganizationsApi.md#getmembershipstats) | **GET** /api/v1/organizations/{organizationId}/membership-stats | Membership, project and invitation counts for an organization
*OrganizationsApi* | [**getOrganization**](docs/OrganizationsApi.md#getorganization) | **GET** /api/v1/organizations/{organizationId} | Get an organization
*OrganizationsApi* | [**getOrganizationProjectedMonthlyChecks**](docs/OrganizationsApi.md#getorganizationprojectedmonthlychecks) | **GET** /api/v1/organizations/{organizationId}/usage/projected-monthly-checks | Project a month of check consumption from the current tracking configuration
*OrganizationsApi* | [**getOrganizationStats**](docs/OrganizationsApi.md#getorganizationstats) | **GET** /api/v1/organizations/{organizationId}/stats | Headline counts for an organization
*OrganizationsApi* | [**listOrganizations**](docs/OrganizationsApi.md#listorganizations) | **GET** /api/v1/organizations | List accessible organizations
*OrganizationsApi* | [**restoreOrganization**](docs/OrganizationsApi.md#restoreorganization) | **POST** /api/v1/organizations/{organizationId}/restore | Restore an archived organization
*OrganizationsApi* | [**updateOrganization**](docs/OrganizationsApi.md#updateorganizationoperation) | **PATCH** /api/v1/organizations/{organizationId} | Update an organization profile
*ProjectsApi* | [**archiveProject**](docs/ProjectsApi.md#archiveproject) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/archive | Archive a project
*ProjectsApi* | [**createCompetitor**](docs/ProjectsApi.md#createcompetitoroperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | Add a competitor to a project
*ProjectsApi* | [**createProject**](docs/ProjectsApi.md#createprojectoperation) | **POST** /api/v1/organizations/{organizationId}/projects | Create a project and the brand monitoring profile its checks run against
*ProjectsApi* | [**deleteCompetitor**](docs/ProjectsApi.md#deletecompetitor) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Remove a competitor from a project
*ProjectsApi* | [**getBrandProfile**](docs/ProjectsApi.md#getbrandprofile) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Get a project\&#39;s brand monitoring profile
*ProjectsApi* | [**getCompetitor**](docs/ProjectsApi.md#getcompetitor) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Get one of a project\&#39;s competitors
*ProjectsApi* | [**getProject**](docs/ProjectsApi.md#getproject) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId} | Get a project and its brand monitoring configuration
*ProjectsApi* | [**listCompetitors**](docs/ProjectsApi.md#listcompetitors) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors | List the competitors tracked by a project
*ProjectsApi* | [**listProjects**](docs/ProjectsApi.md#listprojects) | **GET** /api/v1/organizations/{organizationId}/projects | List an organization\&#39;s projects
*ProjectsApi* | [**listQueryClusters**](docs/ProjectsApi.md#listqueryclusters) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/clusters | List the keyword clusters of a project
*ProjectsApi* | [**restoreProject**](docs/ProjectsApi.md#restoreproject) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/restore | Restore an archived project
*ProjectsApi* | [**updateCompetitor**](docs/ProjectsApi.md#updatecompetitor) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/competitors/{competitorId} | Replace a competitor
*ProjectsApi* | [**updateProject**](docs/ProjectsApi.md#updateprojectoperation) | **PATCH** /api/v1/organizations/{organizationId}/projects/{projectId} | Rename a project
*ProjectsApi* | [**updateProjectBrandProfile**](docs/ProjectsApi.md#updateprojectbrandprofileoperation) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/brand-profile | Replace a project\&#39;s brand monitoring profile
*TrackedQueriesApi* | [**addClustersToTrackedQuery**](docs/TrackedQueriesApi.md#addclusterstotrackedquery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Add a tracked query to clusters
*TrackedQueriesApi* | [**batchChangeTrackedQueriesCheckFrequency**](docs/TrackedQueriesApi.md#batchchangetrackedqueriescheckfrequency) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/check-frequency | Change how often several tracked queries are checked
*TrackedQueriesApi* | [**batchChangeTrackedQueriesNPasses**](docs/TrackedQueriesApi.md#batchchangetrackedqueriesnpasses) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/passes | Change how many passes several tracked queries run per check
*TrackedQueriesApi* | [**batchCreateTrackedQueries**](docs/TrackedQueriesApi.md#batchcreatetrackedqueries) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Create tracked queries
*TrackedQueriesApi* | [**batchForceCheckTrackedQueries**](docs/TrackedQueriesApi.md#batchforcechecktrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check | Check several tracked queries now
*TrackedQueriesApi* | [**batchPauseTrackedQueries**](docs/TrackedQueriesApi.md#batchpausetrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/pause | Pause several tracked queries
*TrackedQueriesApi* | [**batchResumeTrackedQueries**](docs/TrackedQueriesApi.md#batchresumetrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/batch/resume | Resume several tracked queries
*TrackedQueriesApi* | [**bulkAddClustersToTrackedQueries**](docs/TrackedQueriesApi.md#bulkaddclusterstotrackedqueriesoperation) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Add many tracked queries to clusters
*TrackedQueriesApi* | [**bulkDeleteTrackedQueries**](docs/TrackedQueriesApi.md#bulkdeletetrackedqueries) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk-delete | Delete tracked queries
*TrackedQueriesApi* | [**bulkRemoveClustersFromTrackedQueries**](docs/TrackedQueriesApi.md#bulkremoveclustersfromtrackedqueriesoperation) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/bulk/clusters | Remove many tracked queries from clusters
*TrackedQueriesApi* | [**changeTrackedQueryCheckFrequency**](docs/TrackedQueriesApi.md#changetrackedquerycheckfrequency) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/check-frequency | Change how often a tracked query is checked
*TrackedQueriesApi* | [**changeTrackedQueryNPasses**](docs/TrackedQueriesApi.md#changetrackedquerynpasses) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/passes | Change how many passes a tracked query runs per check
*TrackedQueriesApi* | [**countTrackedQueries**](docs/TrackedQueriesApi.md#counttrackedqueries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/count | Count a project\&#39;s tracked queries and price checking them
*TrackedQueriesApi* | [**forceCheckAllActiveTrackedQueries**](docs/TrackedQueriesApi.md#forcecheckallactivetrackedqueries) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/check-all | Check every eligible tracked query of a project now
*TrackedQueriesApi* | [**getTrackedQuery**](docs/TrackedQueriesApi.md#gettrackedquery) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId} | Get a tracked query
*TrackedQueriesApi* | [**pauseTrackedQuery**](docs/TrackedQueriesApi.md#pausetrackedquery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/pause | Pause a tracked query
*TrackedQueriesApi* | [**removeClustersFromTrackedQuery**](docs/TrackedQueriesApi.md#removeclustersfromtrackedquery) | **DELETE** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/clusters | Remove a tracked query from clusters
*TrackedQueriesApi* | [**reportAiResponse**](docs/TrackedQueriesApi.md#reportairesponseoperation) | **POST** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/responses/{aiResponseId}/report | Report a problem with a captured AI answer
*TrackedQueriesApi* | [**resumeTrackedQuery**](docs/TrackedQueriesApi.md#resumetrackedquery) | **PUT** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries/{trackedQueryId}/resume | Resume a tracked query
*TrackedQueriesApi* | [**searchTrackedQueries**](docs/TrackedQueriesApi.md#searchtrackedqueries) | **GET** /api/v1/organizations/{organizationId}/projects/{projectId}/tracked-queries | Search a project\&#39;s tracked queries


### Models

- [AcceptedJobResource](docs/AcceptedJobResource.md)
- [AiResponseReportResource](docs/AiResponseReportResource.md)
- [AiResponseResource](docs/AiResponseResource.md)
- [ApplyClusteringJobOutcome](docs/ApplyClusteringJobOutcome.md)
- [ApplyClusteringJobOutcomeClustersInner](docs/ApplyClusteringJobOutcomeClustersInner.md)
- [ApplyClusteringJobOutcomeFailedInner](docs/ApplyClusteringJobOutcomeFailedInner.md)
- [ApplyClusteringJobOutcomeSkippedClustersInner](docs/ApplyClusteringJobOutcomeSkippedClustersInner.md)
- [ApplyClusteringJobOutcomeSuccessfulInner](docs/ApplyClusteringJobOutcomeSuccessfulInner.md)
- [AsyncJobResource](docs/AsyncJobResource.md)
- [BatchChangeTrackedQueryCheckFrequencyRequestData](docs/BatchChangeTrackedQueryCheckFrequencyRequestData.md)
- [BatchChangeTrackedQueryPassesRequestData](docs/BatchChangeTrackedQueryPassesRequestData.md)
- [BatchCreateQueryClustersOutcome](docs/BatchCreateQueryClustersOutcome.md)
- [BatchCreateQueryClustersOutcomeFailedInner](docs/BatchCreateQueryClustersOutcomeFailedInner.md)
- [BatchCreateQueryClustersOutcomeSuccessfulInner](docs/BatchCreateQueryClustersOutcomeSuccessfulInner.md)
- [BatchCreateQueryClustersRequestData](docs/BatchCreateQueryClustersRequestData.md)
- [BatchCreateTrackedQueriesRequestData](docs/BatchCreateTrackedQueriesRequestData.md)
- [BatchCreateTrackedQueriesResultResource](docs/BatchCreateTrackedQueriesResultResource.md)
- [BatchCreateTrackedQueriesResultResourceFailedInner](docs/BatchCreateTrackedQueriesResultResourceFailedInner.md)
- [BatchCreateTrackedQueriesResultResourceSuccessfulInner](docs/BatchCreateTrackedQueriesResultResourceSuccessfulInner.md)
- [BatchForceCheckTrackedQueries200Response](docs/BatchForceCheckTrackedQueries200Response.md)
- [BatchForceCheckTrackedQueries200ResponseFailedInner](docs/BatchForceCheckTrackedQueries200ResponseFailedInner.md)
- [BatchPauseTrackedQueries200Response](docs/BatchPauseTrackedQueries200Response.md)
- [BatchPauseTrackedQueries200ResponseFailedInner](docs/BatchPauseTrackedQueries200ResponseFailedInner.md)
- [BatchPauseTrackedQueries200ResponseSuccessfulInner](docs/BatchPauseTrackedQueries200ResponseSuccessfulInner.md)
- [BatchResumeTrackedQueries200Response](docs/BatchResumeTrackedQueries200Response.md)
- [BatchTargetsRequestData](docs/BatchTargetsRequestData.md)
- [BatchWriteOutcome](docs/BatchWriteOutcome.md)
- [BatchWriteOutcomeFailedInner](docs/BatchWriteOutcomeFailedInner.md)
- [BrandProfileResource](docs/BrandProfileResource.md)
- [BulkAddClustersToTrackedQueries200Response](docs/BulkAddClustersToTrackedQueries200Response.md)
- [BulkAddClustersToTrackedQueriesRequest](docs/BulkAddClustersToTrackedQueriesRequest.md)
- [BulkRemoveClustersFromTrackedQueries200Response](docs/BulkRemoveClustersFromTrackedQueries200Response.md)
- [BulkRemoveClustersFromTrackedQueriesRequest](docs/BulkRemoveClustersFromTrackedQueriesRequest.md)
- [ChangeMemberRoleRequest](docs/ChangeMemberRoleRequest.md)
- [ChangeTrackedQueryCheckFrequencyRequestData](docs/ChangeTrackedQueryCheckFrequencyRequestData.md)
- [ChangeTrackedQueryPassesRequestData](docs/ChangeTrackedQueryPassesRequestData.md)
- [CitationResource](docs/CitationResource.md)
- [ClusterMembershipRequestData](docs/ClusterMembershipRequestData.md)
- [CompetitorResource](docs/CompetitorResource.md)
- [CreateCompetitorRequest](docs/CreateCompetitorRequest.md)
- [CreateInvitation200Response](docs/CreateInvitation200Response.md)
- [CreateInvitation201Response](docs/CreateInvitation201Response.md)
- [CreateInvitationRequest](docs/CreateInvitationRequest.md)
- [CreateOrganization201Response](docs/CreateOrganization201Response.md)
- [CreateOrganizationRequest](docs/CreateOrganizationRequest.md)
- [CreateProjectRequest](docs/CreateProjectRequest.md)
- [CreateProjectRequestCompetitorsInner](docs/CreateProjectRequestCompetitorsInner.md)
- [CreateQueryCluster409Response](docs/CreateQueryCluster409Response.md)
- [CreateQueryClusterRequest](docs/CreateQueryClusterRequest.md)
- [DeleteQueryCluster200Response](docs/DeleteQueryCluster200Response.md)
- [EntitlementsResource](docs/EntitlementsResource.md)
- [GetAvailableFilters200Response](docs/GetAvailableFilters200Response.md)
- [GetAvailableFilters200ResponseClustersInner](docs/GetAvailableFilters200ResponseClustersInner.md)
- [GetMeStats200Response](docs/GetMeStats200Response.md)
- [GetMeStats200ResponseOrganizations](docs/GetMeStats200ResponseOrganizations.md)
- [GetMeStats200ResponseProjects](docs/GetMeStats200ResponseProjects.md)
- [GetMembershipStats200Response](docs/GetMembershipStats200Response.md)
- [GetMentionSamples400Response](docs/GetMentionSamples400Response.md)
- [GetMentionSamples400ResponseDetailsValueInner](docs/GetMentionSamples400ResponseDetailsValueInner.md)
- [GetMetricGlossary200Response](docs/GetMetricGlossary200Response.md)
- [GetMetricGlossary200ResponseMetricsInner](docs/GetMetricGlossary200ResponseMetricsInner.md)
- [GetOrganizationOverview200Response](docs/GetOrganizationOverview200Response.md)
- [GetOrganizationOverview200ResponseAggregate](docs/GetOrganizationOverview200ResponseAggregate.md)
- [GetOrganizationOverview200ResponseProjectsInner](docs/GetOrganizationOverview200ResponseProjectsInner.md)
- [GetOrganizationStats200Response](docs/GetOrganizationStats200Response.md)
- [GetOrganizationStats200ResponseInvitations](docs/GetOrganizationStats200ResponseInvitations.md)
- [GetOrganizationStats200ResponseMembers](docs/GetOrganizationStats200ResponseMembers.md)
- [GetOrganizationStats200ResponseProjects](docs/GetOrganizationStats200ResponseProjects.md)
- [GetShareOfVoiceFormula200Response](docs/GetShareOfVoiceFormula200Response.md)
- [GetTrackingCoverage200Response](docs/GetTrackingCoverage200Response.md)
- [GetTrackingCoverage200ResponseSampleInner](docs/GetTrackingCoverage200ResponseSampleInner.md)
- [InvitationResource](docs/InvitationResource.md)
- [KeywordListingResource](docs/KeywordListingResource.md)
- [KeywordListingResourceMentionTypeCounts](docs/KeywordListingResourceMentionTypeCounts.md)
- [ListAiResponses200Response](docs/ListAiResponses200Response.md)
- [ListCompetitors200Response](docs/ListCompetitors200Response.md)
- [ListInvitations200Response](docs/ListInvitations200Response.md)
- [ListKeywordListings200Response](docs/ListKeywordListings200Response.md)
- [ListMembers200Response](docs/ListMembers200Response.md)
- [ListOrganizations200Response](docs/ListOrganizations200Response.md)
- [ListProjects200Response](docs/ListProjects200Response.md)
- [ListQueryClusters200Response](docs/ListQueryClusters200Response.md)
- [ListSearchSnapshots200Response](docs/ListSearchSnapshots200Response.md)
- [ListShoppingSnapshots200Response](docs/ListShoppingSnapshots200Response.md)
- [MeResource](docs/MeResource.md)
- [MemberResource](docs/MemberResource.md)
- [OperationEffect](docs/OperationEffect.md)
- [OrganizationResource](docs/OrganizationResource.md)
- [PreviewOrganizationOperation200Response](docs/PreviewOrganizationOperation200Response.md)
- [PreviewOrganizationOperation200ResponseOrganization](docs/PreviewOrganizationOperation200ResponseOrganization.md)
- [PreviewOrganizationOperationRequest](docs/PreviewOrganizationOperationRequest.md)
- [ProjectDetailResource](docs/ProjectDetailResource.md)
- [ProjectDetailResourceCompetitorsInner](docs/ProjectDetailResourceCompetitorsInner.md)
- [ProjectResource](docs/ProjectResource.md)
- [ProjectedMonthlyChecksResource](docs/ProjectedMonthlyChecksResource.md)
- [QueryClusterResource](docs/QueryClusterResource.md)
- [ReportAiResponseRequest](docs/ReportAiResponseRequest.md)
- [SearchResultResource](docs/SearchResultResource.md)
- [SearchSnapshotResource](docs/SearchSnapshotResource.md)
- [SearchTrackedQueries200Response](docs/SearchTrackedQueries200Response.md)
- [ShoppingOfferResource](docs/ShoppingOfferResource.md)
- [ShoppingSnapshotResource](docs/ShoppingSnapshotResource.md)
- [StartBrandDiscoveryJobRequest](docs/StartBrandDiscoveryJobRequest.md)
- [StartBrandNameSuggestionJobRequest](docs/StartBrandNameSuggestionJobRequest.md)
- [StartClusteringJobRequestData](docs/StartClusteringJobRequestData.md)
- [StartKeywordDiscoveryJobRequest](docs/StartKeywordDiscoveryJobRequest.md)
- [StartPromptDiscoveryJobRequest](docs/StartPromptDiscoveryJobRequest.md)
- [SubmittedChecksResource](docs/SubmittedChecksResource.md)
- [SubscriptionResource](docs/SubscriptionResource.md)
- [TrackedQueryCountResource](docs/TrackedQueryCountResource.md)
- [TrackedQueryDetailResource](docs/TrackedQueryDetailResource.md)
- [TrackedQueryResource](docs/TrackedQueryResource.md)
- [TrackedQueryUsageResource](docs/TrackedQueryUsageResource.md)
- [UpdateOrganizationRequest](docs/UpdateOrganizationRequest.md)
- [UpdateProjectBrandProfileRequest](docs/UpdateProjectBrandProfileRequest.md)
- [UpdateProjectRequest](docs/UpdateProjectRequest.md)

### Authorization


Authentication schemes defined for the API:
<a id="ApiKey"></a>
#### ApiKey


- **Type**: HTTP Bearer Token authentication

## About

This TypeScript SDK client supports the [Fetch API](https://fetch.spec.whatwg.org/)
and is automatically generated by the
[OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `1.0.0`
- Package version: `1.0.1`
- Generator version: `7.24.0`
- Build package: `org.openapitools.codegen.languages.TypeScriptFetchClientCodegen`

The generated npm module supports the following:

- Environments
  * Node.js
  * Webpack
  * Browserify
- Language levels
  * ES5 - you must have a Promises/A+ library installed
  * ES6
- Module systems
  * CommonJS
  * ES6 module system

For more information, please visit [https://mencoro.com/contact/](https://mencoro.com/contact/)

## Development

### Building

To build the TypeScript source code, you need to have Node.js and npm installed.
After cloning the repository, navigate to the project directory and run:

```bash
npm install
npm run build
```

### Publishing

Once you've built the package, you can publish it to npm:

```bash
npm publish
```

## License

[Proprietary](https://mencoro.com/legal/)
