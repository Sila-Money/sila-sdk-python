import unittest

from silasdk.users import User
from silasdk.tests.test_config import *


class Test008GetAccountBalanceTest(unittest.TestCase):
    def test_get_account_balance_200(self):
        payload = {
            "user_handle": user_handle,
            "account_name": "default_plaid"
        }

        response = User.getAccountBalance(app, payload, eth_private_key)
        self.assertTrue(response["success"])


if __name__ == '__main__':
    unittest.main()
