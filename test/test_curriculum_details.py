"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.88
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.curriculum_details_educational_experiences import CurriculumDetailsEducationalExperiences
from osis_admission_sdk.model.curriculum_details_professional_experiences import CurriculumDetailsProfessionalExperiences
globals()['CurriculumDetailsEducationalExperiences'] = CurriculumDetailsEducationalExperiences
globals()['CurriculumDetailsProfessionalExperiences'] = CurriculumDetailsProfessionalExperiences
from osis_admission_sdk.model.curriculum_details import CurriculumDetails


class TestCurriculumDetails(unittest.TestCase):
    """CurriculumDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCurriculumDetails(self):
        """Test CurriculumDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CurriculumDetails()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
