# GeneralEducationPropositionDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**reference** | **str** |  | 
**formation** | [**PropositionSearchFormation**](PropositionSearchFormation.md) |  | 
**matricule_candidat** | **str** |  | 
**prenom_candidat** | **str** |  | 
**nom_candidat** | **str** |  | 
**creee_le** | **datetime** |  | 
**statut** | **str** |  | 
**erreurs** | [**[InlineResponse200]**](InlineResponse200.md) |  | 
**curriculum** | **[str]** |  | 
**equivalence_diplome** | **[str]** |  | 
**annee_calculee** | **int, none_type** |  | [optional] 
**pot_calcule** | **str** |  | [optional] 
**date_fin_pot** | **date, none_type** |  | [optional] 
**links** | [**GeneralEducationPropositionDTOLinks**](GeneralEducationPropositionDTOLinks.md) |  | [optional] 
**bourse_double_diplome** | [**DoctoratePropositionDTOBourseRecherche**](DoctoratePropositionDTOBourseRecherche.md) |  | [optional] 
**bourse_internationale** | [**DoctoratePropositionDTOBourseRecherche**](DoctoratePropositionDTOBourseRecherche.md) |  | [optional] 
**bourse_erasmus_mundus** | [**DoctoratePropositionDTOBourseRecherche**](DoctoratePropositionDTOBourseRecherche.md) |  | [optional] 
**reponses_questions_specifiques** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


