import unittest
from silasdk.users import User
from tests.test_config import (
    app,
    business_handle,
    eth_private_key,
    eth_private_key_2,
    sardine_handle,
    eth_private_key_6,
    eth_private_key_3,
    eth_private_key_4,
    instant_ach_handle,
    user_handle,
    user_handle_2
)


class Test004RequestKycTest(unittest.TestCase):
    def test_register_kyc_200_default(self):
        payload = {
            "user_handle": user_handle,
            'kyc_level': 'KYC-STANDARD'
        }

        response = User.requestKyc(app, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status'), "SUCCESS")
        self.assertIsNotNone(response['verification_uuid'])
        self.assertEqual(response.get('status_code'), 200)

        payload = {
            "user_handle": user_handle_2,
        }

        response = User.requestKyc(app, payload, eth_private_key_2)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status'), "SUCCESS")
        self.assertEqual(response.get('status_code'), 200)
        self.assertIsNotNone(response['verification_uuid'])

    def test_register_kyc_200_kyb(self):
        payload = {
            "user_handle": business_handle
        }

        response = User.requestKyc(app, payload, eth_private_key_3)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status'), "SUCCESS")
        self.assertEqual(response.get('status_code'), 200)
        self.assertIsNotNone(response['verification_uuid'])

    def test_register_kyc_200_instant_ach(self):
        payload = {
            'user_handle': instant_ach_handle,
        }

        response = User.requestKyc(app, payload, eth_private_key_4)

        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status'), 'SUCCESS')
        self.assertEqual(response.get('status_code'), 200)
        self.assertIsNotNone(response['verification_uuid'])

        payload = {
            'user_handle': sardine_handle,
            'kyc_level': 'KYC-STANDARD'
        }

        response = User.requestKyc(app, payload, eth_private_key_6)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status'), 'SUCCESS')
        self.assertEqual(response.get('status_code'), 200)
        self.assertIsNotNone(response['verification_uuid'])

    def test_register_kyc_custom_403(self):
        payload = {
            "user_handle": user_handle,
            "kyc_level": "CUSTOM_KYC_FLOW_NAME"
        }

        response = User.requestKyc(app, payload, eth_private_key, True)
        self.assertEqual(response.get('status'), "FAILURE")


if __name__ == '__main__':
    unittest.main()
