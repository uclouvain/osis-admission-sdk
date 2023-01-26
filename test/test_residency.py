"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.62
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.categorie_activite import CategorieActivite
from osis_admission_sdk.model.contexte_formation import ContexteFormation
from osis_admission_sdk.model.residency_communication import ResidencyCommunication
from osis_admission_sdk.model.statut_activite import StatutActivite
globals()['CategorieActivite'] = CategorieActivite
globals()['ContexteFormation'] = ContexteFormation
globals()['ResidencyCommunication'] = ResidencyCommunication
globals()['StatutActivite'] = StatutActivite
from osis_admission_sdk.model.residency import Residency


class TestResidency(unittest.TestCase):
    """Residency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResidency(self):
        """Test Residency"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Residency()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
