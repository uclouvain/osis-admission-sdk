"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.activity_type import ActivityType
from osis_admission_sdk.model.belgian_communities_of_education import BelgianCommunitiesOfEducation
from osis_admission_sdk.model.credit_type import CreditType
from osis_admission_sdk.model.experience_output_curriculum_year import ExperienceOutputCurriculumYear
from osis_admission_sdk.model.experience_type import ExperienceType
from osis_admission_sdk.model.foreign_study_cycle_type import ForeignStudyCycleType
from osis_admission_sdk.model.grade import Grade
from osis_admission_sdk.model.result import Result
from osis_admission_sdk.model.study_system import StudySystem
globals()['ActivityType'] = ActivityType
globals()['BelgianCommunitiesOfEducation'] = BelgianCommunitiesOfEducation
globals()['CreditType'] = CreditType
globals()['ExperienceOutputCurriculumYear'] = ExperienceOutputCurriculumYear
globals()['ExperienceType'] = ExperienceType
globals()['ForeignStudyCycleType'] = ForeignStudyCycleType
globals()['Grade'] = Grade
globals()['Result'] = Result
globals()['StudySystem'] = StudySystem
from osis_admission_sdk.model.experience_output import ExperienceOutput


class TestExperienceOutput(unittest.TestCase):
    """ExperienceOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExperienceOutput(self):
        """Test ExperienceOutput"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ExperienceOutput()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
