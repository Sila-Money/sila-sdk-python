import unittest

from silasdk.tests.test_config import *
from silasdk.users import User


class Test002RegisterTest(unittest.TestCase):
    def test_register_200(self):
        payload = {
            "country": "US",
            "user_handle": user_handle,
            "first_name": 'Example',
            "last_name": 'User',
            "entity_name": 'Example User',
            "identity_value": "123452222",
            "phone": 1234567890,
            "email": "fake@email.com",
            "street_address_1": '123 Main Street',
            "city": 'New City',
            "state": 'OR',
            "postal_code": 97204,
            "crypto_address": eth_address,
            "crypto_alias": "python_wallet_1",
            "birthdate": "1990-05-19"
        }

        payload_2 = {
            "country": "US",
            "user_handle": user_handle_2,
            "first_name": 'Example 2',
            "last_name": 'User 2',
            "entity_name": 'Example User 2',
            "identity_value": "123452222",
            "phone": 1234567890,
            "email": "fake2@email.com",
            "street_address_1": '1232 Main Street',
            "city": 'New City 2',
            "state": 'OR',
            "postal_code": 97204,
            "crypto_address": eth_address_2,
            "crypto_alias": "python_wallet_2",
            "birthdate": "1990-05-12"
        }

        response = User.register(app, payload)
        self.assertEqual(response["status"], "SUCCESS")

        response_2 = User.register(app, payload_2)
        self.assertEqual(response_2["status"], "SUCCESS")


    def test_register_400(self):
        payload = {
            "country": "US",
            "user_handle": user_handle,
            "first_name": 'Example',
            "last_name": 'User',
            "entity_name": 'Example User',
            "identity_value": "123452222",
            "phone": 1234567890,
            "email": "fake@email.com",
            "street_address_1": '123 Main Street',
            "city": 'New City',
            "state": 'OR',
            "postal_code": 97204,
            "crypto_address": eth_address,
            "crypto_alias": "python_wallet_1",
            "birthdate": "1990-05-19"
        }

        response = User.register(app, payload)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == "__main__":
    unittest.main()
