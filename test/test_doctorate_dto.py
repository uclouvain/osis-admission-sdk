"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.58
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.doctorate_dto_links import DoctorateDTOLinks
from osis_admission_sdk.model.doctorate_proposition_dto_bourse_recherche import DoctoratePropositionDTOBourseRecherche
globals()['DoctorateDTOLinks'] = DoctorateDTOLinks
globals()['DoctoratePropositionDTOBourseRecherche'] = DoctoratePropositionDTOBourseRecherche
from osis_admission_sdk.model.doctorate_dto import DoctorateDTO


class TestDoctorateDTO(unittest.TestCase):
    """DoctorateDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDoctorateDTO(self):
        """Test DoctorateDTO"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DoctorateDTO()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
