# CreateProjectRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**WebsiteDomains** | **[]string** | At least one website URL or domain to monitor. | 
**BrandNames** | **[]string** | At least one brand name to match in AI answers and search results. | 
**Competitors** | Pointer to [**[]CreateProjectRequestCompetitorsInner**](CreateProjectRequestCompetitorsInner.md) | Competitors to create with the project. Optional; they can also be added later through the competitor endpoints. | [optional] 

## Methods

### NewCreateProjectRequest

`func NewCreateProjectRequest(name string, websiteDomains []string, brandNames []string, ) *CreateProjectRequest`

NewCreateProjectRequest instantiates a new CreateProjectRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateProjectRequestWithDefaults

`func NewCreateProjectRequestWithDefaults() *CreateProjectRequest`

NewCreateProjectRequestWithDefaults instantiates a new CreateProjectRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateProjectRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateProjectRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateProjectRequest) SetName(v string)`

SetName sets Name field to given value.


### GetWebsiteDomains

`func (o *CreateProjectRequest) GetWebsiteDomains() []string`

GetWebsiteDomains returns the WebsiteDomains field if non-nil, zero value otherwise.

### GetWebsiteDomainsOk

`func (o *CreateProjectRequest) GetWebsiteDomainsOk() (*[]string, bool)`

GetWebsiteDomainsOk returns a tuple with the WebsiteDomains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsiteDomains

`func (o *CreateProjectRequest) SetWebsiteDomains(v []string)`

SetWebsiteDomains sets WebsiteDomains field to given value.


### GetBrandNames

`func (o *CreateProjectRequest) GetBrandNames() []string`

GetBrandNames returns the BrandNames field if non-nil, zero value otherwise.

### GetBrandNamesOk

`func (o *CreateProjectRequest) GetBrandNamesOk() (*[]string, bool)`

GetBrandNamesOk returns a tuple with the BrandNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrandNames

`func (o *CreateProjectRequest) SetBrandNames(v []string)`

SetBrandNames sets BrandNames field to given value.


### GetCompetitors

`func (o *CreateProjectRequest) GetCompetitors() []CreateProjectRequestCompetitorsInner`

GetCompetitors returns the Competitors field if non-nil, zero value otherwise.

### GetCompetitorsOk

`func (o *CreateProjectRequest) GetCompetitorsOk() (*[]CreateProjectRequestCompetitorsInner, bool)`

GetCompetitorsOk returns a tuple with the Competitors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitors

`func (o *CreateProjectRequest) SetCompetitors(v []CreateProjectRequestCompetitorsInner)`

SetCompetitors sets Competitors field to given value.

### HasCompetitors

`func (o *CreateProjectRequest) HasCompetitors() bool`

HasCompetitors returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


