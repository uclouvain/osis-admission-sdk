"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.71
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_admission_sdk
from osis_admission_sdk.api.campus_api import CampusApi  # noqa: E501


class TestCampusApi(unittest.TestCase):
    """CampusApi unit test stubs"""

    def setUp(self):
        self.api = CampusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_campus(self):
        """Test case for list_campus

        """
        pass

    def test_retrieve_campus(self):
        """Test case for retrieve_campus

        """
        pass


if __name__ == '__main__':
    unittest.main()
