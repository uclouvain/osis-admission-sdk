# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PropositionDTO(object):
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
        'type_admission': 'str',
        'sigle_doctorat': 'str',
        'intitule_doctorat_fr': 'str',
        'intitule_doctorat_en': 'str',
        'matricule_candidat': 'str',
        'code_secteur_formation': 'str',
        'bureau_cde': 'str',
        'type_financement': 'str',
        'type_contrat_travail': 'str',
        'titre_projet': 'str',
        'resume_projet': 'str',
        'documents_projet': 'str',
        'doctorat_deja_realise': 'str',
        'institution': 'str'
    }

    attribute_map = {
        'type_admission': 'type_admission',
        'sigle_doctorat': 'sigle_doctorat',
        'intitule_doctorat_fr': 'intitule_doctorat_fr',
        'intitule_doctorat_en': 'intitule_doctorat_en',
        'matricule_candidat': 'matricule_candidat',
        'code_secteur_formation': 'code_secteur_formation',
        'bureau_cde': 'bureau_CDE',
        'type_financement': 'type_financement',
        'type_contrat_travail': 'type_contrat_travail',
        'titre_projet': 'titre_projet',
        'resume_projet': 'resume_projet',
        'documents_projet': 'documents_projet',
        'doctorat_deja_realise': 'doctorat_deja_realise',
        'institution': 'institution'
    }

    def __init__(self, type_admission=None, sigle_doctorat=None, intitule_doctorat_fr=None, intitule_doctorat_en=None, matricule_candidat=None, code_secteur_formation=None, bureau_cde=None, type_financement=None, type_contrat_travail=None, titre_projet=None, resume_projet=None, documents_projet=None, doctorat_deja_realise=None, institution=None):  # noqa: E501
        """PropositionDTO - a model defined in OpenAPI"""  # noqa: E501

        self._type_admission = None
        self._sigle_doctorat = None
        self._intitule_doctorat_fr = None
        self._intitule_doctorat_en = None
        self._matricule_candidat = None
        self._code_secteur_formation = None
        self._bureau_cde = None
        self._type_financement = None
        self._type_contrat_travail = None
        self._titre_projet = None
        self._resume_projet = None
        self._documents_projet = None
        self._doctorat_deja_realise = None
        self._institution = None
        self.discriminator = None

        if type_admission is not None:
            self.type_admission = type_admission
        if sigle_doctorat is not None:
            self.sigle_doctorat = sigle_doctorat
        if intitule_doctorat_fr is not None:
            self.intitule_doctorat_fr = intitule_doctorat_fr
        if intitule_doctorat_en is not None:
            self.intitule_doctorat_en = intitule_doctorat_en
        if matricule_candidat is not None:
            self.matricule_candidat = matricule_candidat
        if code_secteur_formation is not None:
            self.code_secteur_formation = code_secteur_formation
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
        if documents_projet is not None:
            self.documents_projet = documents_projet
        if doctorat_deja_realise is not None:
            self.doctorat_deja_realise = doctorat_deja_realise
        if institution is not None:
            self.institution = institution

    @property
    def type_admission(self):
        """Gets the type_admission of this PropositionDTO.  # noqa: E501


        :return: The type_admission of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._type_admission

    @type_admission.setter
    def type_admission(self, type_admission):
        """Sets the type_admission of this PropositionDTO.


        :param type_admission: The type_admission of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._type_admission = type_admission

    @property
    def sigle_doctorat(self):
        """Gets the sigle_doctorat of this PropositionDTO.  # noqa: E501


        :return: The sigle_doctorat of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._sigle_doctorat

    @sigle_doctorat.setter
    def sigle_doctorat(self, sigle_doctorat):
        """Sets the sigle_doctorat of this PropositionDTO.


        :param sigle_doctorat: The sigle_doctorat of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._sigle_doctorat = sigle_doctorat

    @property
    def intitule_doctorat_fr(self):
        """Gets the intitule_doctorat_fr of this PropositionDTO.  # noqa: E501


        :return: The intitule_doctorat_fr of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._intitule_doctorat_fr

    @intitule_doctorat_fr.setter
    def intitule_doctorat_fr(self, intitule_doctorat_fr):
        """Sets the intitule_doctorat_fr of this PropositionDTO.


        :param intitule_doctorat_fr: The intitule_doctorat_fr of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._intitule_doctorat_fr = intitule_doctorat_fr

    @property
    def intitule_doctorat_en(self):
        """Gets the intitule_doctorat_en of this PropositionDTO.  # noqa: E501


        :return: The intitule_doctorat_en of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._intitule_doctorat_en

    @intitule_doctorat_en.setter
    def intitule_doctorat_en(self, intitule_doctorat_en):
        """Sets the intitule_doctorat_en of this PropositionDTO.


        :param intitule_doctorat_en: The intitule_doctorat_en of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._intitule_doctorat_en = intitule_doctorat_en

    @property
    def matricule_candidat(self):
        """Gets the matricule_candidat of this PropositionDTO.  # noqa: E501


        :return: The matricule_candidat of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._matricule_candidat

    @matricule_candidat.setter
    def matricule_candidat(self, matricule_candidat):
        """Sets the matricule_candidat of this PropositionDTO.


        :param matricule_candidat: The matricule_candidat of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._matricule_candidat = matricule_candidat

    @property
    def code_secteur_formation(self):
        """Gets the code_secteur_formation of this PropositionDTO.  # noqa: E501


        :return: The code_secteur_formation of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._code_secteur_formation

    @code_secteur_formation.setter
    def code_secteur_formation(self, code_secteur_formation):
        """Sets the code_secteur_formation of this PropositionDTO.


        :param code_secteur_formation: The code_secteur_formation of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._code_secteur_formation = code_secteur_formation

    @property
    def bureau_cde(self):
        """Gets the bureau_cde of this PropositionDTO.  # noqa: E501


        :return: The bureau_cde of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._bureau_cde

    @bureau_cde.setter
    def bureau_cde(self, bureau_cde):
        """Sets the bureau_cde of this PropositionDTO.


        :param bureau_cde: The bureau_cde of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._bureau_cde = bureau_cde

    @property
    def type_financement(self):
        """Gets the type_financement of this PropositionDTO.  # noqa: E501


        :return: The type_financement of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._type_financement

    @type_financement.setter
    def type_financement(self, type_financement):
        """Sets the type_financement of this PropositionDTO.


        :param type_financement: The type_financement of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._type_financement = type_financement

    @property
    def type_contrat_travail(self):
        """Gets the type_contrat_travail of this PropositionDTO.  # noqa: E501


        :return: The type_contrat_travail of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._type_contrat_travail

    @type_contrat_travail.setter
    def type_contrat_travail(self, type_contrat_travail):
        """Sets the type_contrat_travail of this PropositionDTO.


        :param type_contrat_travail: The type_contrat_travail of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._type_contrat_travail = type_contrat_travail

    @property
    def titre_projet(self):
        """Gets the titre_projet of this PropositionDTO.  # noqa: E501


        :return: The titre_projet of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._titre_projet

    @titre_projet.setter
    def titre_projet(self, titre_projet):
        """Sets the titre_projet of this PropositionDTO.


        :param titre_projet: The titre_projet of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._titre_projet = titre_projet

    @property
    def resume_projet(self):
        """Gets the resume_projet of this PropositionDTO.  # noqa: E501


        :return: The resume_projet of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._resume_projet

    @resume_projet.setter
    def resume_projet(self, resume_projet):
        """Sets the resume_projet of this PropositionDTO.


        :param resume_projet: The resume_projet of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._resume_projet = resume_projet

    @property
    def documents_projet(self):
        """Gets the documents_projet of this PropositionDTO.  # noqa: E501


        :return: The documents_projet of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._documents_projet

    @documents_projet.setter
    def documents_projet(self, documents_projet):
        """Sets the documents_projet of this PropositionDTO.


        :param documents_projet: The documents_projet of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._documents_projet = documents_projet

    @property
    def doctorat_deja_realise(self):
        """Gets the doctorat_deja_realise of this PropositionDTO.  # noqa: E501


        :return: The doctorat_deja_realise of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._doctorat_deja_realise

    @doctorat_deja_realise.setter
    def doctorat_deja_realise(self, doctorat_deja_realise):
        """Sets the doctorat_deja_realise of this PropositionDTO.


        :param doctorat_deja_realise: The doctorat_deja_realise of this PropositionDTO.  # noqa: E501
        :type: str
        """

        self._doctorat_deja_realise = doctorat_deja_realise

    @property
    def institution(self):
        """Gets the institution of this PropositionDTO.  # noqa: E501


        :return: The institution of this PropositionDTO.  # noqa: E501
        :rtype: str
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this PropositionDTO.


        :param institution: The institution of this PropositionDTO.  # noqa: E501
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
        if not isinstance(other, PropositionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
