import unittest

from silasdk.users import User
from silasdk.tests.test_config import *


class GetAccountsTest(unittest.TestCase):
    def test_get_accounts_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = User.getAccounts(app, payload, eth_private_key)
        self.assertGreater(len(response), 0)

    def test_get_accounts_400(self):
        payload = {
            "user_handle": "none.silamoney.eth"
        }

        response = User.getAccounts(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == '__main__':
    unittest.main()
