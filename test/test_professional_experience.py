"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.38
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.activity_sector import ActivitySector
from osis_admission_sdk.model.activity_type import ActivityType
globals()['ActivitySector'] = ActivitySector
globals()['ActivityType'] = ActivityType
from osis_admission_sdk.model.professional_experience import ProfessionalExperience


class TestProfessionalExperience(unittest.TestCase):
    """ProfessionalExperience unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProfessionalExperience(self):
        """Test ProfessionalExperience"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProfessionalExperience()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
