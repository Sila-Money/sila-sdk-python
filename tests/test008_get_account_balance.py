import unittest, silasdk

from tests.test_config import *

class Test008GetAccountBalanceTest(unittest.TestCase):
    def test_get_account_balance_200(self):
        payload = {
            "user_handle": user_handle,
            "account_name": "default_plaid"
        }

        response = silasdk.User.getAccountBalance(app, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

        payload = {
            "user_handle": user_handle,
            "account_name": "default_mx"
        }

        response_2 = silasdk.User.getAccountBalance(app, payload, eth_private_key)
        self.assertTrue(response_2["success"])
        self.assertIsNotNone(response_2["reference"])


if __name__ == '__main__':
    unittest.main()
