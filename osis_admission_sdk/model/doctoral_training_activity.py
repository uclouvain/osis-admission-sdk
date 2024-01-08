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
    from osis_admission_sdk.model.categorie_activite import CategorieActivite
    from osis_admission_sdk.model.choix_type_epreuve import ChoixTypeEpreuve
    from osis_admission_sdk.model.communication import Communication
    from osis_admission_sdk.model.conference import Conference
    from osis_admission_sdk.model.conference_communication import ConferenceCommunication
    from osis_admission_sdk.model.conference_publication import ConferencePublication
    from osis_admission_sdk.model.contexte_formation import ContexteFormation
    from osis_admission_sdk.model.course import Course
    from osis_admission_sdk.model.paper import Paper
    from osis_admission_sdk.model.publication import Publication
    from osis_admission_sdk.model.residency import Residency
    from osis_admission_sdk.model.residency_communication import ResidencyCommunication
    from osis_admission_sdk.model.seminar import Seminar
    from osis_admission_sdk.model.seminar_communication import SeminarCommunication
    from osis_admission_sdk.model.service import Service
    from osis_admission_sdk.model.statut_activite import StatutActivite
    from osis_admission_sdk.model.ucl_course import UclCourse
    from osis_admission_sdk.model.valorisation import Valorisation
    globals()['CategorieActivite'] = CategorieActivite
    globals()['ChoixTypeEpreuve'] = ChoixTypeEpreuve
    globals()['Communication'] = Communication
    globals()['Conference'] = Conference
    globals()['ConferenceCommunication'] = ConferenceCommunication
    globals()['ConferencePublication'] = ConferencePublication
    globals()['ContexteFormation'] = ContexteFormation
    globals()['Course'] = Course
    globals()['Paper'] = Paper
    globals()['Publication'] = Publication
    globals()['Residency'] = Residency
    globals()['ResidencyCommunication'] = ResidencyCommunication
    globals()['Seminar'] = Seminar
    globals()['SeminarCommunication'] = SeminarCommunication
    globals()['Service'] = Service
    globals()['StatutActivite'] = StatutActivite
    globals()['UclCourse'] = UclCourse
    globals()['Valorisation'] = Valorisation


