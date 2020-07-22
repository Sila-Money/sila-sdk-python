import unittest, silasdk

from silasdk.tests.test_config import *

class Test012GetTransactionsTest(unittest.TestCase):
    def test_get_transactions_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = silasdk.User.getTransactions(app, payload, eth_private_key)
        self.assertTrue(response["success"])

    def test_get_transactions_403(self):
        payload = {
            "user_handle": ""
        }

        response = silasdk.User.getTransactions(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
