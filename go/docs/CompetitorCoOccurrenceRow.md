# CompetitorCoOccurrenceRow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CompetitorId** | **string** |  | 
**SharedResponseCount** | **int32** |  | 
**BrandWins** | **int32** |  | 
**CompetitorWins** | **int32** |  | 
**Ties** | **int32** |  | 
**WinRate** | Pointer to **NullableInt32** |  | [optional] 
**AvgOwnPosition** | Pointer to **NullableFloat32** |  | [optional] 
**AvgCompetitorPosition** | Pointer to **NullableFloat32** |  | [optional] 
**ExampleQueryText** | Pointer to **NullableString** |  | [optional] 
**ExampleAiResponseId** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewCompetitorCoOccurrenceRow

`func NewCompetitorCoOccurrenceRow(competitorId string, sharedResponseCount int32, brandWins int32, competitorWins int32, ties int32, ) *CompetitorCoOccurrenceRow`

NewCompetitorCoOccurrenceRow instantiates a new CompetitorCoOccurrenceRow object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompetitorCoOccurrenceRowWithDefaults

`func NewCompetitorCoOccurrenceRowWithDefaults() *CompetitorCoOccurrenceRow`

NewCompetitorCoOccurrenceRowWithDefaults instantiates a new CompetitorCoOccurrenceRow object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCompetitorId

`func (o *CompetitorCoOccurrenceRow) GetCompetitorId() string`

GetCompetitorId returns the CompetitorId field if non-nil, zero value otherwise.

### GetCompetitorIdOk

`func (o *CompetitorCoOccurrenceRow) GetCompetitorIdOk() (*string, bool)`

GetCompetitorIdOk returns a tuple with the CompetitorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitorId

`func (o *CompetitorCoOccurrenceRow) SetCompetitorId(v string)`

SetCompetitorId sets CompetitorId field to given value.


### GetSharedResponseCount

`func (o *CompetitorCoOccurrenceRow) GetSharedResponseCount() int32`

GetSharedResponseCount returns the SharedResponseCount field if non-nil, zero value otherwise.

### GetSharedResponseCountOk

`func (o *CompetitorCoOccurrenceRow) GetSharedResponseCountOk() (*int32, bool)`

GetSharedResponseCountOk returns a tuple with the SharedResponseCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSharedResponseCount

`func (o *CompetitorCoOccurrenceRow) SetSharedResponseCount(v int32)`

SetSharedResponseCount sets SharedResponseCount field to given value.


### GetBrandWins

`func (o *CompetitorCoOccurrenceRow) GetBrandWins() int32`

GetBrandWins returns the BrandWins field if non-nil, zero value otherwise.

### GetBrandWinsOk

`func (o *CompetitorCoOccurrenceRow) GetBrandWinsOk() (*int32, bool)`

GetBrandWinsOk returns a tuple with the BrandWins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBrandWins

`func (o *CompetitorCoOccurrenceRow) SetBrandWins(v int32)`

SetBrandWins sets BrandWins field to given value.


### GetCompetitorWins

`func (o *CompetitorCoOccurrenceRow) GetCompetitorWins() int32`

GetCompetitorWins returns the CompetitorWins field if non-nil, zero value otherwise.

### GetCompetitorWinsOk

`func (o *CompetitorCoOccurrenceRow) GetCompetitorWinsOk() (*int32, bool)`

GetCompetitorWinsOk returns a tuple with the CompetitorWins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompetitorWins

`func (o *CompetitorCoOccurrenceRow) SetCompetitorWins(v int32)`

SetCompetitorWins sets CompetitorWins field to given value.


### GetTies

`func (o *CompetitorCoOccurrenceRow) GetTies() int32`

GetTies returns the Ties field if non-nil, zero value otherwise.

### GetTiesOk

`func (o *CompetitorCoOccurrenceRow) GetTiesOk() (*int32, bool)`

GetTiesOk returns a tuple with the Ties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTies

`func (o *CompetitorCoOccurrenceRow) SetTies(v int32)`

SetTies sets Ties field to given value.


### GetWinRate

`func (o *CompetitorCoOccurrenceRow) GetWinRate() int32`

GetWinRate returns the WinRate field if non-nil, zero value otherwise.

### GetWinRateOk

`func (o *CompetitorCoOccurrenceRow) GetWinRateOk() (*int32, bool)`

GetWinRateOk returns a tuple with the WinRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWinRate

`func (o *CompetitorCoOccurrenceRow) SetWinRate(v int32)`

SetWinRate sets WinRate field to given value.

### HasWinRate

`func (o *CompetitorCoOccurrenceRow) HasWinRate() bool`

HasWinRate returns a boolean if a field has been set.

### SetWinRateNil

`func (o *CompetitorCoOccurrenceRow) SetWinRateNil(b bool)`

 SetWinRateNil sets the value for WinRate to be an explicit nil

### UnsetWinRate
`func (o *CompetitorCoOccurrenceRow) UnsetWinRate()`

UnsetWinRate ensures that no value is present for WinRate, not even an explicit nil
### GetAvgOwnPosition

`func (o *CompetitorCoOccurrenceRow) GetAvgOwnPosition() float32`

