"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.81
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.jury_dto_membres import JuryDTOMembres
globals()['JuryDTOMembres'] = JuryDTOMembres
from osis_admission_sdk.model.jury_dto import JuryDTO


class TestJuryDTO(unittest.TestCase):
    """JuryDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJuryDTO(self):
        """Test JuryDTO"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JuryDTO()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
