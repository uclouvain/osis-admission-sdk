"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.26
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_admission_sdk
from osis_admission_sdk.model.supervision_dto_signatures_membres_ca import SupervisionDTOSignaturesMembresCA
from osis_admission_sdk.model.supervision_dto_signatures_promoteurs import SupervisionDTOSignaturesPromoteurs
globals()['SupervisionDTOSignaturesMembresCA'] = SupervisionDTOSignaturesMembresCA
globals()['SupervisionDTOSignaturesPromoteurs'] = SupervisionDTOSignaturesPromoteurs
from osis_admission_sdk.model.supervision_dto import SupervisionDTO


class TestSupervisionDTO(unittest.TestCase):
    """SupervisionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSupervisionDTO(self):
        """Test SupervisionDTO"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SupervisionDTO()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
