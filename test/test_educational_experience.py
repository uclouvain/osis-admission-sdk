"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.38
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.educational_experience_educationalexperienceyear_set import EducationalExperienceEducationalexperienceyearSet
from osis_admission_sdk.model.evaluation_system import EvaluationSystem
from osis_admission_sdk.model.grade import Grade
from osis_admission_sdk.model.teaching_type_enum import TeachingTypeEnum
from osis_admission_sdk.model.transcript_type import TranscriptType
globals()['EducationalExperienceEducationalexperienceyearSet'] = EducationalExperienceEducationalexperienceyearSet
globals()['EvaluationSystem'] = EvaluationSystem
globals()['Grade'] = Grade
globals()['TeachingTypeEnum'] = TeachingTypeEnum
globals()['TranscriptType'] = TranscriptType
from osis_admission_sdk.model.educational_experience import EducationalExperience


class TestEducationalExperience(unittest.TestCase):
    """EducationalExperience unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEducationalExperience(self):
        """Test EducationalExperience"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EducationalExperience()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
