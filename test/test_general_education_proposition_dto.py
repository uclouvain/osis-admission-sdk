"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.75
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.doctorate_proposition_dto_bourse_recherche import DoctoratePropositionDTOBourseRecherche
from osis_admission_sdk.model.general_education_proposition_dto_links import GeneralEducationPropositionDTOLinks
from osis_admission_sdk.model.inline_response200 import InlineResponse200
from osis_admission_sdk.model.proposition_search_formation import PropositionSearchFormation
globals()['DoctoratePropositionDTOBourseRecherche'] = DoctoratePropositionDTOBourseRecherche
globals()['GeneralEducationPropositionDTOLinks'] = GeneralEducationPropositionDTOLinks
globals()['InlineResponse200'] = InlineResponse200
globals()['PropositionSearchFormation'] = PropositionSearchFormation
from osis_admission_sdk.model.general_education_proposition_dto import GeneralEducationPropositionDTO


class TestGeneralEducationPropositionDTO(unittest.TestCase):
    """GeneralEducationPropositionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGeneralEducationPropositionDTO(self):
        """Test GeneralEducationPropositionDTO"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GeneralEducationPropositionDTO()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
