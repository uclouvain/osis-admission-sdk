"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.29
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_admission_sdk
from osis_admission_sdk.api.propositions_api import PropositionsApi  # noqa: E501


class TestPropositionsApi(unittest.TestCase):
    """PropositionsApi unit test stubs"""

    def setUp(self):
        self.api = PropositionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_member(self):
        """Test case for add_member

        """
        pass

    def test_approve_by_pdf(self):
        """Test case for approve_by_pdf

        """
        pass

    def test_approve_proposition(self):
        """Test case for approve_proposition

        """
        pass

    def test_complete_confirmation_paper_by_promoter(self):
        """Test case for complete_confirmation_paper_by_promoter

        """
        pass

    def test_create_doctoral_training(self):
        """Test case for create_doctoral_training

        """
        pass

    def test_create_proposition(self):
        """Test case for create_proposition

        """
        pass

    def test_create_signatures(self):
        """Test case for create_signatures

        """
        pass

    def test_destroy_proposition(self):
        """Test case for destroy_proposition

        """
        pass

    def test_list_doctoral_trainings(self):
        """Test case for list_doctoral_trainings

        """
        pass

    def test_list_propositions(self):
        """Test case for list_propositions

        """
        pass

    def test_list_supervised_propositions(self):
        """Test case for list_supervised_propositions

        """
        pass

    def test_reject_proposition(self):
        """Test case for reject_proposition

        """
        pass

    def test_remove_member(self):
        """Test case for remove_member

        """
        pass

    def test_retrieve_confirmation_papers(self):
        """Test case for retrieve_confirmation_papers

        """
        pass

    def test_retrieve_cotutelle(self):
        """Test case for retrieve_cotutelle

        """
        pass

    def test_retrieve_dashboard(self):
        """Test case for retrieve_dashboard

        """
        pass

    def test_retrieve_doctoral_training(self):
        """Test case for retrieve_doctoral_training

        """
        pass

    def test_retrieve_doctoral_training_config(self):
        """Test case for retrieve_doctoral_training_config

        """
        pass

    def test_retrieve_doctorate_dto(self):
        """Test case for retrieve_doctorate_dto

        """
        pass

    def test_retrieve_last_confirmation_paper(self):
        """Test case for retrieve_last_confirmation_paper

        """
        pass

    def test_retrieve_last_confirmation_paper_canvas(self):
        """Test case for retrieve_last_confirmation_paper_canvas

        """
        pass

    def test_retrieve_proposition(self):
        """Test case for retrieve_proposition

        """
        pass

    def test_retrieve_supervision(self):
        """Test case for retrieve_supervision

        """
        pass

    def test_retrieve_verify_project(self):
        """Test case for retrieve_verify_project

        """
        pass

    def test_submit_confirmation_paper(self):
        """Test case for submit_confirmation_paper

        """
        pass

    def test_submit_confirmation_paper_extension_request(self):
        """Test case for submit_confirmation_paper_extension_request

        """
        pass

    def test_submit_doctoral_training(self):
        """Test case for submit_doctoral_training

        """
        pass

    def test_submit_proposition(self):
        """Test case for submit_proposition

        """
        pass

    def test_update_cotutelle(self):
        """Test case for update_cotutelle

        """
        pass

    def test_update_doctoral_training(self):
        """Test case for update_doctoral_training

        """
        pass

    def test_update_proposition(self):
        """Test case for update_proposition

        """
        pass

    def test_verify_proposition(self):
        """Test case for verify_proposition

        """
        pass


if __name__ == '__main__':
    unittest.main()
