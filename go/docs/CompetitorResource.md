# CompetitorResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **string** | The competitor&#39;s display name | 
**WebsiteDomains** | **[]string** | Domains a result is matched against for this competitor | 
**BrandNames** | **[]string** | Names a mention is matched against for this competitor | 

## Methods

### NewCompetitorResource

`func NewCompetitorResource(id string, name string, websiteDomains []string, brandNames []string, ) *CompetitorResource`

NewCompetitorResource instantiates a new CompetitorResource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompetitorResourceWithDefaults

`func NewCompetitorResourceWithDefaults() *CompetitorResource`

NewCompetitorResourceWithDefaults instantiates a new CompetitorResource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *CompetitorResource) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CompetitorResource) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CompetitorResource) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *CompetitorResource) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CompetitorResource) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CompetitorResource) SetName(v string)`

SetName sets Name field to given value.


### GetWebsiteDomains

`func (o *CompetitorResource) GetWebsiteDomains() []string`

GetWebsiteDomains returns the WebsiteDomains field if non-nil, zero value otherwise.

### GetWebsiteDomainsOk

`func (o *CompetitorResource) GetWebsiteDomainsOk() (*[]string, bool)`

GetWebsiteDomainsOk returns a tuple with the WebsiteDomains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsiteDomains

`func (o *CompetitorResource) SetWebsiteDomains(v []string)`

SetWebsiteDomains sets WebsiteDomains field to given value.


### GetBrandNames

`func (o *CompetitorResource) GetBrandNames() []string`

GetBrandNames returns the BrandNames field if non-nil, zero value otherwise.

### GetBrandNamesOk

`func (o *CompetitorResource) GetBrandNamesOk() (*[]string, bool)`

GetBrandNamesOk returns a tuple with the BrandNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrandNames

`func (o *CompetitorResource) SetBrandNames(v []string)`

SetBrandNames sets BrandNames field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


