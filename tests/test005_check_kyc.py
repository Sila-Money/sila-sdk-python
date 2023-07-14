import time
import unittest
from silasdk.users import User
from tests.test_config import (
    app,
    business_handle,
    eth_private_key,
    eth_private_key_2,
    eth_private_key_3,
    user_handle,
    user_handle_2,
    sardine_handle,
    eth_private_key_6
)


class Test005CheckKycTest(unittest.TestCase):
    def test_check_kyc_200(self):
        time.sleep(100)
        payload = {
            "user_handle": user_handle
        }
        response = User.checkKyc(app, payload, eth_private_key)

        payload = {
            "user_handle": user_handle_2
        }
        response_2 = User.checkKyc(app, payload, eth_private_key_2)

        payload = {
            "user_handle": business_handle
        }
        response_3 = User.checkKyc(app, payload, eth_private_key_3)

        payload = {
            "user_handle": sardine_handle,
            "kyc_level": "INSTANT-ACHV2"
        }
        response_4 = User.checkKyc(app, payload, eth_private_key_6)

        self.assertIn(user_handle, response["message"])
        self.assertIsNotNone(response['verification_status'])
        self.assertIsNotNone(response['verification_history'])

        self.assertIn(user_handle_2, response_2["message"])
        self.assertIsNotNone(response_2['verification_status'])
        self.assertIsNotNone(response_2['verification_history'])

        self.assertIn("Business has passed verification", response_3["message"])
        self.assertIsNotNone(response_3['verification_status'])
        self.assertIsNotNone(response_3['verification_history'])

        self.assertIn(sardine_handle, response_4["message"])
        self.assertIsNotNone(response_4['verification_status'])
        self.assertIsNotNone(response_4['verification_history'])


if __name__ == '__main__':
    unittest.main()
