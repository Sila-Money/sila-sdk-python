import unittest
import silasdk

from tests.test_config import *


class Test012GetTransactionsTest(unittest.TestCase):
    def test_get_transactions_200(self):
        payload = {
            "user_handle": user_handle,
            "search_filters": {
                'page': 1,
                'per_page': 1
            }
        }

        response = silasdk.User.getTransactions(app, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertEqual(len(response["transactions"]), 1)
        self.assertEqual(response["transactions"][0]["processing_type"], silasdk.ProcessingTypes.STANDARD_ACH)

    def test_get_transactions_403(self):
        payload = {
            "user_handle": ""
        }

        response = silasdk.User.getTransactions(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