class DoctoralTrainingActivity(ModelComposed):
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
        ('committee',): {
            'None': None,
            'EMPTY': "",
            'YES': "YES",
            'NO': "NO",
            'NA': "NA",
        },
        ('publication_status',): {
            'None': None,
            'EMPTY': "",
            'UNSUBMITTED': "UNSUBMITTED",
            'SUBMITTED': "SUBMITTED",
            'IN_REVIEW': "IN_REVIEW",
            'ACCEPTED': "ACCEPTED",
            'PUBLISHED': "PUBLISHED",
        },
    }

    validations = {
        ('participating_days',): {
            'inclusive_minimum': 0,
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
            'object_type': (str,),  # noqa: E501
            'uuid': (str,),  # noqa: E501
            'status': (StatutActivite,),  # noqa: E501
            'doctorate': (str,),  # noqa: E501
            'reference_promoter_assent': (bool, none_type,),  # noqa: E501
            'reference_promoter_comment': (str,),  # noqa: E501
            'cdd_comment': (str,),  # noqa: E501
            'can_be_submitted': (bool,),  # noqa: E501
            'participating_proof': ([str],),  # noqa: E501
            'children': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'summary': ([str],),  # noqa: E501
            'acceptation_proof': ([str],),  # noqa: E501
            'learning_unit_title': (str,),  # noqa: E501
            'academic_year_title': (str,),  # noqa: E501
            'category': (CategorieActivite,),  # noqa: E501
            'context': (ContexteFormation,),  # noqa: E501
            'type': (ChoixTypeEpreuve,),  # noqa: E501
            'ects': (float,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'start_date': (date, none_type,),  # noqa: E501
            'end_date': (date, none_type,),  # noqa: E501
            'participating_days': (float, none_type,),  # noqa: E501
            'is_online': (bool, none_type,),  # noqa: E501
            'website': (str,),  # noqa: E501
            'country': (str, none_type,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'organizing_institution': (str,),  # noqa: E501
            'comment': (str,),  # noqa: E501
            'committee': (str, none_type,),  # noqa: E501
            'dial_reference': (str,),  # noqa: E501
            'parent': (str,),  # noqa: E501
            'publication_status': (str, none_type,),  # noqa: E501
            'authors': (str,),  # noqa: E501
            'role': (str,),  # noqa: E501
            'keywords': (str,),  # noqa: E501
            'journal': (str,),  # noqa: E501
            'subtitle': (str,),  # noqa: E501
            'subtype': (str,),  # noqa: E501
            'hour_volume': (str,),  # noqa: E501
            'learning_unit_year': (str,),  # noqa: E501
            'academic_year': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        lazy_import()
        val = {
            'Communication': Communication,
            'Conference': Conference,
            'ConferenceCommunication': ConferenceCommunication,
            'ConferencePublication': ConferencePublication,
            'Course': Course,
            'Paper': Paper,
            'Publication': Publication,
            'Residency': Residency,
            'ResidencyCommunication': ResidencyCommunication,
            'Seminar': Seminar,
            'SeminarCommunication': SeminarCommunication,
            'Service': Service,
            'UclCourse': UclCourse,
            'Valorisation': Valorisation,
        }
        if not val:
            return None
        return {'object_type': val}

    attribute_map = {
        'object_type': 'object_type',  # noqa: E501
        'uuid': 'uuid',  # noqa: E501
        'status': 'status',  # noqa: E501
        'doctorate': 'doctorate',  # noqa: E501
        'reference_promoter_assent': 'reference_promoter_assent',  # noqa: E501
        'reference_promoter_comment': 'reference_promoter_comment',  # noqa: E501
        'cdd_comment': 'cdd_comment',  # noqa: E501
        'can_be_submitted': 'can_be_submitted',  # noqa: E501
        'participating_proof': 'participating_proof',  # noqa: E501
        'children': 'children',  # noqa: E501
        'summary': 'summary',  # noqa: E501
        'acceptation_proof': 'acceptation_proof',  # noqa: E501
        'learning_unit_title': 'learning_unit_title',  # noqa: E501
        'academic_year_title': 'academic_year_title',  # noqa: E501
        'category': 'category',  # noqa: E501
        'context': 'context',  # noqa: E501
        'type': 'type',  # noqa: E501
        'ects': 'ects',  # noqa: E501
        'title': 'title',  # noqa: E501
        'start_date': 'start_date',  # noqa: E501
        'end_date': 'end_date',  # noqa: E501
        'participating_days': 'participating_days',  # noqa: E501
        'is_online': 'is_online',  # noqa: E501
        'website': 'website',  # noqa: E501
        'country': 'country',  # noqa: E501
        'city': 'city',  # noqa: E501
        'organizing_institution': 'organizing_institution',  # noqa: E501
        'comment': 'comment',  # noqa: E501
        'committee': 'committee',  # noqa: E501
        'dial_reference': 'dial_reference',  # noqa: E501
        'parent': 'parent',  # noqa: E501
        'publication_status': 'publication_status',  # noqa: E501
        'authors': 'authors',  # noqa: E501
        'role': 'role',  # noqa: E501
        'keywords': 'keywords',  # noqa: E501
        'journal': 'journal',  # noqa: E501
        'subtitle': 'subtitle',  # noqa: E501
        'subtype': 'subtype',  # noqa: E501
        'hour_volume': 'hour_volume',  # noqa: E501
        'learning_unit_year': 'learning_unit_year',  # noqa: E501
        'academic_year': 'academic_year',  # noqa: E501
    }

    read_only_vars = {
        'uuid',  # noqa: E501
        'reference_promoter_assent',  # noqa: E501
        'reference_promoter_comment',  # noqa: E501
        'cdd_comment',  # noqa: E501
        'can_be_submitted',  # noqa: E501
        'children',  # noqa: E501
        'learning_unit_title',  # noqa: E501
        'academic_year_title',  # noqa: E501
        'ects',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """DoctoralTrainingActivity - a model defined in OpenAPI

        Keyword Args:
            object_type (str):
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
            uuid (str): [optional]  # noqa: E501
            status (StatutActivite): [optional]  # noqa: E501
            doctorate (str): [optional]  # noqa: E501
            reference_promoter_assent (bool, none_type): [optional]  # noqa: E501
            reference_promoter_comment (str): [optional]  # noqa: E501
            cdd_comment (str): [optional]  # noqa: E501
            can_be_submitted (bool): [optional]  # noqa: E501
            participating_proof ([str]): [optional]  # noqa: E501
            children ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            summary ([str]): [optional]  # noqa: E501
            acceptation_proof ([str]): [optional]  # noqa: E501
            learning_unit_title (str): [optional]  # noqa: E501
            academic_year_title (str): [optional]  # noqa: E501
            category (CategorieActivite): [optional]  # noqa: E501
            context (ContexteFormation): [optional]  # noqa: E501
            type (ChoixTypeEpreuve): [optional]  # noqa: E501
            ects (float): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            start_date (date, none_type): [optional]  # noqa: E501
            end_date (date, none_type): [optional]  # noqa: E501
            participating_days (float, none_type): [optional]  # noqa: E501
            is_online (bool, none_type): [optional]  # noqa: E501
            website (str): [optional]  # noqa: E501
            country (str, none_type): [optional]  # noqa: E501
            city (str): [optional]  # noqa: E501
            organizing_institution (str): [optional]  # noqa: E501
            comment (str): [optional]  # noqa: E501
            committee (str, none_type): [optional]  # noqa: E501
            dial_reference (str): [optional]  # noqa: E501
            parent (str): [optional]  # noqa: E501
            publication_status (str, none_type): [optional]  # noqa: E501
            authors (str): [optional]  # noqa: E501
            role (str): [optional]  # noqa: E501
            keywords (str): [optional]  # noqa: E501
            journal (str): [optional]  # noqa: E501
            subtitle (str): [optional]  # noqa: E501
            subtype (str): [optional]  # noqa: E501
            hour_volume (str): [optional]  # noqa: E501
            learning_unit_year (str): [optional]  # noqa: E501
            academic_year (int): [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """DoctoralTrainingActivity - a model defined in OpenAPI

        Keyword Args:
            object_type (str):
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
            uuid (str): [optional]  # noqa: E501
            status (StatutActivite): [optional]  # noqa: E501
            doctorate (str): [optional]  # noqa: E501
            reference_promoter_assent (bool, none_type): [optional]  # noqa: E501
            reference_promoter_comment (str): [optional]  # noqa: E501
            cdd_comment (str): [optional]  # noqa: E501
            can_be_submitted (bool): [optional]  # noqa: E501
            participating_proof ([str]): [optional]  # noqa: E501
            children ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            summary ([str]): [optional]  # noqa: E501
            acceptation_proof ([str]): [optional]  # noqa: E501
            learning_unit_title (str): [optional]  # noqa: E501
            academic_year_title (str): [optional]  # noqa: E501
            category (CategorieActivite): [optional]  # noqa: E501
            context (ContexteFormation): [optional]  # noqa: E501
            type (ChoixTypeEpreuve): [optional]  # noqa: E501
            ects (float): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            start_date (date, none_type): [optional]  # noqa: E501
            end_date (date, none_type): [optional]  # noqa: E501
            participating_days (float, none_type): [optional]  # noqa: E501
            is_online (bool, none_type): [optional]  # noqa: E501
            website (str): [optional]  # noqa: E501
            country (str, none_type): [optional]  # noqa: E501
            city (str): [optional]  # noqa: E501
            organizing_institution (str): [optional]  # noqa: E501
            comment (str): [optional]  # noqa: E501
            committee (str, none_type): [optional]  # noqa: E501
            dial_reference (str): [optional]  # noqa: E501
            parent (str): [optional]  # noqa: E501
            publication_status (str, none_type): [optional]  # noqa: E501
            authors (str): [optional]  # noqa: E501
            role (str): [optional]  # noqa: E501
            keywords (str): [optional]  # noqa: E501
            journal (str): [optional]  # noqa: E501
            subtitle (str): [optional]  # noqa: E501
            subtype (str): [optional]  # noqa: E501
            hour_volume (str): [optional]  # noqa: E501
            learning_unit_year (str): [optional]  # noqa: E501
            academic_year (int): [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
          ],
          'oneOf': [
              Communication,
              Conference,
              ConferenceCommunication,
              ConferencePublication,
              Course,
              Paper,
              Publication,
              Residency,
              ResidencyCommunication,
              Seminar,
              SeminarCommunication,
              Service,
              UclCourse,
              Valorisation,
          ],
        }
