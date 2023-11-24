
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.autocomplete_api import AutocompleteApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from osis_admission_sdk.api.autocomplete_api import AutocompleteApi
from osis_admission_sdk.api.campus_api import CampusApi
from osis_admission_sdk.api.diplomatic_post_api import DiplomaticPostApi
from osis_admission_sdk.api.person_api import PersonApi
from osis_admission_sdk.api.propositions_api import PropositionsApi
from osis_admission_sdk.api.scholarship_api import ScholarshipApi
