import unittest, silasdk

from silasdk.tests.test_config import *

class Test004RequestKycTest(unittest.TestCase):
    def test_register_kyc_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = silasdk.User.requestKyc(app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS")

        payload = {
            "user_handle": user_handle_2
        }

        response = silasdk.User.requestKyc(app, payload, eth_private_key_2)
        self.assertEqual(response["status"], "SUCCESS")

        payload = {
            "user_handle": business_handle
        }

        response = silasdk.User.requestKyc(app, payload, eth_private_key_3)
        self.assertEqual(response["status"], "SUCCESS")

    def test_register_kyc_custom_403(self):
        payload = {
            "user_handle": user_handle,
            "kyc_level": "CUSTOM_KYC_FLOW_NAME"
        }

        response = silasdk.User.requestKyc(app, payload, eth_private_key, True)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == '__main__':
    unittest.main()
