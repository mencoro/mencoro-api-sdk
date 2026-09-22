# BrandProfileResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProjectId** | **string** | The project this profile belongs to | 
**BrandNames** | **[]string** | The brand terms a mention in an AI answer is matched against. Empty when none has been configured yet. | 
**WebsiteDomains** | **[]string** | The domains a cited link or a search result is matched against. Empty when none has been configured yet. | 
**Description** | Pointer to **NullableString** | What the brand does, as generated from its names and domains. Null means it has not been generated yet, which is not the same as an empty description. | [optional] 

## Methods

### NewBrandProfileResource

`func NewBrandProfileResource(projectId string, brandNames []string, websiteDomains []string, ) *BrandProfileResource`

NewBrandProfileResource instantiates a new BrandProfileResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBrandProfileResourceWithDefaults

`func NewBrandProfileResourceWithDefaults() *BrandProfileResource`

NewBrandProfileResourceWithDefaults instantiates a new BrandProfileResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProjectId

`func (o *BrandProfileResource) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *BrandProfileResource) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *BrandProfileResource) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.


### GetBrandNames

`func (o *BrandProfileResource) GetBrandNames() []string`

GetBrandNames returns the BrandNames field if non-nil, zero value otherwise.

### GetBrandNamesOk

`func (o *BrandProfileResource) GetBrandNamesOk() (*[]string, bool)`

GetBrandNamesOk returns a tuple with the BrandNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrandNames

`func (o *BrandProfileResource) SetBrandNames(v []string)`

SetBrandNames sets BrandNames field to given value.


### GetWebsiteDomains

`func (o *BrandProfileResource) GetWebsiteDomains() []string`

GetWebsiteDomains returns the WebsiteDomains field if non-nil, zero value otherwise.

### GetWebsiteDomainsOk

`func (o *BrandProfileResource) GetWebsiteDomainsOk() (*[]string, bool)`

GetWebsiteDomainsOk returns a tuple with the WebsiteDomains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsiteDomains

`func (o *BrandProfileResource) SetWebsiteDomains(v []string)`

SetWebsiteDomains sets WebsiteDomains field to given value.


### GetDescription

`func (o *BrandProfileResource) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *BrandProfileResource) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *BrandProfileResource) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *BrandProfileResource) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *BrandProfileResource) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *BrandProfileResource) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


