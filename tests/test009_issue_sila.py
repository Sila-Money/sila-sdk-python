import uuid
import unittest
from silasdk.processingTypes import ProcessingTypes
from silasdk.transactions import Transaction
from tests.poll_until_status import poll
from tests.test_config import (
    app, business_uuid, instant_handle, user_handle, eth_private_key,
    eth_private_key_4, user_handle_2, eth_private_key_2
)


class Test009IssueSilaTest(unittest.TestCase):

    def test_issue_sila_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "default_mx"
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertEqual(response.get("success"), True)

        poll(self, response["transaction_id"], "success",
             app, user_handle, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["transaction_id"])

        payload = {
            "user_handle": user_handle,
            "amount": 420,
            "account_name": "default_mx"
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertEqual(response.get("success"), True)

        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "default_mx"
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertEqual(response.get("success"), True)
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["transaction_id"])

    def test_issue_sila_idempotency_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "default_mx",
            "transaction_idempotency_id": str(uuid.uuid4())
        }

        first_response = Transaction.issue_sila(app, payload, eth_private_key)
        second_response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertEqual(first_response["transaction_id"], second_response["transaction_id"])

    def test_issue_sila_400(self):
        payload = {
            "user_handle": user_handle,
            "amount": "-1"
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_issue_sila_200_with_card_name(self):
        payload = {
            "user_handle": user_handle_2,
            "amount": 200,
            "card_name": "visaas"
        }
        response = Transaction.issue_sila(app, payload, eth_private_key_2)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))

    def test_issue_sila_400_card_name_account(self):
        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "test_account",
            "card_name": "visaas"
        }
        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_issue_sila_instant_settlement_200(self):
        descriptor = "test descriptor"
        payload = {
            "user_handle": instant_handle,
            "amount": 200,
            "account_name": "default_plaid",
            "descriptor": descriptor,
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.INSTANT_SETTLEMENT
        }
        response = Transaction.issue_sila(app, payload, eth_private_key_4)
        self.assertEqual(response.get("success"), True)
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))


if __name__ == '__main__':
    unittest.main()
