import unittest, silasdk
from tests.poll_until_status import *
from tests.test_config import *

class Test010TrasferSilaTest(unittest.TestCase):
    def test_transfer_sila_200(self):
        payload = {
            "user_handle": user_handle,
            "destination": user_handle_2,
            "amount": 100,
            "descriptor": "test descriptor",
            "business_uuid": business_uuid
        }

        response = silasdk.Transaction.transferSila(app, payload, eth_private_key)

        PollUntilStatus.poll(self, response["transaction_id"], "success")

        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["descriptor"], "test descriptor")
        self.assertIsNotNone(response["transaction_id"])

    def test_transfer_sila_400(self):
        payload = {
            "user_handle": user_handle,
            "destination": user_handle_2,
            "crypto": "ETHS",
        }

        response = silasdk.Transaction.transferSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_transfer_sila_401(self):
        payload = {
            "user_handle": "",
            "destination": user_handle_2,
            "crypto": "ETH",
            "amount": 1000
        }

        response = silasdk.Transaction.transferSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == '__main__':
    unittest.main()
