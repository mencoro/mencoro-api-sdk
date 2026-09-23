# ProjectSentimentBreakdown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PerEngine** | [**[]PerEngineSentiment**](PerEngineSentiment.md) |  | 
**PerCompetitor** | [**[]PerCompetitorSentiment**](PerCompetitorSentiment.md) |  | 

## Methods

### NewProjectSentimentBreakdown

`func NewProjectSentimentBreakdown(perEngine []PerEngineSentiment, perCompetitor []PerCompetitorSentiment, ) *ProjectSentimentBreakdown`

NewProjectSentimentBreakdown instantiates a new ProjectSentimentBreakdown object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectSentimentBreakdownWithDefaults

`func NewProjectSentimentBreakdownWithDefaults() *ProjectSentimentBreakdown`

NewProjectSentimentBreakdownWithDefaults instantiates a new ProjectSentimentBreakdown object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPerEngine

`func (o *ProjectSentimentBreakdown) GetPerEngine() []PerEngineSentiment`

GetPerEngine returns the PerEngine field if non-nil, zero value otherwise.

### GetPerEngineOk

`func (o *ProjectSentimentBreakdown) GetPerEngineOk() (*[]PerEngineSentiment, bool)`

GetPerEngineOk returns a tuple with the PerEngine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPerEngine

`func (o *ProjectSentimentBreakdown) SetPerEngine(v []PerEngineSentiment)`

SetPerEngine sets PerEngine field to given value.


### GetPerCompetitor

`func (o *ProjectSentimentBreakdown) GetPerCompetitor() []PerCompetitorSentiment`

GetPerCompetitor returns the PerCompetitor field if non-nil, zero value otherwise.

### GetPerCompetitorOk

`func (o *ProjectSentimentBreakdown) GetPerCompetitorOk() (*[]PerCompetitorSentiment, bool)`

GetPerCompetitorOk returns a tuple with the PerCompetitor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPerCompetitor

`func (o *ProjectSentimentBreakdown) SetPerCompetitor(v []PerCompetitorSentiment)`

SetPerCompetitor sets PerCompetitor field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


