"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.18
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.inline_response200 import InlineResponse200
from osis_admission_sdk.model.proposition_dto_links import PropositionDTOLinks
globals()['InlineResponse200'] = InlineResponse200
globals()['PropositionDTOLinks'] = PropositionDTOLinks
from osis_admission_sdk.model.proposition_dto import PropositionDTO


class TestPropositionDTO(unittest.TestCase):
    """PropositionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPropositionDTO(self):
        """Test PropositionDTO"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PropositionDTO()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
