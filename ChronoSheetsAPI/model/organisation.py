"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from ChronoSheetsAPI.model_utils import (  # noqa: F401
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
)

def lazy_import():
    from ChronoSheetsAPI.model.organisation_pricing_plan import OrganisationPricingPlan
    globals()['OrganisationPricingPlan'] = OrganisationPricingPlan


class Organisation(ModelNormal):
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
        ('subscription_source',): {
            'NONE': "None",
            'STRIPE': "Stripe",
            'APPLEINAPP': "AppleInApp",
            'GOOGLEINAPP': "GoogleInApp",
        },
        ('sign_up_source',): {
            'DESKTOP': "Desktop",
            'MOBILEIOS': "MobileiOS",
            'MOBILEANDROID': "MobileAndroid",
        },
    }

    validations = {
    }

    additional_properties_type = None

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
            'id': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'address_line01': (str,),  # noqa: E501
            'address_line02': (str,),  # noqa: E501
            'suburb': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'postcode': (str,),  # noqa: E501
            'country': (str,),  # noqa: E501
            'phone': (str,),  # noqa: E501
            'email_address': (str,),  # noqa: E501
            'timezone': (str,),  # noqa: E501
            'subscription_customer_id': (str,),  # noqa: E501
            'signup_token': (str,),  # noqa: E501
            'is_active': (bool,),  # noqa: E501
            'stripe_coupon_code': (str,),  # noqa: E501
            'subscription_source': (str,),  # noqa: E501
            'sign_up_source': (str,),  # noqa: E501
            'mobile_sign_up_code': (str,),  # noqa: E501
            'subscription_cycle_start': (datetime,),  # noqa: E501
            'subscription_cycle_end': (datetime,),  # noqa: E501
            'pricing_plans': ([OrganisationPricingPlan],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'Id',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'address_line01': 'AddressLine01',  # noqa: E501
        'address_line02': 'AddressLine02',  # noqa: E501
        'suburb': 'Suburb',  # noqa: E501
        'state': 'State',  # noqa: E501
        'postcode': 'Postcode',  # noqa: E501
        'country': 'Country',  # noqa: E501
        'phone': 'Phone',  # noqa: E501
        'email_address': 'EmailAddress',  # noqa: E501
        'timezone': 'Timezone',  # noqa: E501
        'subscription_customer_id': 'SubscriptionCustomerId',  # noqa: E501
        'signup_token': 'SignupToken',  # noqa: E501
        'is_active': 'IsActive',  # noqa: E501
        'stripe_coupon_code': 'StripeCouponCode',  # noqa: E501
        'subscription_source': 'SubscriptionSource',  # noqa: E501
        'sign_up_source': 'SignUpSource',  # noqa: E501
        'mobile_sign_up_code': 'MobileSignUpCode',  # noqa: E501
        'subscription_cycle_start': 'SubscriptionCycleStart',  # noqa: E501
        'subscription_cycle_end': 'SubscriptionCycleEnd',  # noqa: E501
        'pricing_plans': 'PricingPlans',  # noqa: E501
    }

    _composed_schemas = {}

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
        """Organisation - a model defined in OpenAPI

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
            id (int): The ID of the organisation. [optional]  # noqa: E501
            name (str): The name of the organisation. [optional]  # noqa: E501
            address_line01 (str): Address line 1 of the organisation. [optional]  # noqa: E501
            address_line02 (str): Address line 2 of the organisation. [optional]  # noqa: E501
            suburb (str): The suburb where the organisation is located. [optional]  # noqa: E501
            state (str): The state where the organisation is located. [optional]  # noqa: E501
            postcode (str): The postcode of the organisation. [optional]  # noqa: E501
            country (str): The country of the organisation. [optional]  # noqa: E501
            phone (str): The primary phone contact number of the organisation. [optional]  # noqa: E501
            email_address (str): The primary email address of the organisation. [optional]  # noqa: E501
            timezone (str): The timezone of the organisation. [optional]  # noqa: E501
            subscription_customer_id (str): The customer ID of the payments subscription. [optional]  # noqa: E501
            signup_token (str): The sign up token. [optional]  # noqa: E501
            is_active (bool): Whether or not the organisation is active. [optional]  # noqa: E501
            stripe_coupon_code (str): The payments coupon code. [optional]  # noqa: E501
            subscription_source (str): The source of the subscription. [optional]  # noqa: E501
            sign_up_source (str): The source where the organisation signed up. [optional]  # noqa: E501
            mobile_sign_up_code (str): A temporary mobile sign up code. [optional]  # noqa: E501
            subscription_cycle_start (datetime): The start date and time of the organisations subscription. [optional]  # noqa: E501
            subscription_cycle_end (datetime): The end date and time of the organisations subscription. [optional]  # noqa: E501
            pricing_plans ([OrganisationPricingPlan]): The organisation's pricing plans. [optional]  # noqa: E501
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