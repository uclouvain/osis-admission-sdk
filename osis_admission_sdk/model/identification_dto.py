"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.88
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



class IdentificationDTO(ModelNormal):
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
            'matricule': (str,),  # noqa: E501
            'nom': (str,),  # noqa: E501
            'prenom': (str,),  # noqa: E501
            'autres_prenoms': (str,),  # noqa: E501
            'pays_nationalite': (str,),  # noqa: E501
            'nom_pays_nationalite': (str,),  # noqa: E501
            'sexe': (str,),  # noqa: E501
            'genre': (str,),  # noqa: E501
            'photo_identite': ([str],),  # noqa: E501
            'pays_naissance': (str,),  # noqa: E501
            'nom_pays_naissance': (str,),  # noqa: E501
            'lieu_naissance': (str,),  # noqa: E501
            'etat_civil': (str,),  # noqa: E501
            'pays_residence': (str,),  # noqa: E501
            'carte_identite': ([str],),  # noqa: E501
            'passeport': ([str],),  # noqa: E501
            'numero_registre_national_belge': (str,),  # noqa: E501
            'numero_carte_identite': (str,),  # noqa: E501
            'numero_passeport': (str,),  # noqa: E501
            'langue_contact': (str,),  # noqa: E501
            'nom_langue_contact': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'noma_derniere_inscription_ucl': (str,),  # noqa: E501
            'date_naissance': (date, none_type,),  # noqa: E501
            'annee_naissance': (int, none_type,),  # noqa: E501
            'pays_nationalite_europeen': (bool, none_type,),  # noqa: E501
            'date_expiration_carte_identite': (date, none_type,),  # noqa: E501
            'date_expiration_passeport': (date, none_type,),  # noqa: E501
            'annee_derniere_inscription_ucl': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'matricule': 'matricule',  # noqa: E501
        'nom': 'nom',  # noqa: E501
        'prenom': 'prenom',  # noqa: E501
        'autres_prenoms': 'autres_prenoms',  # noqa: E501
        'pays_nationalite': 'pays_nationalite',  # noqa: E501
        'nom_pays_nationalite': 'nom_pays_nationalite',  # noqa: E501
        'sexe': 'sexe',  # noqa: E501
        'genre': 'genre',  # noqa: E501
        'photo_identite': 'photo_identite',  # noqa: E501
        'pays_naissance': 'pays_naissance',  # noqa: E501
        'nom_pays_naissance': 'nom_pays_naissance',  # noqa: E501
        'lieu_naissance': 'lieu_naissance',  # noqa: E501
        'etat_civil': 'etat_civil',  # noqa: E501
        'pays_residence': 'pays_residence',  # noqa: E501
        'carte_identite': 'carte_identite',  # noqa: E501
        'passeport': 'passeport',  # noqa: E501
        'numero_registre_national_belge': 'numero_registre_national_belge',  # noqa: E501
        'numero_carte_identite': 'numero_carte_identite',  # noqa: E501
        'numero_passeport': 'numero_passeport',  # noqa: E501
        'langue_contact': 'langue_contact',  # noqa: E501
        'nom_langue_contact': 'nom_langue_contact',  # noqa: E501
        'email': 'email',  # noqa: E501
        'noma_derniere_inscription_ucl': 'noma_derniere_inscription_ucl',  # noqa: E501
        'date_naissance': 'date_naissance',  # noqa: E501
        'annee_naissance': 'annee_naissance',  # noqa: E501
        'pays_nationalite_europeen': 'pays_nationalite_europeen',  # noqa: E501
        'date_expiration_carte_identite': 'date_expiration_carte_identite',  # noqa: E501
        'date_expiration_passeport': 'date_expiration_passeport',  # noqa: E501
        'annee_derniere_inscription_ucl': 'annee_derniere_inscription_ucl',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, matricule, nom, prenom, autres_prenoms, pays_nationalite, nom_pays_nationalite, sexe, genre, photo_identite, pays_naissance, nom_pays_naissance, lieu_naissance, etat_civil, pays_residence, carte_identite, passeport, numero_registre_national_belge, numero_carte_identite, numero_passeport, langue_contact, nom_langue_contact, email, noma_derniere_inscription_ucl, *args, **kwargs):  # noqa: E501
        """IdentificationDTO - a model defined in OpenAPI

        Args:
            matricule (str):
            nom (str):
            prenom (str):
            autres_prenoms (str):
            pays_nationalite (str):
            nom_pays_nationalite (str):
            sexe (str):
            genre (str):
            photo_identite ([str]):
            pays_naissance (str):
            nom_pays_naissance (str):
            lieu_naissance (str):
            etat_civil (str):
            pays_residence (str):
            carte_identite ([str]):
            passeport ([str]):
            numero_registre_national_belge (str):
            numero_carte_identite (str):
            numero_passeport (str):
            langue_contact (str):
            nom_langue_contact (str):
            email (str):
            noma_derniere_inscription_ucl (str):

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
            date_naissance (date, none_type): [optional]  # noqa: E501
            annee_naissance (int, none_type): [optional]  # noqa: E501
            pays_nationalite_europeen (bool, none_type): [optional]  # noqa: E501
            date_expiration_carte_identite (date, none_type): [optional]  # noqa: E501
            date_expiration_passeport (date, none_type): [optional]  # noqa: E501
            annee_derniere_inscription_ucl (int, none_type): [optional]  # noqa: E501
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

        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.autres_prenoms = autres_prenoms
        self.pays_nationalite = pays_nationalite
        self.nom_pays_nationalite = nom_pays_nationalite
        self.sexe = sexe
        self.genre = genre
        self.photo_identite = photo_identite
        self.pays_naissance = pays_naissance
        self.nom_pays_naissance = nom_pays_naissance
        self.lieu_naissance = lieu_naissance
        self.etat_civil = etat_civil
        self.pays_residence = pays_residence
        self.carte_identite = carte_identite
        self.passeport = passeport
        self.numero_registre_national_belge = numero_registre_national_belge
        self.numero_carte_identite = numero_carte_identite
        self.numero_passeport = numero_passeport
        self.langue_contact = langue_contact
        self.nom_langue_contact = nom_langue_contact
        self.email = email
        self.noma_derniere_inscription_ucl = noma_derniere_inscription_ucl
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
    def __init__(self, matricule, nom, prenom, autres_prenoms, pays_nationalite, nom_pays_nationalite, sexe, genre, photo_identite, pays_naissance, nom_pays_naissance, lieu_naissance, etat_civil, pays_residence, carte_identite, passeport, numero_registre_national_belge, numero_carte_identite, numero_passeport, langue_contact, nom_langue_contact, email, noma_derniere_inscription_ucl, *args, **kwargs):  # noqa: E501
        """IdentificationDTO - a model defined in OpenAPI

        Args:
            matricule (str):
            nom (str):
            prenom (str):
            autres_prenoms (str):
            pays_nationalite (str):
            nom_pays_nationalite (str):
            sexe (str):
            genre (str):
            photo_identite ([str]):
            pays_naissance (str):
            nom_pays_naissance (str):
            lieu_naissance (str):
            etat_civil (str):
            pays_residence (str):
            carte_identite ([str]):
            passeport ([str]):
            numero_registre_national_belge (str):
            numero_carte_identite (str):
            numero_passeport (str):
            langue_contact (str):
            nom_langue_contact (str):
            email (str):
            noma_derniere_inscription_ucl (str):

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
            date_naissance (date, none_type): [optional]  # noqa: E501
            annee_naissance (int, none_type): [optional]  # noqa: E501
            pays_nationalite_europeen (bool, none_type): [optional]  # noqa: E501
            date_expiration_carte_identite (date, none_type): [optional]  # noqa: E501
            date_expiration_passeport (date, none_type): [optional]  # noqa: E501
            annee_derniere_inscription_ucl (int, none_type): [optional]  # noqa: E501
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

        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.autres_prenoms = autres_prenoms
        self.pays_nationalite = pays_nationalite
        self.nom_pays_nationalite = nom_pays_nationalite
        self.sexe = sexe
        self.genre = genre
        self.photo_identite = photo_identite
        self.pays_naissance = pays_naissance
        self.nom_pays_naissance = nom_pays_naissance
        self.lieu_naissance = lieu_naissance
        self.etat_civil = etat_civil
        self.pays_residence = pays_residence
        self.carte_identite = carte_identite
        self.passeport = passeport
        self.numero_registre_national_belge = numero_registre_national_belge
        self.numero_carte_identite = numero_carte_identite
        self.numero_passeport = numero_passeport
        self.langue_contact = langue_contact
        self.nom_langue_contact = nom_langue_contact
        self.email = email
        self.noma_derniere_inscription_ucl = noma_derniere_inscription_ucl
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
