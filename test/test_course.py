"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.52
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.categorie_activite import CategorieActivite
from osis_admission_sdk.model.contexte_formation import ContexteFormation
from osis_admission_sdk.model.statut_activite import StatutActivite
globals()['CategorieActivite'] = CategorieActivite
globals()['ContexteFormation'] = ContexteFormation
globals()['StatutActivite'] = StatutActivite
from osis_admission_sdk.model.course import Course


class TestCourse(unittest.TestCase):
    """Course unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCourse(self):
        """Test Course"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Course()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
