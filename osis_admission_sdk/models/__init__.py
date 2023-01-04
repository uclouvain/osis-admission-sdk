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
from osis_admission_sdk.model.activity_sector import ActivitySector
from osis_admission_sdk.model.activity_type import ActivityType
from osis_admission_sdk.model.actor_type import ActorType
from osis_admission_sdk.model.admission_type import AdmissionType
from osis_admission_sdk.model.approuver_proposition_command import ApprouverPropositionCommand
from osis_admission_sdk.model.approuver_proposition_par_pdf_command import ApprouverPropositionParPdfCommand
from osis_admission_sdk.model.belgian_communities_of_education import BelgianCommunitiesOfEducation
from osis_admission_sdk.model.campus import Campus
from osis_admission_sdk.model.categorie_activite import CategorieActivite
from osis_admission_sdk.model.choix_commission_proximite import ChoixCommissionProximite
from osis_admission_sdk.model.choix_doctorat_deja_realise import ChoixDoctoratDejaRealise
from osis_admission_sdk.model.choix_genre import ChoixGenre
from osis_admission_sdk.model.choix_langue_redaction_these import ChoixLangueRedactionThese
from osis_admission_sdk.model.civil_state import CivilState
from osis_admission_sdk.model.communication import Communication
from osis_admission_sdk.model.complete_confirmation_paper_by_promoter_command import CompleteConfirmationPaperByPromoterCommand
from osis_admission_sdk.model.completer_comptabilite_proposition_continue_command import CompleterComptabilitePropositionContinueCommand
from osis_admission_sdk.model.completer_comptabilite_proposition_doctorale_command import CompleterComptabilitePropositionDoctoraleCommand
from osis_admission_sdk.model.completer_comptabilite_proposition_generale_command import CompleterComptabilitePropositionGeneraleCommand
from osis_admission_sdk.model.completer_proposition_command import CompleterPropositionCommand
from osis_admission_sdk.model.conference import Conference
from osis_admission_sdk.model.conference_communication import ConferenceCommunication
from osis_admission_sdk.model.conference_publication import ConferencePublication
from osis_admission_sdk.model.confirmation_paper_canvas import ConfirmationPaperCanvas
from osis_admission_sdk.model.confirmation_paper_dto import ConfirmationPaperDTO
from osis_admission_sdk.model.confirmation_paper_dto_demande_prolongation import ConfirmationPaperDTODemandeProlongation
from osis_admission_sdk.model.contexte_formation import ContexteFormation
from osis_admission_sdk.model.continuing_education_accounting_dto import ContinuingEducationAccountingDTO
from osis_admission_sdk.model.continuing_education_completer_curriculum_command import ContinuingEducationCompleterCurriculumCommand
from osis_admission_sdk.model.continuing_education_proposition_dto import ContinuingEducationPropositionDTO
from osis_admission_sdk.model.coordonnees import Coordonnees
from osis_admission_sdk.model.coordonnees_contact import CoordonneesContact
from osis_admission_sdk.model.cotutelle_dto import CotutelleDTO
from osis_admission_sdk.model.course import Course
from osis_admission_sdk.model.curriculum_details import CurriculumDetails
from osis_admission_sdk.model.curriculum_details_educational_experiences import CurriculumDetailsEducationalExperiences
from osis_admission_sdk.model.curriculum_details_educationalexperienceyear_set import CurriculumDetailsEducationalexperienceyearSet
from osis_admission_sdk.model.curriculum_details_professional_experiences import CurriculumDetailsProfessionalExperiences
from osis_admission_sdk.model.dashboard import Dashboard
from osis_admission_sdk.model.dashboard_links import DashboardLinks
from osis_admission_sdk.model.definir_cotutelle_command import DefinirCotutelleCommand
from osis_admission_sdk.model.designer_promoteur_reference_command import DesignerPromoteurReferenceCommand
from osis_admission_sdk.model.diploma_results import DiplomaResults
from osis_admission_sdk.model.doctoral_training_activity import DoctoralTrainingActivity
from osis_admission_sdk.model.doctoral_training_assent import DoctoralTrainingAssent
from osis_admission_sdk.model.doctoral_training_batch import DoctoralTrainingBatch
from osis_admission_sdk.model.doctoral_training_config import DoctoralTrainingConfig
from osis_admission_sdk.model.doctorat_completer_curriculum_command import DoctoratCompleterCurriculumCommand
from osis_admission_sdk.model.doctorat_dto import DoctoratDTO
from osis_admission_sdk.model.doctorate_dto import DoctorateDTO
from osis_admission_sdk.model.doctorate_dto_links import DoctorateDTOLinks
from osis_admission_sdk.model.doctorate_education_accounting_dto import DoctorateEducationAccountingDTO
from osis_admission_sdk.model.doctorate_education_accounting_dto_derniers_etablissements_superieurs_communaute_fr_frequentes import DoctorateEducationAccountingDTODerniersEtablissementsSuperieursCommunauteFrFrequentes
from osis_admission_sdk.model.doctorate_identity_dto import DoctorateIdentityDTO
from osis_admission_sdk.model.doctorate_proposition_dto import DoctoratePropositionDTO
from osis_admission_sdk.model.doctorate_proposition_dto_bourse_recherche import DoctoratePropositionDTOBourseRecherche
from osis_admission_sdk.model.doctorate_proposition_dto_links import DoctoratePropositionDTOLinks
from osis_admission_sdk.model.doctorate_proposition_search_dto import DoctoratePropositionSearchDTO
from osis_admission_sdk.model.educational_experience import EducationalExperience
from osis_admission_sdk.model.educational_experience_educationalexperienceyear_set import EducationalExperienceEducationalexperienceyearSet
from osis_admission_sdk.model.educational_type import EducationalType
from osis_admission_sdk.model.equivalence import Equivalence
from osis_admission_sdk.model.error import Error
from osis_admission_sdk.model.evaluation_system import EvaluationSystem
from osis_admission_sdk.model.foreign_diploma_types import ForeignDiplomaTypes
from osis_admission_sdk.model.formation_continue_dto import FormationContinueDTO
from osis_admission_sdk.model.formation_generale_dto import FormationGeneraleDTO
from osis_admission_sdk.model.general_education_accounting_dto import GeneralEducationAccountingDTO
from osis_admission_sdk.model.general_education_completer_curriculum_command import GeneralEducationCompleterCurriculumCommand
from osis_admission_sdk.model.general_education_proposition_dto import GeneralEducationPropositionDTO
from osis_admission_sdk.model.general_education_proposition_dto_links import GeneralEducationPropositionDTOLinks
from osis_admission_sdk.model.grade import Grade
from osis_admission_sdk.model.high_school_diploma import HighSchoolDiploma
from osis_admission_sdk.model.high_school_diploma_belgian_diploma import HighSchoolDiplomaBelgianDiploma
from osis_admission_sdk.model.high_school_diploma_belgian_diploma_schedule import HighSchoolDiplomaBelgianDiplomaSchedule
from osis_admission_sdk.model.high_school_diploma_foreign_diploma import HighSchoolDiplomaForeignDiploma
from osis_admission_sdk.model.high_school_diploma_high_school_diploma_alternative import HighSchoolDiplomaHighSchoolDiplomaAlternative
from osis_admission_sdk.model.initier_proposition_command import InitierPropositionCommand
from osis_admission_sdk.model.initier_proposition_continue_command import InitierPropositionContinueCommand
from osis_admission_sdk.model.initier_proposition_generale_command import InitierPropositionGeneraleCommand
from osis_admission_sdk.model.inline_response200 import InlineResponse200
from osis_admission_sdk.model.inline_response2001 import InlineResponse2001
from osis_admission_sdk.model.inline_response2002 import InlineResponse2002
from osis_admission_sdk.model.inline_response2003 import InlineResponse2003
from osis_admission_sdk.model.language_knowledge import LanguageKnowledge
from osis_admission_sdk.model.language_knowledge_grade import LanguageKnowledgeGrade
from osis_admission_sdk.model.modifier_choix_formation_continue_command import ModifierChoixFormationContinueCommand
from osis_admission_sdk.model.modifier_choix_formation_generale_command import ModifierChoixFormationGeneraleCommand
from osis_admission_sdk.model.modifier_questions_specifiques_command import ModifierQuestionsSpecifiquesCommand
from osis_admission_sdk.model.modifier_type_admission_doctorale_command import ModifierTypeAdmissionDoctoraleCommand
from osis_admission_sdk.model.paper import Paper
from osis_admission_sdk.model.person import Person
from osis_admission_sdk.model.person_identification import PersonIdentification
from osis_admission_sdk.model.pool_questions import PoolQuestions
from osis_admission_sdk.model.professional_experience import ProfessionalExperience
from osis_admission_sdk.model.proposition_errors import PropositionErrors
from osis_admission_sdk.model.proposition_errors_elements_confirmation import PropositionErrorsElementsConfirmation
from osis_admission_sdk.model.proposition_errors_errors import PropositionErrorsErrors
from osis_admission_sdk.model.proposition_identity_dto import PropositionIdentityDTO
from osis_admission_sdk.model.proposition_search import PropositionSearch
from osis_admission_sdk.model.proposition_search_doctorat import PropositionSearchDoctorat
from osis_admission_sdk.model.proposition_search_doctorate_propositions import PropositionSearchDoctoratePropositions
from osis_admission_sdk.model.proposition_search_formation import PropositionSearchFormation
from osis_admission_sdk.model.proposition_search_general_education_propositions import PropositionSearchGeneralEducationPropositions
from osis_admission_sdk.model.proposition_search_links import PropositionSearchLinks
from osis_admission_sdk.model.proposition_search_links1 import PropositionSearchLinks1
from osis_admission_sdk.model.proposition_search_links2 import PropositionSearchLinks2
from osis_admission_sdk.model.publication import Publication
from osis_admission_sdk.model.refuser_proposition_command import RefuserPropositionCommand
from osis_admission_sdk.model.residency import Residency
from osis_admission_sdk.model.residency_communication import ResidencyCommunication
from osis_admission_sdk.model.result import Result
from osis_admission_sdk.model.scholarship import Scholarship
from osis_admission_sdk.model.sector_dto import SectorDTO
from osis_admission_sdk.model.seminar import Seminar
from osis_admission_sdk.model.seminar_communication import SeminarCommunication
from osis_admission_sdk.model.service import Service
from osis_admission_sdk.model.specific_question import SpecificQuestion
from osis_admission_sdk.model.statut_activite import StatutActivite
from osis_admission_sdk.model.submit_confirmation_paper_command import SubmitConfirmationPaperCommand
from osis_admission_sdk.model.submit_confirmation_paper_extension_request_command import SubmitConfirmationPaperExtensionRequestCommand
from osis_admission_sdk.model.submit_proposition import SubmitProposition
from osis_admission_sdk.model.supervision_actor import SupervisionActor
from osis_admission_sdk.model.supervision_dto import SupervisionDTO
from osis_admission_sdk.model.supervision_dto_promoteur import SupervisionDTOPromoteur
from osis_admission_sdk.model.supervision_dto_signatures_membres_ca import SupervisionDTOSignaturesMembresCA
from osis_admission_sdk.model.supervision_dto_signatures_promoteurs import SupervisionDTOSignaturesPromoteurs
from osis_admission_sdk.model.teaching_type_enum import TeachingTypeEnum
from osis_admission_sdk.model.transcript_type import TranscriptType
from osis_admission_sdk.model.tutor import Tutor
from osis_admission_sdk.model.ucl_course import UclCourse
from osis_admission_sdk.model.valorisation import Valorisation
