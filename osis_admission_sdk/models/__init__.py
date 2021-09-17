# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_admission_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_admission_sdk.model.completer_proposition_command import CompleterPropositionCommand
from osis_admission_sdk.model.doctorat_dto import DoctoratDTO
from osis_admission_sdk.model.initier_proposition_command import InitierPropositionCommand
from osis_admission_sdk.model.proposition_dto import PropositionDTO
from osis_admission_sdk.model.proposition_identity_dto import PropositionIdentityDTO
from osis_admission_sdk.model.proposition_search_dto import PropositionSearchDTO
from osis_admission_sdk.model.sector_dto import SectorDTO
