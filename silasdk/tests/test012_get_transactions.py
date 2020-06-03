import unittest

from silasdk.users import User
from silasdk.tests.test_config import *


class Test012GetTransactionsTest(unittest.TestCase):
    def test_get_transactions_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = User.getTransactions(app, payload, eth_private_key)
        self.assertTrue(response["success"])

    def test_get_transactions_403(self):
        payload = {
            "user_handle": ""
        }

        response = User.getTransactions(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
