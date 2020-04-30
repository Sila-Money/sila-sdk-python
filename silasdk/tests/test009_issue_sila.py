import unittest

from silasdk.transactions import Transaction
from silasdk.tests.test_config import *


class IssueSilaTest(unittest.TestCase):

    def test_issue_sila_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 1000
        }

        response = Transaction.issueSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS")

    def test_issue_sila_400(self):
        payload = {
            "user_handle": user_handle,
            "amount": "-1"
        }

        response = Transaction.issueSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == '__main__':
    unittest.main()
