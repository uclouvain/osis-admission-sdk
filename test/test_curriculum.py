"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.41
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.curriculum_educational_experiences import CurriculumEducationalExperiences
from osis_admission_sdk.model.curriculum_file import CurriculumFile
from osis_admission_sdk.model.curriculum_professional_experiences import CurriculumProfessionalExperiences
globals()['CurriculumEducationalExperiences'] = CurriculumEducationalExperiences
globals()['CurriculumFile'] = CurriculumFile
globals()['CurriculumProfessionalExperiences'] = CurriculumProfessionalExperiences
from osis_admission_sdk.model.curriculum import Curriculum


class TestCurriculum(unittest.TestCase):
    """Curriculum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCurriculum(self):
        """Test Curriculum"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Curriculum()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
