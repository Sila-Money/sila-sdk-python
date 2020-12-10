import unittest, silasdk
from tests.poll_until_status import *
from tests.test_config import *

class Test011CancelTransactionTest(unittest.TestCase):
    def test_cancel_transaction_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "account_name":"default_plaid",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "processing_type": silasdk.ProcessingTypes.STANDARD_ACH
        }

        response = silasdk.Transaction.issueSila(app, payload, eth_private_key)

        payload = {
            "user_handle": user_handle,
            "transaction_id": response["transaction_id"]
        }

        response = silasdk.Transaction.cancelTransaction(app, payload, eth_private_key)

        self.assertTrue(response["success"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["reference"])

    def test_cancel_transaction_400(self):
        payload = {
            "user_handle": user_handle,
        }

        response = silasdk.Transaction.cancelTransaction(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_redeem_sila_403(self):
        payload = {
            "user_handle": user_handle + "wrong",
            "transaction_id": "80aea226-76a3-4b60-a629-25a2db572ec8"
        }

        response = silasdk.Transaction.cancelTransaction(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_redeem_sila_403_redeem(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "account_name":"default_plaid",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "processing_type": silasdk.ProcessingTypes.STANDARD_ACH
        }

        response = silasdk.Transaction.redeemSila(app, payload, eth_private_key)

        payload = {
            "user_handle": user_handle,
            "transaction_id": response["transaction_id"]
        }

        response = silasdk.Transaction.cancelTransaction(app, payload, eth_private_key)

        self.assertEqual(response["status"], "FAILURE")

    def test_redeem_sila_404(self):
        payload = {
            "user_handle": user_handle,
            "transaction_id": "80aea226-76a3-4b60-a629-25a2db572ec8"
        }

        response = silasdk.Transaction.cancelTransaction(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

if __name__ == '__main__':
    unittest.main()
