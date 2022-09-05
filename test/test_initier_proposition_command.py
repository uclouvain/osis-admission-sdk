"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.35
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.admission_type import AdmissionType
from osis_admission_sdk.model.choix_commission_proximite import ChoixCommissionProximite
from osis_admission_sdk.model.choix_doctorat_deja_realise import ChoixDoctoratDejaRealise
from osis_admission_sdk.model.choix_langue_redaction_these import ChoixLangueRedactionThese
globals()['AdmissionType'] = AdmissionType
globals()['ChoixCommissionProximite'] = ChoixCommissionProximite
globals()['ChoixDoctoratDejaRealise'] = ChoixDoctoratDejaRealise
globals()['ChoixLangueRedactionThese'] = ChoixLangueRedactionThese
from osis_admission_sdk.model.initier_proposition_command import InitierPropositionCommand


class TestInitierPropositionCommand(unittest.TestCase):
    """InitierPropositionCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInitierPropositionCommand(self):
        """Test InitierPropositionCommand"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InitierPropositionCommand()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
