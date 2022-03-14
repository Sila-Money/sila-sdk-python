import unittest
import silasdk

from tests.test_config import (
    app, eth_private_key, eth_private_key_4, instant_ach_handle, user_handle, sardine_handle, eth_private_key_6)


class Test007CheckInstantAchTest(unittest.TestCase):
    def test_check_instant_ach(self):
        payload = {
            "user_handle": instant_ach_handle,
            "account_name": "default_plaid"
        }

        response = silasdk.User.check_instant_ach(
            app, payload, eth_private_key_4)
        
        self.assertIsNotNone(response["status"])
        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["reference"])

    def test_check_instant_ach_v2(self):
        payload = {
            "user_handle": sardine_handle,
            "account_name": "default_plaid",
            "kyc_level": "INSTANT-ACHV2"
        }

        response = silasdk.User.check_instant_ach(
            app, payload, eth_private_key_6)
        
        self.assertIsNotNone(response["status"])
        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["reference"])

if __name__ == '__main__':
    unittest.main()
