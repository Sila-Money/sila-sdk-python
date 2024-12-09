import uuid
import unittest
from silasdk.transactions import Transaction
from tests.poll_until_status import poll
from tests.test_config import ( instant_handle, eth_private_key_4,
    app, business_uuid, eth_private_key, user_handle, user_handle_2)


class Test010TransferSilaTest(unittest.TestCase):
    def test_transfer_sila_200(self):
        payload = {
            "user_handle": user_handle,
            "destination": user_handle_2,
            "amount": 1,
            "descriptor": "test descriptor",
            "business_uuid": business_uuid
        }

        response = Transaction.transferSila(
            app, payload, eth_private_key)
        poll(self, response["transaction_id"], "success", app, user_handle, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["descriptor"], "test descriptor")
        self.assertIsNotNone(response["transaction_id"])

    def test_transfer_sila_idempotency_200(self):
        payload = {
            "user_handle": user_handle,
            "destination": user_handle_2,
            "amount": 1,
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "transaction_idempotency_id": str(uuid.uuid4())
        }

        first_response = Transaction.transferSila(app, payload, eth_private_key)
        second_response = Transaction.transferSila(app, payload, eth_private_key)
        self.assertEqual(first_response["transaction_id"], second_response["transaction_id"])

    def test_transfer_sila_400(self):
        payload = {
            "user_handle": user_handle,
            "destination": user_handle_2,
        }

        response = Transaction.transferSila(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_transfer_sila_401(self):
        payload = {
            "user_handle": "",
            "destination": user_handle_2,
            "amount": 1000
        }

        response = Transaction.transferSila(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_transfer_sila_instant_settlement_200(self):
        payload = {
            "user_handle": instant_handle,
            "destination": user_handle_2,
            "amount": 1,
            "descriptor": "test descriptor",
            "business_uuid": business_uuid
        }

        response = Transaction.transferSila(app, payload, eth_private_key_4)
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))


if __name__ == '__main__':
    unittest.main()
