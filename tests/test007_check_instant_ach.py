import unittest
import silasdk

from tests.test_config import (
    app, eth_private_key, eth_private_key_4, instant_ach_handle, user_handle)


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
        
if __name__ == '__main__':
    unittest.main()
