"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.61
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_admission_sdk
from osis_admission_sdk.api.scholarship_api import ScholarshipApi  # noqa: E501


class TestScholarshipApi(unittest.TestCase):
    """ScholarshipApi unit test stubs"""

    def setUp(self):
        self.api = ScholarshipApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_scholarship(self):
        """Test case for retrieve_scholarship

        """
        pass


if __name__ == '__main__':
    unittest.main()
