# osis-admission-sdk
This API delivers data for the Admission project.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.52
- Package version: 1.0.52
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/uclouvain/osis](https://github.com/uclouvain/osis)

## Requirements.

Python >=3.6

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
from osis_admission_sdk.model.formation_continue_dto import FormationContinueDTO
from osis_admission_sdk.model.formation_generale_dto import FormationGeneraleDTO
from osis_admission_sdk.model.inline_response2001 import InlineResponse2001
from osis_admission_sdk.model.inline_response2002 import InlineResponse2002
from osis_admission_sdk.model.inline_response2003 import InlineResponse2003
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
campus = "campus_example" # str | The identifier of the campus where the training takes place (optional)
accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) (optional)
x_user_first_name = "X-User-FirstName_example" # str |  (optional)
x_user_last_name = "X-User-LastName_example" # str |  (optional)
x_user_email = "X-User-Email_example" # str |  (optional)
x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    try:
        api_response = api_instance.list_doctorat_dtos(sigle, campus=campus, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_admission_sdk.ApiException as e:
        print("Exception when calling AutocompleteApi->list_doctorat_dtos: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/admission*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutocompleteApi* | [**list_doctorat_dtos**](docs/AutocompleteApi.md#list_doctorat_dtos) | **GET** /autocomplete/sector/{sigle}/doctorates | 
*AutocompleteApi* | [**list_formation_continue_dtos**](docs/AutocompleteApi.md#list_formation_continue_dtos) | **GET** /autocomplete/continuing-education | 
*AutocompleteApi* | [**list_formation_generale_dtos**](docs/AutocompleteApi.md#list_formation_generale_dtos) | **GET** /autocomplete/general-education | 
*AutocompleteApi* | [**list_persons**](docs/AutocompleteApi.md#list_persons) | **GET** /autocomplete/person | 
*AutocompleteApi* | [**list_scholarships**](docs/AutocompleteApi.md#list_scholarships) | **GET** /autocomplete/{scholarship_type}/scholarship | 
*AutocompleteApi* | [**list_sector_dtos**](docs/AutocompleteApi.md#list_sector_dtos) | **GET** /autocomplete/sector | 
*AutocompleteApi* | [**list_tutors**](docs/AutocompleteApi.md#list_tutors) | **GET** /autocomplete/tutor | 
*CampusApi* | [**list_campus**](docs/CampusApi.md#list_campus) | **GET** /campus | 
*CampusApi* | [**retrieve_campus**](docs/CampusApi.md#retrieve_campus) | **GET** /campus/{uuid} | 
*PersonApi* | [**create_educational_experience**](docs/PersonApi.md#create_educational_experience) | **POST** /curriculum/educational | 
*PersonApi* | [**create_educational_experience_admission**](docs/PersonApi.md#create_educational_experience_admission) | **POST** /propositions/doctorate/{uuid}/curriculum/educational | 
*PersonApi* | [**create_educational_experience_continuing_education_admission**](docs/PersonApi.md#create_educational_experience_continuing_education_admission) | **POST** /propositions/continuing-education/{uuid}/curriculum/educational | 
*PersonApi* | [**create_educational_experience_general_education_admission**](docs/PersonApi.md#create_educational_experience_general_education_admission) | **POST** /propositions/general-education/{uuid}/curriculum/educational | 
*PersonApi* | [**create_language_knowledge**](docs/PersonApi.md#create_language_knowledge) | **POST** /languages_knowledge | 
*PersonApi* | [**create_language_knowledge_admission**](docs/PersonApi.md#create_language_knowledge_admission) | **POST** /propositions/doctorate/{uuid}/languages_knowledge | 
*PersonApi* | [**create_professional_experience**](docs/PersonApi.md#create_professional_experience) | **POST** /curriculum/professional | 
*PersonApi* | [**create_professional_experience_admission**](docs/PersonApi.md#create_professional_experience_admission) | **POST** /propositions/doctorate/{uuid}/curriculum/professional | 
*PersonApi* | [**create_professional_experience_continuing_education_admission**](docs/PersonApi.md#create_professional_experience_continuing_education_admission) | **POST** /propositions/continuing-education/{uuid}/curriculum/professional | 
*PersonApi* | [**create_professional_experience_general_education_admission**](docs/PersonApi.md#create_professional_experience_general_education_admission) | **POST** /propositions/general-education/{uuid}/curriculum/professional | 
*PersonApi* | [**destroy_educational_experience**](docs/PersonApi.md#destroy_educational_experience) | **DELETE** /curriculum/educational/{experience_id} | 
*PersonApi* | [**destroy_educational_experience_admission**](docs/PersonApi.md#destroy_educational_experience_admission) | **DELETE** /propositions/doctorate/{uuid}/curriculum/educational/{experience_id} | 
*PersonApi* | [**destroy_educational_experience_continuing_education_admission**](docs/PersonApi.md#destroy_educational_experience_continuing_education_admission) | **DELETE** /propositions/continuing-education/{uuid}/curriculum/educational/{experience_id} | 
*PersonApi* | [**destroy_educational_experience_general_education_admission**](docs/PersonApi.md#destroy_educational_experience_general_education_admission) | **DELETE** /propositions/general-education/{uuid}/curriculum/educational/{experience_id} | 
*PersonApi* | [**destroy_professional_experience**](docs/PersonApi.md#destroy_professional_experience) | **DELETE** /curriculum/professional/{experience_id} | 
*PersonApi* | [**destroy_professional_experience_admission**](docs/PersonApi.md#destroy_professional_experience_admission) | **DELETE** /propositions/doctorate/{uuid}/curriculum/professional/{experience_id} | 
*PersonApi* | [**destroy_professional_experience_continuing_education_admission**](docs/PersonApi.md#destroy_professional_experience_continuing_education_admission) | **DELETE** /propositions/continuing-education/{uuid}/curriculum/professional/{experience_id} | 
*PersonApi* | [**destroy_professional_experience_general_education_admission**](docs/PersonApi.md#destroy_professional_experience_general_education_admission) | **DELETE** /propositions/general-education/{uuid}/curriculum/professional/{experience_id} | 
*PersonApi* | [**list_language_knowledges**](docs/PersonApi.md#list_language_knowledges) | **GET** /languages_knowledge | 
*PersonApi* | [**list_language_knowledges_admission**](docs/PersonApi.md#list_language_knowledges_admission) | **GET** /propositions/doctorate/{uuid}/languages_knowledge | 
*PersonApi* | [**retrieve_coordonnees**](docs/PersonApi.md#retrieve_coordonnees) | **GET** /coordonnees | 
*PersonApi* | [**retrieve_coordonnees_admission**](docs/PersonApi.md#retrieve_coordonnees_admission) | **GET** /propositions/doctorate/{uuid}/coordonnees | 
*PersonApi* | [**retrieve_coordonnees_continuing_education_admission**](docs/PersonApi.md#retrieve_coordonnees_continuing_education_admission) | **GET** /propositions/continuing-education/{uuid}/coordonnees | 
*PersonApi* | [**retrieve_coordonnees_general_education_admission**](docs/PersonApi.md#retrieve_coordonnees_general_education_admission) | **GET** /propositions/general-education/{uuid}/coordonnees | 
*PersonApi* | [**retrieve_curriculum_details**](docs/PersonApi.md#retrieve_curriculum_details) | **GET** /curriculum | 
*PersonApi* | [**retrieve_curriculum_details_admission**](docs/PersonApi.md#retrieve_curriculum_details_admission) | **GET** /propositions/doctorate/{uuid}/curriculum | 
*PersonApi* | [**retrieve_curriculum_details_continuing_education_admission**](docs/PersonApi.md#retrieve_curriculum_details_continuing_education_admission) | **GET** /propositions/continuing-education/{uuid}/curriculum | 
*PersonApi* | [**retrieve_curriculum_details_general_education_admission**](docs/PersonApi.md#retrieve_curriculum_details_general_education_admission) | **GET** /propositions/general-education/{uuid}/curriculum | 
*PersonApi* | [**retrieve_educational_experience**](docs/PersonApi.md#retrieve_educational_experience) | **GET** /curriculum/educational/{experience_id} | 
*PersonApi* | [**retrieve_educational_experience_admission**](docs/PersonApi.md#retrieve_educational_experience_admission) | **GET** /propositions/doctorate/{uuid}/curriculum/educational/{experience_id} | 
*PersonApi* | [**retrieve_educational_experience_continuing_education_admission**](docs/PersonApi.md#retrieve_educational_experience_continuing_education_admission) | **GET** /propositions/continuing-education/{uuid}/curriculum/educational/{experience_id} | 
*PersonApi* | [**retrieve_educational_experience_general_education_admission**](docs/PersonApi.md#retrieve_educational_experience_general_education_admission) | **GET** /propositions/general-education/{uuid}/curriculum/educational/{experience_id} | 
*PersonApi* | [**retrieve_high_school_diploma**](docs/PersonApi.md#retrieve_high_school_diploma) | **GET** /secondary_studies | 
*PersonApi* | [**retrieve_high_school_diploma_admission**](docs/PersonApi.md#retrieve_high_school_diploma_admission) | **GET** /propositions/doctorate/{uuid}/secondary_studies | 
*PersonApi* | [**retrieve_high_school_diploma_continuing_education_admission**](docs/PersonApi.md#retrieve_high_school_diploma_continuing_education_admission) | **GET** /propositions/continuing-education/{uuid}/secondary-studies | 
*PersonApi* | [**retrieve_high_school_diploma_general_education_admission**](docs/PersonApi.md#retrieve_high_school_diploma_general_education_admission) | **GET** /propositions/general-education/{uuid}/secondary-studies | 
*PersonApi* | [**retrieve_person_identification**](docs/PersonApi.md#retrieve_person_identification) | **GET** /person | 
*PersonApi* | [**retrieve_person_identification_admission**](docs/PersonApi.md#retrieve_person_identification_admission) | **GET** /propositions/doctorate/{uuid}/person | 
*PersonApi* | [**retrieve_person_identification_continuing_education_admission**](docs/PersonApi.md#retrieve_person_identification_continuing_education_admission) | **GET** /propositions/continuing-education/{uuid}/person | 
*PersonApi* | [**retrieve_person_identification_general_education_admission**](docs/PersonApi.md#retrieve_person_identification_general_education_admission) | **GET** /propositions/general-education/{uuid}/person | 
*PersonApi* | [**retrieve_professional_experience**](docs/PersonApi.md#retrieve_professional_experience) | **GET** /curriculum/professional/{experience_id} | 
*PersonApi* | [**retrieve_professional_experience_admission**](docs/PersonApi.md#retrieve_professional_experience_admission) | **GET** /propositions/doctorate/{uuid}/curriculum/professional/{experience_id} | 
*PersonApi* | [**retrieve_professional_experience_continuing_education_admission**](docs/PersonApi.md#retrieve_professional_experience_continuing_education_admission) | **GET** /propositions/continuing-education/{uuid}/curriculum/professional/{experience_id} | 
*PersonApi* | [**retrieve_professional_experience_general_education_admission**](docs/PersonApi.md#retrieve_professional_experience_general_education_admission) | **GET** /propositions/general-education/{uuid}/curriculum/professional/{experience_id} | 
*PersonApi* | [**update_continuing_education_completer_curriculum_command_admission**](docs/PersonApi.md#update_continuing_education_completer_curriculum_command_admission) | **PUT** /propositions/continuing-education/{uuid}/curriculum | 
*PersonApi* | [**update_coordonnees**](docs/PersonApi.md#update_coordonnees) | **PUT** /coordonnees | 
*PersonApi* | [**update_coordonnees_admission**](docs/PersonApi.md#update_coordonnees_admission) | **PUT** /propositions/doctorate/{uuid}/coordonnees | 
*PersonApi* | [**update_coordonnees_continuing_education_admission**](docs/PersonApi.md#update_coordonnees_continuing_education_admission) | **PUT** /propositions/continuing-education/{uuid}/coordonnees | 
*PersonApi* | [**update_coordonnees_general_education_admission**](docs/PersonApi.md#update_coordonnees_general_education_admission) | **PUT** /propositions/general-education/{uuid}/coordonnees | 
*PersonApi* | [**update_doctorat_completer_curriculum_command_admission**](docs/PersonApi.md#update_doctorat_completer_curriculum_command_admission) | **PUT** /propositions/doctorate/{uuid}/curriculum | 
*PersonApi* | [**update_educational_experience**](docs/PersonApi.md#update_educational_experience) | **PUT** /curriculum/educational/{experience_id} | 
*PersonApi* | [**update_educational_experience_admission**](docs/PersonApi.md#update_educational_experience_admission) | **PUT** /propositions/doctorate/{uuid}/curriculum/educational/{experience_id} | 
*PersonApi* | [**update_educational_experience_continuing_education_admission**](docs/PersonApi.md#update_educational_experience_continuing_education_admission) | **PUT** /propositions/continuing-education/{uuid}/curriculum/educational/{experience_id} | 
*PersonApi* | [**update_educational_experience_general_education_admission**](docs/PersonApi.md#update_educational_experience_general_education_admission) | **PUT** /propositions/general-education/{uuid}/curriculum/educational/{experience_id} | 
*PersonApi* | [**update_general_education_completer_curriculum_command_admission**](docs/PersonApi.md#update_general_education_completer_curriculum_command_admission) | **PUT** /propositions/general-education/{uuid}/curriculum | 
*PersonApi* | [**update_high_school_diploma**](docs/PersonApi.md#update_high_school_diploma) | **PUT** /secondary_studies | 
*PersonApi* | [**update_high_school_diploma_admission**](docs/PersonApi.md#update_high_school_diploma_admission) | **PUT** /propositions/doctorate/{uuid}/secondary_studies | 
*PersonApi* | [**update_high_school_diploma_continuing_education_admission**](docs/PersonApi.md#update_high_school_diploma_continuing_education_admission) | **PUT** /propositions/continuing-education/{uuid}/secondary-studies | 
*PersonApi* | [**update_high_school_diploma_general_education_admission**](docs/PersonApi.md#update_high_school_diploma_general_education_admission) | **PUT** /propositions/general-education/{uuid}/secondary-studies | 
*PersonApi* | [**update_person_identification**](docs/PersonApi.md#update_person_identification) | **PUT** /person | 
*PersonApi* | [**update_person_identification_admission**](docs/PersonApi.md#update_person_identification_admission) | **PUT** /propositions/doctorate/{uuid}/person | 
*PersonApi* | [**update_person_identification_continuing_education_admission**](docs/PersonApi.md#update_person_identification_continuing_education_admission) | **PUT** /propositions/continuing-education/{uuid}/person | 
*PersonApi* | [**update_person_identification_general_education_admission**](docs/PersonApi.md#update_person_identification_general_education_admission) | **PUT** /propositions/general-education/{uuid}/person | 
*PersonApi* | [**update_professional_experience**](docs/PersonApi.md#update_professional_experience) | **PUT** /curriculum/professional/{experience_id} | 
*PersonApi* | [**update_professional_experience_admission**](docs/PersonApi.md#update_professional_experience_admission) | **PUT** /propositions/doctorate/{uuid}/curriculum/professional/{experience_id} | 
*PersonApi* | [**update_professional_experience_continuing_education_admission**](docs/PersonApi.md#update_professional_experience_continuing_education_admission) | **PUT** /propositions/continuing-education/{uuid}/curriculum/professional/{experience_id} | 
*PersonApi* | [**update_professional_experience_general_education_admission**](docs/PersonApi.md#update_professional_experience_general_education_admission) | **PUT** /propositions/general-education/{uuid}/curriculum/professional/{experience_id} | 
*PropositionsApi* | [**add_member**](docs/PropositionsApi.md#add_member) | **PUT** /propositions/doctorate/{uuid}/supervision | 
*PropositionsApi* | [**approve_by_pdf**](docs/PropositionsApi.md#approve_by_pdf) | **POST** /propositions/doctorate/{uuid}/supervision/approve-by-pdf | 
*PropositionsApi* | [**approve_proposition**](docs/PropositionsApi.md#approve_proposition) | **POST** /propositions/doctorate/{uuid}/supervision/approve | 
*PropositionsApi* | [**assent_training**](docs/PropositionsApi.md#assent_training) | **POST** /propositions/doctorate/{uuid}/training/assent | 
*PropositionsApi* | [**complete_confirmation_paper_by_promoter**](docs/PropositionsApi.md#complete_confirmation_paper_by_promoter) | **PUT** /propositions/doctorate/{uuid}/supervised_confirmation | 
*PropositionsApi* | [**create_continuing_training_choice**](docs/PropositionsApi.md#create_continuing_training_choice) | **POST** /propositions/continuing-education | 
*PropositionsApi* | [**create_doctoral_training**](docs/PropositionsApi.md#create_doctoral_training) | **POST** /propositions/doctorate/{uuid}/doctoral-training | 
*PropositionsApi* | [**create_general_training_choice**](docs/PropositionsApi.md#create_general_training_choice) | **POST** /propositions/general-education | 
*PropositionsApi* | [**create_proposition**](docs/PropositionsApi.md#create_proposition) | **POST** /propositions | 
*PropositionsApi* | [**create_signatures**](docs/PropositionsApi.md#create_signatures) | **POST** /propositions/doctorate/{uuid}/supervision/request-signatures | 
*PropositionsApi* | [**destroy_continuing_education_proposition**](docs/PropositionsApi.md#destroy_continuing_education_proposition) | **DELETE** /propositions/continuing-education/{uuid} | 
*PropositionsApi* | [**destroy_general_education_proposition**](docs/PropositionsApi.md#destroy_general_education_proposition) | **DELETE** /propositions/general-education/{uuid} | 
*PropositionsApi* | [**destroy_proposition**](docs/PropositionsApi.md#destroy_proposition) | **DELETE** /propositions/doctorate/{uuid} | 
*PropositionsApi* | [**destroy_training**](docs/PropositionsApi.md#destroy_training) | **DELETE** /propositions/doctorate/{uuid}/training/{activity_id} | 
*PropositionsApi* | [**list_complementary_training**](docs/PropositionsApi.md#list_complementary_training) | **GET** /propositions/doctorate/{uuid}/complementary-training | 
*PropositionsApi* | [**list_continuing_specific_questions**](docs/PropositionsApi.md#list_continuing_specific_questions) | **GET** /propositions/continuing-education/{uuid}/{tab}/specific-question | 
*PropositionsApi* | [**list_course_enrollment**](docs/PropositionsApi.md#list_course_enrollment) | **GET** /propositions/doctorate/{uuid}/course-enrollment | 
*PropositionsApi* | [**list_doctoral_training**](docs/PropositionsApi.md#list_doctoral_training) | **GET** /propositions/doctorate/{uuid}/doctoral-training | 
*PropositionsApi* | [**list_doctorate_specific_questions**](docs/PropositionsApi.md#list_doctorate_specific_questions) | **GET** /propositions/doctorate/{uuid}/{tab}/specific-question | 
*PropositionsApi* | [**list_general_specific_questions**](docs/PropositionsApi.md#list_general_specific_questions) | **GET** /propositions/general-education/{uuid}/{tab}/specific-question | 
*PropositionsApi* | [**list_propositions**](docs/PropositionsApi.md#list_propositions) | **GET** /propositions | 
*PropositionsApi* | [**list_supervised_propositions**](docs/PropositionsApi.md#list_supervised_propositions) | **GET** /supervised_propositions | 
*PropositionsApi* | [**partial_update_continuing_training_choice**](docs/PropositionsApi.md#partial_update_continuing_training_choice) | **PATCH** /propositions/continuing-education/{uuid}/training-choice | 
*PropositionsApi* | [**partial_update_doctorate_training_choice**](docs/PropositionsApi.md#partial_update_doctorate_training_choice) | **PATCH** /propositions/doctorate/{uuid}/training_choice | 
*PropositionsApi* | [**partial_update_general_training_choice**](docs/PropositionsApi.md#partial_update_general_training_choice) | **PATCH** /propositions/general-education/{uuid}/training-choice | 
*PropositionsApi* | [**reject_proposition**](docs/PropositionsApi.md#reject_proposition) | **PUT** /propositions/doctorate/{uuid}/supervision/approve | 
*PropositionsApi* | [**remove_member**](docs/PropositionsApi.md#remove_member) | **POST** /propositions/doctorate/{uuid}/supervision | 
*PropositionsApi* | [**retrieve_accounting**](docs/PropositionsApi.md#retrieve_accounting) | **GET** /propositions/doctorate/{uuid}/accounting | 
*PropositionsApi* | [**retrieve_confirmation_papers**](docs/PropositionsApi.md#retrieve_confirmation_papers) | **GET** /propositions/doctorate/{uuid}/confirmation | 
*PropositionsApi* | [**retrieve_continuing_accounting**](docs/PropositionsApi.md#retrieve_continuing_accounting) | **GET** /propositions/continuing-education/{uuid}/accounting | 
*PropositionsApi* | [**retrieve_continuing_education_proposition**](docs/PropositionsApi.md#retrieve_continuing_education_proposition) | **GET** /propositions/continuing-education/{uuid} | 
*PropositionsApi* | [**retrieve_cotutelle**](docs/PropositionsApi.md#retrieve_cotutelle) | **GET** /propositions/doctorate/{uuid}/cotutelle | 
*PropositionsApi* | [**retrieve_dashboard**](docs/PropositionsApi.md#retrieve_dashboard) | **GET** /dashboard | 
*PropositionsApi* | [**retrieve_doctoral_training_config**](docs/PropositionsApi.md#retrieve_doctoral_training_config) | **GET** /propositions/doctorate/{uuid}/training/config | 
*PropositionsApi* | [**retrieve_doctorate_dto**](docs/PropositionsApi.md#retrieve_doctorate_dto) | **GET** /propositions/doctorate/{uuid}/doctorate | 
*PropositionsApi* | [**retrieve_general_accounting**](docs/PropositionsApi.md#retrieve_general_accounting) | **GET** /propositions/general-education/{uuid}/accounting | 
*PropositionsApi* | [**retrieve_general_education_proposition**](docs/PropositionsApi.md#retrieve_general_education_proposition) | **GET** /propositions/general-education/{uuid} | 
*PropositionsApi* | [**retrieve_last_confirmation_paper**](docs/PropositionsApi.md#retrieve_last_confirmation_paper) | **GET** /propositions/doctorate/{uuid}/confirmation/last | 
*PropositionsApi* | [**retrieve_last_confirmation_paper_canvas**](docs/PropositionsApi.md#retrieve_last_confirmation_paper_canvas) | **GET** /propositions/doctorate/{uuid}/confirmation/last/canvas | 
*PropositionsApi* | [**retrieve_pool_questions**](docs/PropositionsApi.md#retrieve_pool_questions) | **GET** /propositions/general-education/{uuid}/pool-questions | 
*PropositionsApi* | [**retrieve_proposition**](docs/PropositionsApi.md#retrieve_proposition) | **GET** /propositions/doctorate/{uuid} | 
*PropositionsApi* | [**retrieve_supervision**](docs/PropositionsApi.md#retrieve_supervision) | **GET** /propositions/doctorate/{uuid}/supervision | 
*PropositionsApi* | [**retrieve_training**](docs/PropositionsApi.md#retrieve_training) | **GET** /propositions/doctorate/{uuid}/training/{activity_id} | 
*PropositionsApi* | [**retrieve_verify_project**](docs/PropositionsApi.md#retrieve_verify_project) | **GET** /propositions/doctorate/{uuid}/verify_project | 
*PropositionsApi* | [**set_reference_promoter**](docs/PropositionsApi.md#set_reference_promoter) | **PUT** /propositions/doctorate/{uuid}/supervision/set-reference-promoter | 
*PropositionsApi* | [**submit_confirmation_paper**](docs/PropositionsApi.md#submit_confirmation_paper) | **PUT** /propositions/doctorate/{uuid}/confirmation/last | 
*PropositionsApi* | [**submit_confirmation_paper_extension_request**](docs/PropositionsApi.md#submit_confirmation_paper_extension_request) | **POST** /propositions/doctorate/{uuid}/confirmation/last | 
*PropositionsApi* | [**submit_continuing_education_proposition**](docs/PropositionsApi.md#submit_continuing_education_proposition) | **POST** /propositions/continuing-education/{uuid}/submit | 
*PropositionsApi* | [**submit_general_education_proposition**](docs/PropositionsApi.md#submit_general_education_proposition) | **POST** /propositions/general-education/{uuid}/submit | 
*PropositionsApi* | [**submit_proposition**](docs/PropositionsApi.md#submit_proposition) | **POST** /propositions/doctorate/{uuid}/submit | 
*PropositionsApi* | [**submit_training**](docs/PropositionsApi.md#submit_training) | **POST** /propositions/doctorate/{uuid}/training/submit | 
*PropositionsApi* | [**update_accounting**](docs/PropositionsApi.md#update_accounting) | **PUT** /propositions/doctorate/{uuid}/accounting | 
*PropositionsApi* | [**update_continuing_accounting**](docs/PropositionsApi.md#update_continuing_accounting) | **PUT** /propositions/continuing-education/{uuid}/accounting | 
*PropositionsApi* | [**update_continuing_specific_question**](docs/PropositionsApi.md#update_continuing_specific_question) | **PUT** /propositions/continuing-education/{uuid}/specific-question | 
*PropositionsApi* | [**update_continuing_training_choice**](docs/PropositionsApi.md#update_continuing_training_choice) | **PUT** /propositions/continuing-education/{uuid}/training-choice | 
*PropositionsApi* | [**update_cotutelle**](docs/PropositionsApi.md#update_cotutelle) | **PUT** /propositions/doctorate/{uuid}/cotutelle | 
*PropositionsApi* | [**update_doctorate_training_choice**](docs/PropositionsApi.md#update_doctorate_training_choice) | **PUT** /propositions/doctorate/{uuid}/training_choice | 
*PropositionsApi* | [**update_general_accounting**](docs/PropositionsApi.md#update_general_accounting) | **PUT** /propositions/general-education/{uuid}/accounting | 
*PropositionsApi* | [**update_general_specific_question**](docs/PropositionsApi.md#update_general_specific_question) | **PUT** /propositions/general-education/{uuid}/specific-question | 
*PropositionsApi* | [**update_general_training_choice**](docs/PropositionsApi.md#update_general_training_choice) | **PUT** /propositions/general-education/{uuid}/training-choice | 
*PropositionsApi* | [**update_pool_questions**](docs/PropositionsApi.md#update_pool_questions) | **PUT** /propositions/general-education/{uuid}/pool-questions | 
*PropositionsApi* | [**update_proposition**](docs/PropositionsApi.md#update_proposition) | **PUT** /propositions/doctorate/{uuid} | 
*PropositionsApi* | [**update_training**](docs/PropositionsApi.md#update_training) | **PUT** /propositions/doctorate/{uuid}/training/{activity_id} | 
*PropositionsApi* | [**verify_continuing_education_proposition**](docs/PropositionsApi.md#verify_continuing_education_proposition) | **GET** /propositions/continuing-education/{uuid}/submit | 
*PropositionsApi* | [**verify_general_education_proposition**](docs/PropositionsApi.md#verify_general_education_proposition) | **GET** /propositions/general-education/{uuid}/submit | 
*PropositionsApi* | [**verify_proposition**](docs/PropositionsApi.md#verify_proposition) | **GET** /propositions/doctorate/{uuid}/submit | 
*ScholarshipApi* | [**retrieve_scholarship**](docs/ScholarshipApi.md#retrieve_scholarship) | **GET** /scholarship/{uuid} | 


## Documentation For Models

 - [AcceptedLanguageEnum](docs/AcceptedLanguageEnum.md)
 - [AccountingConditions](docs/AccountingConditions.md)
 - [AccountingConditionsLastFrenchCommunityHighEducationInstitutesAttended](docs/AccountingConditionsLastFrenchCommunityHighEducationInstitutesAttended.md)
 - [ActionLink](docs/ActionLink.md)
 - [ActivitySector](docs/ActivitySector.md)
 - [ActivityType](docs/ActivityType.md)
 - [ActorType](docs/ActorType.md)
 - [AdmissionType](docs/AdmissionType.md)
 - [ApprouverPropositionCommand](docs/ApprouverPropositionCommand.md)
 - [ApprouverPropositionParPdfCommand](docs/ApprouverPropositionParPdfCommand.md)
 - [BelgianCommunitiesOfEducation](docs/BelgianCommunitiesOfEducation.md)
 - [Campus](docs/Campus.md)
 - [CategorieActivite](docs/CategorieActivite.md)
 - [ChoixCommissionProximite](docs/ChoixCommissionProximite.md)
 - [ChoixDoctoratDejaRealise](docs/ChoixDoctoratDejaRealise.md)
 - [ChoixGenre](docs/ChoixGenre.md)
 - [ChoixLangueRedactionThese](docs/ChoixLangueRedactionThese.md)
 - [CivilState](docs/CivilState.md)
 - [Communication](docs/Communication.md)
 - [CompleteConfirmationPaperByPromoterCommand](docs/CompleteConfirmationPaperByPromoterCommand.md)
 - [CompleterComptabilitePropositionCommand](docs/CompleterComptabilitePropositionCommand.md)
 - [CompleterPropositionCommand](docs/CompleterPropositionCommand.md)
 - [Conference](docs/Conference.md)
 - [ConferenceCommunication](docs/ConferenceCommunication.md)
 - [ConferencePublication](docs/ConferencePublication.md)
 - [ConfirmationPaperCanvas](docs/ConfirmationPaperCanvas.md)
 - [ConfirmationPaperDTO](docs/ConfirmationPaperDTO.md)
 - [ConfirmationPaperDTODemandeProlongation](docs/ConfirmationPaperDTODemandeProlongation.md)
 - [ContexteFormation](docs/ContexteFormation.md)
 - [ContinuingEducationCompleterCurriculumCommand](docs/ContinuingEducationCompleterCurriculumCommand.md)
 - [ContinuingEducationPropositionDTO](docs/ContinuingEducationPropositionDTO.md)
 - [Coordonnees](docs/Coordonnees.md)
 - [CoordonneesContact](docs/CoordonneesContact.md)
 - [CotutelleDTO](docs/CotutelleDTO.md)
 - [Course](docs/Course.md)
 - [CurriculumDetails](docs/CurriculumDetails.md)
 - [CurriculumDetailsEducationalExperiences](docs/CurriculumDetailsEducationalExperiences.md)
 - [CurriculumDetailsEducationalexperienceyearSet](docs/CurriculumDetailsEducationalexperienceyearSet.md)
 - [CurriculumDetailsProfessionalExperiences](docs/CurriculumDetailsProfessionalExperiences.md)
 - [Dashboard](docs/Dashboard.md)
 - [DashboardLinks](docs/DashboardLinks.md)
 - [DefinirCotutelleCommand](docs/DefinirCotutelleCommand.md)
 - [DesignerPromoteurReferenceCommand](docs/DesignerPromoteurReferenceCommand.md)
 - [DiplomaResults](docs/DiplomaResults.md)
 - [DoctoralTrainingActivity](docs/DoctoralTrainingActivity.md)
 - [DoctoralTrainingAssent](docs/DoctoralTrainingAssent.md)
 - [DoctoralTrainingBatch](docs/DoctoralTrainingBatch.md)
 - [DoctoralTrainingConfig](docs/DoctoralTrainingConfig.md)
 - [DoctoratCompleterCurriculumCommand](docs/DoctoratCompleterCurriculumCommand.md)
 - [DoctoratDTO](docs/DoctoratDTO.md)
 - [DoctorateDTO](docs/DoctorateDTO.md)
 - [DoctorateDTOLinks](docs/DoctorateDTOLinks.md)
 - [DoctorateIdentityDTO](docs/DoctorateIdentityDTO.md)
 - [DoctoratePropositionDTO](docs/DoctoratePropositionDTO.md)
 - [DoctoratePropositionDTOBourseRecherche](docs/DoctoratePropositionDTOBourseRecherche.md)
 - [DoctoratePropositionDTOComptabilite](docs/DoctoratePropositionDTOComptabilite.md)
 - [DoctoratePropositionDTOLinks](docs/DoctoratePropositionDTOLinks.md)
 - [DoctoratePropositionSearchDTO](docs/DoctoratePropositionSearchDTO.md)
 - [EducationalExperience](docs/EducationalExperience.md)
 - [EducationalExperienceEducationalexperienceyearSet](docs/EducationalExperienceEducationalexperienceyearSet.md)
 - [EducationalType](docs/EducationalType.md)
 - [Equivalence](docs/Equivalence.md)
 - [Error](docs/Error.md)
 - [EvaluationSystem](docs/EvaluationSystem.md)
 - [ForeignDiplomaTypes](docs/ForeignDiplomaTypes.md)
 - [FormationContinueDTO](docs/FormationContinueDTO.md)
 - [FormationGeneraleDTO](docs/FormationGeneraleDTO.md)
 - [GeneralEducationCompleterCurriculumCommand](docs/GeneralEducationCompleterCurriculumCommand.md)
 - [GeneralEducationPropositionDTO](docs/GeneralEducationPropositionDTO.md)
 - [GeneralEducationPropositionDTOLinks](docs/GeneralEducationPropositionDTOLinks.md)
 - [Grade](docs/Grade.md)
 - [HighSchoolDiploma](docs/HighSchoolDiploma.md)
 - [HighSchoolDiplomaBelgianDiploma](docs/HighSchoolDiplomaBelgianDiploma.md)
 - [HighSchoolDiplomaBelgianDiplomaSchedule](docs/HighSchoolDiplomaBelgianDiplomaSchedule.md)
 - [HighSchoolDiplomaForeignDiploma](docs/HighSchoolDiplomaForeignDiploma.md)
 - [HighSchoolDiplomaHighSchoolDiplomaAlternative](docs/HighSchoolDiplomaHighSchoolDiplomaAlternative.md)
 - [InitierPropositionCommand](docs/InitierPropositionCommand.md)
 - [InitierPropositionContinueCommand](docs/InitierPropositionContinueCommand.md)
 - [InitierPropositionGeneraleCommand](docs/InitierPropositionGeneraleCommand.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [LanguageKnowledge](docs/LanguageKnowledge.md)
 - [LanguageKnowledgeGrade](docs/LanguageKnowledgeGrade.md)
 - [ModifierChoixFormationContinueCommand](docs/ModifierChoixFormationContinueCommand.md)
 - [ModifierChoixFormationGeneraleCommand](docs/ModifierChoixFormationGeneraleCommand.md)
 - [ModifierQuestionsSpecifiquesCommand](docs/ModifierQuestionsSpecifiquesCommand.md)
 - [ModifierTypeAdmissionDoctoraleCommand](docs/ModifierTypeAdmissionDoctoraleCommand.md)
 - [Paper](docs/Paper.md)
 - [Person](docs/Person.md)
 - [PersonIdentification](docs/PersonIdentification.md)
 - [PoolQuestions](docs/PoolQuestions.md)
 - [ProfessionalExperience](docs/ProfessionalExperience.md)
 - [PropositionErrors](docs/PropositionErrors.md)
 - [PropositionErrorsErrors](docs/PropositionErrorsErrors.md)
 - [PropositionIdentityDTO](docs/PropositionIdentityDTO.md)
 - [PropositionSearch](docs/PropositionSearch.md)
 - [PropositionSearchDoctorat](docs/PropositionSearchDoctorat.md)
 - [PropositionSearchDoctoratePropositions](docs/PropositionSearchDoctoratePropositions.md)
 - [PropositionSearchFormation](docs/PropositionSearchFormation.md)
 - [PropositionSearchGeneralEducationPropositions](docs/PropositionSearchGeneralEducationPropositions.md)
 - [PropositionSearchLinks](docs/PropositionSearchLinks.md)
 - [PropositionSearchLinks1](docs/PropositionSearchLinks1.md)
 - [PropositionSearchLinks2](docs/PropositionSearchLinks2.md)
 - [Publication](docs/Publication.md)
 - [RefuserPropositionCommand](docs/RefuserPropositionCommand.md)
 - [Residency](docs/Residency.md)
 - [ResidencyCommunication](docs/ResidencyCommunication.md)
 - [Result](docs/Result.md)
 - [Scholarship](docs/Scholarship.md)
 - [SectorDTO](docs/SectorDTO.md)
 - [Seminar](docs/Seminar.md)
 - [SeminarCommunication](docs/SeminarCommunication.md)
 - [Service](docs/Service.md)
 - [SpecificQuestion](docs/SpecificQuestion.md)
 - [StatutActivite](docs/StatutActivite.md)
 - [SubmitConfirmationPaperCommand](docs/SubmitConfirmationPaperCommand.md)
 - [SubmitConfirmationPaperExtensionRequestCommand](docs/SubmitConfirmationPaperExtensionRequestCommand.md)
 - [SubmitProposition](docs/SubmitProposition.md)
 - [SupervisionActor](docs/SupervisionActor.md)
 - [SupervisionDTO](docs/SupervisionDTO.md)
 - [SupervisionDTOPromoteur](docs/SupervisionDTOPromoteur.md)
 - [SupervisionDTOSignaturesMembresCA](docs/SupervisionDTOSignaturesMembresCA.md)
 - [SupervisionDTOSignaturesPromoteurs](docs/SupervisionDTOSignaturesPromoteurs.md)
 - [TeachingTypeEnum](docs/TeachingTypeEnum.md)
 - [TranscriptType](docs/TranscriptType.md)
 - [Tutor](docs/Tutor.md)
 - [UclCourse](docs/UclCourse.md)
 - [Valorisation](docs/Valorisation.md)


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

