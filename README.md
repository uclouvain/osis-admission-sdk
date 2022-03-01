# osis-admission-sdk
This API delivers data for the Admission project.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.15
- Package version: 1.0.15
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/uclouvain/osis](https://github.com/uclouvain/osis)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import osis_admission_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osis_admission_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import osis_admission_sdk
from pprint import pprint
from osis_admission_sdk.api import autocomplete_api
from osis_admission_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_admission_sdk.model.doctorat_dto import DoctoratDTO
from osis_admission_sdk.model.error import Error
from osis_admission_sdk.model.inline_response2001 import InlineResponse2001
from osis_admission_sdk.model.inline_response2002 import InlineResponse2002
from osis_admission_sdk.model.sector_dto import SectorDTO
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/admission
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_admission_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/admission"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'


# Enter a context with an instance of the API client
with osis_admission_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autocomplete_api.AutocompleteApi(api_client)
    sigle = "sigle_example" # str | 
accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
x_user_first_name = "X-User-FirstName_example" # str |  (optional)
x_user_last_name = "X-User-LastName_example" # str |  (optional)
x_user_email = "X-User-Email_example" # str |  (optional)
x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    try:
        api_response = api_instance.list_doctorat_dtos(sigle, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_admission_sdk.ApiException as e:
        print("Exception when calling AutocompleteApi->list_doctorat_dtos: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/admission*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutocompleteApi* | [**list_doctorat_dtos**](docs/AutocompleteApi.md#list_doctorat_dtos) | **GET** /autocomplete/sector/{sigle}/doctorates | 
*AutocompleteApi* | [**list_persons**](docs/AutocompleteApi.md#list_persons) | **GET** /autocomplete/person | 
*AutocompleteApi* | [**list_sector_dtos**](docs/AutocompleteApi.md#list_sector_dtos) | **GET** /autocomplete/sector | 
*AutocompleteApi* | [**list_tutors**](docs/AutocompleteApi.md#list_tutors) | **GET** /autocomplete/tutor | 
*PersonApi* | [**create_curriculum_experience**](docs/PersonApi.md#create_curriculum_experience) | **POST** /curriculum | 
*PersonApi* | [**create_curriculum_experience_admission**](docs/PersonApi.md#create_curriculum_experience_admission) | **POST** /propositions/{uuid}/curriculum | 
*PersonApi* | [**create_language_knowledge**](docs/PersonApi.md#create_language_knowledge) | **POST** /languages_knowledge | 
*PersonApi* | [**create_language_knowledge_admission**](docs/PersonApi.md#create_language_knowledge_admission) | **POST** /propositions/{uuid}/languages_knowledge | 
*PersonApi* | [**destroy_curriculum_experience**](docs/PersonApi.md#destroy_curriculum_experience) | **DELETE** /curriculum/{xp} | 
*PersonApi* | [**destroy_curriculum_experience_admission**](docs/PersonApi.md#destroy_curriculum_experience_admission) | **DELETE** /propositions/{uuid}/curriculum/{xp} | 
*PersonApi* | [**list_curriculum_experiences**](docs/PersonApi.md#list_curriculum_experiences) | **GET** /curriculum | 
*PersonApi* | [**list_curriculum_experiences_admission**](docs/PersonApi.md#list_curriculum_experiences_admission) | **GET** /propositions/{uuid}/curriculum | 
*PersonApi* | [**list_language_knowledges**](docs/PersonApi.md#list_language_knowledges) | **GET** /languages_knowledge | 
*PersonApi* | [**list_language_knowledges_admission**](docs/PersonApi.md#list_language_knowledges_admission) | **GET** /propositions/{uuid}/languages_knowledge | 
*PersonApi* | [**retrieve_coordonnees**](docs/PersonApi.md#retrieve_coordonnees) | **GET** /coordonnees | 
*PersonApi* | [**retrieve_coordonnees_admission**](docs/PersonApi.md#retrieve_coordonnees_admission) | **GET** /propositions/{uuid}/coordonnees | 
*PersonApi* | [**retrieve_curriculum_experience**](docs/PersonApi.md#retrieve_curriculum_experience) | **GET** /curriculum/{xp} | 
*PersonApi* | [**retrieve_curriculum_experience_admission**](docs/PersonApi.md#retrieve_curriculum_experience_admission) | **GET** /propositions/{uuid}/curriculum/{xp} | 
*PersonApi* | [**retrieve_curriculum_file**](docs/PersonApi.md#retrieve_curriculum_file) | **GET** /curriculum/file | 
*PersonApi* | [**retrieve_curriculum_file_admission**](docs/PersonApi.md#retrieve_curriculum_file_admission) | **GET** /propositions/{uuid}/curriculum/file | 
*PersonApi* | [**retrieve_high_school_diploma**](docs/PersonApi.md#retrieve_high_school_diploma) | **GET** /secondary_studies | 
*PersonApi* | [**retrieve_high_school_diploma_admission**](docs/PersonApi.md#retrieve_high_school_diploma_admission) | **GET** /propositions/{uuid}/secondary_studies | 
*PersonApi* | [**retrieve_person_identification**](docs/PersonApi.md#retrieve_person_identification) | **GET** /person | 
*PersonApi* | [**retrieve_person_identification_admission**](docs/PersonApi.md#retrieve_person_identification_admission) | **GET** /propositions/{uuid}/person | 
*PersonApi* | [**update_coordonnees**](docs/PersonApi.md#update_coordonnees) | **PUT** /coordonnees | 
*PersonApi* | [**update_coordonnees_admission**](docs/PersonApi.md#update_coordonnees_admission) | **PUT** /propositions/{uuid}/coordonnees | 
*PersonApi* | [**update_curriculum_experience**](docs/PersonApi.md#update_curriculum_experience) | **PUT** /curriculum/{xp} | 
*PersonApi* | [**update_curriculum_experience_admission**](docs/PersonApi.md#update_curriculum_experience_admission) | **PUT** /propositions/{uuid}/curriculum/{xp} | 
*PersonApi* | [**update_curriculum_file**](docs/PersonApi.md#update_curriculum_file) | **PUT** /curriculum/file | 
*PersonApi* | [**update_curriculum_file_admission**](docs/PersonApi.md#update_curriculum_file_admission) | **PUT** /propositions/{uuid}/curriculum/file | 
*PersonApi* | [**update_high_school_diploma**](docs/PersonApi.md#update_high_school_diploma) | **PUT** /secondary_studies | 
*PersonApi* | [**update_high_school_diploma_admission**](docs/PersonApi.md#update_high_school_diploma_admission) | **PUT** /propositions/{uuid}/secondary_studies | 
*PersonApi* | [**update_person_identification**](docs/PersonApi.md#update_person_identification) | **PUT** /person | 
*PersonApi* | [**update_person_identification_admission**](docs/PersonApi.md#update_person_identification_admission) | **PUT** /propositions/{uuid}/person | 
*PropositionsApi* | [**add_member**](docs/PropositionsApi.md#add_member) | **PUT** /propositions/{uuid}/supervision | 
*PropositionsApi* | [**approve_by_pdf**](docs/PropositionsApi.md#approve_by_pdf) | **POST** /propositions/{uuid}/approve-by-pdf | 
*PropositionsApi* | [**approve_proposition**](docs/PropositionsApi.md#approve_proposition) | **POST** /propositions/{uuid}/approve | 
*PropositionsApi* | [**create_proposition**](docs/PropositionsApi.md#create_proposition) | **POST** /propositions | 
*PropositionsApi* | [**create_signatures**](docs/PropositionsApi.md#create_signatures) | **POST** /propositions/{uuid}/request_signatures | 
*PropositionsApi* | [**destroy_proposition**](docs/PropositionsApi.md#destroy_proposition) | **DELETE** /propositions/{uuid} | 
*PropositionsApi* | [**list_propositions**](docs/PropositionsApi.md#list_propositions) | **GET** /propositions | 
*PropositionsApi* | [**list_supervised_propositions**](docs/PropositionsApi.md#list_supervised_propositions) | **GET** /supervised_propositions | 
*PropositionsApi* | [**reject_proposition**](docs/PropositionsApi.md#reject_proposition) | **PUT** /propositions/{uuid}/approve | 
*PropositionsApi* | [**remove_member**](docs/PropositionsApi.md#remove_member) | **POST** /propositions/{uuid}/supervision | 
*PropositionsApi* | [**retrieve_cotutelle**](docs/PropositionsApi.md#retrieve_cotutelle) | **GET** /propositions/{uuid}/cotutelle | 
*PropositionsApi* | [**retrieve_dashboard**](docs/PropositionsApi.md#retrieve_dashboard) | **GET** /dashboard | 
*PropositionsApi* | [**retrieve_proposition**](docs/PropositionsApi.md#retrieve_proposition) | **GET** /propositions/{uuid} | 
*PropositionsApi* | [**retrieve_supervision**](docs/PropositionsApi.md#retrieve_supervision) | **GET** /propositions/{uuid}/supervision | 
*PropositionsApi* | [**retrieve_verify_project**](docs/PropositionsApi.md#retrieve_verify_project) | **GET** /propositions/{uuid}/verify_project | 
*PropositionsApi* | [**submit_proposition**](docs/PropositionsApi.md#submit_proposition) | **POST** /propositions/{uuid}/submit | 
*PropositionsApi* | [**update_cotutelle**](docs/PropositionsApi.md#update_cotutelle) | **PUT** /propositions/{uuid}/cotutelle | 
*PropositionsApi* | [**update_proposition**](docs/PropositionsApi.md#update_proposition) | **PUT** /propositions/{uuid} | 
*PropositionsApi* | [**verify_proposition**](docs/PropositionsApi.md#verify_proposition) | **GET** /propositions/{uuid}/submit | 


## Documentation For Models

 - [AcceptedLanguageEnum](docs/AcceptedLanguageEnum.md)
 - [ActionLink](docs/ActionLink.md)
 - [ActivityType](docs/ActivityType.md)
 - [ActorType](docs/ActorType.md)
 - [AdmissionType](docs/AdmissionType.md)
 - [ApprouverPropositionCommand](docs/ApprouverPropositionCommand.md)
 - [ApprouverPropositionParPdfCommand](docs/ApprouverPropositionParPdfCommand.md)
 - [BelgianCommunitiesOfEducation](docs/BelgianCommunitiesOfEducation.md)
 - [ChoixCommissionProximite](docs/ChoixCommissionProximite.md)
 - [ChoixDoctoratDejaRealise](docs/ChoixDoctoratDejaRealise.md)
 - [ChoixLangueRedactionThese](docs/ChoixLangueRedactionThese.md)
 - [CivilState](docs/CivilState.md)
 - [CompleterPropositionCommand](docs/CompleterPropositionCommand.md)
 - [Coordonnees](docs/Coordonnees.md)
 - [CoordonneesContact](docs/CoordonneesContact.md)
 - [CotutelleDTO](docs/CotutelleDTO.md)
 - [CreditType](docs/CreditType.md)
 - [CurriculumFile](docs/CurriculumFile.md)
 - [Dashboard](docs/Dashboard.md)
 - [DashboardLinks](docs/DashboardLinks.md)
 - [DefinirCotutelleCommand](docs/DefinirCotutelleCommand.md)
 - [DiplomaResults](docs/DiplomaResults.md)
 - [DoctoratDTO](docs/DoctoratDTO.md)
 - [EducationalType](docs/EducationalType.md)
 - [Equivalence](docs/Equivalence.md)
 - [Error](docs/Error.md)
 - [ExperienceInput](docs/ExperienceInput.md)
 - [ExperienceOutput](docs/ExperienceOutput.md)
 - [ExperienceOutputCurriculumYear](docs/ExperienceOutputCurriculumYear.md)
 - [ExperienceType](docs/ExperienceType.md)
 - [ForeignDiplomaTypes](docs/ForeignDiplomaTypes.md)
 - [ForeignStudyCycleType](docs/ForeignStudyCycleType.md)
 - [Grade](docs/Grade.md)
 - [HighSchoolDiploma](docs/HighSchoolDiploma.md)
 - [HighSchoolDiplomaBelgianDiploma](docs/HighSchoolDiplomaBelgianDiploma.md)
 - [HighSchoolDiplomaBelgianDiplomaSchedule](docs/HighSchoolDiplomaBelgianDiplomaSchedule.md)
 - [HighSchoolDiplomaForeignDiploma](docs/HighSchoolDiplomaForeignDiploma.md)
 - [InitierPropositionCommand](docs/InitierPropositionCommand.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [LanguageKnowledge](docs/LanguageKnowledge.md)
 - [LanguageKnowledgeGrade](docs/LanguageKnowledgeGrade.md)
 - [Person](docs/Person.md)
 - [PersonIdentification](docs/PersonIdentification.md)
 - [PropositionDTO](docs/PropositionDTO.md)
 - [PropositionDTOLinks](docs/PropositionDTOLinks.md)
 - [PropositionIdentityDTO](docs/PropositionIdentityDTO.md)
 - [PropositionSearch](docs/PropositionSearch.md)
 - [PropositionSearchDTO](docs/PropositionSearchDTO.md)
 - [PropositionSearchLinks](docs/PropositionSearchLinks.md)
 - [PropositionSearchLinks1](docs/PropositionSearchLinks1.md)
 - [PropositionSearchPropositions](docs/PropositionSearchPropositions.md)
 - [RefuserPropositionCommand](docs/RefuserPropositionCommand.md)
 - [Result](docs/Result.md)
 - [SectorDTO](docs/SectorDTO.md)
 - [StudySystem](docs/StudySystem.md)
 - [SupervisionActor](docs/SupervisionActor.md)
 - [SupervisionDTO](docs/SupervisionDTO.md)
 - [SupervisionDTOPromoteur](docs/SupervisionDTOPromoteur.md)
 - [SupervisionDTOSignaturesMembresCA](docs/SupervisionDTOSignaturesMembresCA.md)
 - [SupervisionDTOSignaturesPromoteurs](docs/SupervisionDTOSignaturesPromoteurs.md)
 - [Tutor](docs/Tutor.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in osis_admission_sdk.apis and osis_admission_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from osis_admission_sdk.api.default_api import DefaultApi`
- `from osis_admission_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import osis_admission_sdk
from osis_admission_sdk.apis import *
from osis_admission_sdk.models import *
```

