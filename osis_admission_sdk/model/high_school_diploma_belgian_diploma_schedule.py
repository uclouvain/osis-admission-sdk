"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.71
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



class HighSchoolDiplomaBelgianDiplomaSchedule(ModelNormal):
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
        ('latin',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('greek',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('chemistry',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('physic',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('biology',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('german',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('dutch',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('english',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('french',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('spanish',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('modern_languages_other_label',): {
            'max_length': 25,
        },
        ('modern_languages_other_hours',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('mathematics',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('it',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('social_sciences',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('economic_sciences',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
        ('other_label',): {
            'max_length': 25,
        },
        ('other_hours',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = True

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
            'id': (int,),  # noqa: E501
            'latin': (int,),  # noqa: E501
            'greek': (int,),  # noqa: E501
            'chemistry': (int,),  # noqa: E501
            'physic': (int,),  # noqa: E501
            'biology': (int,),  # noqa: E501
            'german': (int,),  # noqa: E501
            'dutch': (int,),  # noqa: E501
            'english': (int,),  # noqa: E501
            'french': (int,),  # noqa: E501
            'spanish': (int,),  # noqa: E501
            'modern_languages_other_label': (str,),  # noqa: E501
            'modern_languages_other_hours': (int, none_type,),  # noqa: E501
            'mathematics': (int,),  # noqa: E501
            'it': (int,),  # noqa: E501
            'social_sciences': (int,),  # noqa: E501
            'economic_sciences': (int,),  # noqa: E501
            'other_label': (str,),  # noqa: E501
            'other_hours': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'latin': 'latin',  # noqa: E501
        'greek': 'greek',  # noqa: E501
        'chemistry': 'chemistry',  # noqa: E501
        'physic': 'physic',  # noqa: E501
        'biology': 'biology',  # noqa: E501
        'german': 'german',  # noqa: E501
        'dutch': 'dutch',  # noqa: E501
        'english': 'english',  # noqa: E501
        'french': 'french',  # noqa: E501
        'spanish': 'spanish',  # noqa: E501
        'modern_languages_other_label': 'modern_languages_other_label',  # noqa: E501
        'modern_languages_other_hours': 'modern_languages_other_hours',  # noqa: E501
        'mathematics': 'mathematics',  # noqa: E501
        'it': 'it',  # noqa: E501
        'social_sciences': 'social_sciences',  # noqa: E501
        'economic_sciences': 'economic_sciences',  # noqa: E501
        'other_label': 'other_label',  # noqa: E501
        'other_hours': 'other_hours',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """HighSchoolDiplomaBelgianDiplomaSchedule - a model defined in OpenAPI

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
            id (int): [optional]  # noqa: E501
            latin (int): [optional]  # noqa: E501
            greek (int): [optional]  # noqa: E501
            chemistry (int): [optional]  # noqa: E501
            physic (int): [optional]  # noqa: E501
            biology (int): [optional]  # noqa: E501
            german (int): [optional]  # noqa: E501
            dutch (int): [optional]  # noqa: E501
            english (int): [optional]  # noqa: E501
            french (int): [optional]  # noqa: E501
            spanish (int): [optional]  # noqa: E501
            modern_languages_other_label (str): Si autre langue, précisez. [optional]  # noqa: E501
            modern_languages_other_hours (int, none_type): [optional]  # noqa: E501
            mathematics (int): [optional]  # noqa: E501
            it (int): [optional]  # noqa: E501
            social_sciences (int): [optional]  # noqa: E501
            economic_sciences (int): [optional]  # noqa: E501
            other_label (str): Si autres matières optionnelles, précisez. [optional]  # noqa: E501
            other_hours (int, none_type): [optional]  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """HighSchoolDiplomaBelgianDiplomaSchedule - a model defined in OpenAPI

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
            id (int): [optional]  # noqa: E501
            latin (int): [optional]  # noqa: E501
            greek (int): [optional]  # noqa: E501
            chemistry (int): [optional]  # noqa: E501
            physic (int): [optional]  # noqa: E501
            biology (int): [optional]  # noqa: E501
            german (int): [optional]  # noqa: E501
            dutch (int): [optional]  # noqa: E501
            english (int): [optional]  # noqa: E501
            french (int): [optional]  # noqa: E501
            spanish (int): [optional]  # noqa: E501
            modern_languages_other_label (str): Si autre langue, précisez. [optional]  # noqa: E501
            modern_languages_other_hours (int, none_type): [optional]  # noqa: E501
            mathematics (int): [optional]  # noqa: E501
            it (int): [optional]  # noqa: E501
            social_sciences (int): [optional]  # noqa: E501
            economic_sciences (int): [optional]  # noqa: E501
            other_label (str): Si autres matières optionnelles, précisez. [optional]  # noqa: E501
            other_hours (int, none_type): [optional]  # noqa: E501
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
