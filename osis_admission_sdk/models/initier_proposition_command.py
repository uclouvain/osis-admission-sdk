# coding: utf-8

"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InitierPropositionCommand(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'sigle_formation': 'str',
        'annee_formation': 'int',
        'bureau_cde': 'str',
        'type_financement': 'str',
        'type_contrat_travail': 'str',
        'titre_projet': 'str',
        'resume_projet': 'str',
        'documents_projet': 'list[str]',
        'doctorat_deja_realise': 'str',
        'institution': 'str'
    }

    attribute_map = {
        'type': 'type',
        'sigle_formation': 'sigle_formation',
        'annee_formation': 'annee_formation',
        'bureau_cde': 'bureau_CDE',
        'type_financement': 'type_financement',
        'type_contrat_travail': 'type_contrat_travail',
        'titre_projet': 'titre_projet',
        'resume_projet': 'resume_projet',
        'documents_projet': 'documents_projet',
        'doctorat_deja_realise': 'doctorat_deja_realise',
        'institution': 'institution'
    }

    def __init__(self, type=None, sigle_formation=None, annee_formation=None, bureau_cde=None, type_financement=None, type_contrat_travail=None, titre_projet=None, resume_projet=None, documents_projet=None, doctorat_deja_realise='NO', institution=None):  # noqa: E501
        """InitierPropositionCommand - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._sigle_formation = None
        self._annee_formation = None
        self._bureau_cde = None
        self._type_financement = None
        self._type_contrat_travail = None
        self._titre_projet = None
        self._resume_projet = None
        self._documents_projet = None
        self._doctorat_deja_realise = None
        self._institution = None
        self.discriminator = None

        self.type = type
        self.sigle_formation = sigle_formation
        self.annee_formation = annee_formation
        if bureau_cde is not None:
            self.bureau_cde = bureau_cde
        if type_financement is not None:
            self.type_financement = type_financement
        if type_contrat_travail is not None:
            self.type_contrat_travail = type_contrat_travail
        if titre_projet is not None:
            self.titre_projet = titre_projet
        if resume_projet is not None:
            self.resume_projet = resume_projet
        self.documents_projet = documents_projet
        if doctorat_deja_realise is not None:
            self.doctorat_deja_realise = doctorat_deja_realise
        if institution is not None:
            self.institution = institution

    @property
    def type(self):
        """Gets the type of this InitierPropositionCommand.  # noqa: E501


        :return: The type of this InitierPropositionCommand.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InitierPropositionCommand.


        :param type: The type of this InitierPropositionCommand.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ADMISSION", "PRE_ADMISSION"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def sigle_formation(self):
        """Gets the sigle_formation of this InitierPropositionCommand.  # noqa: E501


        :return: The sigle_formation of this InitierPropositionCommand.  # noqa: E501
        :rtype: str
        """
        return self._sigle_formation

    @sigle_formation.setter
    def sigle_formation(self, sigle_formation):
        """Sets the sigle_formation of this InitierPropositionCommand.


        :param sigle_formation: The sigle_formation of this InitierPropositionCommand.  # noqa: E501
        :type: str
        """
        if sigle_formation is None:
            raise ValueError("Invalid value for `sigle_formation`, must not be `None`")  # noqa: E501

        self._sigle_formation = sigle_formation

    @property
    def annee_formation(self):
        """Gets the annee_formation of this InitierPropositionCommand.  # noqa: E501


        :return: The annee_formation of this InitierPropositionCommand.  # noqa: E501
        :rtype: int
        """
        return self._annee_formation

    @annee_formation.setter
    def annee_formation(self, annee_formation):
        """Sets the annee_formation of this InitierPropositionCommand.


        :param annee_formation: The annee_formation of this InitierPropositionCommand.  # noqa: E501
        :type: int
        """
        if annee_formation is None:
            raise ValueError("Invalid value for `annee_formation`, must not be `None`")  # noqa: E501

        self._annee_formation = annee_formation

    @property
    def bureau_cde(self):
        """Gets the bureau_cde of this InitierPropositionCommand.  # noqa: E501


        :return: The bureau_cde of this InitierPropositionCommand.  # noqa: E501
        :rtype: str
        """
        return self._bureau_cde

    @bureau_cde.setter
    def bureau_cde(self, bureau_cde):
        """Sets the bureau_cde of this InitierPropositionCommand.


        :param bureau_cde: The bureau_cde of this InitierPropositionCommand.  # noqa: E501
        :type: str
        """

        self._bureau_cde = bureau_cde

    @property
    def type_financement(self):
        """Gets the type_financement of this InitierPropositionCommand.  # noqa: E501


        :return: The type_financement of this InitierPropositionCommand.  # noqa: E501
        :rtype: str
        """
        return self._type_financement

    @type_financement.setter
    def type_financement(self, type_financement):
        """Sets the type_financement of this InitierPropositionCommand.


        :param type_financement: The type_financement of this InitierPropositionCommand.  # noqa: E501
        :type: str
        """
        allowed_values = ["WORK_CONTRACT", "SEARCH_SCHOLARSHIP", "SELF_FUNDING"]  # noqa: E501
        if type_financement not in allowed_values:
            raise ValueError(
                "Invalid value for `type_financement` ({0}), must be one of {1}"  # noqa: E501
                .format(type_financement, allowed_values)
            )

        self._type_financement = type_financement

    @property
    def type_contrat_travail(self):
        """Gets the type_contrat_travail of this InitierPropositionCommand.  # noqa: E501


        :return: The type_contrat_travail of this InitierPropositionCommand.  # noqa: E501
        :rtype: str
        """
        return self._type_contrat_travail

    @type_contrat_travail.setter
    def type_contrat_travail(self, type_contrat_travail):
        """Sets the type_contrat_travail of this InitierPropositionCommand.


        :param type_contrat_travail: The type_contrat_travail of this InitierPropositionCommand.  # noqa: E501
        :type: str
        """

        self._type_contrat_travail = type_contrat_travail

    @property
    def titre_projet(self):
        """Gets the titre_projet of this InitierPropositionCommand.  # noqa: E501


        :return: The titre_projet of this InitierPropositionCommand.  # noqa: E501
        :rtype: str
        """
        return self._titre_projet

    @titre_projet.setter
    def titre_projet(self, titre_projet):
        """Sets the titre_projet of this InitierPropositionCommand.


        :param titre_projet: The titre_projet of this InitierPropositionCommand.  # noqa: E501
        :type: str
        """

        self._titre_projet = titre_projet

    @property
    def resume_projet(self):
        """Gets the resume_projet of this InitierPropositionCommand.  # noqa: E501


        :return: The resume_projet of this InitierPropositionCommand.  # noqa: E501
        :rtype: str
        """
        return self._resume_projet

    @resume_projet.setter
    def resume_projet(self, resume_projet):
        """Sets the resume_projet of this InitierPropositionCommand.


        :param resume_projet: The resume_projet of this InitierPropositionCommand.  # noqa: E501
        :type: str
        """

        self._resume_projet = resume_projet

    @property
    def documents_projet(self):
        """Gets the documents_projet of this InitierPropositionCommand.  # noqa: E501


        :return: The documents_projet of this InitierPropositionCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._documents_projet

    @documents_projet.setter
    def documents_projet(self, documents_projet):
        """Sets the documents_projet of this InitierPropositionCommand.


        :param documents_projet: The documents_projet of this InitierPropositionCommand.  # noqa: E501
        :type: list[str]
        """
        if documents_projet is None:
            raise ValueError("Invalid value for `documents_projet`, must not be `None`")  # noqa: E501

        self._documents_projet = documents_projet

    @property
    def doctorat_deja_realise(self):
        """Gets the doctorat_deja_realise of this InitierPropositionCommand.  # noqa: E501


        :return: The doctorat_deja_realise of this InitierPropositionCommand.  # noqa: E501
        :rtype: str
        """
        return self._doctorat_deja_realise

    @doctorat_deja_realise.setter
    def doctorat_deja_realise(self, doctorat_deja_realise):
        """Sets the doctorat_deja_realise of this InitierPropositionCommand.


        :param doctorat_deja_realise: The doctorat_deja_realise of this InitierPropositionCommand.  # noqa: E501
        :type: str
        """
        allowed_values = ["YES", "NO", "PARTIAL"]  # noqa: E501
        if doctorat_deja_realise not in allowed_values:
            raise ValueError(
                "Invalid value for `doctorat_deja_realise` ({0}), must be one of {1}"  # noqa: E501
                .format(doctorat_deja_realise, allowed_values)
            )

        self._doctorat_deja_realise = doctorat_deja_realise

    @property
    def institution(self):
        """Gets the institution of this InitierPropositionCommand.  # noqa: E501


        :return: The institution of this InitierPropositionCommand.  # noqa: E501
        :rtype: str
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this InitierPropositionCommand.


        :param institution: The institution of this InitierPropositionCommand.  # noqa: E501
        :type: str
        """

        self._institution = institution

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InitierPropositionCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
