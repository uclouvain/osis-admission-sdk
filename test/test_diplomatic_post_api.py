"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.88
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_admission_sdk
from osis_admission_sdk.api.diplomatic_post_api import DiplomaticPostApi  # noqa: E501


class TestDiplomaticPostApi(unittest.TestCase):
    """DiplomaticPostApi unit test stubs"""

    def setUp(self):
        self.api = DiplomaticPostApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_diplomatic_post(self):
        """Test case for retrieve_diplomatic_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
