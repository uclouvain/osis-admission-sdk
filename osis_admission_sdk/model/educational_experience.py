"""
    Admission API

    This API delivers data for the Admission project.  # noqa: E501

    The version of the OpenAPI document: 1.0.93
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
    from osis_admission_sdk.model.educational_experience_educationalexperienceyear_set import EducationalExperienceEducationalexperienceyearSet
    from osis_admission_sdk.model.evaluation_system import EvaluationSystem
    from osis_admission_sdk.model.grade import Grade
    from osis_admission_sdk.model.teaching_type_enum import TeachingTypeEnum
    from osis_admission_sdk.model.transcript_type import TranscriptType
    globals()['EducationalExperienceEducationalexperienceyearSet'] = EducationalExperienceEducationalexperienceyearSet
    globals()['EvaluationSystem'] = EvaluationSystem
    globals()['Grade'] = Grade
    globals()['TeachingTypeEnum'] = TeachingTypeEnum
    globals()['TranscriptType'] = TranscriptType


class EducationalExperience(ModelNormal):
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
        ('institute_name',): {
            'max_length': 255,
        },
        ('institute_address',): {
            'max_length': 255,
        },
        ('education_name',): {
            'max_length': 255,
        },
        ('rank_in_diploma',): {
            'max_length': 30,
        },
        ('dissertation_title',): {
            'max_length': 255,
        },
        ('dissertation_score',): {
            'max_length': 30,
        },
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
            'educationalexperienceyear_set': ([EducationalExperienceEducationalexperienceyearSet],),  # noqa: E501
            'country': (str, none_type,),  # noqa: E501
            'obtained_diploma': (bool,),  # noqa: E501
            'linguistic_regime': (str, none_type,),  # noqa: E501
            'program': (str, none_type,),  # noqa: E501
            'valuated_from_trainings': ([str],),  # noqa: E501
            'institute': (str, none_type,),  # noqa: E501
            'uuid': (str,),  # noqa: E501
            'institute_name': (str,),  # noqa: E501
            'institute_address': (str,),  # noqa: E501
            'education_name': (str,),  # noqa: E501
            'study_system': (TeachingTypeEnum,),  # noqa: E501
            'evaluation_type': (EvaluationSystem,),  # noqa: E501
            'transcript_type': (TranscriptType,),  # noqa: E501
            'obtained_grade': (Grade,),  # noqa: E501
            'graduate_degree': ([str],),  # noqa: E501
            'graduate_degree_translation': ([str],),  # noqa: E501
            'transcript': ([str],),  # noqa: E501
            'transcript_translation': ([str],),  # noqa: E501
            'rank_in_diploma': (str,),  # noqa: E501
            'expected_graduation_date': (date, none_type,),  # noqa: E501
            'dissertation_title': (str,),  # noqa: E501
            'dissertation_score': (str,),  # noqa: E501
            'dissertation_summary': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'educationalexperienceyear_set': 'educationalexperienceyear_set',  # noqa: E501
        'country': 'country',  # noqa: E501
        'obtained_diploma': 'obtained_diploma',  # noqa: E501
        'linguistic_regime': 'linguistic_regime',  # noqa: E501
        'program': 'program',  # noqa: E501
        'valuated_from_trainings': 'valuated_from_trainings',  # noqa: E501
        'institute': 'institute',  # noqa: E501
        'uuid': 'uuid',  # noqa: E501
        'institute_name': 'institute_name',  # noqa: E501
        'institute_address': 'institute_address',  # noqa: E501
        'education_name': 'education_name',  # noqa: E501
        'study_system': 'study_system',  # noqa: E501
        'evaluation_type': 'evaluation_type',  # noqa: E501
        'transcript_type': 'transcript_type',  # noqa: E501
        'obtained_grade': 'obtained_grade',  # noqa: E501
        'graduate_degree': 'graduate_degree',  # noqa: E501
        'graduate_degree_translation': 'graduate_degree_translation',  # noqa: E501
        'transcript': 'transcript',  # noqa: E501
        'transcript_translation': 'transcript_translation',  # noqa: E501
        'rank_in_diploma': 'rank_in_diploma',  # noqa: E501
        'expected_graduation_date': 'expected_graduation_date',  # noqa: E501
        'dissertation_title': 'dissertation_title',  # noqa: E501
        'dissertation_score': 'dissertation_score',  # noqa: E501
        'dissertation_summary': 'dissertation_summary',  # noqa: E501
    }

    read_only_vars = {
        'valuated_from_trainings',  # noqa: E501
        'uuid',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, educationalexperienceyear_set, country, obtained_diploma, *args, **kwargs):  # noqa: E501
        """EducationalExperience - a model defined in OpenAPI

        Args:
            educationalexperienceyear_set ([EducationalExperienceEducationalexperienceyearSet]):
            country (str, none_type):
            obtained_diploma (bool):

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
            linguistic_regime (str, none_type): [optional]  # noqa: E501
            program (str, none_type): [optional]  # noqa: E501
            valuated_from_trainings ([str]): [optional]  # noqa: E501
            institute (str, none_type): [optional]  # noqa: E501
            uuid (str): [optional]  # noqa: E501
            institute_name (str): [optional]  # noqa: E501
            institute_address (str): [optional]  # noqa: E501
            education_name (str): [optional]  # noqa: E501
            study_system (TeachingTypeEnum): [optional]  # noqa: E501
            evaluation_type (EvaluationSystem): [optional]  # noqa: E501
            transcript_type (TranscriptType): [optional]  # noqa: E501
            obtained_grade (Grade): [optional]  # noqa: E501
            graduate_degree ([str]): [optional]  # noqa: E501
            graduate_degree_translation ([str]): [optional]  # noqa: E501
            transcript ([str]): [optional]  # noqa: E501
            transcript_translation ([str]): [optional]  # noqa: E501
            rank_in_diploma (str): [optional]  # noqa: E501
            expected_graduation_date (date, none_type): [optional]  # noqa: E501
            dissertation_title (str): [optional]  # noqa: E501
            dissertation_score (str): [optional]  # noqa: E501
            dissertation_summary ([str]): [optional]  # noqa: E501
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

        self.educationalexperienceyear_set = educationalexperienceyear_set
        self.country = country
        self.obtained_diploma = obtained_diploma
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
    def __init__(self, educationalexperienceyear_set, country, obtained_diploma, *args, **kwargs):  # noqa: E501
        """EducationalExperience - a model defined in OpenAPI

        Args:
            educationalexperienceyear_set ([EducationalExperienceEducationalexperienceyearSet]):
            country (str, none_type):
            obtained_diploma (bool):

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
            linguistic_regime (str, none_type): [optional]  # noqa: E501
            program (str, none_type): [optional]  # noqa: E501
            valuated_from_trainings ([str]): [optional]  # noqa: E501
            institute (str, none_type): [optional]  # noqa: E501
            uuid (str): [optional]  # noqa: E501
            institute_name (str): [optional]  # noqa: E501
            institute_address (str): [optional]  # noqa: E501
            education_name (str): [optional]  # noqa: E501
            study_system (TeachingTypeEnum): [optional]  # noqa: E501
            evaluation_type (EvaluationSystem): [optional]  # noqa: E501
            transcript_type (TranscriptType): [optional]  # noqa: E501
            obtained_grade (Grade): [optional]  # noqa: E501
            graduate_degree ([str]): [optional]  # noqa: E501
            graduate_degree_translation ([str]): [optional]  # noqa: E501
            transcript ([str]): [optional]  # noqa: E501
            transcript_translation ([str]): [optional]  # noqa: E501
            rank_in_diploma (str): [optional]  # noqa: E501
            expected_graduation_date (date, none_type): [optional]  # noqa: E501
            dissertation_title (str): [optional]  # noqa: E501
            dissertation_score (str): [optional]  # noqa: E501
            dissertation_summary ([str]): [optional]  # noqa: E501
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

        self.educationalexperienceyear_set = educationalexperienceyear_set
        self.country = country
        self.obtained_diploma = obtained_diploma
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
