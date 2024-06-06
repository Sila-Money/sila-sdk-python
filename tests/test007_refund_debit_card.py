import unittest

from silasdk.transactions import Transaction
from tests.test_config import (app, user_handle_2, eth_private_key_2)
import time


class Test007RefundDebitCardTest(unittest.TestCase):
    def test_refund_debit_card_400(self):

        payload = {
            "user_handle": user_handle_2,
            "amount": 200,
            "card_name": "visaas"
        }
        response = Transaction.issue_sila(app, payload, eth_private_key_2)
        time.sleep(4)
        payload = {
            "user_handle": user_handle_2,
        }

        response = Transaction.refundDebitCard(app, payload, eth_private_key_2)
        self.assertFalse(response['success'])
