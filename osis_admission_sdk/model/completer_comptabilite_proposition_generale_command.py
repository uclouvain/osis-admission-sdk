"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.65
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



class CompleterComptabilitePropositionGeneraleCommand(ModelNormal):
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
        return {
            'uuid_proposition': (str,),  # noqa: E501
            'attestation_absence_dette_etablissement': ([str],),  # noqa: E501
            'attestation_enfant_personnel': ([str],),  # noqa: E501
            'carte_resident_longue_duree': ([str],),  # noqa: E501
            'carte_cire_sejour_illimite_etranger': ([str],),  # noqa: E501
            'carte_sejour_membre_ue': ([str],),  # noqa: E501
            'carte_sejour_permanent_membre_ue': ([str],),  # noqa: E501
            'carte_a_b_refugie': ([str],),  # noqa: E501
            'annexe_25_26_refugies_apatrides': ([str],),  # noqa: E501
            'attestation_immatriculation': ([str],),  # noqa: E501
            'carte_a_b': ([str],),  # noqa: E501
            'decision_protection_subsidiaire': ([str],),  # noqa: E501
            'decision_protection_temporaire': ([str],),  # noqa: E501
            'titre_sejour_3_mois_professionel': ([str],),  # noqa: E501
            'fiches_remuneration': ([str],),  # noqa: E501
            'titre_sejour_3_mois_remplacement': ([str],),  # noqa: E501
            'preuve_allocations_chomage_pension_indemnite': ([str],),  # noqa: E501
            'attestation_cpas': ([str],),  # noqa: E501
            'composition_menage_acte_naissance': ([str],),  # noqa: E501
            'acte_tutelle': ([str],),  # noqa: E501
            'composition_menage_acte_mariage': ([str],),  # noqa: E501
            'attestation_cohabitation_legale': ([str],),  # noqa: E501
            'carte_identite_parent': ([str],),  # noqa: E501
            'titre_sejour_longue_duree_parent': ([str],),  # noqa: E501
            'annexe_25_26_refugies_apatrides_decision_protection_parent': ([str],),  # noqa: E501
            'titre_sejour_3_mois_parent': ([str],),  # noqa: E501
            'fiches_remuneration_parent': ([str],),  # noqa: E501
            'attestation_cpas_parent': ([str],),  # noqa: E501
            'decision_bourse_cfwb': ([str],),  # noqa: E501
            'attestation_boursier': ([str],),  # noqa: E501
            'titre_identite_sejour_longue_duree_ue': ([str],),  # noqa: E501
            'titre_sejour_belgique': ([str],),  # noqa: E501
            'demande_allocation_d_etudes_communaute_francaise_belgique': (bool, none_type,),  # noqa: E501
            'enfant_personnel': (bool, none_type,),  # noqa: E501
            'type_situation_assimilation': (str,),  # noqa: E501
            'sous_type_situation_assimilation_1': (str,),  # noqa: E501
            'sous_type_situation_assimilation_2': (str,),  # noqa: E501
            'sous_type_situation_assimilation_3': (str,),  # noqa: E501
            'relation_parente': (str,),  # noqa: E501
            'sous_type_situation_assimilation_5': (str,),  # noqa: E501
            'sous_type_situation_assimilation_6': (str,),  # noqa: E501
            'affiliation_sport': (str,),  # noqa: E501
            'etudiant_solidaire': (bool, none_type,),  # noqa: E501
            'type_numero_compte': (str,),  # noqa: E501
            'numero_compte_iban': (str,),  # noqa: E501
            'iban_valide': (bool, none_type,),  # noqa: E501
            'numero_compte_autre_format': (str,),  # noqa: E501
            'code_bic_swift_banque': (str,),  # noqa: E501
            'prenom_titulaire_compte': (str,),  # noqa: E501
            'nom_titulaire_compte': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'uuid_proposition': 'uuid_proposition',  # noqa: E501
        'attestation_absence_dette_etablissement': 'attestation_absence_dette_etablissement',  # noqa: E501
        'attestation_enfant_personnel': 'attestation_enfant_personnel',  # noqa: E501
        'carte_resident_longue_duree': 'carte_resident_longue_duree',  # noqa: E501
        'carte_cire_sejour_illimite_etranger': 'carte_cire_sejour_illimite_etranger',  # noqa: E501
        'carte_sejour_membre_ue': 'carte_sejour_membre_ue',  # noqa: E501
        'carte_sejour_permanent_membre_ue': 'carte_sejour_permanent_membre_ue',  # noqa: E501
        'carte_a_b_refugie': 'carte_a_b_refugie',  # noqa: E501
        'annexe_25_26_refugies_apatrides': 'annexe_25_26_refugies_apatrides',  # noqa: E501
        'attestation_immatriculation': 'attestation_immatriculation',  # noqa: E501
        'carte_a_b': 'carte_a_b',  # noqa: E501
        'decision_protection_subsidiaire': 'decision_protection_subsidiaire',  # noqa: E501
        'decision_protection_temporaire': 'decision_protection_temporaire',  # noqa: E501
        'titre_sejour_3_mois_professionel': 'titre_sejour_3_mois_professionel',  # noqa: E501
        'fiches_remuneration': 'fiches_remuneration',  # noqa: E501
        'titre_sejour_3_mois_remplacement': 'titre_sejour_3_mois_remplacement',  # noqa: E501
        'preuve_allocations_chomage_pension_indemnite': 'preuve_allocations_chomage_pension_indemnite',  # noqa: E501
        'attestation_cpas': 'attestation_cpas',  # noqa: E501
        'composition_menage_acte_naissance': 'composition_menage_acte_naissance',  # noqa: E501
        'acte_tutelle': 'acte_tutelle',  # noqa: E501
        'composition_menage_acte_mariage': 'composition_menage_acte_mariage',  # noqa: E501
        'attestation_cohabitation_legale': 'attestation_cohabitation_legale',  # noqa: E501
        'carte_identite_parent': 'carte_identite_parent',  # noqa: E501
        'titre_sejour_longue_duree_parent': 'titre_sejour_longue_duree_parent',  # noqa: E501
        'annexe_25_26_refugies_apatrides_decision_protection_parent': 'annexe_25_26_refugies_apatrides_decision_protection_parent',  # noqa: E501
        'titre_sejour_3_mois_parent': 'titre_sejour_3_mois_parent',  # noqa: E501
        'fiches_remuneration_parent': 'fiches_remuneration_parent',  # noqa: E501
        'attestation_cpas_parent': 'attestation_cpas_parent',  # noqa: E501
        'decision_bourse_cfwb': 'decision_bourse_cfwb',  # noqa: E501
        'attestation_boursier': 'attestation_boursier',  # noqa: E501
        'titre_identite_sejour_longue_duree_ue': 'titre_identite_sejour_longue_duree_ue',  # noqa: E501
        'titre_sejour_belgique': 'titre_sejour_belgique',  # noqa: E501
        'demande_allocation_d_etudes_communaute_francaise_belgique': 'demande_allocation_d_etudes_communaute_francaise_belgique',  # noqa: E501
        'enfant_personnel': 'enfant_personnel',  # noqa: E501
        'type_situation_assimilation': 'type_situation_assimilation',  # noqa: E501
        'sous_type_situation_assimilation_1': 'sous_type_situation_assimilation_1',  # noqa: E501
        'sous_type_situation_assimilation_2': 'sous_type_situation_assimilation_2',  # noqa: E501
        'sous_type_situation_assimilation_3': 'sous_type_situation_assimilation_3',  # noqa: E501
        'relation_parente': 'relation_parente',  # noqa: E501
        'sous_type_situation_assimilation_5': 'sous_type_situation_assimilation_5',  # noqa: E501
        'sous_type_situation_assimilation_6': 'sous_type_situation_assimilation_6',  # noqa: E501
        'affiliation_sport': 'affiliation_sport',  # noqa: E501
        'etudiant_solidaire': 'etudiant_solidaire',  # noqa: E501
        'type_numero_compte': 'type_numero_compte',  # noqa: E501
        'numero_compte_iban': 'numero_compte_iban',  # noqa: E501
        'iban_valide': 'iban_valide',  # noqa: E501
        'numero_compte_autre_format': 'numero_compte_autre_format',  # noqa: E501
        'code_bic_swift_banque': 'code_bic_swift_banque',  # noqa: E501
        'prenom_titulaire_compte': 'prenom_titulaire_compte',  # noqa: E501
        'nom_titulaire_compte': 'nom_titulaire_compte',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, uuid_proposition, attestation_absence_dette_etablissement, attestation_enfant_personnel, carte_resident_longue_duree, carte_cire_sejour_illimite_etranger, carte_sejour_membre_ue, carte_sejour_permanent_membre_ue, carte_a_b_refugie, annexe_25_26_refugies_apatrides, attestation_immatriculation, carte_a_b, decision_protection_subsidiaire, decision_protection_temporaire, titre_sejour_3_mois_professionel, fiches_remuneration, titre_sejour_3_mois_remplacement, preuve_allocations_chomage_pension_indemnite, attestation_cpas, composition_menage_acte_naissance, acte_tutelle, composition_menage_acte_mariage, attestation_cohabitation_legale, carte_identite_parent, titre_sejour_longue_duree_parent, annexe_25_26_refugies_apatrides_decision_protection_parent, titre_sejour_3_mois_parent, fiches_remuneration_parent, attestation_cpas_parent, decision_bourse_cfwb, attestation_boursier, titre_identite_sejour_longue_duree_ue, titre_sejour_belgique, *args, **kwargs):  # noqa: E501
        """CompleterComptabilitePropositionGeneraleCommand - a model defined in OpenAPI

        Args:
            uuid_proposition (str):
            attestation_absence_dette_etablissement ([str]):
            attestation_enfant_personnel ([str]):
            carte_resident_longue_duree ([str]):
            carte_cire_sejour_illimite_etranger ([str]):
            carte_sejour_membre_ue ([str]):
            carte_sejour_permanent_membre_ue ([str]):
            carte_a_b_refugie ([str]):
            annexe_25_26_refugies_apatrides ([str]):
            attestation_immatriculation ([str]):
            carte_a_b ([str]):
            decision_protection_subsidiaire ([str]):
            decision_protection_temporaire ([str]):
            titre_sejour_3_mois_professionel ([str]):
            fiches_remuneration ([str]):
            titre_sejour_3_mois_remplacement ([str]):
            preuve_allocations_chomage_pension_indemnite ([str]):
            attestation_cpas ([str]):
            composition_menage_acte_naissance ([str]):
            acte_tutelle ([str]):
            composition_menage_acte_mariage ([str]):
            attestation_cohabitation_legale ([str]):
            carte_identite_parent ([str]):
            titre_sejour_longue_duree_parent ([str]):
            annexe_25_26_refugies_apatrides_decision_protection_parent ([str]):
            titre_sejour_3_mois_parent ([str]):
            fiches_remuneration_parent ([str]):
            attestation_cpas_parent ([str]):
            decision_bourse_cfwb ([str]):
            attestation_boursier ([str]):
            titre_identite_sejour_longue_duree_ue ([str]):
            titre_sejour_belgique ([str]):

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
            demande_allocation_d_etudes_communaute_francaise_belgique (bool, none_type): [optional]  # noqa: E501
            enfant_personnel (bool, none_type): [optional]  # noqa: E501
            type_situation_assimilation (str): [optional]  # noqa: E501
            sous_type_situation_assimilation_1 (str): [optional]  # noqa: E501
            sous_type_situation_assimilation_2 (str): [optional]  # noqa: E501
            sous_type_situation_assimilation_3 (str): [optional]  # noqa: E501
            relation_parente (str): [optional]  # noqa: E501
            sous_type_situation_assimilation_5 (str): [optional]  # noqa: E501
            sous_type_situation_assimilation_6 (str): [optional]  # noqa: E501
            affiliation_sport (str): [optional]  # noqa: E501
            etudiant_solidaire (bool, none_type): [optional]  # noqa: E501
            type_numero_compte (str): [optional]  # noqa: E501
            numero_compte_iban (str): [optional]  # noqa: E501
            iban_valide (bool, none_type): [optional]  # noqa: E501
            numero_compte_autre_format (str): [optional]  # noqa: E501
            code_bic_swift_banque (str): [optional]  # noqa: E501
            prenom_titulaire_compte (str): [optional]  # noqa: E501
            nom_titulaire_compte (str): [optional]  # noqa: E501
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

        self.uuid_proposition = uuid_proposition
        self.attestation_absence_dette_etablissement = attestation_absence_dette_etablissement
        self.attestation_enfant_personnel = attestation_enfant_personnel
        self.carte_resident_longue_duree = carte_resident_longue_duree
        self.carte_cire_sejour_illimite_etranger = carte_cire_sejour_illimite_etranger
        self.carte_sejour_membre_ue = carte_sejour_membre_ue
        self.carte_sejour_permanent_membre_ue = carte_sejour_permanent_membre_ue
        self.carte_a_b_refugie = carte_a_b_refugie
        self.annexe_25_26_refugies_apatrides = annexe_25_26_refugies_apatrides
        self.attestation_immatriculation = attestation_immatriculation
        self.carte_a_b = carte_a_b
        self.decision_protection_subsidiaire = decision_protection_subsidiaire
        self.decision_protection_temporaire = decision_protection_temporaire
        self.titre_sejour_3_mois_professionel = titre_sejour_3_mois_professionel
        self.fiches_remuneration = fiches_remuneration
        self.titre_sejour_3_mois_remplacement = titre_sejour_3_mois_remplacement
        self.preuve_allocations_chomage_pension_indemnite = preuve_allocations_chomage_pension_indemnite
        self.attestation_cpas = attestation_cpas
        self.composition_menage_acte_naissance = composition_menage_acte_naissance
        self.acte_tutelle = acte_tutelle
        self.composition_menage_acte_mariage = composition_menage_acte_mariage
        self.attestation_cohabitation_legale = attestation_cohabitation_legale
        self.carte_identite_parent = carte_identite_parent
        self.titre_sejour_longue_duree_parent = titre_sejour_longue_duree_parent
        self.annexe_25_26_refugies_apatrides_decision_protection_parent = annexe_25_26_refugies_apatrides_decision_protection_parent
        self.titre_sejour_3_mois_parent = titre_sejour_3_mois_parent
        self.fiches_remuneration_parent = fiches_remuneration_parent
        self.attestation_cpas_parent = attestation_cpas_parent
        self.decision_bourse_cfwb = decision_bourse_cfwb
        self.attestation_boursier = attestation_boursier
        self.titre_identite_sejour_longue_duree_ue = titre_identite_sejour_longue_duree_ue
        self.titre_sejour_belgique = titre_sejour_belgique
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
    def __init__(self, uuid_proposition, attestation_absence_dette_etablissement, attestation_enfant_personnel, carte_resident_longue_duree, carte_cire_sejour_illimite_etranger, carte_sejour_membre_ue, carte_sejour_permanent_membre_ue, carte_a_b_refugie, annexe_25_26_refugies_apatrides, attestation_immatriculation, carte_a_b, decision_protection_subsidiaire, decision_protection_temporaire, titre_sejour_3_mois_professionel, fiches_remuneration, titre_sejour_3_mois_remplacement, preuve_allocations_chomage_pension_indemnite, attestation_cpas, composition_menage_acte_naissance, acte_tutelle, composition_menage_acte_mariage, attestation_cohabitation_legale, carte_identite_parent, titre_sejour_longue_duree_parent, annexe_25_26_refugies_apatrides_decision_protection_parent, titre_sejour_3_mois_parent, fiches_remuneration_parent, attestation_cpas_parent, decision_bourse_cfwb, attestation_boursier, titre_identite_sejour_longue_duree_ue, titre_sejour_belgique, *args, **kwargs):  # noqa: E501
        """CompleterComptabilitePropositionGeneraleCommand - a model defined in OpenAPI

        Args:
            uuid_proposition (str):
            attestation_absence_dette_etablissement ([str]):
            attestation_enfant_personnel ([str]):
            carte_resident_longue_duree ([str]):
            carte_cire_sejour_illimite_etranger ([str]):
            carte_sejour_membre_ue ([str]):
            carte_sejour_permanent_membre_ue ([str]):
            carte_a_b_refugie ([str]):
            annexe_25_26_refugies_apatrides ([str]):
            attestation_immatriculation ([str]):
            carte_a_b ([str]):
            decision_protection_subsidiaire ([str]):
            decision_protection_temporaire ([str]):
            titre_sejour_3_mois_professionel ([str]):
            fiches_remuneration ([str]):
            titre_sejour_3_mois_remplacement ([str]):
            preuve_allocations_chomage_pension_indemnite ([str]):
            attestation_cpas ([str]):
            composition_menage_acte_naissance ([str]):
            acte_tutelle ([str]):
            composition_menage_acte_mariage ([str]):
            attestation_cohabitation_legale ([str]):
            carte_identite_parent ([str]):
            titre_sejour_longue_duree_parent ([str]):
            annexe_25_26_refugies_apatrides_decision_protection_parent ([str]):
            titre_sejour_3_mois_parent ([str]):
            fiches_remuneration_parent ([str]):
            attestation_cpas_parent ([str]):
            decision_bourse_cfwb ([str]):
            attestation_boursier ([str]):
            titre_identite_sejour_longue_duree_ue ([str]):
            titre_sejour_belgique ([str]):

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
            demande_allocation_d_etudes_communaute_francaise_belgique (bool, none_type): [optional]  # noqa: E501
            enfant_personnel (bool, none_type): [optional]  # noqa: E501
            type_situation_assimilation (str): [optional]  # noqa: E501
            sous_type_situation_assimilation_1 (str): [optional]  # noqa: E501
            sous_type_situation_assimilation_2 (str): [optional]  # noqa: E501
            sous_type_situation_assimilation_3 (str): [optional]  # noqa: E501
            relation_parente (str): [optional]  # noqa: E501
            sous_type_situation_assimilation_5 (str): [optional]  # noqa: E501
            sous_type_situation_assimilation_6 (str): [optional]  # noqa: E501
            affiliation_sport (str): [optional]  # noqa: E501
            etudiant_solidaire (bool, none_type): [optional]  # noqa: E501
            type_numero_compte (str): [optional]  # noqa: E501
            numero_compte_iban (str): [optional]  # noqa: E501
            iban_valide (bool, none_type): [optional]  # noqa: E501
            numero_compte_autre_format (str): [optional]  # noqa: E501
            code_bic_swift_banque (str): [optional]  # noqa: E501
            prenom_titulaire_compte (str): [optional]  # noqa: E501
            nom_titulaire_compte (str): [optional]  # noqa: E501
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

        self.uuid_proposition = uuid_proposition
        self.attestation_absence_dette_etablissement = attestation_absence_dette_etablissement
        self.attestation_enfant_personnel = attestation_enfant_personnel
        self.carte_resident_longue_duree = carte_resident_longue_duree
        self.carte_cire_sejour_illimite_etranger = carte_cire_sejour_illimite_etranger
        self.carte_sejour_membre_ue = carte_sejour_membre_ue
        self.carte_sejour_permanent_membre_ue = carte_sejour_permanent_membre_ue
        self.carte_a_b_refugie = carte_a_b_refugie
        self.annexe_25_26_refugies_apatrides = annexe_25_26_refugies_apatrides
        self.attestation_immatriculation = attestation_immatriculation
        self.carte_a_b = carte_a_b
        self.decision_protection_subsidiaire = decision_protection_subsidiaire
        self.decision_protection_temporaire = decision_protection_temporaire
        self.titre_sejour_3_mois_professionel = titre_sejour_3_mois_professionel
        self.fiches_remuneration = fiches_remuneration
        self.titre_sejour_3_mois_remplacement = titre_sejour_3_mois_remplacement
        self.preuve_allocations_chomage_pension_indemnite = preuve_allocations_chomage_pension_indemnite
        self.attestation_cpas = attestation_cpas
        self.composition_menage_acte_naissance = composition_menage_acte_naissance
        self.acte_tutelle = acte_tutelle
        self.composition_menage_acte_mariage = composition_menage_acte_mariage
        self.attestation_cohabitation_legale = attestation_cohabitation_legale
        self.carte_identite_parent = carte_identite_parent
        self.titre_sejour_longue_duree_parent = titre_sejour_longue_duree_parent
        self.annexe_25_26_refugies_apatrides_decision_protection_parent = annexe_25_26_refugies_apatrides_decision_protection_parent
        self.titre_sejour_3_mois_parent = titre_sejour_3_mois_parent
        self.fiches_remuneration_parent = fiches_remuneration_parent
        self.attestation_cpas_parent = attestation_cpas_parent
        self.decision_bourse_cfwb = decision_bourse_cfwb
        self.attestation_boursier = attestation_boursier
        self.titre_identite_sejour_longue_duree_ue = titre_identite_sejour_longue_duree_ue
        self.titre_sejour_belgique = titre_sejour_belgique
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
