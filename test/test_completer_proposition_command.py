"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.73
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.choix_commission_proximite import ChoixCommissionProximite
from osis_admission_sdk.model.choix_doctorat_deja_realise import ChoixDoctoratDejaRealise
from osis_admission_sdk.model.choix_langue_redaction_these import ChoixLangueRedactionThese
from osis_admission_sdk.model.choix_type_admission import ChoixTypeAdmission
globals()['ChoixCommissionProximite'] = ChoixCommissionProximite
globals()['ChoixDoctoratDejaRealise'] = ChoixDoctoratDejaRealise
globals()['ChoixLangueRedactionThese'] = ChoixLangueRedactionThese
globals()['ChoixTypeAdmission'] = ChoixTypeAdmission
from osis_admission_sdk.model.completer_proposition_command import CompleterPropositionCommand


class TestCompleterPropositionCommand(unittest.TestCase):
    """CompleterPropositionCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCompleterPropositionCommand(self):
        """Test CompleterPropositionCommand"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CompleterPropositionCommand()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
