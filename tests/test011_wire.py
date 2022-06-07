import time
import unittest
from silasdk.processingTypes import ProcessingTypes
from silasdk.transactions import Transaction
from silasdk.users import User
from tests.test_config import (
    app, eth_private_key, user_handle)

class Test011WireTest(unittest.TestCase):
    
    def test_approve_and_mock_wire_transection_200(self):
        provider_status = "initiated"
        payload = {
            "user_handle": user_handle,
            "amount": 11000,
            "account_name": "default_plaid",
            "processing_type": ProcessingTypes.WIRE,
            "business_uuid": "25e77968-1ca3-4a4b-8e72-506dcac20dc7",
        }
        response = Transaction.redeemSila(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS")
        transaction_id = response["transaction_id"]

        payload = {
            "user_handle": user_handle,
            "search_filters": {
                'page': 1,
                'per_page': 1,
                "transaction_id": transaction_id,
            }
        }
        for _ in range(10):
            if provider_status == "pending_approval":
                break
            time.sleep(10)
            response = User.getTransactions(
                app, payload, eth_private_key)
            provider_status = response["transactions"][0]["provider_status"]
        payload = {
            "user_handle": user_handle,
            "transaction_id": transaction_id,
            "approve": True,
            "notes": "",
            "mock_wire_account_name": "mock_account_success"
        }

        response = Transaction.approveWire(app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS")

        time.sleep(30)
        payload = {
            "user_handle": user_handle,
            "transaction_id": transaction_id,
            "wire_status": "PR"
        }

        response = Transaction.mockWire(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS")


if __name__ == '__main__':
    unittest.main()