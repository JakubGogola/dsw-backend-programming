# coding: utf-8

"""
    User & Order API

    API do zarządzania użytkownikami i ich zamówieniami

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.order_create import OrderCreate

class TestOrderCreate(unittest.TestCase):
    """OrderCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreate:
        """Test OrderCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreate`
        """
        model = OrderCreate()
        if include_optional:
            return OrderCreate(
                user_id = 56,
                total = 1.337
            )
        else:
            return OrderCreate(
                user_id = 56,
                total = 1.337,
        )
        """

    def testOrderCreate(self):
        """Test OrderCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
