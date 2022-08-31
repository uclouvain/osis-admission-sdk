"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.33
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from osis_admission_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from osis_admission_sdk.exceptions import ApiAttributeError


def lazy_import():
    from osis_admission_sdk.model.inline_response200 import InlineResponse200
    from osis_admission_sdk.model.proposition_dto_links import PropositionDTOLinks
    from osis_admission_sdk.model.proposition_search_doctorat import PropositionSearchDoctorat
    globals()['InlineResponse200'] = InlineResponse200
    globals()['PropositionDTOLinks'] = PropositionDTOLinks
    globals()['PropositionSearchDoctorat'] = PropositionSearchDoctorat


class PropositionDTO(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'uuid': (str,),  # noqa: E501
            'type_admission': (str,),  # noqa: E501
            'reference': (str,),  # noqa: E501
            'doctorat': (PropositionSearchDoctorat,),  # noqa: E501
            'matricule_candidat': (str,),  # noqa: E501
            'code_secteur_formation': (str,),  # noqa: E501
            'bourse_preuve': ([str],),  # noqa: E501
            'documents_projet': ([str],),  # noqa: E501
            'graphe_gantt': ([str],),  # noqa: E501
            'proposition_programme_doctoral': ([str],),  # noqa: E501
            'projet_formation_complementaire': ([str],),  # noqa: E501
            'lettres_recommandation': ([str],),  # noqa: E501
            'langue_redaction_these': (str,),  # noqa: E501
            'lieu_these': (str,),  # noqa: E501
            'doctorat_deja_realise': (str,),  # noqa: E501
            'domaine_these': (str,),  # noqa: E501
            'fiche_archive_signatures_envoyees': ([str],),  # noqa: E501
            'statut': (str,),  # noqa: E501
            'erreurs': ([InlineResponse200],),  # noqa: E501
            'justification': (str,),  # noqa: E501
            'commission_proximite': (str,),  # noqa: E501
            'type_financement': (str,),  # noqa: E501
            'type_contrat_travail': (str,),  # noqa: E501
            'eft': (int, none_type,),  # noqa: E501
            'bourse_recherche': (str,),  # noqa: E501
            'bourse_date_debut': (date, none_type,),  # noqa: E501
            'bourse_date_fin': (date, none_type,),  # noqa: E501
            'duree_prevue': (int, none_type,),  # noqa: E501
            'temps_consacre': (int, none_type,),  # noqa: E501
            'titre_projet': (str,),  # noqa: E501
            'resume_projet': (str,),  # noqa: E501
            'institut_these': (str, none_type,),  # noqa: E501
            'institution': (str,),  # noqa: E501
            'date_soutenance': (date, none_type,),  # noqa: E501
            'raison_non_soutenue': (str,),  # noqa: E501
            'links': (PropositionDTOLinks,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'uuid': 'uuid',  # noqa: E501
        'type_admission': 'type_admission',  # noqa: E501
        'reference': 'reference',  # noqa: E501
        'doctorat': 'doctorat',  # noqa: E501
        'matricule_candidat': 'matricule_candidat',  # noqa: E501
        'code_secteur_formation': 'code_secteur_formation',  # noqa: E501
        'bourse_preuve': 'bourse_preuve',  # noqa: E501
        'documents_projet': 'documents_projet',  # noqa: E501
        'graphe_gantt': 'graphe_gantt',  # noqa: E501
        'proposition_programme_doctoral': 'proposition_programme_doctoral',  # noqa: E501
        'projet_formation_complementaire': 'projet_formation_complementaire',  # noqa: E501
        'lettres_recommandation': 'lettres_recommandation',  # noqa: E501
        'langue_redaction_these': 'langue_redaction_these',  # noqa: E501
        'lieu_these': 'lieu_these',  # noqa: E501
        'doctorat_deja_realise': 'doctorat_deja_realise',  # noqa: E501
        'domaine_these': 'domaine_these',  # noqa: E501
        'fiche_archive_signatures_envoyees': 'fiche_archive_signatures_envoyees',  # noqa: E501
        'statut': 'statut',  # noqa: E501
        'erreurs': 'erreurs',  # noqa: E501
        'justification': 'justification',  # noqa: E501
        'commission_proximite': 'commission_proximite',  # noqa: E501
        'type_financement': 'type_financement',  # noqa: E501
        'type_contrat_travail': 'type_contrat_travail',  # noqa: E501
        'eft': 'eft',  # noqa: E501
        'bourse_recherche': 'bourse_recherche',  # noqa: E501
        'bourse_date_debut': 'bourse_date_debut',  # noqa: E501
        'bourse_date_fin': 'bourse_date_fin',  # noqa: E501
        'duree_prevue': 'duree_prevue',  # noqa: E501
        'temps_consacre': 'temps_consacre',  # noqa: E501
        'titre_projet': 'titre_projet',  # noqa: E501
        'resume_projet': 'resume_projet',  # noqa: E501
        'institut_these': 'institut_these',  # noqa: E501
        'institution': 'institution',  # noqa: E501
        'date_soutenance': 'date_soutenance',  # noqa: E501
        'raison_non_soutenue': 'raison_non_soutenue',  # noqa: E501
        'links': 'links',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, uuid, type_admission, reference, doctorat, matricule_candidat, code_secteur_formation, bourse_preuve, documents_projet, graphe_gantt, proposition_programme_doctoral, projet_formation_complementaire, lettres_recommandation, langue_redaction_these, lieu_these, doctorat_deja_realise, domaine_these, fiche_archive_signatures_envoyees, statut, erreurs, *args, **kwargs):  # noqa: E501
        """PropositionDTO - a model defined in OpenAPI

        Args:
            uuid (str):
            type_admission (str):
            reference (str):
            doctorat (PropositionSearchDoctorat):
            matricule_candidat (str):
            code_secteur_formation (str):
            bourse_preuve ([str]):
            documents_projet ([str]):
            graphe_gantt ([str]):
            proposition_programme_doctoral ([str]):
            projet_formation_complementaire ([str]):
            lettres_recommandation ([str]):
            langue_redaction_these (str):
            lieu_these (str):
            doctorat_deja_realise (str):
            domaine_these (str):
            fiche_archive_signatures_envoyees ([str]):
            statut (str):
            erreurs ([InlineResponse200]):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            justification (str): [optional]  # noqa: E501
            commission_proximite (str): [optional]  # noqa: E501
            type_financement (str): [optional]  # noqa: E501
            type_contrat_travail (str): [optional]  # noqa: E501
            eft (int, none_type): [optional]  # noqa: E501
            bourse_recherche (str): [optional]  # noqa: E501
            bourse_date_debut (date, none_type): [optional]  # noqa: E501
            bourse_date_fin (date, none_type): [optional]  # noqa: E501
            duree_prevue (int, none_type): [optional]  # noqa: E501
            temps_consacre (int, none_type): [optional]  # noqa: E501
            titre_projet (str): [optional]  # noqa: E501
            resume_projet (str): [optional]  # noqa: E501
            institut_these (str, none_type): [optional]  # noqa: E501
            institution (str): [optional]  # noqa: E501
            date_soutenance (date, none_type): [optional]  # noqa: E501
            raison_non_soutenue (str): [optional]  # noqa: E501
            links (PropositionDTOLinks): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.uuid = uuid
        self.type_admission = type_admission
        self.reference = reference
        self.doctorat = doctorat
        self.matricule_candidat = matricule_candidat
        self.code_secteur_formation = code_secteur_formation
        self.bourse_preuve = bourse_preuve
        self.documents_projet = documents_projet
        self.graphe_gantt = graphe_gantt
        self.proposition_programme_doctoral = proposition_programme_doctoral
        self.projet_formation_complementaire = projet_formation_complementaire
        self.lettres_recommandation = lettres_recommandation
        self.langue_redaction_these = langue_redaction_these
        self.lieu_these = lieu_these
        self.doctorat_deja_realise = doctorat_deja_realise
        self.domaine_these = domaine_these
        self.fiche_archive_signatures_envoyees = fiche_archive_signatures_envoyees
        self.statut = statut
        self.erreurs = erreurs
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, uuid, type_admission, reference, doctorat, matricule_candidat, code_secteur_formation, bourse_preuve, documents_projet, graphe_gantt, proposition_programme_doctoral, projet_formation_complementaire, lettres_recommandation, langue_redaction_these, lieu_these, doctorat_deja_realise, domaine_these, fiche_archive_signatures_envoyees, statut, erreurs, *args, **kwargs):  # noqa: E501
        """PropositionDTO - a model defined in OpenAPI

        Args:
            uuid (str):
            type_admission (str):
            reference (str):
            doctorat (PropositionSearchDoctorat):
            matricule_candidat (str):
            code_secteur_formation (str):
            bourse_preuve ([str]):
            documents_projet ([str]):
            graphe_gantt ([str]):
            proposition_programme_doctoral ([str]):
            projet_formation_complementaire ([str]):
            lettres_recommandation ([str]):
            langue_redaction_these (str):
            lieu_these (str):
            doctorat_deja_realise (str):
            domaine_these (str):
            fiche_archive_signatures_envoyees ([str]):
            statut (str):
            erreurs ([InlineResponse200]):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            justification (str): [optional]  # noqa: E501
            commission_proximite (str): [optional]  # noqa: E501
            type_financement (str): [optional]  # noqa: E501
            type_contrat_travail (str): [optional]  # noqa: E501
            eft (int, none_type): [optional]  # noqa: E501
            bourse_recherche (str): [optional]  # noqa: E501
            bourse_date_debut (date, none_type): [optional]  # noqa: E501
            bourse_date_fin (date, none_type): [optional]  # noqa: E501
            duree_prevue (int, none_type): [optional]  # noqa: E501
            temps_consacre (int, none_type): [optional]  # noqa: E501
            titre_projet (str): [optional]  # noqa: E501
            resume_projet (str): [optional]  # noqa: E501
            institut_these (str, none_type): [optional]  # noqa: E501
            institution (str): [optional]  # noqa: E501
            date_soutenance (date, none_type): [optional]  # noqa: E501
            raison_non_soutenue (str): [optional]  # noqa: E501
            links (PropositionDTOLinks): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.uuid = uuid
        self.type_admission = type_admission
        self.reference = reference
        self.doctorat = doctorat
        self.matricule_candidat = matricule_candidat
        self.code_secteur_formation = code_secteur_formation
        self.bourse_preuve = bourse_preuve
        self.documents_projet = documents_projet
        self.graphe_gantt = graphe_gantt
        self.proposition_programme_doctoral = proposition_programme_doctoral
        self.projet_formation_complementaire = projet_formation_complementaire
        self.lettres_recommandation = lettres_recommandation
        self.langue_redaction_these = langue_redaction_these
        self.lieu_these = lieu_these
        self.doctorat_deja_realise = doctorat_deja_realise
        self.domaine_these = domaine_these
        self.fiche_archive_signatures_envoyees = fiche_archive_signatures_envoyees
        self.statut = statut
        self.erreurs = erreurs
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
