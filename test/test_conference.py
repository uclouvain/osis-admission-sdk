"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.41
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.categorie_activite import CategorieActivite
from osis_admission_sdk.model.conference_communication import ConferenceCommunication
from osis_admission_sdk.model.conference_publication import ConferencePublication
from osis_admission_sdk.model.contexte_formation import ContexteFormation
from osis_admission_sdk.model.statut_activite import StatutActivite
globals()['CategorieActivite'] = CategorieActivite
globals()['ConferenceCommunication'] = ConferenceCommunication
globals()['ConferencePublication'] = ConferencePublication
globals()['ContexteFormation'] = ContexteFormation
globals()['StatutActivite'] = StatutActivite
from osis_admission_sdk.model.conference import Conference


class TestConference(unittest.TestCase):
    """Conference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConference(self):
        """Test Conference"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Conference()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
