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
from osis_admission_sdk.model.actor_type import ActorType
from osis_admission_sdk.model.add_supervision_actor import AddSupervisionActor
from osis_admission_sdk.model.admission_type import AdmissionType
from osis_admission_sdk.model.choix_bureau_cde import ChoixBureauCDE
from osis_admission_sdk.model.choix_doctorat_deja_realise import ChoixDoctoratDejaRealise
from osis_admission_sdk.model.choix_langue_redaction_these import ChoixLangueRedactionThese
from osis_admission_sdk.model.completer_proposition_command import CompleterPropositionCommand
from osis_admission_sdk.model.cotutelle_dto import CotutelleDTO
from osis_admission_sdk.model.definir_cotutelle_command import DefinirCotutelleCommand
from osis_admission_sdk.model.doctorat_dto import DoctoratDTO
from osis_admission_sdk.model.error import Error
from osis_admission_sdk.model.initier_proposition_command import InitierPropositionCommand
from osis_admission_sdk.model.inline_response200 import InlineResponse200
from osis_admission_sdk.model.inline_response2001 import InlineResponse2001
from osis_admission_sdk.model.person import Person
from osis_admission_sdk.model.proposition_dto import PropositionDTO
from osis_admission_sdk.model.proposition_identity_dto import PropositionIdentityDTO
from osis_admission_sdk.model.proposition_search_dto import PropositionSearchDTO
from osis_admission_sdk.model.sector_dto import SectorDTO
from osis_admission_sdk.model.supervision_dto import SupervisionDTO
from osis_admission_sdk.model.supervision_dto_promoteur import SupervisionDTOPromoteur
from osis_admission_sdk.model.supervision_dto_signatures_membres_ca import SupervisionDTOSignaturesMembresCA
from osis_admission_sdk.model.supervision_dto_signatures_promoteurs import SupervisionDTOSignaturesPromoteurs
from osis_admission_sdk.model.tutor import Tutor
