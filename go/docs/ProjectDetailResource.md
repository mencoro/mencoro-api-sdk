# ProjectDetailResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**OrganizationId** | **string** |  | 
**Name** | **string** |  | 
**Status** | **string** |  | 
**CreatedAt** | **time.Time** |  | 
**WebsiteDomains** | **[]string** | Domains the project is monitored for. Empty when the project has no brand monitoring profile yet. | 
**BrandNames** | **[]string** | Brand names matched in AI answers and search results. Empty when the project has no brand monitoring profile yet. | 
**Competitors** | [**[]ProjectDetailResourceCompetitorsInner**](ProjectDetailResourceCompetitorsInner.md) | Competitors this project is measured against. Empty when none are configured. | 

## Methods

### NewProjectDetailResource

`func NewProjectDetailResource(id string, organizationId string, name string, status string, createdAt time.Time, websiteDomains []string, brandNames []string, competitors []ProjectDetailResourceCompetitorsInner, ) *ProjectDetailResource`

NewProjectDetailResource instantiates a new ProjectDetailResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectDetailResourceWithDefaults

`func NewProjectDetailResourceWithDefaults() *ProjectDetailResource`

NewProjectDetailResourceWithDefaults instantiates a new ProjectDetailResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ProjectDetailResource) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ProjectDetailResource) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ProjectDetailResource) SetId(v string)`

SetId sets Id field to given value.


### GetOrganizationId

`func (o *ProjectDetailResource) GetOrganizationId() string`

GetOrganizationId returns the OrganizationId field if non-nil, zero value otherwise.

### GetOrganizationIdOk

`func (o *ProjectDetailResource) GetOrganizationIdOk() (*string, bool)`

GetOrganizationIdOk returns a tuple with the OrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationId

`func (o *ProjectDetailResource) SetOrganizationId(v string)`

SetOrganizationId sets OrganizationId field to given value.


### GetName

`func (o *ProjectDetailResource) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ProjectDetailResource) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ProjectDetailResource) SetName(v string)`

SetName sets Name field to given value.


### GetStatus

`func (o *ProjectDetailResource) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ProjectDetailResource) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ProjectDetailResource) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetCreatedAt

`func (o *ProjectDetailResource) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ProjectDetailResource) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ProjectDetailResource) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetWebsiteDomains

`func (o *ProjectDetailResource) GetWebsiteDomains() []string`

GetWebsiteDomains returns the WebsiteDomains field if non-nil, zero value otherwise.

### GetWebsiteDomainsOk

`func (o *ProjectDetailResource) GetWebsiteDomainsOk() (*[]string, bool)`

GetWebsiteDomainsOk returns a tuple with the WebsiteDomains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsiteDomains

`func (o *ProjectDetailResource) SetWebsiteDomains(v []string)`

SetWebsiteDomains sets WebsiteDomains field to given value.


### GetBrandNames

`func (o *ProjectDetailResource) GetBrandNames() []string`

GetBrandNames returns the BrandNames field if non-nil, zero value otherwise.

### GetBrandNamesOk

`func (o *ProjectDetailResource) GetBrandNamesOk() (*[]string, bool)`

GetBrandNamesOk returns a tuple with the BrandNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrandNames

`func (o *ProjectDetailResource) SetBrandNames(v []string)`

SetBrandNames sets BrandNames field to given value.


### GetCompetitors

`func (o *ProjectDetailResource) GetCompetitors() []ProjectDetailResourceCompetitorsInner`

GetCompetitors returns the Competitors field if non-nil, zero value otherwise.

### GetCompetitorsOk

`func (o *ProjectDetailResource) GetCompetitorsOk() (*[]ProjectDetailResourceCompetitorsInner, bool)`

GetCompetitorsOk returns a tuple with the Competitors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitors

`func (o *ProjectDetailResource) SetCompetitors(v []ProjectDetailResourceCompetitorsInner)`

SetCompetitors sets Competitors field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


