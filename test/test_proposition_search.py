"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.21
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.proposition_search_links import PropositionSearchLinks
from osis_admission_sdk.model.proposition_search_propositions import PropositionSearchPropositions
globals()['PropositionSearchLinks'] = PropositionSearchLinks
globals()['PropositionSearchPropositions'] = PropositionSearchPropositions
from osis_admission_sdk.model.proposition_search import PropositionSearch


class TestPropositionSearch(unittest.TestCase):
    """PropositionSearch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPropositionSearch(self):
        """Test PropositionSearch"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PropositionSearch()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
