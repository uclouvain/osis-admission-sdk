"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.76
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.categorie_activite import CategorieActivite
from osis_admission_sdk.model.contexte_formation import ContexteFormation
from osis_admission_sdk.model.seminar_communication import SeminarCommunication
from osis_admission_sdk.model.statut_activite import StatutActivite
globals()['CategorieActivite'] = CategorieActivite
globals()['ContexteFormation'] = ContexteFormation
globals()['SeminarCommunication'] = SeminarCommunication
globals()['StatutActivite'] = StatutActivite
from osis_admission_sdk.model.seminar import Seminar


class TestSeminar(unittest.TestCase):
    """Seminar unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSeminar(self):
        """Test Seminar"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Seminar()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
