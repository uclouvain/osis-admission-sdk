"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_admission_sdk
from osis_admission_sdk.api.person_api import PersonApi  # noqa: E501


class TestPersonApi(unittest.TestCase):
    """PersonApi unit test stubs"""

    def setUp(self):
        self.api = PersonApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_coordonnees(self):
        """Test case for retrieve_coordonnees

        """
        pass

    def test_retrieve_high_school_diploma(self):
        """Test case for retrieve_high_school_diploma

        """
        pass

    def test_retrieve_person_identification(self):
        """Test case for retrieve_person_identification

        """
        pass

    def test_update_coordonnees(self):
        """Test case for update_coordonnees

        """
        pass

    def test_update_high_school_diploma(self):
        """Test case for update_high_school_diploma

        """
        pass

    def test_update_person_identification(self):
        """Test case for update_person_identification

        """
        pass


if __name__ == '__main__':
    unittest.main()
