import unittest

from silasdk.transactions import Transaction
from silasdk.tests.test_config import *


class Test011RedeemSilaTest(unittest.TestCase):
    def test_redeem_sila_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 1000,
            "account_name":"default_plaid",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid
        }

        response = Transaction.redeemSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["descriptor"], "test descriptor")
        self.assertIsNotNone(response["transaction_id"])

    def test_redeem_sila_400(self):
        payload = {
            "user_handle": user_handle
        }

        response = Transaction.redeemSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_redeem_sila_401(self):
        payload = {
            "user_handle": "",
            "amount": "-1"
        }

        response = Transaction.redeemSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

if __name__ == '__main__':
    unittest.main()
