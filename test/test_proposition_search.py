"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.56
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.proposition_search_doctorate_propositions import PropositionSearchDoctoratePropositions
from osis_admission_sdk.model.proposition_search_general_education_propositions import PropositionSearchGeneralEducationPropositions
from osis_admission_sdk.model.proposition_search_links import PropositionSearchLinks
globals()['PropositionSearchDoctoratePropositions'] = PropositionSearchDoctoratePropositions
globals()['PropositionSearchGeneralEducationPropositions'] = PropositionSearchGeneralEducationPropositions
globals()['PropositionSearchLinks'] = PropositionSearchLinks
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
