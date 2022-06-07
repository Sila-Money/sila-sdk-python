import unittest
from silasdk.processingTypes import ProcessingTypes
from silasdk.transactions import Transaction
from tests.test_config import (sardine_handle, eth_private_key_6,
    app, business_uuid, eth_private_key, user_handle)


class Test011CancelTransactionTest(unittest.TestCase):
    def test_cancel_transaction_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "default_plaid",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH
        }

        response = Transaction.issueSila(app, payload, eth_private_key)

        payload = {
            "user_handle": user_handle,
            "transaction_id": response["transaction_id"]
        }

        response = Transaction.cancelTransaction(
            app, payload, eth_private_key)

        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["reference"])

    def test_cancel_transaction_400(self):
        payload = {
            "user_handle": user_handle,
        }

        response = Transaction.cancelTransaction(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_redeem_sila_403(self):
        payload = {
            "user_handle": user_handle + "wrong",
            "transaction_id": "80aea226-76a3-4b60-a629-25a2db572ec8"
        }

        response = Transaction.cancelTransaction(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_redeem_sila_404(self):
        payload = {
            "user_handle": user_handle,
            "transaction_id": "80aea226-76a3-4b60-a629-25a2db572ec8"
        }

        response = Transaction.cancelTransaction(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_cancel_transaction_instant_settelment_200(self):
        payload = {
            "user_handle": sardine_handle,
            "amount": 200,
            "account_name": "default_plaid",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.INSTANT_SETTLEMENT
        }

        response = Transaction.issueSila(app, payload, eth_private_key_6)
        payload = {
            "user_handle": user_handle,
            "transaction_id": response["transaction_id"]
        }

        response = Transaction.cancelTransaction(
            app, payload, eth_private_key)
        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["reference"])


if __name__ == '__main__':
    unittest.main()
