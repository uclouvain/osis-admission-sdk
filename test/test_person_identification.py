"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.83
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.choix_genre import ChoixGenre
from osis_admission_sdk.model.choix_sexe import ChoixSexe
from osis_admission_sdk.model.civil_state import CivilState
globals()['ChoixGenre'] = ChoixGenre
globals()['ChoixSexe'] = ChoixSexe
globals()['CivilState'] = CivilState
from osis_admission_sdk.model.person_identification import PersonIdentification


class TestPersonIdentification(unittest.TestCase):
    """PersonIdentification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPersonIdentification(self):
        """Test PersonIdentification"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PersonIdentification()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
