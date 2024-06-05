import unittest
import time
import uuid

from silasdk.users import User
from tests.test_config import (app, basic_individual_handle, business_handle, eth_address, eth_address_2,
                               eth_address_3, eth_address_4, eth_address_5, user_handle, user_handle_2, 
                               instant_ach_handle, sardine_handle, eth_address_6, business_handle_2, eth_address_7)

timestamp = time.time()

class Test002RegisterTest(unittest.TestCase):
    def test_register_200(self):
        payload = {
            "country": "US",
            "user_handle": user_handle,
            "first_name": 'Example',
            "last_name": 'User',
            "entity_name": 'Example User',
            "identity_value": "123458877",
            "identity_alias": "SSN",
            "phone": "1234567890",
            "email": "fake@email.com",
            "address_alias": "default",
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
            "identity_alias": "SSN",
            "identity_value": "123458877",
            "phone": "1234567890",
            "email": f"fake{timestamp}@email.com",
            "address_alias": "default",
            "street_address_1": '1232 Main Street',
            "city": 'New City 2',
            "state": 'OR',
            "postal_code": 97204,
            "crypto_address": eth_address_2,
            "crypto_alias": "python_wallet_2",
            "birthdate": "1990-05-12"
        }

        instant_ach = {
            "country": "US",
            "user_handle": instant_ach_handle,
            "first_name": 'Instant',
            "last_name": 'Ach',
            "entity_name": 'Instant Ach',
            "identity_alias": "SSN",
            "identity_value": "123458877",
            "phone": "1234567890",
            "sms_opt_in": True,
            "email": "intant@email.com",
            "address_alias": "default",
            "street_address_1": '1232 Main Street',
            "city": 'New City',
            "state": 'OR',
            "postal_code": 97204,
            "crypto_address": eth_address_4,
            "crypto_alias": "default",
            "birthdate": "1994-01-08",
            "device_fingerprint": "test_instant_ach"
        }

        business = {
            "country": "US",
            "user_handle": business_handle,
            "entity_name": 'Business name',
            "identity_alias": "EIN",
            "identity_value": "123458877",
            "phone": "1234567890",
            "email": "fake2@email.com",
            "address_alias": "default",
            "street_address_1": '1232 Main Street',
            "city": 'New City 2',
            "state": 'OR',
            "postal_code": 97204,
            "crypto_address": eth_address_3,
            "crypto_alias": "python_wallet_2",
            "type": "business",
            "business_type": "corporation",
            "business_website": "https://www.yourbusinesscustomer.com",
            "doing_business_as": "Your Business Customer Alias Co.",
            "naics_code": 721
        }

        sardine = {
            "country": "US",
            "user_handle": sardine_handle,
            "first_name": 'Example 2',
            "last_name": 'User 2',
            "entity_name": 'Example User 2',
            "identity_alias": "SSN",
            "identity_value": "123458877",
            "phone": "1234567890",
            "email": "fake2@email.com",
            "address_alias": "default",
            "street_address_1": '1232 Main Street',
            "city": 'New City 2',
            "state": 'OR',
            "postal_code": 97204,
            "crypto_address": eth_address_6,
            "crypto_alias": "python_wallet_2",
            "birthdate": "1990-05-12",
            "device_fingerprint": "test_sardine",
            "session_identifier": str(uuid.uuid4())
        }

        business_with_registration_state = {
            "country": "US",
            "user_handle": business_handle_2,
            "entity_name": 'Business name',
            "identity_alias": "EIN",
            "identity_value": "123458877",
            "phone": "1234567890",
            "email": "fake2@email.com",
            "address_alias": "default",
            "street_address_1": '1232 Main Street',
            "city": 'New City 2',
            "state": 'OR',
            "postal_code": 97204,
            "crypto_address": eth_address_7,
            "crypto_alias": "python_wallet_2",
            "type": "business",
            "business_type": "corporation",
            "business_website": "https://www.yourbusinesscustomer.com",
            "doing_business_as": "Your Business Customer Alias Co.",
            "naics_code": 721,
            "registration_state":"NY"
        }

        response = User.register(app, payload)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status_code'), 200)
        self.assertEqual(response.get('status'), 'SUCCESS')

        response = User.register(app, payload_2)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status_code'), 200)
        self.assertEqual(response.get('status'), 'SUCCESS')

        response = User.register(app, business)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status_code'), 200)
        self.assertEqual(response.get('status'), 'SUCCESS')
        self.assertTrue(response.get('business_uuid'))

        response = User.register(app, instant_ach)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status_code'), 200)
        self.assertEqual(response.get('status'), 'SUCCESS')

        response = User.register(app, sardine)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status_code'), 200)
        self.assertEqual(response.get('status'), 'SUCCESS')

        response = User.register(app, business_with_registration_state)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status_code'), 200)
        self.assertEqual(response.get('status'), 'SUCCESS')
        
    def test_register_200_basic(self):
        basic_individual = {
            'user_handle': basic_individual_handle,
            'crypto_address': eth_address_5,
            'first_name': 'Basic',
            'last_name': 'Test'
        }

        response = User.register(app, basic_individual)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status_code'), 200)
        self.assertEqual(response.get('status'), 'SUCCESS')

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
