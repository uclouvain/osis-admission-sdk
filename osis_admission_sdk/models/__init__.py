# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_admission_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_admission_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_admission_sdk.model.action_link import ActionLink
from osis_admission_sdk.model.activity_type import ActivityType
from osis_admission_sdk.model.actor_type import ActorType
from osis_admission_sdk.model.admission_type import AdmissionType
from osis_admission_sdk.model.approuver_proposition_command import ApprouverPropositionCommand
from osis_admission_sdk.model.approuver_proposition_par_pdf_command import ApprouverPropositionParPdfCommand
from osis_admission_sdk.model.belgian_communities_of_education import BelgianCommunitiesOfEducation
from osis_admission_sdk.model.choix_commission_proximite import ChoixCommissionProximite
from osis_admission_sdk.model.choix_doctorat_deja_realise import ChoixDoctoratDejaRealise
from osis_admission_sdk.model.choix_genre import ChoixGenre
from osis_admission_sdk.model.choix_langue_redaction_these import ChoixLangueRedactionThese
from osis_admission_sdk.model.civil_state import CivilState
from osis_admission_sdk.model.complete_confirmation_paper_by_promoter_command import CompleteConfirmationPaperByPromoterCommand
from osis_admission_sdk.model.completer_proposition_command import CompleterPropositionCommand
from osis_admission_sdk.model.confirmation_paper_canvas import ConfirmationPaperCanvas
from osis_admission_sdk.model.confirmation_paper_dto import ConfirmationPaperDTO
from osis_admission_sdk.model.confirmation_paper_dto_demande_prolongation import ConfirmationPaperDTODemandeProlongation
from osis_admission_sdk.model.coordonnees import Coordonnees
from osis_admission_sdk.model.coordonnees_contact import CoordonneesContact
from osis_admission_sdk.model.cotutelle_dto import CotutelleDTO
from osis_admission_sdk.model.credit_type import CreditType
from osis_admission_sdk.model.curriculum_file import CurriculumFile
from osis_admission_sdk.model.dashboard import Dashboard
from osis_admission_sdk.model.dashboard_links import DashboardLinks
from osis_admission_sdk.model.definir_cotutelle_command import DefinirCotutelleCommand
from osis_admission_sdk.model.diploma_results import DiplomaResults
from osis_admission_sdk.model.doctorat_dto import DoctoratDTO
from osis_admission_sdk.model.doctorate_dto import DoctorateDTO
from osis_admission_sdk.model.doctorate_dto_links import DoctorateDTOLinks
from osis_admission_sdk.model.doctorate_identity_dto import DoctorateIdentityDTO
from osis_admission_sdk.model.educational_type import EducationalType
from osis_admission_sdk.model.equivalence import Equivalence
from osis_admission_sdk.model.error import Error
from osis_admission_sdk.model.experience_input import ExperienceInput
from osis_admission_sdk.model.experience_output import ExperienceOutput
from osis_admission_sdk.model.experience_output_curriculum_year import ExperienceOutputCurriculumYear
from osis_admission_sdk.model.experience_type import ExperienceType
from osis_admission_sdk.model.foreign_diploma_types import ForeignDiplomaTypes
from osis_admission_sdk.model.foreign_study_cycle_type import ForeignStudyCycleType
from osis_admission_sdk.model.grade import Grade
from osis_admission_sdk.model.high_school_diploma import HighSchoolDiploma
from osis_admission_sdk.model.high_school_diploma_belgian_diploma import HighSchoolDiplomaBelgianDiploma
from osis_admission_sdk.model.high_school_diploma_belgian_diploma_schedule import HighSchoolDiplomaBelgianDiplomaSchedule
from osis_admission_sdk.model.high_school_diploma_foreign_diploma import HighSchoolDiplomaForeignDiploma
from osis_admission_sdk.model.high_school_diploma_high_school_diploma_alternative import HighSchoolDiplomaHighSchoolDiplomaAlternative
from osis_admission_sdk.model.initier_proposition_command import InitierPropositionCommand
from osis_admission_sdk.model.inline_response200 import InlineResponse200
from osis_admission_sdk.model.inline_response2001 import InlineResponse2001
from osis_admission_sdk.model.inline_response2002 import InlineResponse2002
from osis_admission_sdk.model.language_knowledge import LanguageKnowledge
from osis_admission_sdk.model.language_knowledge_grade import LanguageKnowledgeGrade
from osis_admission_sdk.model.person import Person
from osis_admission_sdk.model.person_identification import PersonIdentification
from osis_admission_sdk.model.proposition_dto import PropositionDTO
from osis_admission_sdk.model.proposition_dto_links import PropositionDTOLinks
from osis_admission_sdk.model.proposition_identity_dto import PropositionIdentityDTO
from osis_admission_sdk.model.proposition_search import PropositionSearch
from osis_admission_sdk.model.proposition_search_dto import PropositionSearchDTO
from osis_admission_sdk.model.proposition_search_links import PropositionSearchLinks
from osis_admission_sdk.model.proposition_search_links1 import PropositionSearchLinks1
from osis_admission_sdk.model.proposition_search_propositions import PropositionSearchPropositions
from osis_admission_sdk.model.refuser_proposition_command import RefuserPropositionCommand
from osis_admission_sdk.model.result import Result
from osis_admission_sdk.model.sector_dto import SectorDTO
from osis_admission_sdk.model.study_system import StudySystem
from osis_admission_sdk.model.submit_confirmation_paper_command import SubmitConfirmationPaperCommand
from osis_admission_sdk.model.submit_confirmation_paper_extension_request_command import SubmitConfirmationPaperExtensionRequestCommand
from osis_admission_sdk.model.supervision_actor import SupervisionActor
from osis_admission_sdk.model.supervision_dto import SupervisionDTO
from osis_admission_sdk.model.supervision_dto_promoteur import SupervisionDTOPromoteur
from osis_admission_sdk.model.supervision_dto_signatures_membres_ca import SupervisionDTOSignaturesMembresCA
from osis_admission_sdk.model.supervision_dto_signatures_promoteurs import SupervisionDTOSignaturesPromoteurs
from osis_admission_sdk.model.tutor import Tutor
