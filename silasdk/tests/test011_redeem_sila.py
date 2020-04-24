import unittest

from silasdk.transactions import Transaction
from silasdk.tests.test_config import *


class RedeemSilaTest(unittest.TestCase):
    def test_redeem_sila_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 1000
        }

        response = Transaction.redeemSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS")

    def test_redeem_sila_400(self):
        payload = {
            "user_handle": user_handle
        }

        response = Transaction.redeemSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS")

    def test_redeem_sila_401(self):
        payload = {
            "user_handle": "",
            "amount": "-1"
        }

        response = Transaction.redeemSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

if __name__ == '__main__':
    unittest.main()
