"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.27
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.categorie_activite import CategorieActivite
from osis_admission_sdk.model.statut_activite import StatutActivite
globals()['CategorieActivite'] = CategorieActivite
globals()['StatutActivite'] = StatutActivite
from osis_admission_sdk.model.publication import Publication


class TestPublication(unittest.TestCase):
    """Publication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPublication(self):
        """Test Publication"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Publication()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()