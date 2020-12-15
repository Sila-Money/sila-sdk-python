import unittest
from silasdk.users import User
from tests.test_config import (app, business_handle, eth_private_key, eth_private_key_2,
                               eth_private_key_3, eth_private_key_4, instant_ach_handle, user_handle, user_handle_2)


class Test004RequestKycTest(unittest.TestCase):
    def test_register_kyc_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = User.requestKyc(app, payload, eth_private_key)
        self.assertEqual(response.get('status'), "SUCCESS")
        self.assertTrue(response.get('success'))
        self.assertEqual(response.get('status_code'), 200)

        payload = {
            "user_handle": user_handle_2
        }

        response = User.requestKyc(app, payload, eth_private_key_2)
        self.assertEqual(response.get('status'), "SUCCESS")
        self.assertTrue(response.get('success'))
        self.assertEqual(response.get('status_code'), 200)

        payload = {
            "user_handle": business_handle
        }

        response = User.requestKyc(app, payload, eth_private_key_3)
        self.assertEqual(response.get('status'), "SUCCESS")
        self.assertTrue(response.get('success'))
        self.assertEqual(response.get('status_code'), 200)

        payload = {
            'user_handle': instant_ach_handle,
            'kyc_level': 'INSTANT-ACH'
        }
        response = User.requestKyc(app, payload, eth_private_key_4)
        self.assertTrue(response.get('success'))
        self.assertEqual(response.get('status'), 'SUCCESS')
        self.assertEqual(response.get('status_code'), 200)

    def test_register_kyc_custom_403(self):
        payload = {
            "user_handle": user_handle,
            "kyc_level": "CUSTOM_KYC_FLOW_NAME"
        }

        response = User.requestKyc(app, payload, eth_private_key, True)
        self.assertEqual(response.get('status'), "FAILURE")


if __name__ == '__main__':
    unittest.main()
