"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.3
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

    def test_create_language_knowledge(self):
        """Test case for create_language_knowledge

        """
        pass

    def test_list_language_knowledges(self):
        """Test case for list_language_knowledges

        """
        pass

    def test_retrieve_coordonnees(self):
        """Test case for retrieve_coordonnees

        """
        pass

    def test_retrieve_coordonnees_admission(self):
        """Test case for retrieve_coordonnees_admission

        """
        pass

    def test_retrieve_high_school_diploma(self):
        """Test case for retrieve_high_school_diploma

        """
        pass

    def test_retrieve_high_school_diploma_admission(self):
        """Test case for retrieve_high_school_diploma_admission

        """
        pass

    def test_retrieve_person_identification(self):
        """Test case for retrieve_person_identification

        """
        pass

    def test_retrieve_person_identification_admission(self):
        """Test case for retrieve_person_identification_admission

        """
        pass

    def test_update_coordonnees(self):
        """Test case for update_coordonnees

        """
        pass

    def test_update_coordonnees_admission(self):
        """Test case for update_coordonnees_admission

        """
        pass

    def test_update_high_school_diploma(self):
        """Test case for update_high_school_diploma

        """
        pass

    def test_update_high_school_diploma_admission(self):
        """Test case for update_high_school_diploma_admission

        """
        pass

    def test_update_person_identification(self):
        """Test case for update_person_identification

        """
        pass

    def test_update_person_identification_admission(self):
        """Test case for update_person_identification_admission

        """
        pass


if __name__ == '__main__':
    unittest.main()