GetAvgOwnPosition returns the AvgOwnPosition field if non-nil, zero value otherwise.

### GetAvgOwnPositionOk

`func (o *CompetitorCoOccurrenceRow) GetAvgOwnPositionOk() (*float32, bool)`

GetAvgOwnPositionOk returns a tuple with the AvgOwnPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgOwnPosition

`func (o *CompetitorCoOccurrenceRow) SetAvgOwnPosition(v float32)`

SetAvgOwnPosition sets AvgOwnPosition field to given value.

### HasAvgOwnPosition

`func (o *CompetitorCoOccurrenceRow) HasAvgOwnPosition() bool`

HasAvgOwnPosition returns a boolean if a field has been set.

### SetAvgOwnPositionNil

`func (o *CompetitorCoOccurrenceRow) SetAvgOwnPositionNil(b bool)`

 SetAvgOwnPositionNil sets the value for AvgOwnPosition to be an explicit nil

### UnsetAvgOwnPosition
`func (o *CompetitorCoOccurrenceRow) UnsetAvgOwnPosition()`

UnsetAvgOwnPosition ensures that no value is present for AvgOwnPosition, not even an explicit nil
### GetAvgCompetitorPosition

`func (o *CompetitorCoOccurrenceRow) GetAvgCompetitorPosition() float32`

GetAvgCompetitorPosition returns the AvgCompetitorPosition field if non-nil, zero value otherwise.

### GetAvgCompetitorPositionOk

`func (o *CompetitorCoOccurrenceRow) GetAvgCompetitorPositionOk() (*float32, bool)`

GetAvgCompetitorPositionOk returns a tuple with the AvgCompetitorPosition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgCompetitorPosition

`func (o *CompetitorCoOccurrenceRow) SetAvgCompetitorPosition(v float32)`

SetAvgCompetitorPosition sets AvgCompetitorPosition field to given value.

### HasAvgCompetitorPosition

`func (o *CompetitorCoOccurrenceRow) HasAvgCompetitorPosition() bool`

HasAvgCompetitorPosition returns a boolean if a field has been set.

### SetAvgCompetitorPositionNil

`func (o *CompetitorCoOccurrenceRow) SetAvgCompetitorPositionNil(b bool)`

 SetAvgCompetitorPositionNil sets the value for AvgCompetitorPosition to be an explicit nil

### UnsetAvgCompetitorPosition
`func (o *CompetitorCoOccurrenceRow) UnsetAvgCompetitorPosition()`

UnsetAvgCompetitorPosition ensures that no value is present for AvgCompetitorPosition, not even an explicit nil
### GetExampleQueryText

`func (o *CompetitorCoOccurrenceRow) GetExampleQueryText() string`

GetExampleQueryText returns the ExampleQueryText field if non-nil, zero value otherwise.

### GetExampleQueryTextOk

`func (o *CompetitorCoOccurrenceRow) GetExampleQueryTextOk() (*string, bool)`

GetExampleQueryTextOk returns a tuple with the ExampleQueryText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExampleQueryText

`func (o *CompetitorCoOccurrenceRow) SetExampleQueryText(v string)`

SetExampleQueryText sets ExampleQueryText field to given value.

### HasExampleQueryText

`func (o *CompetitorCoOccurrenceRow) HasExampleQueryText() bool`

HasExampleQueryText returns a boolean if a field has been set.

### SetExampleQueryTextNil

`func (o *CompetitorCoOccurrenceRow) SetExampleQueryTextNil(b bool)`

 SetExampleQueryTextNil sets the value for ExampleQueryText to be an explicit nil

### UnsetExampleQueryText
`func (o *CompetitorCoOccurrenceRow) UnsetExampleQueryText()`

UnsetExampleQueryText ensures that no value is present for ExampleQueryText, not even an explicit nil
### GetExampleAiResponseId

`func (o *CompetitorCoOccurrenceRow) GetExampleAiResponseId() string`

GetExampleAiResponseId returns the ExampleAiResponseId field if non-nil, zero value otherwise.

### GetExampleAiResponseIdOk

`func (o *CompetitorCoOccurrenceRow) GetExampleAiResponseIdOk() (*string, bool)`

GetExampleAiResponseIdOk returns a tuple with the ExampleAiResponseId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExampleAiResponseId

`func (o *CompetitorCoOccurrenceRow) SetExampleAiResponseId(v string)`

SetExampleAiResponseId sets ExampleAiResponseId field to given value.

### HasExampleAiResponseId

`func (o *CompetitorCoOccurrenceRow) HasExampleAiResponseId() bool`

HasExampleAiResponseId returns a boolean if a field has been set.

### SetExampleAiResponseIdNil

`func (o *CompetitorCoOccurrenceRow) SetExampleAiResponseIdNil(b bool)`

 SetExampleAiResponseIdNil sets the value for ExampleAiResponseId to be an explicit nil

### UnsetExampleAiResponseId
`func (o *CompetitorCoOccurrenceRow) UnsetExampleAiResponseId()`

UnsetExampleAiResponseId ensures that no value is present for ExampleAiResponseId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


